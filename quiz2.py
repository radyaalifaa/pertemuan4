a = []       
while True:  
    angka = int(input("masukkan angka utnuk list, \n '-1000' jika sudah cukup \n :" ))
    if angka == -1000:
        break
    a.append(angka)
print(f"list anda adalah {a}")
if len(a)==0:
    print("list anda kosong silahkan isi angka !")
else:
    angka_terbesar = a[0]
    for angka in a :
        if angka > angka_terbesar:
            angka_terbesar = angka
    print(f"angka terbesar adalah {angka_terbesar}")