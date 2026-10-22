import tkinter as tk

def hasil_prediksi():
    label_hasil.config(text="Teknologi Informasi")

jendela = tk.Tk()
jendela.title("Prediksi Prodi")

label_judul = tk.Label(jendela, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14))
label_judul.grid(row=0, column=0, columnspan=2, pady=10)

