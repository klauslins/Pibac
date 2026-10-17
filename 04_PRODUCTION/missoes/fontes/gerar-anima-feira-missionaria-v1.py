import json, math, os, shutil
from PIL import Image, ImageDraw, ImageFont
SP = "/private/tmp/claude-501/-Volumes-Jess--Lima/fb9b4d6f-02dd-4a62-825a-2bdcbd7f667b/scratchpad"
REPO = "/Volumes/Jessé_Lima/05_DEV/Pibac"

tk = json.load(open(f"{REPO}/00_BRAND/tokens/tokens.json"))
def cor(*p):
    n = tk["cor"]
    for k in p: n = n[k]
    return n["$value"]
MARCA, PROFUNDA, TERRA = cor("marca","primaria"), cor("marca","profunda"), cor("marca","apoio")
AREIA, TINTA, SUAVE = cor("neutra","areia"), cor("neutra","tinta"), cor("texto","suave")

def archivo(t, p=900, l=125):
    f = ImageFont.truetype(f"{SP}/fonts/Archivo.ttf", t); f.set_variation_by_axes([p, l]); return f
def mont(t, e="SemiBold"):
    return ImageFont.truetype(f"/Users/klaus/Library/Fonts/Montserrat-{e}.ttf", t)
def cabe(texto, largura, tam_max, peso=900, larg=125):
    t = tam_max
    while t > 20:
        f = archivo(t, peso, larg)
        if f.getbbox(texto)[2] - f.getbbox(texto)[0] <= largura: return f
        t -= 2
    return archivo(20, peso, larg)

W, H, FPS, DUR = 1080, 1920, 30, 7.0
M = 84; CAIXA = W - 2*M

molde = Image.open(f"{REPO}/04_PRODUCTION/missoes/fontes/molde-video-missoes-v1.psd").convert("RGBA")
TOPO = molde.crop((0, 0, W, 374))
RODAPE = molde.crop((0, 1393, W, 1761))
RODAPE_Y = H - RODAPE.height

def suave(p):
    """Amortecimento: rápido no começo, assenta no fim. Sem repique."""
    p = max(0.0, min(1.0, p))
    return 1 - pow(1 - p, 3)

fM = cabe("MISSIONÁRIA", CAIXA, 120)
fB = archivo(32, 800); bbB = fB.getbbox("BARRACAS")
BARRACAS = [("Churrasco","Min. Homens"), ("Caldos","Min. Juventude"),
            ("Sobremesas","Min. Mulheres"), ("Hambúrguer","Min. Recepção"),
            ("Pastel e Esfirra","Embaixadores do Rei"), ("Sorvete e Açaí","PIBAC Kids"),
            ("Bebidas","Mensageiras do Rei")]

# ─── cada elemento: (t_inicio, duracao, desenha(d, dy)) ─────────────────────
def pos():
    """Devolve a lista de elementos com suas coordenadas finais, como na arte."""
    el, y = [], 420
    el.append(("feira", y, lambda d, Y: d.text((M, Y), "FEIRA", font=archivo(70), fill=PROFUNDA)))
    y += 74
    yM = y
    el.append(("miss", yM, lambda d, Y: d.text((M, Y), "MISSIONÁRIA", font=fM, fill=MARCA)))
    y += fM.size + 16
    yP = y
    def selo(d, Y):
        d.rounded_rectangle([M, Y, M+226, Y+50], radius=25, fill=TERRA)
        d.text((M+113, Y+25), "6ª EDIÇÃO", font=mont(24, "Bold"), fill=AREIA, anchor="mm")
    el.append(("selo", yP, selo)); y += 86
    yD = y
    def data(d, Y):
        d.rectangle([M, Y+4, M+7, Y+100], fill=TERRA)
        d.text((M+26, Y), "17 DE OUTUBRO", font=archivo(50, 800), fill=TINTA)
        d.text((M+26, Y+54), "16H ÀS 22H", font=archivo(50, 800), fill=TINTA)
    el.append(("data", yD, data)); y += 122
    yL = y
    el.append(("local", yL, lambda d, Y: d.text((M, Y), "Rua Jerivá, Lote 5 — próximo ao colégio CIESB",
                                                font=mont(25, "Medium"), fill=SUAVE)))
    y += 62
    yBar = y
    def barr(d, Y):
        d.text((M, Y), "BARRACAS", font=fB, fill=MARCA)
        lx = M + (bbB[2]-bbB[0]) + 26; ly = Y + (bbB[1]+bbB[3])//2
        d.line([(lx, ly), (W-M, ly)], fill=TERRA, width=3)
    el.append(("barracas", yBar, barr)); y += 60
    col_w, lin_h = CAIXA//2, 78
    for i, (nome, mi) in enumerate(BARRACAS):
        cx = M + (i % 2) * col_w; cy = y + (i // 2) * lin_h
        el.append((f"b{i}", cy, (lambda cx, nome, mi: lambda d, Y: (
            d.text((cx, Y), nome, font=mont(31, "Bold"), fill=PROFUNDA),
            d.text((cx, Y+37), mi, font=mont(23, "Medium"), fill=SUAVE)))(cx, nome, mi)))
    y += 4*lin_h + 4
    yV = y
    def verso(d, Y):
        d.rectangle([M, Y, W-M, Y+3], fill=TERRA)
        d.text((M, Y+22), "“E como ouvirão se não há quem pregue?", font=mont(24, "MediumItalic"), fill=TINTA)
        d.text((M, Y+55), "E como pregarão, se não forem enviados?”", font=mont(24, "MediumItalic"), fill=TINTA)
        d.text((M, Y+86), "ROMANOS 10.14,15", font=mont(20, "Bold"), fill=MARCA)
    el.append(("verso", yV, verso))
    return el

ELEMENTOS = pos()
TEMPOS = {"feira":0.00,"miss":0.18,"selo":0.52,"data":0.70,"local":0.95,"barracas":1.12}
for i in range(7): TEMPOS[f"b{i}"] = 1.34 + i*0.13
TEMPOS["verso"] = 2.40
ENTRADA = 0.62

frames = f"{SP}/arte/frames"
shutil.rmtree(frames, ignore_errors=True); os.makedirs(frames)
N = int(FPS*DUR)
for n in range(N):
    t = n/FPS
    art = Image.new("RGB", (W, H), AREIA)
    art.paste(TOPO, (0, 0), TOPO)
    for nome, y0, desenha in ELEMENTOS:
        p = suave((t - TEMPOS[nome]) / ENTRADA)
        if p <= 0: continue
        cam = Image.new("RGBA", (W, H), (0,0,0,0))
        desenha(ImageDraw.Draw(cam), y0 + int(round((1-p)*34)))
        if p < 1:
            a = cam.getchannel("A").point(lambda v: int(v*p))
            cam.putalpha(a)
        art.paste(cam, (0, 0), cam)
    art.paste(RODAPE, (0, RODAPE_Y), RODAPE)
    art.save(f"{frames}/{n:04d}.png")
print(f"{N} quadros renderizados")
