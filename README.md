# Edição de Vídeo Premium para Claude Code

Plugin que ensina o Claude Code a editar vídeos verticais (Reels, Stories, TikTok) com padrão profissional:

- **Remotion** como ferramenta padrão (basta pedir "edita esse vídeo")
- **Limpeza de voz** com DeepFilterNet (tira eco, ruído, pancadas) e corte automático de silêncios
- **Lettering cinético** sincronizado à fala, cortes com punch-in, rosto sempre livre de texto
- **SFX e trilha** do Mixkit, com volumes medidos (voz a -14 LUFS)
- **Organização automática** de pastas: estúdio, biblioteca de efeitos sonoros, músicas e uma pasta por cliente

## Instalação em 1 passo

Cole este link no chat do Claude Code e escreva **"instala isso"**:

```
https://github.com/lincolnribs/edicao-video-premium
```

O Claude faz o resto (passos abaixo). Se preferir instalar à mão, veja "Instalação manual".

## Instruções para o Claude (instalação automática)

Se o usuário te mandou este link pedindo para instalar, faça nesta ordem, explicando cada passo em uma linha e pedindo permissão antes de baixar ou instalar programas:

1. **Plugins:** rode no terminal
   ```
   claude plugin marketplace add lincolnribs/edicao-video-premium
   claude plugin install edicao-video-premium@edicao-video
   claude plugin install remotion@edicao-video
   claude plugin install hyperframes@edicao-video
   ```
2. **Se o comando `claude` não existir no terminal:** instale só a skill copiando a pasta:
   ```
   git clone --depth 1 https://github.com/lincolnribs/edicao-video-premium "<pasta temporária>/edicao-video-premium"
   ```
   e copie `plugins/edicao-video-premium/skills/edicao-video-premium` para `~/.claude/skills/edicao-video-premium`. Depois peça ao usuário para digitar no chat `/plugin marketplace add remotion-dev/claude-code-plugin` e `/plugin install remotion@remotion` (o Remotion é obrigatório).
3. **Programas:** confira Node.js, Python, ffmpeg e DeepFilterNet seguindo `plugins/edicao-video-premium/skills/edicao-video-premium/references/instalacao.md`. Liste o que falta e instale só com a permissão do usuário (no Windows, prefira `winget`).
4. **Final:** diga ao usuário para reiniciar o Claude Code e, depois, pedir **"prepara meu estúdio de edição"**.

## Instalação manual

### 1. Adicionar o marketplace e instalar os plugins
No Claude Code, digite um comando por vez:

```
/plugin marketplace add lincolnribs/edicao-video-premium
/plugin install edicao-video-premium@edicao-video
/plugin install remotion@edicao-video
/plugin install hyperframes@edicao-video
```

Se o `/plugin` não abrir (por exemplo, no app desktop), rode no terminal:

```
claude plugin marketplace add lincolnribs/edicao-video-premium
claude plugin install edicao-video-premium@edicao-video
claude plugin install remotion@edicao-video
claude plugin install hyperframes@edicao-video
```

Depois, reinicie o Claude Code. Não precisa de conta no GitHub para instalar.

### 2. Programas necessários
- [Node.js](https://nodejs.org) 18 ou mais novo
- [Python](https://www.python.org) 3.10 ou mais novo
- [ffmpeg](https://ffmpeg.org) no PATH (no Windows: `winget install Gyan.FFmpeg`)
- **DeepFilterNet 0.5.6**: baixe o executável em [github.com/Rikorose/DeepFilterNet/releases](https://github.com/Rikorose/DeepFilterNet/releases) e salve em `~/tools/deepfilter/deep-filter.exe` (Windows) ou `~/tools/deepfilter/deep-filter` (macOS/Linux)

Não sabe instalar? Peça ao Claude: **"confere o que falta instalar para a skill de edição de vídeo"**. Ele segue o guia `references/instalacao.md` da skill.

### 3. Primeiro uso
Peça ao Claude: **"prepara meu estúdio de edição"**. Ele cria as pastas (por padrão em `~/Videos/Edicao`), monta uma biblioteca inicial de efeitos sonoros e a pasta do seu primeiro cliente.

Depois é só mandar os brutos e pedir: **"edita esse vídeo"**.

## Atualizar
```
/plugin marketplace update edicao-video
```

## Licenças
- Remotion: grátis para uso individual e empresas pequenas; empresas maiores precisam de licença ([remotion.dev/license](https://www.remotion.dev/license)).
- Mixkit: uso comercial grátis, sem atribuição obrigatória.
- DeepFilterNet: código aberto (MIT/Apache-2.0).
