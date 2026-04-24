#
# UTS Sistem Pakar
# Data diambil dari jurnal "Sistem Pakar Deteksi Penyakit pada Anak Menggunakan Metode Forward Chaining"
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
	"L01": "bab cair lebih dari 3x sehari",
	"L02": "lesu",
	"L03": "nafsu makan berkurang",
	"L04": "keram pada perut",
	"L05": "perut kembung",
	"L06": "demam",
	"L07": "muntah",
	"L08": "kejang 1-2x sehari",
	"L09": "bab cair",
	"L10": "sesak nafas",
	"L11": "terlihat sangat mengantuk",
	"L12": "batuk",
	"L13": "pilek",
	"L14": "menggigil",
	"L15": "dada terasa sakit",
	"L16": "sakit kepala",
	"L17": "nafas berbunyi",
	"L18": "faktor keturunan",
	"L19": "susah tidur",
	"L20": "anak tampak kurus",
	"L21": "pucat",
	"L22": "gatal sekitar anus",
	"L23": "gelisah atau tidak nyaman saat tidur",
	"L24": "iritasi kulit sekitar anus",
	"L25": "sering sakit perut",
}
kode_gejala = {v: k for k, v in data_gejala.items()}

aturan = [
	["T01", ["L01", "L02", "L03", "L04", "L05", "L06", "L07"]        ],
	["T02", ["L06", "L07", "L08", "L09", "L10", "L11", "L12", "L13"] ],
	["T03", ["L03", "L06", "L10", "L12", "L14", "L15", "L16", ]      ],
	["T04", ["L02", "L10", "L12", "L17", "L18", "L19"]               ],
	["T05", ["L20", "L21", "L22", "L23", "L24", "L25"]               ],
]

def forward_chaining(fakta, aturan):
	for hasil, kondisi in aturan:
		memenuhi_kondisi_aturan = all(k in fakta for k in kondisi)
		if memenuhi_kondisi_aturan:
			return data_penyakit[hasil]

def daftar_gejala_ke_kode(kasus):
	hasil = []
	for k in kasus:
		hasil.append(kode_gejala[k])
	return hasil

###############################################################################

print()
print("--- Sistem Pakar Deteksi Penyakit pada Anak Menggunakan Metode Forward Chaining ---")
print()
print("Tugas UTS Sistem Pakar:")
print("    Rizky Alhafiz   (200504064)")
print("    Ryan Alfiansyah (230504109)")
print("    M. Fadli        (240504066)")
print()

def print_daftar(daftar):
	for k, v in daftar:
		print("   ", k, ":", v)

print("Data penyakit:")
print_daftar(data_penyakit.items())
print()

print("Data gejala:")
print_daftar(data_gejala.items())
print()

print("Aturan:")
print_daftar(aturan)
print()

daftar_kasus = [
	[
		"demam",
		"kejang 1-2x sehari",
		"bab cair","muntah",
		"sesak nafas",
		"terlihat sangat mengantuk",
		"batuk",
		"pilek"
	],
	[
		"lesu",
		"sesak nafas",
		"batuk",
		"pilek",
		"nafas berbunyi",
		"faktor keturunan",
		"susah tidur"
	],
	[
		"anak tampak kurus",
		"pucat",
		"gatal sekitar anus",
		"gelisah atau tidak nyaman saat tidur",
		"iritasi kulit sekitar anus",
		"sering sakit perut"
	],
]

print("Contoh input-output:")
for kasus in daftar_kasus:
	fakta = daftar_gejala_ke_kode(kasus)
	hasil = forward_chaining(fakta, aturan)
	print("    Kasus:", kasus)
	print("    Hasil:", hasil)
	print()