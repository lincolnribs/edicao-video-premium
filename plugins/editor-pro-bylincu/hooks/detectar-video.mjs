// Ativação automática do editor-pro-bylincu.
// Roda a cada mensagem do usuário, mas só fala alguma coisa quando o pedido é de edição de vídeo,
// e no máximo uma vez por sessão (custo: ~60 tokens). Nunca bloqueia a mensagem.
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

let entrada = {};
try {
  entrada = JSON.parse(readFileSync(0, "utf8") || "{}");
} catch {
  process.exit(0);
}

const texto = String(entrada.prompt || "").toLowerCase();
const sessao = String(entrada.session_id || "sem-sessao").replace(/[^a-z0-9-]/gi, "");

const objeto = /\b(v[ií]deos?|reels?|takes?|brutos?|tiktok|shorts|stories|lettering|legendas?|talking ?head|b-?roll|motion)\b/;
const acao = /\b(edit\w*|edi[tç]\w*|mont\w*|cort\w*|corta|fa[zç]\w*|cri\w*|renderiz\w*|legend\w*|limp\w*|melhor\w*|tratar|trata)\b/;
const direto = /\b(edita|edite|editar) (esse|este|isso|isto|o|meu|minha|esses|estes)\b/;
const outraFerramenta = /\bhyper ?frames\b/;

const ehVideo = (direto.test(texto) || (objeto.test(texto) && acao.test(texto))) && !outraFerramenta.test(texto);
if (!ehVideo) process.exit(0);

const pasta = join(tmpdir(), "editor-pro-bylincu");
const marca = join(pasta, sessao);
if (existsSync(marca)) process.exit(0);
try {
  mkdirSync(pasta, { recursive: true });
  writeFileSync(marca, "1");
} catch {}

const aviso =
  "Pedido de edição de vídeo detectado: carregue a skill editor-pro-bylincu (Skill tool) ANTES de qualquer outra " +
  "skill de vídeo e siga o fluxo dela, com Remotion como ferramenta padrão. Não carregue as skills do HyperFrames " +
  "a menos que o usuário peça HyperFrames pelo nome.";

// Acentos viram \uXXXX para não depender da codificação do terminal.
const json = JSON.stringify({ hookSpecificOutput: { hookEventName: "UserPromptSubmit", additionalContext: aviso } })
  .replace(/[\u007f-￿]/g, (c) => "\\u" + c.charCodeAt(0).toString(16).padStart(4, "0"));
process.stdout.write(json);
