#
# UTS Sistem Pakar
# Data diambil dari jurnal "Sistem Pakar Deteksi Penyakit pada Anak Menggunakan Metode Forward Chaining"
# https://jsisfotek.org/index.php/JSisfotek/article/view/34/34
#
# Rizky Alhafiz   (200504064)
# Ryan Alfiansyah (230504109)
# M. Fadli        (240504066)
#

data_penyakit = {
	"T01": "Diare",
	"T02": "Kejang Demam",
	"T03": "Bronchopneumonia",
	"T04": "Asma",
	"T05": "Cacingan",
}

data_gejala = {
	"L01": "Bab cair lebih dari 3x sehari",
	"L02": "Lesu",
	"L03": "Nafsu makan berkurang",
	"L04": "Keram pada perut",
	"L05": "Perut kembung",
	"L06": "Demam",
	"L07": "Muntah",
	"L08": "Kejang 1-2x sehari",
	"L09": "Bab cair",
	"L10": "Sesak nafas",
	"L11": "Terlihat sangat mengantuk",
	"L12": "Batuk",
	"L13": "Pilek",
	"L14": "Menggigil",
	"L15": "Dada terasa sakit",
	"L16": "Sakit kepala",
	"L17": "Nafas berbunyi",
	"L18": "Faktor keturunan",
	"L19": "Susah tidur",
	"L20": "Anak tampak kurus",
	"L21": "Pucat",
	"L22": "Gatal sekitar anus",
	"L23": "Gelisah atau tidak nyaman saat tidur",
	"L24": "Iritasi kulit sekitar anus",
	"L25": "Sering sakit perut",
}
index_gejala = list(data_gejala.keys())

aturan = [
	["T01", ["L01", "L02", "L03", "L04", "L05", "L06", "L07"]        ],
	["T02", ["L06", "L07", "L08", "L09", "L10", "L11", "L12", "L13"] ],
	["T03", ["L03", "L06", "L10", "L12", "L14", "L15", "L16"]        ],
	["T04", ["L02", "L10", "L12", "L17", "L18", "L19"]               ],
	["T05", ["L20", "L21", "L22", "L23", "L24", "L25"]               ],
]

def forward_chaining(fakta):
	kandidat = []
	mungkin = False
	for hasil, kondisi in aturan:
		inferensi = [k in fakta for k in kondisi]
		if sum(inferensi) >= 4: # heuristik
			kandidat.append((hasil, kondisi))
			mungkin = True
		if all(inferensi):
			mungkin = False

	if len(kandidat) > 0:
		terbaik = max(kandidat, key=lambda val: len(val[1]))
		return data_penyakit[terbaik[0]] + (" (Kemungkinan)" if mungkin else "")

def analisa():
	fakta = [index_gejala[i] for i, var in enumerate(isi_centang) if var.get()]
	analisa = forward_chaining(fakta)

	if analisa == None:
		hasil.config(text=f"Hasil analisa tidak diketahui")
	else:
		hasil.config(text=f"Hasil analisa: {analisa}")

###############################################################################

from tkinter import *

font1 = ("Segoe UI", 14, "normal")
font2 = ("Segoe UI", 20, "normal")

isi_centang = []

window = Tk()
window.title("Aplikasi Deteksi Penyakit Anak")

Label(window, text="Sistem Pakar Deteksi Penyakit pada Anak Menggunakan Metode Forward Chaining", font=font1).pack(padx=20, pady=20)

frame = Frame(window)
for i, (k, v) in enumerate(data_gejala.items()):
	var = BooleanVar()
	isi_centang.append(var)
	tombol = Checkbutton(frame, text=v, variable=var, command=analisa, width=30, anchor="w")
	row = i % 10
	col = i // 10
	tombol.grid(row=row, column=col)
frame.pack(padx=20, pady=10)

hasil = Label(window, text="", font=font2, wraplength=700)
hasil.pack(pady=10)
analisa() # set kosong label hasil

Label(window, text="\nRizky Alhafiz (200504064), Ryan Alfiansyah (230504109), M. Fadli (240504066)").pack(anchor="w")

window.mainloop()