from PIL import Image
import numpy as np


def image_to_ascii(image_path, output_file="ascii_art.txt", scale=0.1):
    img = Image.open(image_path).convert('L')

    width, height = img.size
    new_width = int(width * scale)
    new_height = int(height * scale * 0.5)  
    img = img.resize((new_width, new_height))

    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

    pixels = np.array(img.getdata()).reshape((new_height, new_width))
    ascii_str = ''

    for row in pixels:
        for pixel in row:
            index = int(pixel / 255 * (len(ascii_chars) - 1))
            ascii_str += ascii_chars[index]
        ascii_str += '\n'

    with open(output_file, 'w') as f:
        f.write(ascii_str)

    print(f"ASCII art sauvegardé dans {output_file}")


# Utilisation
image_to_ascii(
    image_path="goku.png",
    output_file="art_ascii.txt",
    scale=0.15
)
