APPUNTI DI FISICA 1 (Scienze Fisiche e Informatiche)

DESCRIZIONE
Questo progetto raccoglie una sintesi completa e formalizzata del corso di Fisica I, con un particolare focus sulla meccanica classica e la termodinamica. Il documento e' scritto interamente in LaTeX, utilizzando lo stile ClassicThesis per un'estetica curata e accademica.

PANORAMICA DEL PROGETTO
Gli appunti coprono diversi ambiti fondamentali, tra cui:
- Cinematica: Studio del moto, sistemi di riferimento, moti unidimensionali e circolari.
- Dinamica del Punto e dei Sistemi: Principi di Newton, forze, attriti e leggi di conservazione.
- Urti: Dinamica degli urti elastici e anelastici.
- Corpo Rigido: Rotazioni, momenti d'inerzia e oscillazioni.
- Termodinamica (in corso di integrazione).

I diagrammi sono realizzati tramite TikZ per garantire alta qualita' vettoriale.

STRUTTURA DELLA REPOSITORY
La cartella e' organizzata nei seguenti moduli:

/Capitoli        Contiene i file .tex dei singoli argomenti.
/Figure          Asset grafici e immagini utilizzate nel documento.
/Frontespizio    Configurazione della pagina del titolo.
/Appunti_Originali  Materiale di riferimento e scansioni originali.
Appunti_di_Fisica_1.tex  Il file principale da compilare.

REQUISITI E COMPILAZIONE
Per generare il PDF e' necessaria una distribuzione LaTeX (es. TeX Live o MiKTeX).

1. Clona la repository:
   git clone https://github.com/Giosue-tanz/Appunti-di-Fisica-1---Universit-di-Pisa

2. Compila il file principale (sono necessarie almeno due passate):
   pdflatex Appunti_di_Fisica_1.tex

Librerie consigliate: ClassicThesis, TikZ, TColorBox.

AUTORI
Giosuè Aiello e Chiara Rustici
Studenti di Fisica presso il Dipartimento di Fisica dell'Universita' di Pisa

LICENZA
Questo progetto e' rilasciato sotto licenza Creative Commons Attribution-NonCommercial 4.0 International.
