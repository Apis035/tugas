# Rizky Alhafiz
# Implementasi RSA, 02 Oktober 2026

# --------------------------------------------------------

import random, math

# p, q: bilangan prima
# return: kunci publik, kunci privat
def generate_kunci(p, q):
	n  = p * q
	φn = (p-1)*(q-1)
	e  = 0
	while True:
		e = random.randint(1, φn)
		if math.gcd(e, φn) == 1: break
	d = pow(e, -1, φn)
	return (n, e), (n, d)


def enkripsi(pesan, kpub):
	enkrip = []
	for p in pesan:
		proses = ord(p)
		proses = pow(proses, kpub[1], kpub[0])
		enkrip.append(proses)
	return enkrip


def dekripsi(pesan, kpriv):
	dekrip = ""
	for p in pesan:
		proses = pow(p, kpriv[1], kpriv[0])
		proses = chr(proses)
		dekrip += proses
	return dekrip

# --------------------------------------------------------

def tes_enkripsi_dekripsi(pesan, p, q, judul):
	kpub, kpriv = generate_kunci(p, q)
	cipher      = enkripsi(pesan,  kpub)
	decipher    = dekripsi(cipher, kpriv)
	print()
	print("  ", judul)
	print("---------------------------------------------------")
	print("   Prima p, q:   ", p, q)
	print("   Kunci publik: ", kpub)
	print("   Kunci private:", kpriv)
	print("   Pesan:        ", pesan)
	print("   Terenkripsi   ", cipher)
	print("   Didekripsi:   ", decipher)
	print()

# --------------------------------------------------------

pesan = "Ayam Bakar"

print()
print("   Pesan:", pesan)
tes_enkripsi_dekripsi(pesan, 43, 11, "Tes dengan p = 43, q = 11")
tes_enkripsi_dekripsi(pesan, 13, 31, "Tes dengan p = 13, q = 31")
tes_enkripsi_dekripsi(pesan, 20, 12, "Tes gagal karena p dan q bukan bilangan prima")