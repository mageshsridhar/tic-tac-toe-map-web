"""Builds index.html (the published page) from template.html and the 138 finished boards in endings.json."""
from pathlib import Path

here = Path(__file__).parent
page = (here / "template.html").read_text()
data = (here / "endings.json").read_text().strip()
(here / "index.html").write_text(page.replace("/*DATA*/", data, 1))
print("Wrote", here / "index.html")
