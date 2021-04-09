nama = str(input("Masukkan nama anda: "))
n = int(input("Masukkan banyaknya nilai yang akan dihitung:" ))
xn = 0
for x in range(n):
    x = x + 1
    nilai = int(input("Masukkan nilai anda ke-%d: "%(x)))
    xn += nilai
    ratarata = xn/n
print(nama+',','jumlah total nilai anda adalah: {}'.format(xn))
print("Hi,", nama+"!", "Hasil rata-rata anda adalah:", ratarata)
