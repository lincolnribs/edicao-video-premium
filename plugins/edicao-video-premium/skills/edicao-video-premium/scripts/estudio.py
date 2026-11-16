"""
Organização das pastas de edição (estúdio, biblioteca de SFX/músicas e clientes).

Uso:
  python estudio.py onde                       # mostra onde está o estúdio (ou que não existe)
  python estudio.py criar [--raiz PASTA]       # cria o estúdio (padrão: ~/Videos/Edicao)
  python estudio.py cliente "Nome do Cliente"  # cria a pasta do cliente com LEIAME e histórico
  python estudio.py clientes                   # lista os clientes
  python estudio.py normalizar-sfx             # deixa todos os SFX da biblioteca no mesmo pico

O caminho do estúdio fica salvo em ~/.edicao-video/config.json.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from datetime import date

CONFIG = os.path.join(os.path.expanduser("~"), ".edicao-video", "config.json")
RAIZ_PADRAO = os.path.join(os.path.expanduser("~"), "Videos", "Edicao")

CATEGORIAS_SFX = ["whoosh", "pop", "click", "ding", "impacto", "sucesso", "transicao", "digitacao", "ambiente"]
PASTAS_CLIENTE = ["01-brutos", "02-referencias", "03-marca", "04-musica", "projeto", "entregas"]

AUDIO = (".wav", ".mp3", ".ogg", ".flac", ".m4a", ".aiff")

LEIAME_ESTUDIO = """# Estúdio de edição

- `_biblioteca/sfx/<categoria>/` efeitos sonoros (originais). Versões niveladas em `_biblioteca/sfx/_normalizados/`.
- `_biblioteca/musicas/` trilhas baixadas (cada uma com a origem em `CREDITOS.md`).
- `_biblioteca/stock/` vídeos e imagens de banco (Mixkit, Pexels...), com `CREDITOS.md`.
- `clientes/<cliente>/` um cliente por pasta (ver o `LEIAME.md` de cada um).
- `entregues/` clientes finalizados (mover a pasta inteira para cá).
"""

LEIAME_CLIENTE = """# {nome}

**Status:** ativo · **Ferramenta:** Remotion · **Criado em:** {hoje}

## Pastas
- `01-brutos/` material cru recebido (não editar os originais)
- `02-referencias/` vídeos e posts de referência de estilo
- `03-marca/` logos, fontes, paleta, manual da marca
- `04-musica/` trilha enviada pelo cliente ou escolhida para ele
- `projeto/` projeto Remotion (código, `public/`, `out/` de testes)
- `entregas/` vídeos finais aprovados (MP4)

## Identidade (preencher antes do primeiro vídeo)
- Cores:
- Fontes:
- Tom / persona (calma, enérgica, técnica, divertida...):
- Lettering (estilo, onde fica, palavras de destaque):
- Legenda: sim / não · estilo:
- Elementos (cards, ícones, formas, transição própria):
- Música: cliente manda / escolhemos (gênero preferido: ) / sem música
- Fechamento (logo, CTA, contatos):

## Regras do cliente
- (ex.: nome da marca sempre completo, marcas que não podem aparecer, o que já foi reprovado)

## Como abrir
```
cd projeto
npm install      (só na primeira vez)
npm run dev      (abre o editor)
npx remotion render src/index.ts <Composicao> "../entregas/<nome>.mp4"
```
"""

HISTORICO_CLIENTE = """# Histórico de material usado

Antes de escolher takes, b-roll, cenas ou música, conferir aqui: material que já saiu em
vídeo entregue NÃO se repete (só efeitos sonoros podem repetir).

| Data | Vídeo | Takes / b-roll usados | Música | Observações do cliente |
|---|---|---|---|---|
"""


def ler_config():
    try:
        with open(CONFIG, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def salvar_config(cfg):
    os.makedirs(os.path.dirname(CONFIG), exist_ok=True)
    with open(CONFIG, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def raiz_ou_sair():
    raiz = ler_config().get("raiz")
    if not raiz or not os.path.isdir(raiz):
        raise SystemExit("Estúdio ainda não criado. Rode: python estudio.py criar [--raiz PASTA]")
    return raiz


def slug(nome):
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "cliente"


def escrever_se_nao_existe(caminho, texto):
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(texto)


def cmd_onde(_):
    raiz = ler_config().get("raiz")
    if raiz and os.path.isdir(raiz):
        print(f"Estúdio: {raiz}")
    else:
        print("Estúdio não criado ainda.")


def cmd_criar(a):
    raiz = os.path.abspath(os.path.expanduser(a.raiz or RAIZ_PADRAO))
    for cat in CATEGORIAS_SFX + ["_normalizados"]:
        os.makedirs(os.path.join(raiz, "_biblioteca", "sfx", cat), exist_ok=True)
    for p in ("musicas", "stock"):
        os.makedirs(os.path.join(raiz, "_biblioteca", p), exist_ok=True)
        escrever_se_nao_existe(os.path.join(raiz, "_biblioteca", p, "CREDITOS.md"),
                               "# Créditos\n\n| Arquivo | Origem (URL) | Autor | Licença |\n|---|---|---|---|\n")
    for p in ("clientes", "entregues"):
        os.makedirs(os.path.join(raiz, p), exist_ok=True)
    escrever_se_nao_existe(os.path.join(raiz, "LEIAME.md"), LEIAME_ESTUDIO)
    salvar_config({**ler_config(), "raiz": raiz})
    print(f"Estúdio pronto em: {raiz}")
    vazias = [c for c in CATEGORIAS_SFX if not os.listdir(os.path.join(raiz, "_biblioteca", "sfx", c))]
    if vazias:
        print("Categorias de SFX vazias: " + ", ".join(vazias))


def cmd_cliente(a):
    raiz = raiz_ou_sair()
    pasta = os.path.join(raiz, "clientes", slug(a.nome))
    for p in PASTAS_CLIENTE:
        os.makedirs(os.path.join(pasta, p), exist_ok=True)
    escrever_se_nao_existe(os.path.join(pasta, "LEIAME.md"),
                           LEIAME_CLIENTE.format(nome=a.nome, hoje=date.today().strftime("%d/%m/%Y")))
    escrever_se_nao_existe(os.path.join(pasta, "historico.md"), HISTORICO_CLIENTE)
    print(f"Cliente pronto em: {pasta}")


def cmd_clientes(_):
    raiz = raiz_ou_sair()
    for grupo in ("clientes", "entregues"):
        nomes = sorted(os.listdir(os.path.join(raiz, grupo)))
        print(f"{grupo}: " + (", ".join(nomes) if nomes else "(nenhum)"))


def pico_db(arquivo):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", arquivo, "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else None


def cmd_normalizar(a):
    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg não encontrado no PATH.")
    raiz = raiz_ou_sair()
    base = os.path.join(raiz, "_biblioteca", "sfx")
    saida_base = os.path.join(base, "_normalizados")
    feitos = 0
    for cat in sorted(os.listdir(base)):
        if cat.startswith("_") or not os.path.isdir(os.path.join(base, cat)):
            continue
        for nome in sorted(os.listdir(os.path.join(base, cat))):
            if not nome.lower().endswith(AUDIO):
                continue
            ent = os.path.join(base, cat, nome)
            os.makedirs(os.path.join(saida_base, cat), exist_ok=True)
            sai = os.path.join(saida_base, cat, os.path.splitext(nome)[0] + ".wav")
            if os.path.exists(sai) and not a.refazer:
                continue
            pico = pico_db(ent)
            if pico is None:
                print(f"  pulei (sem áudio): {cat}/{nome}")
                continue
            ganho = a.pico - pico
            subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", ent,
                            "-af", f"volume={ganho:.2f}dB", "-ar", "48000", sai], check=True)
            feitos += 1
    print(f"{feitos} SFX nivelados em {saida_base} (pico {a.pico} dBFS).")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Organização do estúdio de edição")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("onde").set_defaults(f=cmd_onde)
    p = sub.add_parser("criar"); p.add_argument("--raiz"); p.set_defaults(f=cmd_criar)
    p = sub.add_parser("cliente"); p.add_argument("nome"); p.set_defaults(f=cmd_cliente)
    sub.add_parser("clientes").set_defaults(f=cmd_clientes)
    p = sub.add_parser("normalizar-sfx")
    p.add_argument("--pico", type=float, default=-3.0, help="pico alvo em dBFS (padrão -3)")
    p.add_argument("--refazer", action="store_true")
    p.set_defaults(f=cmd_normalizar)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
