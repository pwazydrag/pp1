class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        pom=message[0].upper()+message[1:].lower()
        pom+=" BYE."
        self.message = pom
'''
class SMS(Message):
    def __init__(self, nrtel, nadawca, odbiorca):
        self.nrtel=nrtel
        self.nadawca=nadawca
        self.odbiorca=odbiorca
    def __str__(self):
        return f"Wysyłanie SMS...\n"
        '''
