import sqlite3, qrcode, os

# Crear carpeta para guardar los QR
os.makedirs("qrs", exist_ok=True)

with sqlite3.connect("base_datos.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT dni, nombres, apellidos FROM alumnos")
    alumnos = cursor.fetchall()

for dni, nombres, apellidos in alumnos:
    img = qrcode.make(dni)  # 🔹 solo el DNI en el QR
    nombre_archivo = f"qrs/{dni}.png"
    img.save(nombre_archivo)
    print(f"✅ QR generado para {nombres} {apellidos} ({dni})")
