# Catálogo de skills de vídeo (em português)

Versão em português, adaptada do **Awesome Claude Video Skills** (github.com/zhuyansen/awesome-claude-video-skills, lista em domínio público CC0), com dados de 19/11/2026: **526 repositórios** de skills e kits que fazem o Claude Code criar ou editar vídeo, separados por tipo. Cada um teve o README lido e recebeu uma nota de segurança da Agent Skills Hub: **SAFE** (508) ou **CAUTION** (18).

Os nomes e as descrições pertencem aos autores, e cada projeto tem a própria licença: confira antes de usar em trabalho de cliente. Atenção com **AGPL-3.0**, que obriga a abrir o código de quem distribui, e com projetos sem licença.

Lista completa e busca: `python scripts/catalogo.py tipos | tipo <id> | busca "<termo>"`. Essa busca mostra só os SAFE; adicione `--todos` para ver também os CAUTION.

## Regras de segurança (sempre)
1. Indique só repositórios **SAFE**. CAUTION, só se o usuário pedir, e avisando do risco.
2. **Nunca instale nada sozinho.** Mostre o nome, o link, a licença e o que a skill faz, e peça aprovação.
3. Antes de instalar, leia o README e os scripts de instalação. Desconfie de `curl | bash`, de downloads de executáveis e de pedidos de chave de API ou de pagamento.
4. Prefira instalar como skill ou plugin do Claude Code, numa pasta própria. Nunca rode código do repositório como administrador.
5. Muitas skills dependem de serviços pagos (ElevenLabs, HeyGen, Atlas Cloud, Suno, Midjourney). Avise antes.

## Precisa mesmo de outra skill?
No teste da lista, 16 skills e o Claude Code **sem nenhuma skill** fizeram o mesmo filme promocional de 15 segundos, e todos passaram nos quatro critérios: o arquivo abre, tem a duração e o tamanho pedidos, todo o texto ficou legível e a imagem se move. O que muda entre eles é o tempo (de 2 a 23,5 minutos), o som (9 dos 16 colocaram) e o visual.

Uma skill só vale a pena quando traz um **visual próprio**, um **fluxo de trabalho** ou edição de **footage real**. Para edição de Reels com pessoa falando, o editor-pro-bylincu já cobre o caso. Use o catálogo quando o pedido for de outro tipo.

**As escolhas da lista:**
- Filme pronto rápido: **vincentsch/explainroo** (2 min, com som e visual próprio).
- Uma ideia contínua, sem cortes: **feitangyuan/onetake**.
- Seu próprio design no Remotion: **remotion-dev/skills** (render confiável; traga a direção visual).
- HyperFrames foi o mais lento do teste (23,5 min para 15 s).

## Tipos (id para o script)
| id | Tipo | Para quê |
|---|---|---|
| general | Frameworks e kits | motores de render e kits completos |
| promo | Promo e demos | lançamento de produto, anúncio, demo |
| explainer | Explicativos | aula, tutorial, conteúdo narrado |
| editing | Edição | cortes, legenda, b-roll, recap de footage existente |
| shorts | Shorts e redes | vertical para Reels, Shorts, TikTok |
| avatar | Avatares | apresentador digital, lip-sync |
| story | Histórias e animação | conto animado, curta, cena cinematográfica |
| motion | Motion graphics | logo animado, títulos, UI, GIF |
| craft | Roteiro e estudo | roteiro, análise de cenas, aprendizado |
| music | Clipes musicais | clipe feito em código |

## Destaques por tipo (SAFE, por estrelas)

### Frameworks e kits
- **heygen-com/hyperframes** (Apache-2.0): editor de vídeo com IA em HTML; o projeto gerado é editável quadro a quadro.
- **nexu-io/openmotion** (Apache-2.0): transforma um vídeo de referência em motion editável com o kit da marca.
- **remotion-dev/skills**: skills oficiais do Remotion.
- **bangtutorial/bang-motion** (MIT): aberturas, promos, vinhetas e tipografia cinética no navegador, com cinco estilos de explicativo.
- **digitalsamba/claude-code-video-toolkit** (MIT): roteiro, locução por IA, música, clipes e render com modelos abertos baratos.
- **iart-ai/motion-skills** (MIT): 56 skills de motion, animação e vídeo (tipografia cinética, gráficos de dados e mais).

### Promo e demos
- **feitangyuan/onetake**: filmes sem corte de slide; cada momento nasce do anterior, com uma câmera contínua.
- **Tejashmakwana/motionmaxxing** (Apache-2.0): deixa vídeos com cara de IA com acabamento de motion designer.
- **echris6/motion-video-kit** (MIT): vídeos corporativos premium, com crítico independente e princípios tirados de 28 filmes de lançamento.
- **charlie947/motion-graphics-skills** (MIT): 13 skills de motion nível lançamento, tudo em código.
- **AbubakrChan/product-launch-motion** (MIT): lançamento de produto estilo Dribbble, com forma contínua, molas e cursor guiando as mudanças.
- **aaitor/skill-video-studio**: vídeo de produto com captura real do navegador, composição com a marca e masterização local.

### Explicativos
- **vincentsch/explainroo** (MIT): explicativos e demos com voz local (Kokoro), tempo por palavra (Whisper), tudo grátis.
- **EverMind-AI/Raven** (Apache-2.0): curta animado desenhado à mão a partir do histórico de um repositório Git.
- **adithya-s-k/manim_skill** (MIT): animações no estilo 3Blue1Brown com Manim.
- **Moh4696/cinematic-skill** (MIT): filmes narrados com câmera contínua sobre fotos, mapas e cards.
- **Alisa0808/vox-director** (MIT): explicativo estilo Vox com colagem de papel (usa Atlas Cloud, pago).

### Edição
- **FireRedTeam/FireRed-OpenStoryline** (Apache-2.0): agente de edição em que você dirige por intenção, em linguagem natural.
- **Agentchengfeng/chengfeng-videocut-skills** (Apache-2.0): agente de corte de vídeo feito com skills do Claude Code.
- **JimLiu/baocut**: agente com linha do tempo editável: transcreve, legenda, traduz, dubla, corta e anima.
- **Barty-Bart/motion-graphics**: motion para vídeos de pessoa falando (talking head).
- **Vibha-Ramprakash/claude-video-effects**: 51 efeitos para talking head, com rastreio de rosto e camadas atrás da cabeça.
- **hetpatel-11/Adobe_Premiere_Pro_MCP** (MIT): controla o Premiere Pro pelo Claude via MCP.
- Atenção: **0xsline/OpenChatCut** e **pireel/pireel** são AGPL-3.0.

### Shorts e redes
- **artemnovitckii/claude-animation-skills**: 11 skills de animação para Reels sem footage (low-poly, voxel, cartoon 3D).
- **hassancs91/claude-faceless-shorts-creator** (MIT): fábrica de Shorts sem rosto em Remotion, com legenda exata por palavra (voz ElevenLabs, paga).
- **0xS4N4TG/papercut-explainer** (MIT): Reels explicativos verticais em papel recortado, com biblioteca Remotion.
- **haiderfarooq3/paper-reel** (MIT): Reels 9:16 sem rosto em papel recortado, legenda palavra a palavra, grátis e local.
- **fendouai/ViralForge** (Apache-2.0): desmonta ganchos e roteiros de vídeos virais e replica a estrutura.

### Avatares
- **cclank/lanshu-create-ai-presenter-video** (MIT): vídeo de apresentador por IA a partir de roteiro e foto autorizada.
- **heygen-com/skills** (MIT): skills oficiais da HeyGen para criar avatar e produzir vídeo (pago).
- **Upload-Post/avatar-mix** (MIT): vídeos com avatar HeyGen, fundo animado, música, SFX e legendas estilo Hormozi.

### Histórias e animação
- **lemomo-ai/lemo-opuscar**: 99 estilos de filme prontos em código, cada um com prompt de estilo e filme de exemplo.
- **alchaincyf/huashu-art-motion** (MIT): 35 estilos artísticos e 9 formas de narrar, para dar movimento a pinturas.
- **JohnHeibel/ClaudeAnimationBase** (MIT): kit para animar desenhos pintados à mão (p5.js + p5.brush).
- **edenfunf/reelmimic** (MIT): você mostra um vídeo que ama e ele faz outro no mesmo estilo.

### Motion graphics
- **diffusionstudio/lottie** (MIT): animações Lottie prontas para produção.
- **nolangz/pixel2motion** (MIT): anima logos (raster para SVG animado), com prévia em GIF ou vídeo.
- **alexgreensh/anidoodle** (Apache-2.0): ilustração e animação em código, em dezenas de estilos.
- **ythx-101/live-panel-skill** (MIT): diagrama de arquitetura animado a partir de um JSON ou de um arquivo do Excalidraw.

### Roteiro e estudo
- **jtydhr88/screenwriting-skills** (MIT): roteiro de cinema e TV, e dramaturgia.
- **adityaarsharma/youtube-marketing-skills** (MIT): 21 comandos de crescimento para YouTube.

### Clipes musicais
- **EGSECDA/vocaloid-style-mv-pipeline** (MIT): clipe com letra, desenhado à mão, estilo Vocaloid.
- **Win-Hao/music-mv** (MIT): ouve a música, define o estilo, faz o roteiro e desenha cada quadro em código.
- **SyanChen7/dancing-notes** (MIT): visualização de música em Remotion.

## Como entrar na lista original (critério dos curadores)
1. O projeto faz ou edita vídeo ou motion.
2. Um agente consegue operá-lo (skill, plugin, MCP ou kit para agentes).
3. Tem README.
4. Com 50 estrelas ou mais, entra só pelo tema. Abaixo disso, precisa de um README de qualidade, que mostre o resultado, tenha início com um comando e documentação completa.
