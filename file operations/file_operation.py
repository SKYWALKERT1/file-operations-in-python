takimlarveoyuncular = {
    "Galatasaray.txt": [
        "futbolcular,mevki",
        "icardi,forvet",
        "muslera,kaleci",
        "sachaboey,sağbek",
        "angelinho,solbek",
        "torreira,ortasaha",
        "mertens,orta saha",
        "nelsson,defans",
        "Abdülkerim,defans",
        "kerem,solkanat",
        "tete,sağkanat",
        "zaha,ortasaha"
    ],
    "Fenerbahçe.txt": [
        "futbolcular,mevki",
        "lıvakovic,kaleci",
        "osayi-samuel,sağ kanat",
        "djiku,stoper",
        "oosterwolde,defans",
        "Kadıoğlu,ortasaha",
        "yüksek,önlibero",
        "fred,forvet",
        "can,ortasaha",
        "szymanski,sağkanat",
        "mor,orta saha",
        "dzeko,forvet"
    ],
    "Beşiktaş.txt": [
        "futbolcular,mevki",
        "destanoğlu,kaleci",
        "masuaku,solbek",
        "uysal,stoper",
        "sanuç,stoper",
        "rosier,defans",
        "redmond,sağortasaha",
        "uçan,ortasaha",
        "gedson,ortasaha",
        "nkoudou,forvet",
        "muleka,forvet",
        "tosun,forvet"
    ],
    "Trabzonspor.txt": [
        "futbolcular,mevki",
        "çakır,kaleci",
        "larsen,defans",
        "benkovic,defans",
        "fernandez,orta saha",
        "elmalı,defans",
        "mendy,defans",
        "özdemir,orta saha",
        "visca,sağ orta saha",
        "ömür,orta saha",
        "pepe,sağ kanat",
        "onuachu,forvet"
    ]
}

# Dosyaları oluşturur ve verileri yazmayı sağlar.
for dosyaadi, oyuncular in takimlarveoyuncular.items():
    with open(dosyaadi, 'w', encoding='utf-8') as dosya:
        dosya.write('\n'.join(oyuncular))

# Oluşturulan dosyalardan verileri okur ve ekrana yazdırmayı sağlar.
for dosyaadi in takimlarveoyuncular.keys():
    print(f"\n{dosyaadi.split('.')[0]} Takımı Oyuncu Listesi:")
    with open(dosyaadi, 'r', encoding='utf-8') as dosya:
        for satir in dosya:
            print(satir.strip())