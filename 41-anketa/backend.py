from docxtpl import DocxTemplate
def fillDoc(info,fayl="anketa.docx"):
    anketa = DocxTemplate("anketa.docx")
    anketa.render(info)
    filename = f"{info['familiya']}_anketa.docx"
    anketa.save(filename)
    return filename