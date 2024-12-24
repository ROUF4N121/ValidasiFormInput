import re

def validate_form(nama_lengkap, nomor_telepon, email):
    errors = []

    # Validasi nama lengkap (hanya huruf)
    if not nama_lengkap.replace(" ", "").isalpha():
        errors.append("Nama lengkap hanya boleh berisi huruf.")

    # Validasi nomor telepon (hanya angka)
    if not nomor_telepon.isdigit():
        errors.append("Nomor telepon hanya boleh berisi angka.")

    # Validasi email (mengandung '@' dan '.')
    if "@" not in email or "." not in email:
        errors.append("Email harus mengandung karakter '@' dan '.'.")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Data pendaftaran valid.")

# Input data
nama_lengkap = input("Masukkan nama lengkap: ")
nomor_telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

# Validasi data
validate_form(nama_lengkap, nomor_telepon, email)
