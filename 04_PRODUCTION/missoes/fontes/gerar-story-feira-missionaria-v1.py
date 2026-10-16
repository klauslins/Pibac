import json
from PIL import Image, ImageDraw, ImageFont
SP = "/private/tmp/claude-501/-Volumes-Jess--Lima/fb9b4d6f-02dd-4a62-825a-2bdcbd7f667b/scratchpad"
REPO = "/Volumes/Jessé_Lima/05_DEV/Pibac"

# cores vindas do tokens.json — nunca hex na mao (AGENTS.md §2.11)
tk = json.load(open(f"{REPO}/00_BRAND/tokens/tokens.json"))
def cor(*p):
    n = tk["cor"]
    for k in p: n = n[k]
    return n["$value"]
MARCA, PROFUNDA, TERRA = cor("marca","primaria"), cor("marca","profunda"), cor("marca","apoio")

AREIA, TINTA, SUAVE = cor("neutra","areia"), cor("neutra","tinta"), cor("texto","suave")

def archivo(tam, peso=900, larg=125):
    f = ImageFont.truetype(f"{SP}/fonts/Archivo.ttf", tam)
    f.set_variation_by_axes([peso, larg])     # [Weight, Width]
    return f
def mont(tam, estilo="SemiBold"):
    return ImageFont.truetype(f"/Users/klaus/Library/Fonts/Montserrat-{estilo}.ttf", tam)

def cabe(texto, largura, tam_max, peso=900, larg=125):
    """Maior corpo de Archivo em que o texto ainda cabe na largura dada."""
    tam = tam_max
    while tam > 20:
        f = archivo(tam, peso, larg)
        if f.getbbox(texto)[2] - f.getbbox(texto)[0] <= largura:
            return f
        tam -= 2
    return archivo(20, peso, larg)

W, H = 1080, 1920
art = Image.new("RGB", (W, H), AREIA)
d = ImageDraw.Draw(art)

molde = Image.open(f"{REPO}/04_PRODUCTION/missoes/fontes/molde-video-missoes-v1.psd").convert("RGBA")
# o molde tem dois blocos: topo em 0-374 e rodape em 1393-1761. O rodape e
# colado rente ao pe da peca, para nao sobrar faixa de fundo embaixo dele.
topo = molde.crop((0, 0, W, 374))
rodape = molde.crop((0, 1393, W, 1761))
art.paste(topo, (0, 0), topo)
RODAPE_Y = H - rodape.height
art.paste(rodape, (0, RODAPE_Y), rodape)

M = 84                                      # margem lateral
def txt(x, y, s, fonte, fill, anchor="la", espaco=None):
    d.text((x, y), s, font=fonte, fill=fill, anchor=anchor)
    return y + (espaco if espaco is not None else fonte.size)

CAIXA = W - 2*M
y = 420
y = txt(M, y, "FEIRA", archivo(70), PROFUNDA, espaco=74)
fM = cabe("MISSIONÁRIA", CAIXA, 120)
y = txt(M, y, "MISSIONÁRIA", fM, MARCA, espaco=fM.size + 16)

d.rounded_rectangle([M, y, M+226, y+50], radius=25, fill=TERRA)
d.text((M+113, y+25), "6ª EDIÇÃO", font=mont(24, "Bold"), fill=AREIA, anchor="mm")
y += 86

d.rectangle([M, y+4, M+7, y+100], fill=TERRA)
txt(M+26, y, "17 DE OUTUBRO", archivo(50, 800), TINTA, espaco=0)
txt(M+26, y+54, "16H ÀS 22H", archivo(50, 800), TINTA, espaco=0)
y += 122

y = txt(M, y, "Rua Jerivá, Lote 5 — próximo ao colégio CIESB", mont(25, "Medium"), SUAVE, espaco=62)

# a linha comeca depois da largura real do texto, nunca num valor chutado
fB = archivo(32, 800)
bbB = fB.getbbox("BARRACAS")
txt(M, y, "BARRACAS", fB, MARCA, espaco=0)
linha_x = M + (bbB[2] - bbB[0]) + 26
linha_y = y + (bbB[1] + bbB[3]) // 2          # meio da altura das maiusculas
d.line([(linha_x, linha_y), (W-M, linha_y)], fill=TERRA, width=3)
y += 60

BARRACAS = [("Churrasco","Min. Homens"), ("Caldos","Min. Juventude"),
            ("Sobremesas","Min. Mulheres"), ("Hambúrguer","Min. Recepção"),
            ("Pastel e Esfirra","Embaixadores do Rei"), ("Sorvete e Açaí","PIBAC Kids"),
            ("Bebidas","Mensageiras do Rei")]
col_w, lin_h = CAIXA//2, 78
for i, (nome, min_) in enumerate(BARRACAS):
    cx = M + (i % 2) * col_w
    cy = y + (i // 2) * lin_h
    d.text((cx, cy), nome, font=mont(31, "Bold"), fill=PROFUNDA)
    d.text((cx, cy+37), min_, font=mont(23, "Medium"), fill=SUAVE)
y += 4 * lin_h + 4

d.rectangle([M, y, W-M, y+3], fill=TERRA)
y += 22
y = txt(M, y, "“E como ouvirão se não há quem pregue?", mont(24, "MediumItalic"), TINTA, espaco=33)
y = txt(M, y, "E como pregarão, se não forem enviados?”", mont(24, "MediumItalic"), TINTA, espaco=31)
txt(M, y, "ROMANOS 10.14,15", mont(20, "Bold"), MARCA, espaco=0)
y += 24

art.save(f"{SP}/arte/story-feira-missionaria-v1.png")
print("gerado:", art.size, "| miolo termina em y =", y, "| rodape comeca em", RODAPE_Y, "->", "OK" if y < RODAPE_Y else "INVADE")
