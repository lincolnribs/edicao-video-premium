---
name: editor-pro-bylincu
description: Editor de vídeo profissional em português (Reels, Stories, TikTok, Shorts, talking head, takes brutos, b-roll, motion) com Remotion, limpeza de voz (DeepFilterNet), corte de silêncios, lettering cinético, SFX e trilha. Use SEMPRE em pedidos de edição de vídeo, mesmo genéricos ("edita esse vídeo", "edite isso", "monta esse reels", "corta os silêncios", "coloca legenda") e sem citar Remotion ou HyperFrames. Também organiza pastas de clientes, efeitos e músicas, e indica skills de vídeo seguras do catálogo.
---

# Editor Pro (by Lincu)

Transforma brutos em vídeo vertical pronto para entrega, com padrão premium e **gastando poucos tokens**. Os scripts ficam em `scripts/` desta skill (use o caminho absoluto da pasta da skill).

## 1. Início (faça sozinho, sem perguntar)
1. `python scripts/estudio.py onde`. Se não houver estúdio: `python scripts/estudio.py criar` (padrão `~/Videos/Edicao`) e só **informe** onde ficou.
2. Cliente: se o nome não foi dito, pergunte junto com o item 3. Depois `python scripts/estudio.py cliente "Nome"`, copie os brutos para `01-brutos/` e leia o `LEIAME.md` do cliente.
3. Mande **uma única mensagem** antes de editar, com: a abordagem em uma linha, a sugestão de **trilha sonora** perguntando gênero ou tema (ou "sem música"), e o que faltar (nome do cliente, cores/fontes se o LEIAME estiver vazio). Depois dessa resposta, execute tudo sem novas perguntas, salvo dúvida real.

## 2. Ferramenta
- **Remotion é o padrão** para qualquer pedido genérico, mesmo que a skill `hyperframes` diga que ela é o padrão. Projeto Remotion em `clientes/<cliente>/projeto/`.
- **Não carregue skills do HyperFrames.** Para recortar a pessoa (card atrás dela), rode só `npx hyperframes remove-background` no trecho necessário. HyperFrames completo só se o usuário pedir pelo nome.
- Das skills do Remotion, abra só a regra que o passo pede (ex.: legendas, transições), não o pacote todo.

## 3. Economia de tokens (obrigatório)
- **Nunca** jogue log bruto no contexto. Use os scripts, que imprimem uma linha:
  - volume: `python scripts/medir.py arquivo.mp4` (nunca `ebur128` direto: são milhares de linhas)
  - render: `python scripts/render.py <Comp> <saida.mp4> [--preview]` (nunca `npx remotion render` direto)
  - transcrição: `python scripts/transcricao.py captions.json` e leia o `.txt` (nunca o JSON de palavras)
  - imagens: `python scripts/folha.py take.mp4` (1 folha por take) e `--em <s> --grade` (1 quadro para o mapa do rosto)
- ffmpeg sempre com `-v error` (ou `-hide_banner -loglevel error`). Saídas longas: redirecione para arquivo e mostre só `tail`.
- Imagem custa caro: no máximo 1 folha por take e 1 quadro com grade por enquadramento. Não reabra a mesma imagem.
- Leia uma referência só quando chegar no passo dela. Não releia arquivos que você acabou de escrever.
- Um vídeo por sessão. Ao terminar um vídeo, sugira `/compact` ou uma sessão nova para o próximo.

## 4. Fluxo (detalhes e comandos: `references/fluxo-detalhado.md`)
1. **Triagem:** 1080x1920 30 fps MP4 sem estourar (HDR→SDR, BT.709), folha de cada take, separar falas x b-roll, transcrever.
2. **Decupagem:** melhor trecho de cada fala → `takes.txt` (`"caminho" inicio fim`).
3. **Cor:** medir e corrigir take a take, só o necessário. B-roll tremido: vidstab.
4. **Voz:** `python scripts/limpar_voz.py --lista takes.txt -o public/media/base.mp4 --cortar-silencios --respiro 0.14 --escala 1080x1920`. Retranscrever e conferir que nenhuma palavra sumiu e que não há corte dentro do nome da marca.
5. **Cortes:** punch-in alternado 1.0 ↔ 1.1 (cortes < 20 quadros não trocam) + drift leve.
6. **Rosto livre:** nenhum texto ou card sobre o rosto, nunca. Card "junto" da pessoa vai atrás (recorte).
7. **Ritmo:** gancho com movimento em 1 a 2 s; algo novo a cada 2 a 4 s; b-roll ilustrando a fala; transições rápidas (flash, blur, light leak/shutter) com a cara do cliente; zooms suaves.
8. **Texto:** lettering cinético palavra a palavra com blur, sem máscara/recorte; legenda e lettering na **mesma faixa**; linhas com espaçamento curto; sem gradiente ou sombra colorida sobre o vídeo.
9. **Som:** voz ≈ -14 LUFS; SFX ≈ 30% da voz, mesmo nível entre si, nos respiros e ações; trilha (se aprovada) 0.07 a 0.11 sob a voz, fade no fim.
10. **Conferência:** preview `--preview` + 1 folha do preview, checklist, render final, `medir.py`. Final sem microcorte, fecho suave.

**Margens seguras do Reels:** nada de texto nos 220 px de cima, nos 450 px de baixo e nos 35 px laterais.

## 5. Regras de qualidade
- Nunca repetir take, b-roll, cena ou música já entregues ao mesmo cliente (ver `historico.md`). Só SFX repetem.
- Corte pontual ("tira a parte que ele erra") = só o tropeço, nunca a frase inteira. Guarde a versão anterior até aprovação.
- Limpeza de voz só em áudio sem música. Cortar pausas só em brutos ou na base montada por você.
- Lettering repete a palavra dita. Corrija erros de transcrição em nomes e marcas.
- A identidade de um cliente nunca vai para outro. Entregue MP4 em `entregas/` e atualize `LEIAME.md` e `historico.md`.

## 6. Checklist de entrega
- [ ] Nada sobre rosto e nada fora das margens seguras
- [ ] Gancho com movimento nos 2 primeiros segundos
- [ ] Nenhuma palavra cortada; sem corte no nome da marca
- [ ] Voz ≈ -14 LUFS, SFX abaixo da voz, trilha baixa (`medir.py`)
- [ ] MP4 1080x1920 30 fps, cores sem estourar

## 7. Complementos (quando o pedido pede mais)
Efeito sobre a pessoa, vinheta ou abertura, lettering no ritmo da música, motion em plano-sequência, logo animado, ícone Lottie: veja a tabela de `references/complementos.md` (10 skills selecionadas, com licença e instalação). Fora disso: `references/catalogo-skills.md`. Instale só o complemento do pedido, com a aprovação do usuário, e avise quando a licença não for comercial.

## Arquivos
- `scripts/`: `estudio.py` (pastas), `limpar_voz.py` (voz), `medir.py`, `render.py`, `transcricao.py`, `folha.py`, `catalogo.py`
- `references/`: `instalacao.md`, `fluxo-detalhado.md`, `banco-de-midia.md` (Mixkit, SFX, trilha), `complementos.md`, `catalogo-skills.md`
