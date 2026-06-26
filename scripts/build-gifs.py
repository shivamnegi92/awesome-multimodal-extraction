#!/usr/bin/env python3
"""Build the README hero GIF for awesome-multimodal-extraction.

An image thumbnail + a caption go in; entities come out, each tagged by the
modality it came from (img / txt). SVG frames -> PNG (rsvg-convert) -> GIF
(Pillow). No ffmpeg/gifski.
"""
import os
import subprocess
import tempfile
from PIL import Image

W, H = 880, 440
BG, CARD, FG, DIM, BORDER = "#0d1117", "#161b22", "#c9d1d9", "#8b949e", "#30363d"
TYPE = {"ORG": "#79c0ff", "GPE": "#7ee787", "DATE": "#ffa657", "PRODUCT": "#d2a8ff"}
MONO = 'font-family:"SF Mono","JetBrains Mono",Menlo,Consolas,monospace;'
SANS = "font-family:-apple-system,Segoe UI,Roboto,sans-serif;"

# (text, type, source)
ENTS = [
    ("Globex", "ORG", "img"),
    ("Paris", "GPE", "txt"),
    ("March 3", "DATE", "img"),
    ("Model X", "PRODUCT", "txt"),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def frame(n):
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<style>.m{{{MONO}}}.s{{{SANS}}}</style>',
        f'<rect width="{W}" height="{H}" fill="{BG}"/>',
        f'<text x="36" y="42" class="s" font-size="20" font-weight="700" fill="{FG}">Multimodal Extraction</text>',
        f'<text x="38" y="64" class="m" font-size="12" fill="{DIM}">image + text in -> structured entities out</text>',
        # INPUT card
        f'<rect x="36" y="86" width="380" height="200" rx="10" fill="{CARD}" stroke="{BORDER}"/>',
        f'<text x="52" y="110" class="m" font-size="12" fill="{DIM}">INPUT</text>',
        # mock image thumbnail
        f'<rect x="52" y="122" width="150" height="120" rx="6" fill="#0d1117" stroke="{BORDER}"/>',
        f'<rect x="64" y="134" width="80" height="14" rx="3" fill="#79c0ff"/>',          # logo bar
        f'<text x="68" y="145" class="s" font-size="10" font-weight="700" fill="#0d1117">GLOBEX</text>',
        f'<rect x="64" y="158" width="120" height="8" rx="2" fill="#30363d"/>',
        f'<rect x="64" y="172" width="100" height="8" rx="2" fill="#30363d"/>',
        f'<rect x="64" y="206" width="70" height="20" rx="3" fill="#ffa657"/>',           # banner
        f'<text x="70" y="220" class="s" font-size="10" font-weight="700" fill="#0d1117">MARCH 3</text>',
        f'<text x="214" y="140" class="m" font-size="11" fill="{DIM}">image</text>',
        # caption text
        f'<text x="214" y="170" class="s" font-size="14" fill="{FG}">caption:</text>',
        f'<text x="214" y="192" class="s" font-size="14" fill="{FG}">"Model X lands</text>',
        f'<text x="214" y="212" class="s" font-size="14" fill="{FG}"> in Paris!"</text>',
        f'<text x="214" y="236" class="m" font-size="11" fill="{DIM}">text</text>',
        # OUTPUT
        f'<text x="450" y="110" class="m" font-size="12" fill="{DIM}">EXTRACTED ENTITIES</text>',
    ]
    y = 128
    for i, (t, ty, src) in enumerate(ENTS):
        if i >= n:
            break
        p.append(f'<rect x="450" y="{y}" width="104" height="28" rx="6" fill="{TYPE[ty]}"/>')
        p.append(f'<text x="502" y="{y+19}" text-anchor="middle" class="m" font-size="12" font-weight="700" fill="#0d1117">{ty}</text>')
        p.append(f'<text x="566" y="{y+19}" class="s" font-size="15" fill="{FG}">{esc(t)}</text>')
        sc = "#79c0ff" if src == "img" else "#7ee787"
        p.append(f'<rect x="700" y="{y+4}" width="58" height="20" rx="10" fill="none" stroke="{sc}"/>')
        p.append(f'<text x="729" y="{y+18}" text-anchor="middle" class="m" font-size="10" fill="{sc}">{src}</text>')
        y += 40
    p.append("</svg>")
    return "\n".join(p)


def main():
    tmp = tempfile.mkdtemp()
    imgs, durs = [], []
    seq = [(0, 900)] + [(i, 800) for i in range(1, len(ENTS) + 1)] + [(len(ENTS), 2600)]
    for j, (n, ms) in enumerate(seq):
        path = os.path.join(tmp, f"f{j:02d}.png")
        sp = path + ".svg"
        open(sp, "w").write(frame(n))
        subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), sp, "-o", path], check=True)
        os.remove(sp)
        imgs.append(Image.open(path).convert("RGB"))
        durs.append(ms)
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "demo.gif"))
    imgs[0].save(out, save_all=True, append_images=imgs[1:], duration=durs, loop=0, optimize=True, disposal=2)
    print("wrote", out, f"({len(imgs)} frames, {os.path.getsize(out)//1024} KB)")


def build_decision():
    w, h = 900, 540
    DT = {"a": "#79c0ff", "b": "#d2a8ff", "c": "#7ee787", "d": "#ffa657", "e": "#f2cc60"}
    steps = [
        ("Input is a PDF or scanned doc?", "Docling / Marker / MinerU", "a"),
        ("Just need clean text (OCR)?", "Surya / PaddleOCR / Tesseract", "b"),
        ("Arbitrary fields from an image?", "VLM (Qwen2.5-VL) + schema", "c"),
        ("Tiny / on-device?", "moondream / SmolVLM", "d"),
        ("Image+text NER (social media)?", "GLiNER + MNER models", "e"),
    ]
    qx, qw, qh, cx, cw, y0, gap = 40, 380, 50, 480, 380, 100, 78

    def frame(n):
        p = [f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{GRAY}"/></marker></defs>']
        head(p, w, "Which multimodal tool should I pick?", "answer top-down; first YES wins")
        for i, (q, rec, c) in enumerate(steps):
            if i >= n:
                continue
            y = y0 + i * gap
            p.append(f'<rect x="{qx}" y="{y}" width="{qw}" height="{qh}" rx="10" fill="{CARD}" stroke="{BORDER}"/>')
            p.append(f'<text x="{qx+18}" y="{y+31}" class="s" font-size="15" fill="{FG}">{esc(q)}</text>')
            ay = y + qh // 2
            p.append(f'<line x1="{qx+qw}" y1="{ay}" x2="{cx}" y2="{ay}" stroke="{GRAY}" stroke-width="2" marker-end="url(#ar)"/>')
            p.append(f'<text x="{qx+qw+16}" y="{ay-6}" class="m" font-size="10" fill="{DT[c]}">YES</text>')
            p.append(f'<rect x="{cx}" y="{y+5}" width="{cw}" height="40" rx="8" fill="{DT[c]}"/>')
            p.append(f'<text x="{cx+cw/2}" y="{y+31}" text-anchor="middle" class="s" font-size="15" font-weight="700" fill="#0d1117">{esc(rec)}</text>')
            if i < len(steps) - 1:
                p.append(f'<line x1="{qx+30}" y1="{y+qh}" x2="{qx+30}" y2="{y+gap}" stroke="{BORDER}" stroke-width="2"/>')
                p.append(f'<text x="{qx+40}" y="{y+qh+17}" class="m" font-size="9" fill="{DIM}">no</text>')
        if n > len(steps):
            yd = y0 + len(steps) * gap
            p.append(f'<text x="{qx+18}" y="{yd+4}" class="m" font-size="12" fill="{DIM}">else:</text>')
            p.append(f'<rect x="{cx}" y="{yd-14}" width="{cw}" height="40" rx="8" fill="none" stroke="#56d4dd" stroke-width="2"/>')
            p.append(f'<text x="{cx+cw/2}" y="{yd+12}" text-anchor="middle" class="s" font-size="15" font-weight="700" fill="#56d4dd">Florence-2 (general vision)</text>')
        return p

    tmp = tempfile.mkdtemp()
    imgs, durs = [], []
    seq = [(0, 700)] + [(i, 800) for i in range(1, len(steps) + 1)] + [(len(steps) + 1, 900), (len(steps) + 1, 3000)]
    for jj, (n, ms) in enumerate(seq):
        path = os.path.join(tmp, f"d{jj:02d}.png")
        sp = path + ".svg"
        open(sp, "w").write("\n".join([f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>.m{{{MONO}}}.s{{{SANS}}}</style><rect width="{w}" height="{h}" fill="{BG}"/>'] + frame(n) + ["</svg>"]))
        subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), sp, "-o", path], check=True)
        os.remove(sp)
        imgs.append(Image.open(path).convert("RGB"))
        durs.append(ms)
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "decision.gif"))
    imgs[0].save(out, save_all=True, append_images=imgs[1:], duration=durs, loop=0, optimize=True, disposal=2)
    print("wrote", out, f"({len(imgs)} frames, {os.path.getsize(out)//1024} KB)")


def head(p, w, title, sub):
    p.append(f'<text x="36" y="42" class="s" font-size="20" font-weight="700" fill="{FG}">{esc(title)}</text>')
    p.append(f'<text x="38" y="64" class="m" font-size="12" fill="{DIM}">{esc(sub)}</text>')


GRAY = "#6e7681"

if __name__ == "__main__":
    main()
    build_decision()
