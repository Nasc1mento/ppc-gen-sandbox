from docx import Document    

class PageBreak:
    def __init__(self, doc = Document()):
       self.doc = doc

    def run(self):
        self.doc.add_page_break()