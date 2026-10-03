from pathlib import Path

WIDTH = 520
HEIGHT = 300

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}" height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<rect width="100%" height="100%" rx="18"
      fill="#0d1117" stroke="#30363d" stroke-width="2"/>

<text x="30" y="42"
      font-family="monospace"
      font-size="22"
      font-weight="bold"
      fill="#58a6ff">
    shubh@github
</text>

<line x1="30" y1="62" x2="490" y2="62"
      stroke="#30363d"/>

<text x="30" y="100"
      font-family="monospace"
      font-size="17"
      fill="#8b949e">Role</text>

<text x="180" y="100"
      font-family="monospace"
      font-size="17"
      fill="#ffffff">CSE Student</text>

<text x="30" y="140"
      font-family="monospace"
      font-size="17"
      fill="#8b949e">Stack</text>

<text x="180" y="140"
      font-family="monospace"
      font-size="17"
      fill="#ffffff">Python • Java</text>

<text x="30" y="180"
      font-family="monospace"
      font-size="17"
      fill="#8b949e">Focus</text>

<text x="180" y="180"
      font-family="monospace"
      font-size="17"
      fill="#ffffff">AI / ML</text>

<text x="30" y="220"
      font-family="monospace"
      font-size="17"
      fill="#8b949e">Projects</text>

<text x="180" y="220"
      font-family="monospace"
      font-size="17"
      fill="#ffffff">Hackathons</text>

<text x="30" y="260"
      font-family="monospace"
      font-size="17"
      fill="#8b949e">Learning</text>

<text x="180" y="260"
      font-family="monospace"
      font-size="17"
      fill="#ffffff">DSA • Full Stack</text>

</svg>
"""

output = Path("info-card.svg")
output.write_text(svg, encoding="utf-8")

print(f"Created: {output.resolve()}")