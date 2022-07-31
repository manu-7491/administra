#!/usr/bin/python3
import fitz
from pprint import pprint

doc = fitz.open("25-07-2022.pdf")

print(f"""
        Paginas: {str(doc.page_count)}
    """)

#pprint(doc.get_toc())

for pagina in doc.pages(step=1):
    internet = 0
    texto = pagina.get_textpage().extractText()
    palabras = texto.lower().strip().split(" ")
    for palabra in palabras:
        if palabra == "\ntotal":
                internet += 1
    print(f"Veces que se repite la palabra 'total' en la página {str(pagina.number)}: {str(internet)}") 
  
  
  
  
  
    # Cerrar el documento
doc.close()



"""


with open("25-07-2022.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
 
# Save all text to a txt file.
with open('output.txt', 'w') as f:
    f.write("\n\n".join(pdf))

"""

#if __name__ == '__main__': sys.exit(main(sys.argv))
