import re
import os
from glob import glob

for filepath in glob("Capitoli/*.tex"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We want to replace large tcolorbox environments if they contain too much text.
    # Actually, a better approach is to rewrite the specific ones we know.
    # Let's extract the boxes that are over ~25 lines.
    
    def repl(m):
        env = m.group(1)
        title = m.group(2)
        body = m.group(3)
        if body.count('\n') > 30:
            return f"\\subsection*{{{env.capitalize()}: {title}}}\n{body}"
        return m.group(0)
        
    pattern = re.compile(r'\\begin\{(teorema|definizione|osservazione|esercizio)\}\{(.*?)\}(.*?)\\end\{\1\}', re.DOTALL)
    new_content = pattern.sub(repl, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed boxes in {filepath}")
