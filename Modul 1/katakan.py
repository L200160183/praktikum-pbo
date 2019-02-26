def katakanlah(angka, lv=0):
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    level = ['', 'ribu', 'juta']
    if lv == 0:
        angka = '{:0,.0f}'.format(int(angka))
        angka = angka.split(",")
    katakan = []
    for x in angka[::-1]:
        if int(x[-2:])<20 and int(x[-2:])>0:
            print(satuan[int(x[-2:])-1])
        elif int(x[-2:])>0:
            if int(x[-1])!=0:
                print(satuan[int(x[-1])-1])
            if int(x[-2]) != 0:
                print(satuan[int(x[-2])-1]+" puluh")
        if int(x[0])>=2 and len(x)==3 :
            katakan.append(satuan[int(x[0])-1]+" ratus")
        elif len(x)==3 and int(x[0])!=0 :
            print("seratus")
        print(level[lv])
        lv+=1
    return(katakan)
