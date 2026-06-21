import fitz
import os

pdf_path = "Appunti_Originali/Corpo rigido e oscillazioni.pdf"
out_dir = "Appunti_Originali/Corpo_rigido_img"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for p in [5, 10, 15, 20]:
    page = doc.load_page(p)
    pix = page.get_pixmap(dpi=150)
    out_path = os.path.join(out_dir, f"page_{p}.png")
    pix.save(out_path)
    print(f"Saved {out_path}")
