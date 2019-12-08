class Termometr():
    def __init__(self):
        self.temperature=0
        self.ready=False
    def włączTermometr(self):
        self.ready=True
    def wyłączTermometr(self):
        self.ready=False
    def zmierzTemperature(self):
        import random
        new_temperature=random.uniform(34.0, 42.0)
        pom=round(new_temperature, 1)
        self.temperature=pom
    def wyswietlTemperature(self):
        if self.ready==False:
            print("Termometr jest wyłączony.")
        else:
            if self.temperature >= 37.0 and self.temperature< 41.0:
                print(f"Zmierzona temperatura: {self.temperature} (gorączka)")
            elif self.temperature >= 34.0 and self.temperature<37.0:
                print(f"Zmierzona temperatura: {self.temperature}")
            elif self.temperature >=41.0:
                print(f"Zmierzona temperatura: {self.temperature} (ZAGROŻENIE ŻYCIA!!!!!)")
       
myTerm=Termometr()
myTerm.włączTermometr()
myTerm.zmierzTemperature()
myTerm.wyswietlTemperature()
myTerm.wyłączTermometr()
