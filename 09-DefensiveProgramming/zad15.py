student = 'Mateusz'
stypendium = 950
wydatki = 920
assert type(student)==str, "Podałes nieprawidłowe imię!"
assert type(stypendium)==int, "Wartość stypendium powinna być liczbą!"
assert type(wydatki)==int, "Wartość wydatków powinna być liczbą!"
print('Student: {}'.format(student.upper()))
print('stypendium: {} zł'.format(stypendium))
print('Wydatki: {} zł'.format(wydatki))
print('Oszczędności: {} zł'.format(stypendium-wydatki))