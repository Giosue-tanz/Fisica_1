import re

filepath = "Capitoli/Corpo_rigido_e_oscillazioni.tex"
with open(filepath, "r") as f:
    content = f.read()

# Remove standalone preamble stuff
patterns_to_remove = [
    r"\\documentclass.*?\{.*?\}\n",
    r"\\usepackage.*?\{.*?\}\n",
    r"\\geometry.*?\{.*?\}\n",
    r"\\begin\{document\}\n",
    r"\\end\{document\}\n",
]

for p in patterns_to_remove:
    content = re.sub(p, "", content)

# Fix \xmark to \ding{55} (assuming pifont will be loaded)
content = content.replace(r"\xmark", r"\ding{55}")

# Fix figure[H] to figure[ht] or similar
content = content.replace(r"\begin{figure}[H]", r"\begin{figure}[ht]")

with open(filepath, "w") as f:
    f.write(content)

print("Cleaned up Capitoli/Corpo_rigido_e_oscillazioni.tex")
