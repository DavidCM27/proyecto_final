# sistema_login_memoria.py

import os

# Archivo donde se guardarán los usuarios
ARCHIVO_USUARIOS = "usuarios.txt"


def cargar_usuarios():
    usuarios = {}
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 2:
                    usuario, contraseña = partes
                    usuarios[usuario] = contraseña
    return usuarios


def guardar_usuario(usuario, contraseña):
    with open(ARCHIVO_USUARIOS, "a") as archivo:
        archivo.write(f"{usuario},{contraseña}\n")


def agregar_usuario(usuarios):
    print("\n--- Agregar nuevo usuario ---")
    nuevo_usuario = input("Nuevo nombre de usuario: ").strip()
    if nuevo_usuario in usuarios:
        print("El usuario ya existe.\n")
        return
    nueva_contraseña = input("Contraseña: ").strip()
    usuarios[nuevo_usuario] = nueva_contraseña
    guardar_usuario(nuevo_usuario, nueva_contraseña)
    print(f"Usuario '{nuevo_usuario}' guardado correctamente.\n")


def iniciar_sesion(usuarios):
    print("\n--- Inicio de sesión ---")
    usuario = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    if usuario in usuarios:
        if usuarios[usuario] == contraseña:
            print(f"\n Bienvenido, {usuario}!\n")
        else:
            print("Contraseña incorrecta.\n")
    else:
        print("El usuario no existe.\n")


def menu():
    usuarios = cargar_usuarios()
    while True:
        print("===== MENÚ =====")
        print("1. Iniciar sesión")
        print("2. Agregar usuario")
        print("3. Salir")
        opcion = input("Selecciona una opción (1/2/3): ").strip()

        if opcion == "1":
            iniciar_sesion(usuarios)
        elif opcion == "2":
            agregar_usuario(usuarios)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    menu()
