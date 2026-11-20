# Complementos incluídos

O pacote do Editor Pro já traz 8 skills de terceiros, e o remotion-director é instalado junto pelo marketplace. Todas são grátis para uso comercial (MIT ou Apache-2.0), têm nota SAFE no catálogo e foram conferidas em 20/11/2026: licença, plataforma, dependências e uma varredura do código. As versões e os créditos estão em `THIRD_PARTY_NOTICES.md`, na raiz do repositório.

## Regra de uso
- **O editor-pro-bylincu é o diretor.** Ele decide quando chamar um complemento, que faz só a parte dele (efeito, vinheta, abertura, logo). O resultado volta para o projeto Remotion do cliente como clipe ou camada.
- Siga as regras do editor por cima das do complemento: rosto livre, margens seguras, identidade do cliente e economia de tokens.
- Se um complemento pedir API paga (ElevenLabs, Gemini, OpenAI), pergunte antes ao usuário. Todos funcionam sem ela.

## Qual usar para cada pedido

| Pedido | Skill | Licença |
|---|---|---|
| Efeito viral sobre pessoa falando (texto atrás da cabeça, órbita, recorte) | `effects` | MIT |
| Vinheta, abertura ou peça de motion a partir de uma frase, com crítico | `remotion-director` | MIT |
| Lettering e títulos no ritmo da música | `kinetic-typography` | MIT |
| Abertura, bumper ou explicativo animado 9:16 | `bang-motion` | MIT |
| Motion sem cara de IA (ideia da marca, timing medido) | `motionmaxxing` | Apache-2.0 |
| Comercial premium com rodadas de crítica e regras de áudio | `business-motion-film` | MIT |
| Motion contínuo, uma forma que nunca corta, cortado na batida | `product-launch-motion` | MIT |
| Logo animado para o fechamento | `pixel2motion` | MIT |
| Ícone ou sticker animado (Lottie) | `text-to-lottie` | MIT |

## O que cada uma precisa
- **effects:** Python e ffmpeg. Rastreia o rosto e evita cobri-lo. Uso: `/effects <nome do efeito>`.
- **remotion-director:** Node, Git e ffmpeg 5.1+. Propõe direções, faz três prévias, critica e renderiza a escolhida.
- **kinetic-typography:** Remotion ou GSAP.
- **bang-motion:** navegador e ffmpeg. Aceita vídeo como camada e exporta MP4 quadro a quadro.
- **motionmaxxing:** Node 22+, Python, ffmpeg e Chrome. A voz pela ElevenLabs é opcional e paga.
- **business-motion-film:** são princípios e roteiros de crítica que servem para qualquer motor de render.
- **product-launch-motion:** Python com Playwright e ffmpeg. HTML puro com molas, tempo guiado pela música e motion blur real. Substitui o onetake, que não era grátis para uso comercial.
- **pixel2motion:** Python. Transforma PNG ou JPG em SVG animado, com prévia em GIF ou vídeo.
- **text-to-lottie:** gera JSON Lottie pronto para usar em cards.

## Atualizar os complementos (manutenção do repositório)
`python tools/complementos.py` baixa a versão mais nova de cada um, copia só o que a skill usa e regenera `THIRD_PARTY_NOTICES.md`. Revise o diff antes de publicar.

## Laboratório (fora do pacote, só se o usuário pedir)
- **openmotion** (nexu-io/openmotion, Apache-2.0): transforma um vídeo de referência em motion editável com o kit da marca. É um app grande, e vários recursos usam APIs pagas.
- **OpenKatana** (rk0neki/OpenKatana, Apache-2.0): alternativa aberta ao Katana da Higgsfield. Precisa de ComfyUI, GPU e modelos baixados.
- **openjutsu** (D3voz/openjutsu, MIT): troca de personagem em vídeo. Precisa de ComfyUI e GPU forte. Use só com autorização de quem aparece no vídeo.
