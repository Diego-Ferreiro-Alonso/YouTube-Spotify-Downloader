# Espacio para librerias
from pytubefix import YouTube
import os

# Programa principal
def main():
    while True:
        print("----------------------------------------------")
        print("\033[31mBienvenido al descargador de videos de YouTube\033[0m")
        print("----------------------------------------------")

        print("\n\033[31mVersión 0.0.0\033[0m")

        print("\nMenú:")
        print("1. Descargar video de YouTube en formato MP4")
        print("2. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            youtube_mp4()
            break
        elif opcion == "2":
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def youtube_mp4():
    url = input("\nIngresa la URL del video de YouTube: ")
    downloads_folder = os.path.expanduser("~/Descargas")
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4").get_highest_resolution()
    stream.download(output_path=downloads_folder)
    print(f"\nVideo descargado exitosamente en: {downloads_folder}")

if __name__ == "__main__":
    main()