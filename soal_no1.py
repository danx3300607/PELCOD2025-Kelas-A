durasi_per_menit = 35 #menit
total_episode = 10

total_menit = total_episode * durasi_per_menit
jam = total_menit // 60 #dibagi dan dibulatkan
sisa_menit = total_menit % 60
print("total tonton:", total_menit, "menit")
print("atau:", jam, "jam", sisa_menit, "menit")