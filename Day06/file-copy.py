import shutil

#
# Funkcja kopiujaca pliki
#
def copy_file(src, dst, buffer_size=4096):
    with open(src,"rb") as f1, open(dst, "wb") as f2:
        while True:
            #odczytaj z src
            buf = f1.read(buffer_size)
            #sprawdz czy nie koniec
            if not buf:
                break
            #zapisz do dst
            f2.write(buf)
        f2.flush()


#copy_file("plik.png", "plik2.png", 1024*1024)
shutil.copy("plik.png", "plik2.png")