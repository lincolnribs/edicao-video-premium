# Banco de mídia: SFX, trilhas e b-roll

Tudo grátis para uso comercial. Registre a origem de cada arquivo no `CREDITOS.md` da pasta da biblioteca (arquivo, URL, autor, licença). Peça permissão ao usuário antes de baixar.

## Mixkit (principal)
Licença Mixkit: uso comercial grátis, sem atribuição obrigatória (não pode revender o arquivo solto).

- **Busca:** skill `assetseeker` (tem busca no Mixkit) ou as páginas:
  - Vídeos: `https://mixkit.co/free-stock-video/<termo>/`
  - Músicas por tag: `https://mixkit.co/free-stock-music/tag/<tag>/` (ex.: corporate, funk, hip-hop, chill, inspiring, cinematic, electronic, acoustic)
  - Efeitos: `https://mixkit.co/free-sound-effects/<categoria>/` (ex.: whoosh, click, pop, transition, notification, swoosh)
- **Download direto pelo ID** (o número na URL do item):
  - Vídeo: `https://assets.mixkit.co/videos/<ID>/<ID>-1080.mp4` (se falhar, `-720.mp4`)
  - Música: `https://assets.mixkit.co/music/<ID>/<ID>.mp3`
  - Efeito: `https://assets.mixkit.co/active_storage/sfx/<ID>/<ID>-preview.mp3`
- B-roll horizontal num vídeo vertical: nunca esticar; usar recorte 9:16 do centro de interesse, card, ou tela dividida.

## Outras fontes
- **Pexels / Pixabay** (vídeo e imagem), **Freesound** (SFX, conferir se a licença é CC0), pela skill `assetseeker`.
- **`@remotion/sfx`**: alguns sons prontos (whoosh, whip, ding, clique de mouse, virar página, switch). Bom para começar quando a biblioteca está vazia.

## Biblioteca inicial de SFX (quando o usuário não tem nenhuma)
Baixe 3 a 5 sons por categoria para `_biblioteca/sfx/<categoria>/` e rode `python scripts/estudio.py normalizar-sfx`:

| Categoria | Quando usar |
|---|---|
| whoosh | entrada de lettering, troca de cena, zoom |
| transicao | transições de cena maiores |
| pop | card/ícone aparecendo |
| click | botão, seleção, check |
| ding | destaque de número, preço, acerto |
| impacto | palavra forte, revelação (com moderação) |
| sucesso | conclusão, CTA |
| digitacao | legenda digitando, busca |
| ambiente | ar de fundo em telas de motion sem voz |

## Trilha sonora
- **Sempre sugerir** e perguntar gênero/tema antes. Ofereça 2 a 3 opções do Mixkit (nome + link de prévia) para o usuário escolher.
- Ideias por tema: varejo/ferramentas → groove/funk leve; saúde/clínica → piano/ambient suave; corporativo/serviços → corporate/inspiring; comida → acústico/chill alegre; promoção/Black Friday → eletrônico/hip-hop com batida.
- Nunca reutilizar a mesma música em dois vídeos do mesmo cliente (conferir `historico.md`).
- Salve em `clientes/<cliente>/04-musica/` (ou `_biblioteca/musicas/`) com crédito.

## Volumes (medir, não chutar)
- Voz: ≈ -14 LUFS integrado, estéreo.
- SFX: ≈ 30% do nível da voz (≈ -8 a -10 dB abaixo; com voz a -14 LUFS, SFX perto de -24 a -26 LUFS). Todos no mesmo nível. Pico alinhado à ação na tela (+1 frame).
- Trilha: ≈ 0.07 a 0.11 de volume no Remotion sob a voz (≈ -30 a -33 LUFS), fade-in curto, fade-out no fechamento; pode subir um pouco onde não há fala.
- Medir: `ffmpeg -i final.mp4 -af ebur128 -f null -` (linha "I:" no resumo). Para medir um trecho só: `-ss <ini> -t <dur>` antes do `-i`.
