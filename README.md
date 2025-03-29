# Convertisseur d'Image en Art ASCII 🎨

Un script Python simple mais puissant qui transforme vos images en art ASCII.

## 📋 Description

Ce projet convertit n'importe quelle image en art ASCII, créant une représentation textuelle de l'image en utilisant différents caractères ASCII pour représenter les différentes nuances de gris.

## ✨ Fonctionnalités

- Conversion d'images en art ASCII
- Support de différents formats d'image (PNG, JPG, etc.)
- Possibilité d'ajuster l'échelle de l'image de sortie
- Sauvegarde automatique dans un fichier texte

## 🚀 Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/kenny516/img_to_char.git
```

2. Installez les dépendances requises :
```bash
pip install Pillow numpy
```

## 💻 Utilisation

```python
from main import image_to_ascii

image_to_ascii(
    image_path="chemin/vers/votre/image.png",
    output_file="art_ascii.txt",
    scale=0.15
)
```

### Paramètres

- `image_path` : Chemin vers l'image à convertir
- `output_file` : Nom du fichier de sortie (par défaut : "ascii_art.txt")
- `scale` : Facteur d'échelle pour redimensionner l'image (par défaut : 0.1)

## 📝 Exemple

```
@@@@###SSS%%%???***+++;;;:::,,,....
@@@@###SSS%%%???***+++;;;:::,,,....
@@@@###SSS%%%???***+++;;;:::,,,....
```

## 🛠️ Technologies utilisées

- Python 3.x
- Pillow (PIL)
- NumPy

## 📄 Licence

Ce projet est sous licence MIT.
