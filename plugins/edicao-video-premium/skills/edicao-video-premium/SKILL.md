---
name: edicao-video-premium
description: Padrão de edição premium de vídeos verticais (Reels, Stories, TikTok, talking head, takes brutos, b-roll, motion) com Remotion, limpeza de voz por DeepFilterNet, corte de silêncios, lettering cinético, SFX e trilha do Mixkit. Use SEMPRE que pedirem para editar um vídeo de forma genérica ("edita esse vídeo", "edite isso", "monta esse reels", "faz a edição desses takes", "deixa esse vídeo profissional", "corta os silêncios", "coloca lettering/legenda"), mesmo sem citar Remotion ou HyperFrames. Também organiza as pastas de clientes, efeitos sonoros e músicas para quem ainda não tem.
---

# Edição de vídeo premium

Fluxo completo para transformar brutos em vídeo vertical pronto para entrega, com o mesmo padrão de qualidade em todo cliente.

## Regra 1: ferramenta padrão é o Remotion

- Pedido genérico ("edita esse vídeo", "edite isso", "faz um reels com isso") = **Remotion**, com as skills do plugin Remotion (`remotion-best-practices` como porta de entrada, `remotion-create`, `remotion-captions`, `remotion-render`).
- Isso vale **mesmo que a skill `hyperframes` diga que é o framework padrão**. Esta skill tem prioridade para edição de vídeo.
- Use HyperFrames só quando o usuário pedir HyperFrames pelo nome, ou como ferramenta auxiliar: `npx hyperframes remove-background` para recortar a pessoa e colocar card atrás dela.
- Se o projeto do cliente já existe em outra ferramenta (o `LEIAME.md` diz qual), continue nela.

## Regra 2: conversar antes de executar

1. Diga em uma linha a abordagem (ex.: "vou usar Remotion + limpeza de voz + lettering cinético") e pergunte se é válido.
2. **Sempre sugira trilha sonora** e pergunte o gênero ou tema (ex.: corporativo leve, groove/funk animado, eletrônico, lo-fi, acústico, inspiracional, cinematográfico, sem música). Se o cliente já mandou a música ou pediu sem música, respeite. Nunca escolha música sozinho sem perguntar.
3. Responda no idioma do usuário. Em textos que vão para a tela em português: "para" (nunca "pra") e sem travessão.

## Regra 3: organização (antes do primeiro vídeo)

O usuário pode não ter nenhuma pasta pronta. Rode o organizador (script desta skill, use o caminho absoluto da pasta da skill):

```bash
python scripts/estudio.py onde                      # já existe estúdio?
python scripts/estudio.py criar                     # cria em ~/Videos/Edicao (ou --raiz "outra pasta"; pergunte onde ele prefere)
python scripts/estudio.py cliente "Nome do Cliente" # pasta do cliente + LEIAME.md + historico.md
python scripts/estudio.py normalizar-sfx            # nivela os SFX baixados
```

Estrutura criada:

```
Edicao/
  _biblioteca/sfx/{whoosh,pop,click,ding,impacto,sucesso,transicao,digitacao,ambiente}/ + _normalizados/
  _biblioteca/musicas/  (com CREDITOS.md)
  _biblioteca/stock/    (com CREDITOS.md)
  clientes/<cliente>/{01-brutos,02-referencias,03-marca,04-musica,projeto,entregas}/ + LEIAME.md + historico.md
  entregues/
```

- **Biblioteca de SFX vazia?** Monte uma inicial antes de editar (ver `references/banco-de-midia.md`: Mixkit, Freesound pela skill `assetseeker`, ou os sons do `@remotion/sfx`). Use sempre os arquivos de `_normalizados/`.
- Copie os brutos que o usuário enviar para `01-brutos/` (sem alterar os originais) e crie o projeto Remotion dentro de `projeto/`.
- **Antes de editar um cliente, leia o `LEIAME.md` dele.** Se a seção "Identidade" estiver vazia, pergunte cores, fontes, tom e referências (ou extraia de `02-referencias/` e `03-marca/`) e preencha. A identidade de um cliente nunca se copia para outro.
- Ao entregar: atualize `LEIAME.md` (como renderizar, decisões) e `historico.md` (takes, b-roll e música usados, feedback).

## O fluxo (10 passos)

Detalhes, comandos ffmpeg e receitas Remotion em `references/fluxo-detalhado.md`.

1. **Triagem:** converter para 1080x1920 30 fps MP4 (respeitar rotação, sem estourar a imagem: HDR → SDR, BT.709, faixa limitada). Contact sheet de cada take, separar falas x b-roll, transcrever as falas (Whisper).
2. **Decupagem:** escolher o melhor trecho de cada fala (sem tropeços e repetições) → `takes.txt` com `"caminho" inicio fim`.
3. **Cor:** medir cada take e corrigir só o necessário, take a take (nada de filtro igual para tudo). B-roll tremido: estabilizar (vidstab).
4. **Voz:** `python scripts/limpar_voz.py --lista takes.txt -o base.mp4 --cortar-silencios --respiro 0.14 --escala 1080x1920` (DeepFilterNet + corte de pausas, gera `base.cortes.json`). Todo talking head bruto passa por isso. Retranscrever a base e conferir que nenhuma palavra sumiu e que não há corte no meio do nome da marca.
5. **Cortes:** punch-in alternado (1.0 ↔ 1.1; cortes com menos de 20 frames não trocam) + leve drift dentro do plano.
6. **Rosto livre:** mapear o rosto em cada plano (stills com grade). Nenhum texto, legenda ou card sobre o rosto, nunca. Card "junto" da pessoa vai atrás dela (recorte).
7. **Ritmo:** gancho com movimento em 1 a 2 s; algo novo a cada 2 a 4 s; b-roll e telas de motion nos argumentos; transições com a cara do cliente.
8. **Texto:** lettering cinético sincronizado à fala, entrada palavra a palavra com blur, sem máscara/recorte. Poucas palavras por vez, espaçamento apertado, repetir a palavra dita. Legenda discreta só onde não há lettering e só se o cliente usa legenda.
9. **Som:** voz ≈ -14 LUFS estéreo; SFX abaixo da voz (≈30% do nível), mesmo volume entre si, poucos e sutis, nos respiros e ações; trilha (se aprovada) ≈ 0.07 a 0.11 de volume sob a voz, com fade no fim.
10. **Conferência:** preview em baixa (`--scale=0.4`) + contact sheet, checklist abaixo, render final MP4, medir volume (`ffmpeg -i final.mp4 -af ebur128 -f null -`).

## Regras de qualidade (valem para todos)

- Nunca repetir take, b-roll, cena ou música já usados em vídeo entregue do mesmo cliente (conferir `historico.md` e `entregas/`). Só SFX repetem. Manter a identidade, inovar no motion.
- Corte pontual pedido ("tira a parte que ele erra") = remover só o tropeço, nunca a frase inteira. Medir o áudio, mostrar o que sai, guardar cópia da versão anterior até aprovação.
- Limpeza de voz só em áudio SEM música mixada. Cortar pausas só em brutos ou na base montada por você (muda a duração).
- Footage de baixa qualidade não fica esticado em tela cheia.
- Em motion com tipografia na tela, sem legenda de apoio (a não ser que peçam).
- Corrigir erros de transcrição em nomes próprios e marcas.
- Entrega: vídeo com voz + SFX (+ trilha, se aprovada). Se o usuário for mexer no som depois, entregar também `Separados/` (vídeo mudo, `Falas.wav`, `Efeitos Sonoros.wav`, `Trilha.wav`).

## Checklist antes de entregar

- [ ] Nenhum texto/card sobre rosto (stills de todo plano com pessoa)
- [ ] Gancho com movimento nos primeiros 2 s
- [ ] Nenhuma palavra cortada; sem corte dentro do nome da marca
- [ ] Nada sobreposto (gráfico e texto não disputam a mesma área)
- [ ] Voz ≈ -14 LUFS; SFX abaixo da voz; trilha baixa
- [ ] MP4 1080x1920 30 fps, cores sem estourar
- [ ] `LEIAME.md` e `historico.md` do cliente atualizados

## Arquivos desta skill

- `scripts/estudio.py` organização de pastas, clientes e biblioteca de SFX
- `scripts/limpar_voz.py` DeepFilterNet + corte de silêncios + loudnorm
- `references/instalacao.md` o que instalar (primeira vez)
- `references/fluxo-detalhado.md` comandos e receitas de cada passo
- `references/banco-de-midia.md` Mixkit, SFX, trilhas, créditos e volumes
