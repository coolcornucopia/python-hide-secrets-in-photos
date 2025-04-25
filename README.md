# python-hide-secrets-in-photos
The goal of this github repo is to offer Python :snake: scripts for hiding secrets in photos.

> [!note]
> Python scripts here are simple and short, without too many dependencies and without "main", arg parsing...
> The goal is to simplify copy/paste of these scripts into online Python compiler or to your own scripts...


---

**Table of contents**

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->



## Installation
Create a virtual env and install dependencies with your favorite tools. Below an simple example based on ```pip```

```bash
# Create the virtual env and activate it
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
# or use simple commands like "pip install opencv-python"

# Leave the virtual env when necessary with the command "deactivate"
```


## Hiding secrets with XOR operator
:construction:
From https://puzzling.stackexchange.com/questions/28494/this-is-important-i-need-you-to-listen
https://i.sstatic.net/B7g38.png
"XOR the image with itself rotated 180°"

```bash
python decode.py enigma_encoded.png enigma_decoded.png
```


## Hiding secrets in photo metadata
:construction:

https://exiftool.org/ 
Install: simple unzip on Linux

Few examples:
```bash
# Get all metadata information
exiftool enigma_full.png
exiftool -v enigma_full.png # verbose mode

# Remove all metadata
exiftool -all= enigma_full.png

# Add an artist field
exiftool -Artist="Coucou, bonne idee de chercher ici, mais il n'y a pas la reponse ;-) Philippe" enigma_full.png
```


## Extra tips
### Adding a photo on top of your photo with secret
:construction:
I use Inkscape for combining photos and illustrations.
When exporting, you may need to enable "CAIRO_ANTIALIAS_NONE".


## TODO list
:construction:


## Any questions or comments are welcome :bird:
If you have any comments or questions, feel free to send me an email at coolcornucopia@outlook.com :email:.

--

Peace

coolcornucopia :smile:
