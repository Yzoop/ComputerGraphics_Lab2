import os

from PIL import Image
__IMG_EXTENSIONS = ("jpg", "gif", "tif", "bmp", "png", "pcx")
COLOR_DEPTH = {'RGBA': 32, 'CMYK': 32, 'L': 8, 'P': 8, 'I': 32, 'F': 32, 'RGB': 24, '1': 1, 'YCbCr': 24}

def imgs_stat(imgs_names, base_path, check_if_img=True):
    if check_if_img:
        is_img = lambda path: path.lower().endswith(__IMG_EXTENSIONS)
    else:
        is_img = lambda path: True
    for name in imgs_names:
        if is_img(name):
            img = Image.open(os.path.join(base_path, name))
            img.load()
            stat = {"NAME": name,
                    "SIZE": img.size,
                    "DPI": img.info.get("dpi", "-"),
                    "COMPRESSION": img.info.get("compression", "-"),
                    "COLOR_DEPTH": COLOR_DEPTH.get(img.mode, "-")}
            yield stat