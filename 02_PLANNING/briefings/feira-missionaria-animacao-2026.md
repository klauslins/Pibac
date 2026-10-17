# Feira Missionária — 6ª edição · Story 9:16

**Cliente:** Primeira Igreja Batista de Águas Claras (PIBAC)
**Peça:** Story de 15s, 1080×1920, 60fps · publicação no dia do evento
**Pipeline:** animation · atelier · fluid grammar (stage family **light**)
**Data:** 17/10/2026 — a feira é hoje, 16h

---

## Fio condutor

**A onda do símbolo da PIBAC.** Uma linha só, desenhada por uma função
compartilhada, que ganha função nova em cada tempo:

| Tempo | O que a onda é |
|---|---|
| 1 | o traço que sublinha o **É HOJE!** |
| 2 | a régua sob **Feira Missionária** |
| 3 | desce e vira a **bancada** onde a informação se apoia |
| 4 | a bancada onde as **barracas se acumulam** |
| 5 | sobe e **abre** para revelar o versículo |
| 6 | assenta como a onda da **própria marca** |

O sentido: água é o nome do bairro e é batismo. A onda sai da marca, atravessa
a feira e volta para a marca — e é ela que leva a mensagem.

> Autorizado pelo `00_BRAND/grafismos/grafismos.md`, que já registra a onda do
> símbolo como repertório gráfico da igreja. **O logotipo em si nunca é
> redesenhado** — só posicionado, escalado e esmaecido (`AGENTS.md` §2.12).

---

## Stage — família clara

A PIBAC é identidade clara. Fundo **areia `#EFEAE4`**, sem glow, profundidade
por sombra suave e escala. Grão baixo, só como anti-banding.

**Acento único:** `#007CC2`, a cor principal da igreja. Marca a palavra que
importa, nunca tudo.

**Tipografia:** Archivo Expanded Black em caixa alta para anúncio, Montserrat
para o resto — a regra dos dois registros do design system. Sobre a cor
principal, texto **branco puro**: é o único que tem contraste (4,50:1).

---

## Beat sheet (60fps · 900 quadros)

| # | Quadros | Tempo | Conteúdo | Movimento |
|---|---|---|---|---|
| 1 | 0–150 | 0–2,5s | **É HOJE!** | Slam legível em 0,3s. Onda desenha por baixo |
| 2 | 120–270 | 2–4,5s | *nossa* **FEIRA MISSIONÁRIA** · 6ª edição | Onda vira régua. Câmera empurra devagar |
| 3 | 250–430 | 4,2–7,2s | **17 DE OUTUBRO · 16H ÀS 22H** · Rua Jerivá, 5 | Onda desce e vira bancada. Quadro segura |
| 4 | 410–700 | 6,8–11,7s | **as 7 barracas acumulando** | Uma a cada 28 quadros, **ficam**. Termina cheio |
| 5 | 680–810 | 11,3–13,5s | *"E como ouvirão se não há quem pregue?"* | Onda sobe e abre. Rack para o versículo |
| 6 | 790–900 | 13,2–15s | **PIBAC + marca da campanha** | Onda assenta na marca. Parado 1,2s |

**Seams:** cada tempo sobrepõe o seguinte por ~30 quadros. A onda é desenhada
pela mesma função nos dois lados do seam — é o mesmo objeto trocando de dono.

---

## O que não entra

- Corte seco: um plano contínuo, a câmera nunca para
- Gatilho de escassez. A urgência aqui é **verdadeira** — o evento é hoje
- Promessa de resultado, teologia de prosperidade (`AGENTS.md` §1)
- Logo redesenhado, recolorido ou com brilho
- Montagem estroboscópica das barracas: elas **acumulam**, não piscam

---

## Conteúdo (do cartaz aprovado, nada inventado)

6ª edição · 17 de outubro · 16h às 22h · Rua Jerivá, Lote 5, próximo ao
colégio CIESB.

Churrasco (Min. Homens) · Caldos (Min. Juventude) · Sobremesas (Min. Mulheres) ·
Hambúrguer (Min. Recepção) · Pastel e Esfirra (Embaixadores do Rei) ·
Sorvete e Açaí (PIBAC Kids) · Bebidas (Mensageiras do Rei).

Versículo: *"E como ouvirão se não há quem pregue?"* — Romanos 10.14,15.

## Assets

| Arquivo | Origem |
|---|---|
| `pibac-sigla.svg`, `pibac-completo.svg` | `00_BRAND/logo/horizontal/svg/` — vetor oficial, texto em contorno |
| `mn-rodape.png` | rodapé do `molde-video-missoes-v1.psd`, material aprovado da campanha |

Sem download externo. Sem crédito gasto.
