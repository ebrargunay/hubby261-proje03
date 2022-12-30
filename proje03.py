import tkinter as tk
from gensim.models import KeyedVectors
pencere = tk.Tk()
pencere.title("Benzer Kelimeler")

etiket = tk.Label(pencere, text="Aramak İstediğiniz Anahtar Kelimeyi Giriniz:")
etiket.pack(padx=20, pady=20)

metinAlani = tk.Entry(pencere)
metinAlani.pack(padx=20, pady=20)

buton = tk.Button(pencere, text="Aramayı Başlatmak İçin Tıklayın")
buton.pack(padx=20, pady=20)

print("Bu Modelde Wikipedia Makalelerindeki Kelimelerin Benzerlik Oranlarını Ölçüyoruz Denemek İçin Lütfen Bekleyiniz.")
print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

def benzerKelimeler(self):
    anahtarKelimeler = metinAlani.get().lower()
    listeKelimeler = anahtarKelimeler.split()

    for anahtarKelime in listeKelimeler:
        print("Girilen Kelime: " + str(anahtarKelime))
        oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))
        print(oneriler)

        for oneri in oneriler:
            if anahtarKelime not in oneri[0]:
                print("https://www.google.com.tr/search?q=" + oneri[0])


buton.bind("<Button-1>", benzerKelimeler)

pencere.mainloop()