#!/usr/bin/env python
# coding: utf-8

# In[9]:


# soal yang pertama 
def cari_nilai_terbaik(daftar):
    daftar.sort(reverse=True)
    nilai_terbaik = daftar[:3]
    
    return nilai_terbaik
nilai = [80,70,75,88,67]
nilai_terbaik = cari_nilai_terbaik(nilai)

print("Tiga nilai terbaik adalah:", nilai_terbaik)




# In[11]:


# soal yang kedua 
nilai = []
while True:
    masukan = input("Masukkan angka (ketik 'done' untuk selesai): ")
    if masukan == 'done':
        break
    else:
        try:
            angka = float(masukan)
            nilai.append(angka)
        except ValueError:
            print("Masukan tidak valid. Silakan masukkan angka atau 'done'.")
if nilai:
    print("Nilai maksimum:", max(nilai))
    print("Nilai minimum:", min(nilai))
else:
    print("Tidak ada nilai yang dimasukkan.")


# In[ ]:




