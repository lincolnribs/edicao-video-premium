"""
Gera UMA imagem pequena para olhar o vídeo gastando poucos tokens.

Uso:
  python folha.py take.mp4                    # folha de contato: até 20 quadros em grade 5x4, 180 px cada
  python folha.py take.mp4 --quadros 12       # menos quadros (mais barato)
  python folha.py take.mp4 --em 12.5 --grade  # um quadro só, com grade a cada 100 px (mapa do rosto)

Imprime só o caminho da imagem. Abra a imagem uma vez; não gere várias do mesmo take.
"""
import argparse
import os
import subprocess
import sys


def duracao(v):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v],
                       capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--quadros", type=int, default=20)
    ap.add_argument("--em", type=float, help="segundo de um quadro único")
    ap.add_argument("--grade", action="store_true", help="linhas a cada 100 px (coordenadas do vídeo original)")
    ap.add_argument("-o", "--saida")
    a = ap.parse_args()
    os.makedirs(".work", exist_ok=True)
    base = os.path.splitext(os.path.basename(a.video))[0]
    if a.em is not None:
        saida = a.saida or os.path.join(".work", f"quadro-{base}-{a.em:g}.jpg")
        vf = ("drawgrid=w=iw:h=100:t=2:c=red@0.7," if a.grade else "") + "scale=360:-2"
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(a.em), "-i", a.video, "-frames:v", "1", "-vf", vf, "-q:v", "4", saida]
    else:
        n = max(1, min(a.quadros, 30))
        cols = min(5, n)
        rows = -(-n // cols)
        intervalo = max(duracao(a.video) / n, 0.1)
        saida = a.saida or os.path.join(".work", f"folha-{base}.jpg")
        vf = f"fps=1/{intervalo:.3f},scale=180:-2,tile={cols}x{rows}"
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", a.video, "-vf", vf, "-frames:v", "1", "-q:v", "5", saida]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit("ffmpeg falhou: " + r.stderr.strip()[-300:])
    print(saida)


if __name__ == "__main__":
    main()
