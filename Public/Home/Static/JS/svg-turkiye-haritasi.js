/*! SVG Türkiye Haritası | MIT Lisans | dnomak.com */

function svgturkiyeharitasi() {
    const element = document.querySelector("#svg-turkiye-haritasi");
    const info    = document.querySelector(".il-isimleri");

    element.addEventListener(
        "mouseover",
        function (event) {
            const risk = window.gelen_veri[event.target.parentNode.id];
            if (event.target.tagName === "path" && event.target.parentNode.id !== "guney-kibris") {
                $(info).css("background", `${window.risk_renk[risk]} !important`);
                info.innerHTML = `
                    <div style="background: ${window.risk_renk[risk]};">
                        <span class="secilen-il">${event.target.parentNode.getAttribute('data-iladi')}</span>
                        <hr>
                        <span class="secilen-il">${risk} Risk Grubu</span>
                    </div>
                `;
            }
        }
    );

    element.addEventListener(
        "mousemove",
        function (event) {
            info.style.top = event.pageY + 25 + "px";
            info.style.left = event.pageX + "px";
        }
    );

    element.addEventListener(
        "mouseout",
        function (event) {
            info.innerHTML = "";
        }
    );

    element.addEventListener(
        "click",
        function (event) {
            const il          = event.target.parentNode.getAttribute("data-iladi");
            const risk        = window.gelen_veri[event.target.parentNode.id];
            const risk_verisi = window.risk_detay[risk];

            if (risk) {
                $("#baslik").html(`<p style="color: #a7a1ae; text-align:center;">${il} | ${risk} Risk</p>`)
            } else {
                $("#baslik").html("<p id='baslik' class='text-center' style='font-weight:bold; letter-spacing:0.2em'>Lütfen Yaşadığınız Şehri Seçiniz..</p>")
            }

            $(".sonuc").html(risk_verisi || "<hr>");

            window.scroll({
                top: $(".sonuc").offset().top - 40,
                behavior: "smooth"
            });
        }
    );
}