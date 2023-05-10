# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI     import cikis_yap, hata_yakala
from Core    import Motor
from asyncio import run

if __name__ == "__main__":
    try:
        run(Motor.basla())
        cikis_yap(False)
    except Exception as hata:
        hata_yakala(hata)