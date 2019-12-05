class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no=1
        self.channels=[]
        self.volume=0
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def set_channel(self, new_channel_no):
        self.channel_no=new_channel_no
    def set_channels(self, channels_list):
        self.channels=channels_list
    def volume_up(self):
        if self.volume==10:
            self.volume=10
        else:
            self.volume+=1
    def volume_down(self):
        if self.volume==0:
            self.volume=0
        else:
            self.volume-=1
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
        pom=self.channel_no-1
        if self.is_on==True and len(self.channels)>0:
            return f"Telewizor jest załączony, kanał {self.channel_no} ({self.channels[pom]}), głośność wynosi: {self.volume} "
        elif self.is_on==True and len(self.channels)==0:
            return f"Telewizor jest załączony, kanał {self.channel_no}, głośność wynosi: {self.volume}"
        else:
            return "Telewizor nie jest załączony"
        
myTV=TV()
print(myTV.show_status())
myTV.on()
print(myTV.show_status())
tab=["TVP1", "TVP2", "POLSAT", "TVN", "FILMBOX"]
myTV.set_channels(tab)
myTV.show_channels()
print(myTV.show_status())
myTV.set_channel(4)
for xd in range (0,13):
    myTV.volume_up()
for xD in range (0,5):
    myTV.volume_down()
print(myTV.show_status())
