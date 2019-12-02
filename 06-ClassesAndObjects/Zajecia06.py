#7 + #8 + #9
class University():
# konstruktor obiektu (metoda __init__)
    def __init__(self):
# cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname='Uniwersytet Ekonomiczny w Krakowie'
# zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    def set_name(self,new_name):
        self.name = new_name
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self,new_fullname):
        self.fullname=new_fullname
nazwaUniwersytetu=University()
nazwaUniwersytetu.print_name()
nazwaUniwersytetu.print_fullname()
nazwaUniwersytetu.set_fullname("test")
nazwaUniwersytetu.print_fullname()
#newnazwa=University()
#newnazwa.set_name('AGH')
#newnazwa.print_name()

#10 + #11 + #12 + #13
class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no=1
        self.channels=[]
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def set_channel(self, new_channel_no):
        self.channel_no=new_channel_no
    def set_channels(self, channels_list):
        self.channels=channels_list
    def show_channels(self):
        pom=0
        if (len(self.channels)==0):
            print("Telewizor niezaprogramowany.")
        else:
            print("LISTA KANAŁÓW TV")
            for v in self.channels:
                pom+=1
                print(pom, end=". ")
                print(v)
    def show_status(self):
        if self.is_on==True:
            return f"Telewizor jest załączony, kanał {self.channel_no}"
        else:
            return "Telewizor nie jest załączony"

    
telewizor=TV()
print(telewizor.show_status())
telewizor.on()
print(telewizor.show_status())
telewizor.set_channel(13)
print(telewizor.show_status())
telewizor.off()
print(telewizor.show_status())
print()
tab=["TVP1", "TVP2", "POLSAT", "TVN", "FILMBOX"]
myTV=TV()
print(myTV.show_status())
myTV.on()
print(myTV.show_status())
myTV.show_channels()
myTV.set_channels(tab)
myTV.show_channels()
myTV.show_status()
myTV.off()
print()

'''
VISUAL STUDIO CODE <- PYTHON
trzeba kliknac na code extensions
i potem bedzie dzialac
python python for visual code
file -> autosave
CTRL + F5 uruchomienie

'''