import React from "react";
import {
  AbsoluteFill,
  CalculateMetadataFunction,
  Img,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont as loadArchivo } from "@remotion/google-fonts/Archivo";
import { loadFont as loadMontserrat } from "@remotion/google-fonts/Montserrat";
import {
  Camera,
  Layer,
  MaskedWords,
  ShutterBlur,
  Stage,
  ease,
  sec,
  tween,
} from "../../src/fluid";

// Feira Missionária 6ª edição — Story 9:16, 15s.
// Direção: projects/pibac-feira-missionaria/brief/PROMPT.md
// Fio condutor: a ONDA do símbolo da PIBAC. Traço sob o "É HOJE!" -> régua do
// título -> bancada da informação -> bancada onde as barracas se acumulam ->
// sobe e abre para o versículo -> assenta como a onda da própria marca.
// Família de stage: clara (a PIBAC é identidade clara — nunca sobre preto).

const { fontFamily: ARCHIVO } = loadArchivo("normal", {
  weights: ["700", "900"],
  subsets: ["latin", "latin-ext"],
});
const { fontFamily: MONT } = loadMontserrat("normal", {
  weights: ["400", "500", "600", "700"],
  subsets: ["latin", "latin-ext"],
});

// Tokens — 00_BRAND/tokens/tokens.json. Nenhum hex inventado.
const MARCA = "#007CC2";
const PROFUNDA = "#475E6B";
const TERRA = "#A68A69";
const AREIA = "#EFEAE4";
const TINTA = "#242D33";
const SUAVE = "#5C727F";
const BRANCO = "#FFFFFF";

const W = 1080;
const H = 1920;
const FPS = 60;
const TOTAL = 20;
const M = 92; // margem lateral

const EXPANDED = { fontVariationSettings: "'wdth' 125" } as const;

// ───────────────────────────────────────────────── o fio: uma função só
// Todo tempo desenha a onda com ESTA função. Nos seams os dois lados chamam
// a mesma coisa no mesmo quadro — é o mesmo objeto trocando de dono.
const ondaPath = (y: number, amp: number, fase: number, largura = W): string => {
  const passos = 48;
  const pts: string[] = [];
  for (let i = 0; i <= passos; i++) {
    const t = i / passos;
    const x = t * largura;
    const yy = y + Math.sin(t * Math.PI * 3 + fase) * amp * Math.sin(t * Math.PI);
    pts.push(`${i === 0 ? "M" : "L"}${x.toFixed(1)},${yy.toFixed(1)}`);
  }
  return pts.join(" ");
};

const Onda: React.FC<{ y: number; amp: number; fase: number; desenho: number; cor?: string; peso?: number }> = ({
  y,
  amp,
  fase,
  desenho,
  cor = MARCA,
  peso = 7,
}) => {
  const d = ondaPath(y, amp, fase);
  const comp = 2400;
  return (
    <svg width={W} height={H} style={{ position: "absolute", inset: 0 }}>
      {[0, 1, 2].map((i) => (
        <path
          key={i}
          d={ondaPath(y + i * 20, amp * (1 - i * 0.18), fase + i * 0.5)}
          fill="none"
          stroke={cor}
          strokeWidth={peso - i}
          strokeLinecap="round"
          opacity={i === 0 ? 1 : 0.45 - i * 0.12}
          strokeDasharray={comp}
          strokeDashoffset={comp * (1 - Math.max(0, Math.min(1, desenho - i * 0.08)))}
        />
      ))}
      <path d={d} fill="none" stroke="none" />
    </svg>
  );
};

// ───────────────────────────────────────────────── tempos
// 20s a 60fps = 1200 quadros. As barracas ficam com 420 — sete entradas a
// cada 30 quadros e ainda ~3,5s com as sete na tela, tempo de ler.
const B = {
  hoje: [0, 150],
  titulo: [130, 290],
  data: [270, 480],
  barracas: [460, 880],
  verso: [860, 1200],
  assina: [980, 1200],
} as const;

const vivo = (f: number, [a, b]: readonly [number, number]) => f >= a - 1 && f <= b + 40;
const ateOFim = (f: number, a: number) => f >= a - 1;

// aparece com amortecimento e sobe 34px
const entra = (f: number, at: number, dur = 34) => {
  const p = tween(f, [at, at + dur], [0, 1], ease.glide);
  return { opacity: p, transform: `translateY(${(1 - p) * 34}px)` };
};
const sai = (f: number, at: number, dur = 20) => tween(f, [at, at + dur], [1, 0], ease.glide);

const BARRACAS: [string, string][] = [
  ["Churrasco", "Min. Homens"],
  ["Caldos", "Min. Juventude"],
  ["Sobremesas", "Min. Mulheres"],
  ["Hambúrguer", "Min. Recepção"],
  ["Pastel e Esfirra", "Embaixadores do Rei"],
  ["Sorvete e Açaí", "PIBAC Kids"],
  ["Bebidas", "Mensageiras do Rei"],
];

export interface SceneProps {}

export const Scene: React.FC<SceneProps> = () => {
  const frame = useCurrentFrame();

  // a onda: posição e desenho ao longo da peça inteira
  const ondaY = 980
    + tween(frame, [B.titulo[0], B.data[0]], [0, 90], ease.glide)
    + tween(frame, [B.data[1] - 60, B.barracas[0] + 60], [0, 260], ease.glide)
    + tween(frame, [B.verso[0], B.verso[0] + 70], [0, -680], ease.glide)
    + tween(frame, [B.assina[0], B.assina[0] + 70], [0, 215], ease.glide);
  const ondaDesenho = tween(frame, [12, 110], [0, 1], ease.glide);
  const ondaAmp = 26
    + tween(frame, [B.data[0], B.data[0] + 60], [0, -16], ease.glide)
    + tween(frame, [B.verso[0], B.verso[0] + 60], [0, 22], ease.glide);
  const ondaFase = frame / 90;

  const empurra = frame >= B.barracas[0] - 30 && frame <= B.barracas[0] + 20;

  return (
    <Stage base={AREIA} glows={[]} grain={0.035} vignette={0.16} seed="pibac-feira">
      {/* moldura do molde aprovado: a marca da PIBAC em cima e a assinatura da
          campanha embaixo, presentes o tempo todo. Sem moldura o quadro 9:16
          fica com um terço chapado em cima e outro embaixo. */}
      <Camera
        keys={[
          { frame: 0, z: -90, y: 10 },
          { frame: sec(2.5, FPS), z: -40 },
          { frame: sec(4.8, FPS), z: 0, y: 0 },
          { frame: sec(8.0, FPS), z: 22, ry: 0.5 },
          { frame: sec(14.5, FPS), z: 50, ry: -0.4 },
          { frame: sec(16.6, FPS), z: 0, ry: 0, easing: ease.whip },
          { frame: sec(TOTAL, FPS), z: 20 },
        ]}
        drift={{ amount: 7, rotate: 0.22 }}
      >
        <Layer depth={-70}>
          <Img src={staticFile("pibac/mn-topo.png")} style={{ position: "absolute", left: 0, top: 0, width: W }} />
          <Img src={staticFile("pibac/mn-rodape.png")} style={{ position: "absolute", left: 0, bottom: 0, width: W }} />
        </Layer>

        {/* o fio, sempre presente, por baixo de tudo */}
        <Layer depth={-30}>
          <Onda y={ondaY} amp={ondaAmp} fase={ondaFase} desenho={ondaDesenho} />
        </Layer>

        <Layer depth={0}>
          {/* 1 — É HOJE! */}
          {vivo(frame, B.hoje) && (
            <AbsoluteFill style={{ opacity: sai(frame, B.titulo[0] - 8, 26) }}>
              <div style={{ position: "absolute", left: M, top: 640 }}>
                <div
                  style={{
                    fontFamily: ARCHIVO,
                    ...EXPANDED,
                    fontWeight: 900,
                    fontSize: 196,
                    lineHeight: 0.92,
                    color: MARCA,
                    letterSpacing: "-0.01em",
                  }}
                >
                  <MaskedWords words={[{ text: "É HOJE!" }]} start={4} duration={0.42} />
                </div>
              </div>
            </AbsoluteFill>
          )}

          {/* 2 — o nome da feira */}
          {vivo(frame, B.titulo) && (
            <AbsoluteFill style={{ opacity: sai(frame, B.data[0] - 8, 26) }}>
              <div style={{ position: "absolute", left: M, top: 500, width: W - 2 * M }}>
                <div
                  style={{
                    fontFamily: MONT,
                    fontWeight: 500,
                    fontSize: 44,
                    color: SUAVE,
                    ...entra(frame, B.titulo[0] + 6),
                  }}
                >
                  nossa
                </div>
                <div
                  style={{
                    fontFamily: ARCHIVO,
                    ...EXPANDED,
                    fontWeight: 900,
                    fontSize: 118,
                    lineHeight: 0.94,
                    color: TINTA,
                    marginTop: 8,
                    ...entra(frame, B.titulo[0] + 16),
                  }}
                >
                  FEIRA
                </div>
                <div
                  style={{
                    fontFamily: ARCHIVO,
                    ...EXPANDED,
                    fontWeight: 900,
                    fontSize: 118,
                    lineHeight: 0.94,
                    color: MARCA,
                    ...entra(frame, B.titulo[0] + 26),
                  }}
                >
                  MISSIONÁRIA
                </div>
                <div
                  style={{
                    display: "inline-block",
                    marginTop: 26,
                    padding: "12px 30px",
                    borderRadius: 999,
                    background: TERRA,
                    color: AREIA,
                    fontFamily: MONT,
                    fontWeight: 700,
                    fontSize: 28,
                    ...entra(frame, B.titulo[0] + 42),
                  }}
                >
                  6ª EDIÇÃO
                </div>
              </div>
            </AbsoluteFill>
          )}

          {/* 3 — quando e onde */}
          {vivo(frame, B.data) && (
            <AbsoluteFill style={{ opacity: sai(frame, B.barracas[0] - 8, 26) }}>
              <div style={{ position: "absolute", left: M, top: 520, width: W - 2 * M }}>
                <div
                  style={{
                    fontFamily: ARCHIVO,
                    ...EXPANDED,
                    fontWeight: 900,
                    fontSize: 98,
                    lineHeight: 0.96,
                    color: TINTA,
                    ...entra(frame, B.data[0] + 8),
                  }}
                >
                  17 DE
                  <br />
                  OUTUBRO
                </div>
                <div
                  style={{
                    fontFamily: ARCHIVO,
                    ...EXPANDED,
                    fontWeight: 700,
                    fontSize: 72,
                    color: MARCA,
                    marginTop: 18,
                    ...entra(frame, B.data[0] + 26),
                  }}
                >
                  16H ÀS 22H
                </div>
                <div
                  style={{
                    fontFamily: MONT,
                    fontWeight: 500,
                    fontSize: 36,
                    color: SUAVE,
                    marginTop: 34,
                    lineHeight: 1.35,
                    ...entra(frame, B.data[0] + 44),
                  }}
                >
                  Rua Jerivá, Lote 5
                  <br />
                  próximo ao colégio CIESB
                </div>
              </div>
            </AbsoluteFill>
          )}

          {/* 4 — as barracas acumulando */}
          {vivo(frame, B.barracas) && (
            <AbsoluteFill style={{ opacity: sai(frame, B.verso[0] - 12, 26) }}>
              <div style={{ position: "absolute", left: M, top: 430, width: W - 2 * M }}>
                <div
                  style={{
                    fontFamily: ARCHIVO,
                    ...EXPANDED,
                    fontWeight: 700,
                    fontSize: 46,
                    color: MARCA,
                    marginBottom: 30,
                    ...entra(frame, B.barracas[0]),
                  }}
                >
                  BARRACAS
                </div>
                {BARRACAS.map(([nome, min], i) => {
                  const at = B.barracas[0] + 30 + i * 30;
                  const e = entra(frame, at, 30);
                  return (
                    <div
                      key={nome}
                      style={{ display: "flex", alignItems: "baseline", gap: 20, marginBottom: 32, ...e }}
                    >
                      <span
                        style={{
                          width: 12,
                          height: 12,
                          borderRadius: 999,
                          background: TERRA,
                          display: "inline-block",
                          flexShrink: 0,
                        }}
                      />
                      <span style={{ fontFamily: MONT, fontWeight: 700, fontSize: 52, color: PROFUNDA }}>
                        {nome}
                      </span>
                      <span style={{ fontFamily: MONT, fontWeight: 500, fontSize: 31, color: SUAVE }}>
                        {min}
                      </span>
                    </div>
                  );
                })}
              </div>
            </AbsoluteFill>
          )}

          {/* 5 — o versículo */}
          {ateOFim(frame, B.verso[0]) && (
            <AbsoluteFill>
              <div style={{ position: "absolute", left: M, top: 985, width: W - 2 * M }}>
                <div
                  style={{
                    fontFamily: MONT,
                    fontWeight: 600,
                    fontStyle: "italic",
                    fontSize: 66,
                    lineHeight: 1.2,
                    color: TINTA,
                    ...entra(frame, B.verso[0] + 10, 40),
                  }}
                >
                  “E como ouvirão
                  <br />
                  se não há quem pregue?”
                </div>
                <div
                  style={{
                    fontFamily: MONT,
                    fontWeight: 700,
                    fontSize: 26,
                    color: MARCA,
                    marginTop: 26,
                    letterSpacing: "0.08em",
                    ...entra(frame, B.verso[0] + 40, 30),
                  }}
                >
                  ROMANOS 10.14,15
                </div>
              </div>
            </AbsoluteFill>
          )}

          {/* 6 — fecha onde começou: a urgência e a hora */}
          {vivo(frame, B.assina) && (
            <AbsoluteFill>
              <ShutterBlur active={frame >= B.assina[0] && frame <= B.assina[0] + 14} samples={8}>
                <div style={{ position: "absolute", left: M, top: 470, width: W - 2 * M }}>
                  <div
                    style={{
                      fontFamily: ARCHIVO,
                      ...EXPANDED,
                      fontWeight: 900,
                      fontSize: 150,
                      lineHeight: 0.92,
                      color: MARCA,
                      ...entra(frame, B.assina[0] + 4, 26),
                    }}
                  >
                    É HOJE!
                  </div>
                  <div
                    style={{
                      fontFamily: ARCHIVO,
                      ...EXPANDED,
                      fontWeight: 700,
                      fontSize: 62,
                      color: TINTA,
                      marginTop: 28,
                      ...entra(frame, B.assina[0] + 24, 30),
                    }}
                  >
                    16H ÀS 22H
                  </div>
                  <div
                    style={{
                      fontFamily: MONT,
                      fontWeight: 500,
                      fontSize: 33,
                      color: SUAVE,
                      marginTop: 16,
                      ...entra(frame, B.assina[0] + 38, 30),
                    }}
                  >
                    Rua Jerivá, Lote 5 · próximo ao colégio CIESB
                  </div>
                </div>
              </ShutterBlur>
            </AbsoluteFill>
          )}
        </Layer>
      </Camera>
    </Stage>
  );
};

export const calculateMetadata: CalculateMetadataFunction<SceneProps> = async () => ({
  durationInFrames: TOTAL * FPS,
  fps: FPS,
  width: W,
  height: H,
});
