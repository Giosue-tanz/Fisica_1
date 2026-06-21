import fitz
import os

def extract_all(pdf_path, out_dir, start_page=0):
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    for p in range(start_page, doc.page_count):
        page = doc.load_page(p)
        pix = page.get_pixmap(dpi=150)
        out_path = os.path.join(out_dir, f"page_{p}.png")
        pix.save(out_path)
        print(f"Saved {out_path}")

extract_all("Appunti_Originali/Corpo rigido e oscillazioni.pdf", "Appunti_Originali/Corpo_rigido_img", 12)
extract_all("Appunti_Originali/Reattività e suatemi inerziali rotanti e a amassa variabile.pdf", "Appunti_Originali/Reattivita_img", 0)
extract_all("Appunti_Originali/Termodinamico.pdf", "Appunti_Originali/Termodinamico_img", 0)
