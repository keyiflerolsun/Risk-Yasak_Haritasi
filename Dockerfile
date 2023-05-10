# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

# * Docker İmajı
FROM python:3.10.8-slim-buster

# * Dil ve Bölge
ENV LANGUAGE="C.UTF-8" LANG="C.UTF-8" LC_ALL="C.UTF-8" TZ="Europe/Istanbul"

# * Python Standart Değişkenler
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING="UTF-8"

# * Çalışma Alanı
WORKDIR /usr/src/riskharitasi
COPY ./ /usr/src/riskharitasi

# ? Sistem Kurulumları
# RUN apt-get update -y && \
#     apt-get install --no-install-recommends -y \
#     git

# ? Gereksiz Dosyaların Silinmesi
# RUN rm -rf /var/lib/apt/lists/*

# * Gerekli Paketlerin Yüklenmesi
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -U setuptools wheel && \
    python3 -m pip install --no-cache-dir -Ur requirements.txt

# * Python Çalıştırılması
CMD ["python3", "basla.py"]