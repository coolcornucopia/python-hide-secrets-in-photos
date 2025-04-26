# python-hide-secrets-in-photos
The goal of this github repo is to offer Python :snake: scripts for hiding secrets in photos.
:construction:
| Methods | Examples |
| :---: | :---: |
| Hiding secrets with XOR operator | ![](res/xor180_secret_msg.png) |
| Hiding secrets in photo metadata | ![](res/metadata_secret_msg.png) <br>The metadata secret message is: <br>"**Hi, this is my secret msg, have fun :-)**" |


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
# Update the 2 following commands according to your needs
export MYPHOTO=res/metadata_secret_msg.png
export EXIFTOOL=~/Downloads/exiftool/Image-ExifTool-13.27/exiftool

# Get all metadata information
${EXIFTOOL} ${MYPHOTO}
${EXIFTOOL} -v ${MYPHOTO} # verbose mode

# Remove all metadata
${EXIFTOOL} -all= ${MYPHOTO}

# Add an artist field
${EXIFTOOL} -Artist="Hi, this is my secret msg, have fun :-)" ${MYPHOTO}

# Check metadata updates
${EXIFTOOL} ${MYPHOTO}
```


## Extra tips
### Adding a photo on top of your photo with secret
:construction:
I use Inkscape for combining photos and illustrations.
When exporting, you may need to enable "CAIRO_ANTIALIAS_NONE".


## Used resources & Credits
* [res/gary-bendig-6GMq7AGxNbE-unsplash.jpg](res/gary-bendig-6GMq7AGxNbE-unsplash.jpg): Photo by [Gary Bendig](https://unsplash.com/@kris_ricepees?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/raccoon-walking-on-lawn-grass-6GMq7AGxNbE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
* [res/jairo-alzate-sssxyuZape8-unsplash.jpg](res/jairo-alzate-sssxyuZape8-unsplash.jpg): Photo by [Jairo Alzate](https://unsplash.com/@jairoalzate?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/short-coated-brown-puppy-on-white-floor-sssxyuZape8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)


## TODO list
:construction:


## Any questions or comments are welcome :bird:
If you have any comments or questions, feel free to send me an email at coolcornucopia@outlook.com :email:.

--

Peace

coolcornucopia :smile:
