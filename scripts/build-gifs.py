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


if __name__ == "__main__":
    main()
