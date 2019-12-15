from message9 import Message
class EMAIL(Message):
    def __init__(self, adresnadawcy, adresodbiorcy, temat):
        self.adresnadawcy=adresnadawcy
        self.adresodbiorcy=adresodbiorcy
        self.temat=temat
    def send(self):
        print(f"Wysyłanie emaila...\nOd:\t{self.adresnadawcy}\nDo:\t{self.adresodbiorcy}\nTemat:\t{self.temat}\nTreść:\t{self.message}")
e1=EMAIL("Ja","Ty","Ważne")
e1.set_message("Pozdrawiam.")
e1.send()