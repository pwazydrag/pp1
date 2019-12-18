osoba = {
    "imie": "Marek",
    "nazwisko": "Banach",
    "wiek": 25,
    "hobby": ["programowanie","wycieczki"],
    "student": True,
    "telefon":{"stacjonarny":"2233","komorkowy":"7788"} }
print(osoba)
print()
print(osoba["nazwisko"])
print()
print(*osoba["hobby"], sep=", ")
print()
osoba["nazwisko"]="Nowak"
osoba["student"]=False
osoba["płeć"]="mężczyzna"
osoba["hobby"].append("rower")
osoba["telefon"]["służbowy"]=3131
for f in osoba:
    print(f,":", osoba[f])
print()