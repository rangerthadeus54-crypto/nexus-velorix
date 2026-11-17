from pathlib import Path

from Retchan import HTML


project_root = Path(__file__).parent
output_directory = project_root / "public"
output_directory.mkdir(exist_ok=True)
(output_directory / "index.html").write_text(HTML, encoding="utf-8")
print(f"Built static site at {output_directory / 'index.html'}")
