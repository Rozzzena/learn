from PIL import Image
import os

arq_lista = os.listdir("material de teste")


for arquivo in arq_lista:
    # abrir
    imagem = Image.open(f"material de teste/{arquivo}")

    # salvar
    imagem.save(f"material de teste/{arquivo.replace('jpg', 'tiff')}")

# com base em https://youtu.be/YGzD2kEfZNc