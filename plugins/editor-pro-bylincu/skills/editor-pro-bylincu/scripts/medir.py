"""
Mede volume (LUFS) e imprime UMA linha por arquivo, em vez das milhares de linhas do ebur128.

Uso:
  python medir.py final.mp4 [outro.wav ...]
  python medir.py final.mp4 --ini 12.5 --dur 3      # só um trecho
"""
import argparse
import re
import subprocess
import sys


def medir(arquivo, ini=None, dur=None):
    cmd = ["ffmpeg", "-hide_banner", "-nostats"]
    if ini is not None:
        cmd += ["-ss", str(ini)]
    if dur is not None:
        cmd += ["-t", str(dur)]
    cmd += ["-i", arquivo, "-map", "a:0", "-af", "ebur128=peak=true", "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    resumo = r.stderr[r.stderr.rfind("Summary:"):] if "Summary:" in r.stderr else ""
    if not resumo:
        return f"{arquivo}: sem áudio ou erro ({r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'ffmpeg falhou'})"
    pega = lambda rotulo: (re.search(rotulo + r":\s*(-?[\d.]+|-inf)", resumo) or [None, "?"])[1]
    return f"{arquivo}: integrado {pega('I')} LUFS | pico {pega('Peak')} dBTP | faixa {pega('LRA')} LU"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivos", nargs="+")
    ap.add_argument("--ini", type=float)
    ap.add_argument("--dur", type=float)
    a = ap.parse_args()
    for f in a.arquivos:
        print(medir(f, a.ini, a.dur))


if __name__ == "__main__":
    main()
