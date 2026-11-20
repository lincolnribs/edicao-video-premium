# Fluxo detalhado (comandos e receitas)

Trabalhe dentro de `clientes/<cliente>/projeto/`. Rascunhos e testes em `projeto/.work/` (pode apagar depois da entrega).

## 1. Triagem

**Conferir o take** (rotação, HDR, fps):
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,color_transfer,color_primaries:stream_side_data=rotation -of default=nw=1 "take.MOV"
```

**Converter para 1080x1920 30 fps MP4 sem estourar** (SDR comum):
```bash
ffmpeg -i "take.MOV" -vf "scale=1080:1920:force_original_aspect_ratio=increase:in_range=tv:out_range=tv,crop=1080:1920,fps=30,format=yuv420p" \
  -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:v libx264 -crf 16 -preset slow -c:a aac -b:a 192k public/media/take01.mp4
```
- `color_transfer` = `arib-std-b67` (HLG) ou `smpte2084` (PQ) → é HDR: antes do scale, tonemap
  `zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p`.
- Take deitado sem metadado de rotação: `transpose=1` (horário) ou `transpose=2` (anti-horário). Entrelaçado: `yadif` no início.

Todo ffmpeg com `-v error` (sem o log de progresso).

**Folha de contato** (uma imagem pequena por take, até 20 quadros):
```bash
python scripts/folha.py public/media/take01.mp4          # imprime só o caminho da imagem
```
Olhe cada folha uma vez para separar falas x b-roll, achar tomadas ruins e saber onde fica o rosto.

**Transcrever** cada fala com Whisper (skill `remotion-captions`), salvar o JSON e converter para texto curto:
```bash
python scripts/transcricao.py public/media/take01.json   # gera take01.txt: "[00:01.2-00:03.8] frase"
```
Leia o `.txt`, nunca o JSON de palavras.

## 2. Decupagem
`takes.txt`, uma linha por trecho escolhido (segundos), na ordem do vídeo:
```
"C:/caminho/01-brutos/take01.mp4" 1.20 6.85
"C:/caminho/01-brutos/take03.mp4" 0.40 9.10
```
Pule tropeços, repetições e frases que o próprio apresentador refez (fique com a melhor). Na dúvida entre duas versões, pergunte.

## 3. Cor (take a take)
Meça antes de corrigir: extraia um quadro e veja médias por canal das áreas claras (parede branca, camisa). Ex. em Python/ffmpeg: `signalstats` ou um script com Pillow.
- Amarelado (azul baixo): `colorchannelmixer=rr=0.975:bb=1.05` e tirar amarelo `huesaturation=hue=0:saturation=-0.4:colors=y` (ffmpeg 7+).
- Escuro/chapado: curva com lift suave `curves=all='0/0 0.25/0.29 0.5/0.55 1/1'`, `eq=contrast=1.03:saturation=1.06`.
- Não deixe escuro nem laranja demais: compare antes/depois lado a lado (`hstack`) e mostre ao usuário se a mudança for grande.
- **Estabilizar b-roll tremido:**
```bash
ffmpeg -i broll.mp4 -vf vidstabdetect=shakiness=6:result=.work/t.trf -f null -
ffmpeg -i broll.mp4 -vf "vidstabtransform=input=.work/t.trf:smoothing=25:zoom=3,unsharp=5:5:0.6" -c:v libx264 -crf 16 broll-estab.mp4
```

## 4. Voz e base
```bash
python scripts/limpar_voz.py --lista takes.txt -o public/media/base.mp4 --cortar-silencios --respiro 0.14 --escala 1080x1920
```
- Gera `base.mp4` (voz limpa, -14 LUFS, estéreo) + `base.cortes.json` (trechos mantidos: `arquivo`, `inicio`, `fim`, `quadro_saida`, `quadros`). Um momento `t` do take original vira o quadro `quadro_saida + (t - inicio) * 30` na base.
- Retranscreva `base.mp4` e compare com a transcrição dos takes: mesma contagem de palavras por frase. Confira que nenhum corte caiu dentro do nome da marca (ajuste o fim da palavra no `takes.txt` se preciso).
- Só limpar a voz de um vídeo já editado (sem mudar duração): sem `--cortar-silencios`.
- Ainda com eco forte: a alternativa é o Adobe Podcast Enhance (site, envia o áudio para a Adobe): o usuário decide e faz o upload.

## 5. Cortes com punch-in (Remotion)
Para cada trecho do `cortes.json`, alterne a escala no corte e faça um drift leve:
```tsx
const escalaBase = i % 2 === 0 ? 1.0 : 1.1;            // trechos < 20 quadros herdam a escala do anterior
const drift = interpolate(frame, [0, duracao], [0, 0.015]);
<div style={{transform: `scale(${escalaBase + drift})`, transformOrigin: "50% 35%"}}>
  <OffthreadVideo src={staticFile("media/base.mp4")} startFrom={inicioDoTrecho} />
</div>
```
`transformOrigin` perto dos olhos mantém o rosto no lugar.

## 6. Mapa do rosto
Gere um quadro de cada enquadramento com pessoa, com grade a cada 100 px, e anote a faixa vertical do rosto (ex.: y 290 a 630). Texto só acima da cabeça ou abaixo do queixo (peito/roupa), sempre dentro das margens seguras (220 px em cima, 450 px embaixo, 35 px nas laterais). Depois do punch-in, confira de novo (a escala move o rosto).
```bash
python scripts/folha.py public/media/base.mp4 --em 4.0 --grade   # 1 quadro pequeno com grade
```
Anote a faixa do rosto num comentário do código para não precisar abrir a imagem de novo.
Card que precisa ficar atrás da pessoa: `npx hyperframes remove-background` só no trecho necessário (corte o trecho antes), mesmo zoom do plano, e empilhe: vídeo → card → pessoa recortada.

## 7. Ritmo
- 0 a 2 s: movimento (tela de motion ilustrando a primeira frase, b-roll forte, zoom com lettering). Nunca abrir parado.
- A cada 2 a 4 s algo muda: lettering, punch-in, b-roll, card, ícone.
- Argumentos e números: b-roll ou tela de motion. Pessoa de volta nas frases de conexão e no CTA.
- Transições ligadas à marca (formas, logo, cor do cliente); flash/blur/whip com moderação.

## 8. Lettering e legenda (Remotion)
Entrada palavra a palavra com blur, sem `overflow: hidden`:
```tsx
const Palavra: React.FC<{texto: string; inicio: number}> = ({texto, inicio}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const p = spring({frame: frame - inicio, fps, config: {damping: 200}, durationInFrames: 12});
  return (
    <span style={{display: "inline-block", opacity: p, filter: `blur(${(1 - p) * 12}px)`,
                  transform: `translateY(${(1 - p) * 18}px)`, marginRight: "0.22em"}}>{texto}</span>
  );
};
```
- `inicio` de cada palavra = tempo da transcrição da base × fps (adiante 1 a 2 quadros para a palavra aparecer junto com a fala).
- 2 a 4 palavras por vez, linhas coladas (`lineHeight` 0.95 a 1.05), espaçamento apertado; destaque por peso/fonte/cor da marca, não por caixas pesadas.
- Repita a palavra dita (não troque por sinônimo ou resumo).
- Legenda (se o cliente usa): pequena, discreta, sem pontuação, só onde não há lettering.

## 9. Som (Remotion)
```tsx
<Audio src={staticFile("sfx/whoosh-01.wav")} volume={0.3} />          // a partir de _normalizados/
<Audio src={staticFile("musica/trilha.mp3")} volume={(f) => interpolate(f, [0, 15, dur - 30, dur], [0, 0.08, 0.08, 0], {extrapolateRight: "clamp"})} />
```
Copie para `public/` só os SFX/músicas usados. Depois do render, meça e ajuste: SFX ≈ 30% da voz, trilha bem baixa.

## 10. Conferência e render
```bash
python scripts/render.py <Comp> .work/preview.mp4 --preview
python scripts/folha.py .work/preview.mp4
python scripts/render.py <Comp> "../entregas/<Cliente> - <Titulo>.mp4"
python scripts/medir.py "../entregas/<Cliente> - <Titulo>.mp4"
```
O `render.py` guarda o log em `.work/render.log` e só mostra as últimas linhas se der erro.
Passe o checklist do `SKILL.md`, atualize `LEIAME.md` e `historico.md`, e mostre ao usuário onde está o arquivo.
