# Catálogo completo de skills de vídeo

Primeiro, veja `complementos.md`: lá estão os selecionados para o nosso fluxo. Use este catálogo só quando o pedido sair do que eles cobrem.

**Fonte:** Awesome Claude Video Skills (github.com/zhuyansen/awesome-claude-video-skills, lista em domínio público CC0), dados de 19/11/2026. São 526 repositórios, cada um com nota de segurança da Agent Skills Hub: SAFE (508) ou CAUTION (18). Os nomes e as descrições são dos autores, e cada projeto tem a própria licença.

## Buscar (sem carregar o arquivo inteiro)
```bash
python scripts/catalogo.py tipos                    # 10 tipos com a contagem
python scripts/catalogo.py tipo shorts --top 10     # os mais estrelados de um tipo
python scripts/catalogo.py busca "music video"      # por termo (só SAFE; --todos inclui CAUTION)
```
Tipos: `general` (frameworks), `promo`, `explainer`, `editing`, `shorts`, `avatar`, `story` (animação), `motion`, `craft` (roteiro), `music`.

## Antes de indicar qualquer um
1. Só SAFE. CAUTION, só a pedido do usuário e com aviso.
2. Licença: AGPL-3.0, PolyForm Noncommercial e projetos sem licença não servem para trabalho de cliente sem conferir.
3. Plataforma: muitos só rodam em Mac ou Linux.
4. Custos: vários dependem de APIs pagas (ElevenLabs, HeyGen, Suno, Atlas Cloud, Gemini).
5. Nunca instale sozinho. Mostre nome, link, licença e o que faz, e peça aprovação. Desconfie de `curl | bash` e de downloads de executáveis.

## O que o teste da lista mostrou
16 skills e o Claude Code sem nenhuma skill fizeram o mesmo promo de 15 segundos, e todos passaram nos quatro critérios. A diferença ficou no tempo (de 2 a 23,5 minutos), no som e no visual. Uma skill nova só vale a pena se trouxer um visual próprio, um fluxo de trabalho ou edição de footage real.
