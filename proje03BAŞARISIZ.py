from gensim.models import KeyedVectors
print("Bu Modelde Wikipedia Makalelerindeki Kelimelerin Benzerlik Oranlarını Ölçüyoruz Denemek İçin Lütfen Bekleyiniz.")
print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

print("Benzerlik Mi Ölçmek İstersiniz Yoksa Farklılık Mı?")
    input("Benzerlik/Farklılık:")

if "Benzerlik" in input:
    def benzerKelimeler():
        anahtarKelime = input("Aramak İstediğiniz Anahtar Kelimeyi Giriniz: ").lower()
        print(" ")
        print("Girilen Kelime : "+ str(anahtarKelime))
        print(" ")
        print("Anahtar Kelimeye En Yakın Kelimeler:")
        print(" ")
        oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))
        print(oneriler)
        print(" ")
        print("Ziyaret Etmek İsteyebileceğiniz Linkler:")
        print(" ")

            # İlk 10 öneriyi göster
        for index, oneri in enumerate(oneriler):
            if anahtarKelime not in oneri[0]:
                print("https://www.google.com/search?q=" + oneri[0])

        benzerKelimeler()

    benzerKelimeler()
else:
    def farkliBul():

        anahtarKelimeler = input("Anahtar Kelimeler: ").lower().split()

        benzerlik = (kelimeVektoru.doesnt_match(anahtarKelimeler))
        print(benzerlik)
        print("----------")
        farkliBul()


    farkliBul()