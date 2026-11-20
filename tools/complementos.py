"""
Empacota os complementos (skills de terceiros) dentro do plugin Editor Pro.
Ferramenta de manutenção do repositório: não é usada pelo Claude durante a edição.

Uso:
  python tools/complementos.py --fonte <pasta com os clones>   # usa clones já baixados
  python tools/complementos.py                                  # baixa (git clone --depth 1) numa pasta temporária

Copia só o que cada skill usa (sem demos, GIFs, vídeos e documentação do site),
mantém LICENSE/NOTICE de cada projeto e regenera THIRD_PARTY_NOTICES.md.
Nenhum código dos complementos é executado.
"""
import argparse
import fnmatch
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "plugins", "editor-pro-bylincu", "skills")

# repo, pasta da skill no repo, pasta destino, pastas extras da raiz do repo, licença
COMPLEMENTOS = [
    ("Vibha-Ramprakash/claude-video-effects", ".", "effects", [], "MIT"),
    ("iart-ai/kinetic-typography-skills", "skills/kinetic-typography", "kinetic-typography", ["scripts"], "MIT"),
    ("bangtutorial/bang-motion", ".", "bang-motion", [], "MIT"),
    ("Tejashmakwana/motionmaxxing", ".", "motionmaxxing", [], "Apache-2.0"),
    ("echris6/motion-video-kit", "business-motion-film", "business-motion-film", [], "MIT"),
    ("AbubakrChan/product-launch-motion", ".", "product-launch-motion", [], "MIT"),
    ("nolangz/pixel2motion", ".", "pixel2motion", [], "MIT"),
    ("diffusionstudio/lottie", "skills/text-to-lottie", "text-to-lottie", [], "MIT"),
]

IGNORAR_DIRS = {".git", ".github", "docs", "legacy", "evals", "gallery", "demo", "demos", ".claude-plugin",
                ".codex-plugin", "node_modules", "__pycache__", "agents", "tests"}
IGNORAR_ARQ = ["*.gif", "*.mp4", "*.mov", "*.webm", "*.webp", "README*", "CHANGELOG*", "CONTRIBUTING*",
               "showcase.*", "preview.*", ".gitignore", ".gitattributes", "install.sh", "*.psd"]
LICENCAS = ["LICENSE", "LICENSE.md", "LICENSE.txt", "NOTICE", "NOTICE.md"]


def ignorar(_dir, nomes):
    fora = set()
    for n in nomes:
        caminho = os.path.join(_dir, n)
        if os.path.isdir(caminho) and n in IGNORAR_DIRS:
            fora.add(n)
        elif os.path.isfile(caminho) and any(fnmatch.fnmatch(n, p) for p in IGNORAR_ARQ):
            fora.add(n)
    return fora


def commit(pasta):
    r = subprocess.run(["git", "-C", pasta, "rev-parse", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip()[:12] or "?"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonte", help="pasta onde estão os clones (um subdiretório por repositório)")
    a = ap.parse_args()
    fonte = a.fonte or tempfile.mkdtemp(prefix="complementos-")
    linhas = []
    for repo, sub, alvo, extras, lic in COMPLEMENTOS:
        clone = os.path.join(fonte, repo.split("/")[1])
        if not os.path.isdir(clone):
            subprocess.run(["git", "-c", "core.longpaths=true", "clone", "-q", "--depth", "1",
                            f"https://github.com/{repo}.git", clone], check=True)
        origem = os.path.normpath(os.path.join(clone, sub))
        dest = os.path.join(DESTINO, alvo)
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        shutil.copytree(origem, dest, ignore=ignorar)
        for extra in extras:
            src = os.path.join(clone, extra)
            if os.path.isdir(src) and not os.path.exists(os.path.join(dest, extra)):
                shutil.copytree(src, os.path.join(dest, extra), ignore=ignorar)
        for nome in LICENCAS:
            src = os.path.join(clone, nome)
            if os.path.isfile(src) and not os.path.exists(os.path.join(dest, nome)):
                shutil.copy2(src, os.path.join(dest, nome))
        tam = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(dest) for f in fs)
        sha = commit(clone)
        linhas.append(f"| `{alvo}` | [{repo}](https://github.com/{repo}) | `{sha}` | {lic} |")
        print(f"ok {alvo:24s} {tam / 1e6:5.1f} MB  {repo}@{sha}")
    with open(os.path.join(RAIZ, "THIRD_PARTY_NOTICES.md"), "w", encoding="utf-8") as f:
        f.write("# Complementos de terceiros\n\n"
                "Estas skills vêm dos projetos abaixo, copiadas sem alterações no código (só ficaram de fora demos, "
                "GIFs, vídeos e documentação do site). Cada pasta mantém a licença original (LICENSE/NOTICE). "
                "Os direitos são dos autores.\n\n"
                "| Pasta em `plugins/editor-pro-bylincu/skills/` | Projeto | Versão (commit) | Licença |\n|---|---|---|---|\n"
                + "\n".join(linhas) + "\n\n"
                "O **remotion-director** (github.com/Zane-0x5a/remotion-director, MIT) é instalado direto do "
                "repositório do autor pelo marketplace `bylincu`.\n")
    print("THIRD_PARTY_NOTICES.md atualizado")


if __name__ == "__main__":
    main()
