---
tipo: guia-de-pasta
cliente: pibac
titulo: 06_MEDIA
usar_quando: precisar saber o que vai, e o que nao vai, em 06_MEDIA/
status: ativo
atualizado: 2026-09-10
---

# 06_MEDIA — Banco de mídia

> **Matéria-prima audiovisual.** Foto, vídeo e áudio do cliente — o que foi
> captado e já está tratado.

> [!WARNING]
> **Parte desta pasta não sobe para o GitHub.** Material bruto de câmera são
> dezenas de GB e nunca é usado diretamente. Ele existe no SSD e no backup, mas
> o Git ignora. O que versionamos é o resultado tratado.

## O que está no Git e o que não está

| Subpasta | No Git? |
|---|---|
| `fotos/tratadas/` | ✅ sim |
| `fotos/originais/` | 🚫 não — bruto de câmera, fica no SSD |
| `videos/editados/` | ✅ sim |
| `videos/motion/` | ✅ sim |
| `videos/brutos/` | 🚫 não — bruto de câmera, fica no SSD |
| `audio/narracoes/` | ✅ sim *(exceto `.wav` e `.aif`)* |
| `audio/trilhas/` | ✅ sim *(exceto `.wav` e `.aif`)* |

Áudio sobe comprimido (`.mp3`, `.m4a`). O `.wav` da sessão de gravação fica fora.

## O que NÃO vai aqui

| Isso | Vai em |
|---|---|
| Foto já aplicada em peça | `04_PRODUCTION/` ou `05_EXPORTS/` |
| Mockup de marca | `00_BRAND/mockups/` |
| Vídeo exportado para publicar | `05_EXPORTS/` |

A diferença: **06 é acervo, 05 é entrega.** A mesma foto pode viver nos dois —
tratada aqui, aplicada lá.

## Como nomear

Foto de captação leva a data do dia:

```
fotos/tratadas/foto-evento-nome-2026-09-22-v1.jpg
videos/editados/reels-porta-voz-apresentacao-v1.mp4
audio/narracoes/narracao-institucional-v1.mp3
```

## Direito de uso

> [!IMPORTANT]
> Foto de banco de imagem, trilha e fonte de terceiro têm licença. Antes de usar,
> confirme o direito e registre a origem. Verificação é humana — não delegue à IA.

📖 [`_META/NOMENCLATURA.md`](../_META/NOMENCLATURA.md)
