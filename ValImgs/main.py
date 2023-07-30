from importlib_resources import files

import ValImgs.imgs as imgs


def get_imgs(path: str):
    data = files(imgs)
    img = data / path
    return str(img)
