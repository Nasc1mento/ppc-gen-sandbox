from docx import Document    

class PageBreak:
    def __init__(self, doc = None):
       self.doc = doc or Document()

    def run(self):
        self.doc.add_page_break()