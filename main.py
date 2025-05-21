import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot
from docx import Document

from components import __sequency__


# class App(QObject):
#     def __init__(self):
#         QObject.__init__(self)

#     @Slot()
#     def engine(self):
#         doc = Document()
#         self._loop(doc)
#         doc.save('demo.docx')    

#     def _loop(self, doc):
#         for c in __sequency__.components:
#             c(doc).run()         

if __name__ == '__main__':
    # app = QGuiApplication(sys.argv)
    # engine = QQmlApplicationEngine()
    # backend = App()
    # engine.rootContext().setContextProperty("backend", backend)
    # engine.addImportPath(sys.path[0])
    # engine.loadFromModule("ui", "Main")
    # if not engine.rootObjects():
    #     sys.exit(-1)
    # exit_code = app.exec()
    # del engine
    # sys.exit(exit_code)
    def engine():
        doc = Document()
        _loop(doc)
        doc.save('generated/demo.docx')    

    def _loop(doc):
        for c in __sequency__.components:
            c(doc).run()  

    engine()