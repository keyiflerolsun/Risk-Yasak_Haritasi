# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from re     import compile, sub
from random import choice

async def risk_veri():
    # url      = "https://covid19.saglik.gov.tr/"
    # istek    = get(url)
    # secici   = Selector(istek.text)
    # _iller   = secici.xpath("//div[@class='svg-turkiye-haritasi']//@data-iladi").getall()
    # _riskler = secici.xpath("//div[@class='svg-turkiye-haritasi']//@data-durum").getall()
    _iller   = ["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]
    _riskler = [choice(["Düşük", "Orta", "Yüksek", "Çok Yüksek"]) for _ in range(81)]

    html_temizle = lambda veri: sub(compile(r"<.*?>"), "", veri)
    tr2eng       = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")

    iller   = [il.replace("İ", "i").lower().translate(tr2eng) for il in _iller]
    riskler = [html_temizle(risk).strip() for risk in _riskler]

    return dict(zip(iller, riskler))