$(function () {
    $.ajax({
        url: "/veri",
        type: "POST",
        dataType: "JSON",
        data: { "nak_nak": "@KekikAkademi" },
        beforeSend: function () {
            document.getElementById("yukleniyo").classList.add("spin");
            $("#yukleniyo").html('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" style="fill:#fff;transform:;-ms-filter:"><path d="M12,22c5.421,0,10-4.579,10-10h-2c0,4.337-3.663,8-8,8s-8-3.663-8-8c0-4.336,3.663-8,8-8V2C6.579,2,2,6.58,2,12 C2,17.421,6.579,22,12,22z"></path></svg>');
        },
        success: function (data) {
            window.gelen_veri = data;
            svgturkiyeharitasi();
            $.each(window.gelen_veri, function (key, value) {
                $('#' + key + ' path').css({ "fill": risk_renk[value] });
                $('#' + key + ' path').hover(function () {
                    $(this).css("fill", "#a7a1ae");
                }, function () {
                    $(this).css("fill", risk_renk[value]);
                });
            });
            $('.svg-turkiye-haritasi').show();
            $('#yukleniyo').remove();
        },
        error: function (error) {
            return false;
        }
    });
});

var risk_renk = {
    'Çok Yüksek': '#df1a23',
    'Yüksek': '#f8931f',
    'Orta': '#f0e513',
    'Düşük': '#0071c1'
}

var dusuk_risk = `<hr>
<div class="table-responsive w-100 justify-content-center text-center" id="table2">
    <table class="table">
        <tbody>
            <tr>
                <th scope="row" class="table-dark">Sokağa Çıkmak</th>
                <th class="bg-success">Her gün, 05.00'ten 21.00'e kadar serbest</th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">65+ ve 20- yaş grubu</th>
                <th class="bg-success">Serbest, Toplu Taşıma Serbest</th>
            </tr>
            <tr>
                <th scope="row"></th>
                <th></th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">Okul öncesi</th>
                <th class="bg-success">Açık</th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">İlkokul</th>
                <th class="bg-success">Açık</th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">Ortaokul</th>
                <th class="bg-success">Açık</th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">Lise</th>
                <th class="bg-success">Açık</th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">8. ve 12. sınıflar</th>
                <th class="bg-success">Açık</th>
            </tr>
            <tr>
                <th scope="row"></th>
                <th></th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">Restoran/ Cafe/ Çay Bahçesi</th>
                <th class="bg-warning">07.00-19.00 arası %50 kapasite ile serbest</th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">Halı Saha/ Yüzme Havuzu</th>
                <th class="bg-warning">09.00-19.00 arası serbest</th>
            </tr>
            <tr>
                <th scope="row"></th>
                <th></th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">Nikah</th>
                <th class="bg-warning">100 kişi ve 1 saati aşmamak şartıyla serbest</th>
            </tr>
            <tr>
                <th scope="row"></th>
                <th></th>
            </tr>
            <tr>
                <th scope="row" class="table-dark">Genel Kurullar</th>
                <th class="bg-warning">300 kişiye kadar serbest</th>
            </tr>
        </tbody>
    </table>
</div>
<hr>`;

var orta_risk = `<hr>
    <div class="table-responsive w-100 justify-content-center text-center" id="table2">
        <table class="table">
            <tbody>
                <tr>
                    <th scope="row" class="table-dark">Sokağa Çıkmak</th>
                    <th class="bg-success">Her gün, 05.00'ten 21.00'e kadar serbest</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">65+ ve 20- yaş grubu</th>
                    <th class="bg-success">Serbest, Toplu Taşıma Serbest</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Okul öncesi</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">İlkokul</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Ortaokul</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Lise</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">8. ve 12. sınıflar</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Restoran/ Cafe/ Çay Bahçesi</th>
                    <th class="bg-warning">07.00-19.00 arası %50 kapasite ile serbest</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Halı Saha/ Yüzme Havuzu</th>
                    <th class="bg-warning">09.00-19.00 arası serbest</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Nikah</th>
                    <th class="bg-warning">100 kişi ve 1 saati aşmamak şartıyla serbest</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Genel Kurullar</th>
                    <th class="bg-warning">300 kişiye kadar serbest</th>
                </tr>
            </tbody>
        </table>
    </div>
<hr>`;

var yuksek_risk = `<hr>
    <div class="table-responsive w-100 justify-content-center text-center" id="table3">
        <table class="table">
            <tbody>
                <tr>
                    <th scope="row" class="table-dark">Sokağa Çıkmak</th>
                    <th class="bg-warning">Pazar günü hariç, 05.00'ten 21.00'e kadar serbest</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">65+ ve 20- yaş grubu</th>
                    <th class="bg-warning">Gevşetilecek, Toplu Taşıma Serbest</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Okul öncesi</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">İlkokul</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Ortaokul</th>
                    <th class="bg-danger">Kapalı</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Lise</th>
                    <th class="bg-warning">Yüz yüze sınav</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">8. ve 12. sınıflar</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Restoran/ Cafe/ Çay Bahçesi</th>
                    <th class="bg-warning">07.00-19.00 arası %50 kapasite ile serbest</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Halı Saha/ Yüzme Havuzu</th>
                    <th class="bg-danger">Yasak</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Nikah</th>
                    <th class="bg-warning">50 kişi ve 1 saati aşmamak şartıyla serbest</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Genel Kurullar</th>
                    <th class="bg-warning">300 kişiye kadar serbest</th>
                </tr>
            </tbody>
        </table>
    </div>
<hr>`;

var cok_yuksek_risk = `<hr>
    <div class="table-responsive w-100 justify-content-center text-center" id="table4">
        <table class="table">
            <tbody>
                <tr>
                    <th scope="row" class="table-dark">Sokağa Çıkmak</th>
                    <th class="bg-warning">Pazar günü hariç, 05.00'ten 21.00'e kadar serbest</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">65+ ve 20- yaş grubu</th>
                    <th class="bg-warning">Gevşetilecek, Toplu Taşıma Yasak</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Okul öncesi</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">İlkokul</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Ortaokul</th>
                    <th class="bg-danger">Kapalı</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Lise</th>
                    <th class="bg-warning">Yüz yüze sınav</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">8. ve 12. sınıflar</th>
                    <th class="bg-success">Açık</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Restoran/ Cafe/ Çay Bahçesi</th>
                    <th class="bg-danger">Yasak</th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Halı Saha/ Yüzme Havuzu</th>
                    <th class="bg-danger">Yasak</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Nikah</th>
                    <th class="bg-warning">50 kişi ve 1 saati aşmamak şartıyla serbest</th>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <th></th>
                </tr>
                <tr>
                    <th scope="row" class="table-dark">Genel Kurullar</th>
                    <th class="bg-danger">Yasak</th>
                </tr>
            </tbody>
        </table>
    </div>
<hr>`;

var risk_detay = {
    "Düşük": dusuk_risk,
    "Orta": orta_risk,
    "Yüksek": yuksek_risk,
    "Çok Yüksek": cok_yuksek_risk
}
