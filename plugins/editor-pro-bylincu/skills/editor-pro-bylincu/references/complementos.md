# Complementos selecionados

Skills de terceiros que somam ao editor-pro-bylincu. Saíram de 526 repositórios do catálogo: todos têm nota SAFE, foram conferidos em 20/11/2026 (licença, plataforma, dependências) e cobrem algo que o editor não faz sozinho.

## Como usar
- **Instale só quando o pedido precisar.** Toda skill instalada entra na lista de contexto de todas as conversas. Instalar todas "por garantia" volta a gastar tokens.
- **Peça aprovação antes**, dizendo o nome, o link, o que a skill faz e a licença. Leia o README e o script de instalação antes de rodar.
- **Uso comercial:** confira a coluna Licença. O trabalho para cliente é comercial.
- O editor continua sendo o diretor do vídeo: o complemento faz a parte dele (efeito, vinheta, abertura) e o resultado volta para o projeto Remotion do cliente como clipe ou camada.

## Qual usar para cada pedido

| Pedido | Complemento | Licença | Windows |
|---|---|---|---|
| Efeito viral sobre pessoa falando (texto atrás da cabeça, órbita, recorte) | claude-video-effects | MIT | sim |
| Vinheta, abertura ou peça de motion a partir de uma frase, com crítico | remotion-director | MIT | sim |
| Lettering e títulos no ritmo da música | kinetic-typography-skills | MIT | sim |
| Abertura, bumper, explicativo animado 9:16 | bang-motion | MIT | sim |
| Motion "nível lançamento" e acabamento anti-cara-de-IA | motionmaxxing · motion-graphics-skills | Apache-2.0 · MIT | sim |
| Comercial premium com rodadas de crítica e regras de áudio | motion-video-kit | MIT | sim |
| Motion contínuo, sem cortes (plano-sequência) | onetake | **não comercial** (Pro: US$ 79) | sim |
| Logo animado para fechamento | pixel2motion | MIT | sim |
| Ícone ou sticker animado (Lottie) | lottie | MIT | sim |

## Detalhes e instalação

**claude-video-effects** · github.com/Vibha-Ramprakash/claude-video-effects
51 efeitos para talking head (rastreio de rosto, camadas atrás da pessoa). Confere quadros e evita cobrir o rosto. Precisa de Python e ffmpeg.
`git clone https://github.com/Vibha-Ramprakash/claude-video-effects ~/.claude/skills/effects` · uso: `/effects <nome do efeito>`

**remotion-director** · github.com/Zane-0x5a/remotion-director
O "diretor de vídeo": recebe uma frase, propõe direções, faz três prévias, critica e renderiza a escolhida. Em Remotion, igual ao nosso fluxo. Precisa de Node, Git e ffmpeg 5.1+.
`/plugin marketplace add Zane-0x5a/remotion-director` e `/plugin install remotion-director@remotion-director`

**kinetic-typography-skills** · github.com/iart-ai/kinetic-typography-skills
Tipografia cinética sincronizada à batida, para títulos e redes. Remotion ou GSAP.
`/plugin marketplace add iart-ai/kinetic-typography-skills` e `/plugin install kinetic-typography-skills`

**bang-motion** · github.com/bangtutorial/bang-motion
Aberturas, promos, bumpers, tipografia cinética e cinco estilos de explicativo, com exportação em MP4 quadro a quadro. Aceita vídeo como camada.
`/plugin marketplace add bangtutorial/bang-motion` e `/plugin install bang-motion@bang-motion`

**motionmaxxing** · github.com/Tejashmakwana/motionmaxxing
Tira a "cara de IA" do motion: ideia própria da marca, timing medido em 53 momentos profissionais e conferência do render por script. Precisa de Node 22+, Python, ffmpeg e Chrome. A voz pela ElevenLabs é opcional e paga. O GSAP embutido tem licença própria.
`git clone https://github.com/Tejashmakwana/motionmaxxing ~/.claude/skills/motionmaxxing`

**motion-graphics-skills** · github.com/charlie947/motion-graphics-skills
13 skills de motion para lançamento, tudo em código, sem chave de API. Instale só a skill do trabalho.
`npx skills add charlie947/motion-graphics-skills`

**motion-video-kit** · github.com/echris6/motion-video-kit
Comerciais premium: ciclo de crítica independente ("quem faz não julga"), 16 mecanismos de motion, régua de qualidade e regras de áudio (música, SFX, mixagem). Os princípios também servem para o nosso fluxo.
`git clone https://github.com/echris6/motion-video-kit` e copie a pasta `business-motion-film` para `~/.claude/skills/`

**onetake** · github.com/feitangyuan/onetake
Motion em plano-sequência: cada momento nasce do anterior, sem corte de slide. **Licença PolyForm Noncommercial:** grátis só para uso pessoal ou estudo. Para cliente, é preciso o onetake Pro (US$ 79, pagamento único, com licença comercial). Precisa de Python com playwright, numpy, scipy, Pillow e matplotlib.
`git clone https://github.com/feitangyuan/onetake ~/.claude/skills/onetake`

**pixel2motion** · github.com/nolangz/pixel2motion
Transforma logo em imagem (PNG/JPG) em SVG animado, com prévia em GIF ou vídeo. Bom para o fechamento do Reels.
`git clone https://github.com/nolangz/pixel2motion ~/.claude/skills/pixel2motion`

**lottie** · github.com/diffusionstudio/lottie
Gera animações Lottie prontas para usar (ícones e stickers animados em cards).
`npx skills add diffusionstudio/lottie`

## Laboratório (pesado, só se o usuário pedir)
- **openmotion** (nexu-io/openmotion, Apache-2.0): transforma um vídeo de referência em motion editável com o kit da marca. É um app grande, e vários recursos usam APIs pagas.
- **OpenKatana** (rk0neki/OpenKatana, Apache-2.0): alternativa aberta ao Katana da Higgsfield (edição por agente com ComfyUI). Precisa de GPU e de modelos baixados.
- **openjutsu** (D3voz/openjutsu, MIT): troca de personagem em vídeo, alternativa local ao Genjutsu da Higgsfield. Precisa de ComfyUI e GPU forte. Use só com autorização de quem aparece no vídeo.

## Ficaram de fora (e por quê)
- ghost-editor: só roda em Mac com Apple silicon.
- facecammaxxing: só macOS e Linux.
- claude-shorts: no Windows, só pelo WSL.
- erduo-broll-loop-engineering: Windows não verificado, e o Agent Motion é não comercial.
- reelmimic e mrpaidsocial-video-editor-agent: dependem de chaves de API pagas.
- Katana (Higgsfield): produto fechado e pago, não é repositório aberto.
