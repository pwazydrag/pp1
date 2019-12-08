class ebook():
    def __init__(self, author, title, pamount):
        self.author=author
        self.title=title
        self.pamount=pamount
        self.current_page=1
        self.is_open=False
    def ebook_open(self):
        self.is_open=True
    def ebook_close(self):
        self.is_open=False
    def page_read(self):
        if self.is_open==True:
            self.current_page+=1
        else:
            print("Książka jest zamknięta, nie możesz tego zrobić.")
    def ebook_status(self):
        if self.is_open==True:
            print(f"Autor książki to: {self.author}, jej tytuł to: {self.title}, liczba jej stron: {self.pamount}, znajdujesz się na stronie numer {self.current_page}")
        else:
            print("Książka jest zamknięta.")
numer_rachunku=12345678901234567812345678            
widoknumeru=""
widoknumeru+=str(numer_rachunku)[0:2]
poma=2
pomb=6
for v in range (0,6):
    widoknumeru+=" "
    widoknumeru+=str(numer_rachunku)[poma:pomb]
    poma+=4
    pomb+=4
print(widoknumeru)