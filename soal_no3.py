import math

print("===perjalanan motor===")
print("1. hitung bensin dari jarak ")
print("2. hitung jarak  dari bensin")
pilihan = input("pilih menu (1/2:)")

#data dasar
konsumsi = 2.7 # km per liter

if pilihan == "1":
    #input jarak
    jarak_tempuh = float(input("masukkan total jarak (km):"))
    NIM3 = int(input("masukkan 3 angka terakhir NIM:"))
    NIM1 = (int(input("masukkan 1 angka terakhir NIM:")))

    kapasitas_tangki = NIM1 if NIM1 != 0 else 5
    harga_bensin = int("1" + str(NIM3) + "0")

    #hitung bensin
    total_bensin = jarak_tempuh / konsumsi

    #diskon Jika > 3 liter
    if total_bensin > 3:
        harga_bensin -= 500 #DISKON

    total_biaya = total_bensin * harga_bensin
    isi_tangki = math.floor(total_bensin / kapasitas_tangki)

    print("=== Hasil ===")
    print(f"Total bensin dibutuhkan : {total_bensin :.2f} liter")
    print(f"harga bensin / liter    : Rp {harga_bensin :}")
    print(f"total biaya bensin      : Rp {total_biaya :,.0f}")
    print(f"isi tangki penuh        : {isi_tangki} kali")
elif pilihan == "2":
    #input bensin
    bensin = float(input("masukkan total bensin (liter):"))
    jarak = bensin * konsumsi
    print("=== Hasil ===")
    print(f"dengan {bensin :.2f} liter bensin, motor bisa menempuh {math.ceil(jarak):.0f} km")

else:
    print("pilihan tidak valid")


