"""
Busca no catálogo de skills de vídeo (526 repositórios, com nota de segurança) sem carregar o arquivo inteiro.
Fonte: awesome-claude-video-skills (CC0). Por padrão mostra só os marcados como SAFE.

Uso:
  python catalogo.py tipos
  python catalogo.py tipo shorts [--top 10]
  python catalogo.py busca "talking head" [--top 10] [--todos]   # --todos inclui os CAUTION
"""
import argparse
import json
import os
import sys

ARQ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "catalogo.json"))
NOMES = {
    "general": "Frameworks e kits", "promo": "Promo e demos", "explainer": "Explicativos",
    "editing": "Edição", "shorts": "Shorts e redes", "avatar": "Avatares", "story": "Histórias e animação",
    "motion": "Motion graphics", "craft": "Roteiro e estudo", "music": "Clipes musicais",
}


def linha(i):
    desc = (i.get("description") or "").replace("\n", " ")
    desc = desc[:110] + ("…" if len(desc) > 110 else "")
    alerta = "" if i["security_grade"] == "safe" else " [CAUTION]"
    return f"{i['repo_full_name']} ★{i['stars']} {i.get('license') or '?'}{alerta} | {desc}"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("acao", choices=["tipos", "tipo", "busca"])
    ap.add_argument("termo", nargs="?")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--todos", action="store_true")
    a = ap.parse_args()
    with open(ARQ, encoding="utf-8") as f:
        dados = json.load(f)
    itens = [i for i in dados["skills"] if a.todos or i["security_grade"] == "safe"]
    if a.acao == "tipos":
        for k in dados["kinds"]:
            n = sum(1 for i in itens if i["kind"] == k["id"])
            print(f"{k['id']}: {NOMES.get(k['id'], k['en'])} ({n})")
        print(f"catálogo de {dados.get('generated', '?')}")
        return
    if not a.termo:
        raise SystemExit("informe o tipo ou o termo de busca")
    if a.acao == "tipo":
        sel = [i for i in itens if i["kind"] == a.termo]
    else:
        termos = a.termo.lower().split()
        sel = [i for i in itens if all(t in (i["repo_full_name"] + " " + (i.get("description") or "")).lower() for t in termos)]
    sel.sort(key=lambda i: -i["stars"])
    for i in sel[:a.top]:
        print(linha(i))
    print(f"({min(len(sel), a.top)} de {len(sel)})")


if __name__ == "__main__":
    main()
