import os

target = "Capitoli/Corpo_rigido_e_oscillazioni.tex"
src_dir = "Appunti_Originali/Trascrizioni"
pages = list(range(13, 22))

with open(target, "a") as f:
    for page in pages:
        filename = os.path.join(src_dir, f"corpo_rigido_page_{page}.tex")
        if os.path.exists(filename):
            with open(filename, "r") as src:
                f.write("\n" + src.read())
