import tkinter as tk

def hasil_prediksi():
    label_hasil.config(text="Teknologi Informasi")

jendela = tk.Tk()
jendela.title("Prediksi Prodi")

label_judul = tk.Label(jendela, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14))
label_judul.grid(row=0, column=0, columnspan=2, pady=10)

# 10 input nilai mata pelajaran
for i in range(10):
    tk.Label(jendela, text="Nilai Mapel " + str(i + 1)).grid(row=i + 1, column=0, padx=10, pady=2)
    tk.Entry(jendela).grid(row=i + 1, column=1, padx=10, pady=2)

