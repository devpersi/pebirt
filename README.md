# Persi's Easy Bulk Image Resize Tool
PEBIRT is a free and open source lightweight python console app designed to simplify bulk image cropping and resizing. It is a ridiculously tiny script thanks to using [Pillow](https://github.com/python-pillow/Pillow/)'s image processing, inspired by [rembg](https://github.com/danielgatis/rembg/tree/main?tab=readme-ov-file#usage-as-a-library)'s bulk background removal ease of use. Combine them to speed up uniform image uploads.

## Overview
In the spirit of automating the boring things with python, this tool automates cropping images to a square 1:1 ratio and resizing them by default to 800x800, my preferred image size for e-shop product images. It is ideal for e-commerce data entry *enthusiasts* with beginner python experience.

## Features
- Bulk processing: Resize and crop multiple images at once without manual intervention
- Customizable output size: Default is 800x800, but you can modify dimensions as needed
- Lightweight and fast: A minimalistic Python script with no unnecessary complexity
- PNG file support: Works by default with .png files, but can be extended to other formats
- Simple setup: Just drop images in the folder and run the script - no complex configurations needed

## Requirements
- [Python](https://www.python.org/downloads/)
- [Pillow](https://github.com/python-pillow/Pillow/)

## Getting started with PEBIRT
1. Clone or download the repository to your local machine
2. Place your images in the project folder
3. Open a terminal and cd into the project folder
4. Make sure [Python](https://www.python.org/downloads/) is installed by running
    ```bash
        python -V
    ```
5. Install requirements by running
    ```bash
        pip install -r requirements.txt 
    ``` 
6. Run
    ```bash
        python resize.py
    ```
>Default behaviour only works with .png files. You can choose the filetype by adjusting path.glob pattern in resize.py

## Configuration
### Cropping
Default cropping behaviour:
- Detect whether the image is wider or taller
- Center the crop to 1:1 square ratio
- Resolution agnostic
>You can choose a different ratio by adjusting the crop function - don't forget to change the pixel width and height in the resize function to match your new ratio

### Resizing
Default resizing behaviour:
- Resize image to 800x800 using the Lanczos algorithm
>You can choose a different size by adjusting the pixel width and height in the resize function

## Contributing
Contributions are welcome! If you have ideas to improve the process or find any issues feel free to submit a pull request or open an issue describing the problem.

Happy resizing!
