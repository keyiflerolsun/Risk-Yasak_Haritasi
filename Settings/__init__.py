# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from yaml import load, FullLoader

with open("AYAR.yml", "r", encoding="utf-8") as yaml_dosyasi:
    AYAR = load(yaml_dosyasi, Loader=FullLoader)