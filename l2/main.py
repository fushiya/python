from gui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class Morse:

    def __init__(self):
        self.alphabetEng = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
                            "O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2",
                            "3","4","5","6","7","8","9","0",".",",","!",":",";"," ",
                            "(",")","-","?", "_", "'", "/", "+", "\n"]

        self.alphabetMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                              "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                              "..-","...-",".--","-..-","-.--","--..",".----","..---","...--",
                              "....-",".....","-....","--...","---..","----.","-----","......",
                              ".-.-.-","--..--","---...","-.-.-.","-...-","-.--.-","-.--.-",
                              "-....-","..--..","..--.-",".----.","-..-.",".-.-.", "\n"]

    def engToMorse(self, text):
        out = str()
        for i in text:
            if i.upper() in self.alphabetEng:
                out += self.alphabetMorse[ self.alphabetEng.index(i.upper()) ] + " "
        return out[:-1]

    def morseToEng(self, text):
        out = str()
        for i in text.split(" "):
            if i in self.alphabetMorse:
                out += self.alphabetEng[ self.alphabetMorse.index(i) ]
        return out



class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.translate = Morse()
        self.ui.pushButton.clicked.connect(self.startEngToMorse)
        self.ui.pushButton_2.clicked.connect(self.startMorseToEng)

    def startEngToMorse(self):
        self.ui.plainTextEdit.setPlainText( self.translate.engToMorse(self.ui.plainTextEdit.toPlainText()) )

    def startMorseToEng(self):
        self.ui.plainTextEdit.setPlainText( self.translate.morseToEng(self.ui.plainTextEdit.toPlainText()) )


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = window()
    application.show()
    sys.exit(app.exec())