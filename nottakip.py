import tkinter as tk
from tkinter import messagebox

# Ortalama hesaplama fonksiyonu
def ortalama_hesapla():
    try:
        not1 = float(entry_not1.get())
        not2 = float(entry_not2.get())
        not3 = float(entry_not3.get())
        ortalama = (not1 + not2 + not3) / 3
        label_sonuc.config(text=f"Ortalama: {ortalama:.2f}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli notlar giriniz.")

# Ana pencere
pencere = tk.Tk()
pencere.title("Öğrenci Not Takip Sistemi")
pencere.geometry("300x300")

# Öğrenci adı
tk.Label(pencere, text="Ad Soyad:").pack()
entry_ad = tk.Entry(pencere)
entry_ad.pack()

# Not girişleri
tk.Label(pencere, text="1. Not:").pack()
entry_not1 = tk.Entry(pencere)
entry_not1.pack()

tk.Label(pencere, text="2. Not:").pack()
entry_not2 = tk.Entry(pencere)
entry_not2.pack()

tk.Label(pencere, text="3. Not:").pack()
entry_not3 = tk.Entry(pencere)
entry_not3.pack()

# Hesapla butonu
tk.Button(pencere, text="Ortalama Hesapla", command=ortalama_hesapla).pack(pady=10)

# Sonuç etiketi
label_sonuc = tk.Label(pencere, text="")
label_sonuc.pack()

# Pencereyi çalıştır
pencere.mainloop()
