# Produção visual — direção, depoimento, briefing e prompts de IA

---

## Direção de foto e vídeo

Quando pedirem um plano de cobertura, pense em **narrativa visual**. "Grave
bastante" não é direção — é o contrário dela.

```
ABERTURA      fachada · ambiente · pessoas chegando · detalhes
COMUNIDADE    abraços · conversas · famílias · crianças · voluntários · interação
CULTO/EVENTO  palco · louvor · Palavra · congregação · reações
DETALHES      Bíblia · mãos · instrumentos · decoração · materiais
ENCERRAMENTO  comunhão · oração · despedida · plano geral
```

Busque sempre imagem que **conte história**. Um plano geral da congregação diz
quantos eram; uma mão segurando a Bíblia aberta diz o que estavam fazendo ali.

> [!IMPORTANT]
> **Cobertura de culto tem material próprio no repositório** — não reinvente:
>
> - [manual de cobertura](../../../../01_STRATEGY/guia-de-conteudo/manual-stories-culto.md) — os seis blocos, o padrão e o que é regra
> - [roteiro de uso](../../../../03_CONTENT/roteiros/_modelo-cobertura-culto.md) — a página que o voluntário segue durante o culto
>
> Esta estrutura de cinco blocos serve para **eventos** — aniversário, formatura,
> ação social, casamento, congresso. Para culto, use o manual.

**Crianças aparecem na etapa COMUNIDADE.** Toda vez que dirigir uma cobertura,
inclua a autorização de imagem no plano (`AGENTS.md` §2.8) e a alternativa:
mãos na atividade, material sobre a mesa, professor de frente, criança de costas
ou fora de foco.

---

## Depoimentos

**Nunca faça pergunta de sim ou não.** Ela devolve "sim", e aí não há
depoimento.

Perguntas que abrem:

- *O que Deus falou com você hoje?*
- *O que mais marcou você nessa experiência?*
- *Como foi servir aqui hoje?*
- *O que você leva desse encontro para sua semana?*

Com jovens, linguagem mais natural — a pergunta precisa soar como conversa, não
como formulário.

Antes de publicar depoimento: a pessoa consentiu? Se o relato toca em saúde,
família ou situação financeira, o consentimento precisa ser explícito e
registrado (`AGENTS.md` §2.9).

---

## Briefing de peça gráfica

Um briefing que o designer consegue usar responde, no mínimo:

| | |
|---|---|
| **O que é a peça** | post, story, banner, card, impresso |
| **Onde vai** | canal e formato — isso define a proporção |
| **O que precisa estar escrito** | texto exato, já revisado |
| **A informação que não pode faltar** | data, hora, local |
| **Hierarquia** | o que a pessoa lê primeiro, segundo, terceiro |
| **Referência visual** | peça anterior que funcionou, se houver |
| **Prazo** | |

Cor, tipografia e grafismo saem do
[design system](../../../../00_BRAND/design-system.md) — nunca de escolha do dia.

---

## Prompts para geração e edição de imagem por IA

Aqui a regra é uma só: **seja específico ao ponto de não sobrar interpretação.**

### Edição de foto real da igreja

O risco é a IA "melhorar" o que ninguém pediu — trocar um rosto, mudar a roupa,
inventar uma pessoa ao fundo. Em fotografia documental de igreja isso não é
retoque, é falsificação do registro.

Por isso, todo prompt de edição precisa **listar o que preservar**:

> Remove only the cellphone from the person's hand. Preserve the person's exact
> identity, facial features, body position, arm position, clothing, background,
> lighting, framing and all other people. Do not add new people or objects. Do
> not reposition the subject.

Sempre preserve explicitamente: **pessoas · identidade · posição · ambiente ·
características físicas · composição original.**

Nunca deixe a IA "melhorar indiscriminadamente" uma foto documental.

### Geração de imagem

Descreva com precisão: enquadramento, luz, ambiente, paleta, o que aparece e o
que **não** aparece.

Imagem gerada por IA não substitui registro real da igreja. Ela serve para
fundo, textura, conceito — nunca para simular um momento que não aconteceu, nem
para representar pessoas da comunidade.

### A marca nunca entra num prompt

Não peça para a IA desenhar, recriar ou "melhorar" o logo da PIBAC. A marca sai
de [`00_BRAND/logo/`](../../../../00_BRAND/logo/) — é arquivo, não é geração
(`AGENTS.md` §2.12).
