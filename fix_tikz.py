import re
from glob import glob

for filepath in glob("Capitoli/*.tex"):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace teal with mypen
    content = content.replace("teal", "mypen")
    
    # Replace gray!30 for fills with gray!10
    content = content.replace("fill=gray!30", "fill=gray!10")
    content = content.replace("fill=gray!20", "fill=gray!10")
    
    # Axes color
    content = content.replace("gray!80", "black!80")
    
    # Check for z-axis circle
    # The prompt asks for: \draw (x, y) circle (2pt); \fill (x, y) circle (0.5pt); for out of page axis.
    # Usually this is \odot. If there are \odot uses, maybe leave them.
    
    with open(filepath, 'w') as f:
        f.write(content)
        
print("Tikz colors fixed.")
