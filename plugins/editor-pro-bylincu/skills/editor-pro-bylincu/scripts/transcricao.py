"""
Converte o JSON de palavras do Whisper em texto curto por frase (com tempos).
Leia o .txt gerado, nunca o JSON (o JSON tem 10x mais tokens).

Aceita: lista de captions do Remotion ({text, startMs, endMs}), whisper.cpp ({transcription:[{offsets,text}]}),
ou lista de palavras ({word|text, start, end} em segundos).

Uso:
  python transcricao.py captions.json            # gera captions.txt e imprime o caminho + nº de palavras
  python transcricao.py captions.json --mostrar  # também imprime o texto
  python transcricao.py captions.json --pausa 0.5 --max 12
"""
import argparse
import json
import os
import sys


def palavras(dados):
    if isinstance(dados, dict):
        for chave in ("captions", "words", "segments", "transcription", "chunks"):
            if isinstance(dados.get(chave), list):
                return palavras(dados[chave])
        return []
    saida = []
    for p in dados:
        texto = (p.get("text") or p.get("word") or "").strip()
        if not texto:
            continue
        if "startMs" in p:
            ini, fim = p["startMs"] / 1000, p.get("endMs", p["startMs"]) / 1000
        elif "offsets" in p:
            ini, fim = p["offsets"]["from"] / 1000, p["offsets"]["to"] / 1000
        elif "timestamp" in p and isinstance(p["timestamp"], (list, tuple)):
            ini, fim = p["timestamp"][0], p["timestamp"][1] or p["timestamp"][0]
        else:
            ini, fim = float(p.get("start", 0)), float(p.get("end", p.get("start", 0)))
        saida.append((ini, fim, texto))
    return saida


def mmss(t):
    return f"{int(t // 60):02d}:{t % 60:04.1f}"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--pausa", type=float, default=0.45, help="pausa (s) que quebra a frase")
    ap.add_argument("--max", type=int, default=14, help="máximo de palavras por linha")
    ap.add_argument("--mostrar", action="store_true")
    a = ap.parse_args()
    with open(a.json, encoding="utf-8-sig") as f:
        ws = palavras(json.load(f))
    linhas, atual = [], []
    for w in ws:
        if atual and (w[0] - atual[-1][1] > a.pausa or len(atual) >= a.max):
            linhas.append(atual)
            atual = []
        atual.append(w)
    if atual:
        linhas.append(atual)
    texto = "\n".join(f"[{mmss(l[0][0])}-{mmss(l[-1][1])}] " + " ".join(w[2] for w in l) for l in linhas)
    saida = os.path.splitext(a.json)[0] + ".txt"
    with open(saida, "w", encoding="utf-8") as f:
        f.write(texto + "\n")
    print(f"ok: {saida} ({len(ws)} palavras, {len(linhas)} frases)")
    if a.mostrar:
        print(texto)


if __name__ == "__main__":
    main()
