from requests import get
from parsel import Selector
from re import compile, sub

def risk_durumlari():
    url = 'https://covid19.saglik.gov.tr/'
    istek = get(url)
    secici = Selector(istek.text)

    html_temizle = lambda veri: sub(compile('<.*?>'), '', veri)
    tr2eng  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")

    il_adi     = secici.xpath("//div[@class='svg-turkiye-haritasi']//@data-iladi").getall()
    temiz_il   = [il.replace('İ', 'i').lower().translate(tr2eng) for il in il_adi]
    risk_durum = secici.xpath("//div[@class='svg-turkiye-haritasi']//@data-durum").getall()
    temiz_risk = [html_temizle(risk).strip() for risk in risk_durum]

    return dict(zip(temiz_il, temiz_risk))

# from json import dumps
# print(dumps(risk_durumlari(), indent=2, ensure_ascii=False, sort_keys=False))