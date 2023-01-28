from importlib_resources import files
from . import imgs


def get_imgs(path: str):
    data = files(imgs)
    img = data / path
    return str(img)
