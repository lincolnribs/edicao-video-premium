# Edição de Vídeo Premium para Claude Code

Plugin que ensina o Claude Code a editar vídeos verticais (Reels, Stories, TikTok) com padrão profissional:

- **Remotion** como ferramenta padrão (basta pedir "edita esse vídeo")
- **Limpeza de voz** com DeepFilterNet (tira eco, ruído, pancadas) e corte automático de silêncios
- **Lettering cinético** sincronizado à fala, cortes com punch-in, rosto sempre livre de texto
- **SFX e trilha** do Mixkit, com volumes medidos (voz a -14 LUFS)
- **Organização automática** de pastas: estúdio, biblioteca de efeitos sonoros, músicas e uma pasta por cliente

## Instalação

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

Depois, reinicie o Claude Code.

> Se o repositório for **privado**, você precisa ter sido convidado e estar logado no GitHub neste computador (`gh auth login` ou credenciais do git).

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
