from message import Message
class SMS(Message):
    def __init__(self, nrtel, nadawca, odbiorca):
        self.nrtel=nrtel
        self.nadawca=nadawca
        self.odbiorca=odbiorca
    def send(self):
        print(f"Wysyłanie SMS...\nOd:\t{self.nadawca}\nDo:\t{self.odbiorca}\nTreść:\t{self.message} ")
s1=SMS(66666662,"Ja","On")
s1.set_message("będę PóŹniej.")
s1.send()