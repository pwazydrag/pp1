#13
def wspak(string):
    a=string.replace(" ","")
    return a
tekst="uniwersytet ekonomiczny w KRAKOWIE"
def rozstrzelone(string):
    a=" ".join(string)
    return a
def litery(string):
    a = string.title()
    return a
print(wspak(tekst))
print(rozstrzelone(tekst))
print(litery(tekst))