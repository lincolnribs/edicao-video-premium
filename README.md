# Editor Pro by Lincu

Editor de vídeo profissional em português para o Claude Code. Você manda os brutos, pede **"edita esse vídeo"** e ele entrega o Reels pronto.

- **Ativa sozinho:** reconhece pedidos de edição de vídeo e entra em ação, sem precisar chamar
- **Remotion** como ferramenta padrão
- **Limpeza de voz** com DeepFilterNet (eco, ruído, pancadas) e corte automático de silêncios
- **Lettering cinético** sincronizado à fala, punch-in nos cortes, rosto sempre livre de texto
- **SFX e trilha** do Mixkit, com volumes medidos (voz a -14 LUFS)
- **Organização automática** de pastas: estúdio, biblioteca de efeitos, músicas e uma pasta por cliente
- **Econômico:** scripts que resumem logs, transcrições e imagens para gastar poucos tokens
- **Catálogo em português** de 526 skills de vídeo com nota de segurança (avatar, clipe, animação, explicativo...)

## Instalar (1 passo)

Cole este link no chat do Claude Code e escreva **"instala isso"**:

```
https://github.com/lincolnribs/editor-pro-bylincu
```

## Instruções para o Claude (instalação automática)

Se o usuário te mandou este link pedindo para instalar, faça nesta ordem, explicando cada passo em uma linha e pedindo permissão antes de baixar ou instalar programas:

1. **Plugins:** rode no terminal
   ```
   claude plugin marketplace add lincolnribs/editor-pro-bylincu
   claude plugin install editor-pro-bylincu@bylincu
   claude plugin install remotion@bylincu
   ```
2. **Se o comando `claude` não existir no terminal:** peça ao usuário para digitar no chat, um por vez:
   `/plugin marketplace add lincolnribs/editor-pro-bylincu`, `/plugin install editor-pro-bylincu@bylincu` e `/plugin install remotion@bylincu`.
   Sem `/plugin` disponível: `git clone --depth 1 https://github.com/lincolnribs/editor-pro-bylincu` numa pasta temporária e copie `plugins/editor-pro-bylincu/skills/editor-pro-bylincu` para `~/.claude/skills/editor-pro-bylincu` (assim fica sem a ativação automática).
3. **Programas:** confira Node.js, Python, ffmpeg e DeepFilterNet seguindo `plugins/editor-pro-bylincu/skills/editor-pro-bylincu/references/instalacao.md`. Liste o que falta e instale só com a permissão do usuário (no Windows, prefira `winget`).
4. **Final:** diga ao usuário para reiniciar o Claude Code e depois mandar o vídeo pedindo **"edita esse vídeo"**.

## Instalação manual

No Claude Code, um comando por vez:

```
/plugin marketplace add lincolnribs/editor-pro-bylincu
/plugin install editor-pro-bylincu@bylincu
/plugin install remotion@bylincu
```

No terminal, troque `/plugin` por `claude plugin`. Reinicie o Claude Code depois. Não precisa de conta no GitHub.

**Programas:** [Node.js](https://nodejs.org) 18+, [Python](https://www.python.org) 3.10+, [ffmpeg](https://ffmpeg.org) no PATH (Windows: `winget install Gyan.FFmpeg`) e o **DeepFilterNet 0.5.6** ([releases](https://github.com/Rikorose/DeepFilterNet/releases)) salvo em `~/tools/deepfilter/deep-filter.exe` (Windows) ou `~/tools/deepfilter/deep-filter` (macOS/Linux).

## Usar
- Mande os brutos e peça **"edita esse vídeo"**. Na primeira vez ele cria as pastas (em `~/Videos/Edicao`) e faz só uma rodada de perguntas: cliente, trilha e identidade visual.
- Também dá para chamar direto com `/editor-pro-bylincu`.
- Dica de economia: um vídeo por conversa. Ao terminar, use `/compact` ou abra uma conversa nova.

## Atualizar
```
/plugin marketplace update bylincu
```

## Créditos e licenças
- Catálogo de skills adaptado do [Awesome Claude Video Skills](https://github.com/zhuyansen/awesome-claude-video-skills) (CC0). Cada projeto listado tem a própria licença.
- Remotion: grátis para uso individual e empresas pequenas; empresas maiores precisam de licença ([remotion.dev/license](https://www.remotion.dev/license)).
- Mixkit: uso comercial grátis, sem atribuição obrigatória. DeepFilterNet: MIT/Apache-2.0.
