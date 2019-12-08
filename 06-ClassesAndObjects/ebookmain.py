from ebook import ebook
HGames=ebook("Suzanne Collins", "Hunger Games", 400)
HGames.ebook_open()
HGames.ebook_status()
for v in range (0,51):
    HGames.page_read()
HGames.ebook_status()
HGames.ebook_close()
HGames.page_read()