from flask import flash, Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)
from elsa import cli

links = [
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/1.%20OBJETO%20Y%20AMBITO%20DE%20APLICACION/",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/2.%20TERMINOS%20Y%20DEFINICIONES/",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/3.%20ESQUEMAS%20DE%20INSTALACION%20PARA%20LA%20RECARGA%20DE%20VEHICULOS%20ELECTRICOS/",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/4.%20PREVISION%20DE%20CARGAS%20SEGUN%20EL%20ESQUEMA%20DE%20LA%20INSTALACION/      ",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/4.%20PREVISION%20DE%20CARGAS%20SEGUN%20EL%20ESQUEMA%20DE%20LA%20INSTALACION/  ",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/6.%20PROTECCION%20PARA%20GARANTIZAR%20LA%20SEGURIDAD/",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/7.%20CONDICIONES%20PARTICULARES%20DE%20INSTALACION/",
]
cardsxl = [
        # "especifico":"active",
        {
            "n": "cardsxl_0",
            "especifico": "active",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "holla caracola",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": links[1],
            "link2": "#",
        },
        {
            "n": "cardsxl_1",
            "especifico": "active",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "holla caracola",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": links[2],
            "link2": "#",
        },
        {
            "n": "cardsxl_2",
            "especifico": "active",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "holla caracola",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": links[3],
            "link2": "#",
        },
        {
            "n": "cardsxl_3",
            "especifico": "active",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "holla caracola",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": links[4],
            "link2": "#",
        },
]
marketing = [
        # "especifico":"order-md-2",
        # https://fontawesome.com/v5.15/icons?d=gallery&p=2
        {
            "n": 0,
            "especifico": "order-md-2",
            "headline": "ESTUDIO GRATUITO",
            "headline2": "Contacto",
            "content": "Ayudamos a nuestros clientes a MINIMIZANDO su inversion.",
            "content2": "",
            "ico": "fa-pencil-ruler",
            "img2": "",
            "link": "#",
            "link2": "#",
        },
        {
            "n": 0,
            "especifico": "",
            "headline": "SUBVENCION",
            "headline2": "",
            "content": "Gestionamos su subvencion de hasta el 40 % con el plan MOVES III",
            "content2": "",
            "ico": "fa-euro-sign",
            "img2": "",
            "link": "#",
            "link2": "#",
        },
        {
            "n": 0,
            "especifico": "order-md-2",
            "headline": "PROYECTO",
            "headline2": "",
            "content": "Elaboramos y supervisamos los proyectos de nuestros clientes",
            "content2": "",
            "ico": "fa-project-diagram",
            "img2": "",
            "link": "#",
            "link2": "#",
        },
        {
            "n": 0,
            "especifico": "order-md-2",
            "headline": "INSTALACION",
            "headline2": "Contacto",
            "content": "Ejecutamos proyectos llave en mano.",
            "content2": "",
            "ico": "fa-tools",
            "img2": "",
            "link": "#",
            "link2": "#",
        },
        {
            "n": 0,
            "especifico": "order-md-2",
            "headline": "CERTIFICACION",
            "headline2": "Contacto",
            "content": "Legalizamos su instalacion",
            "content2": "",
            "ico": "fa-certificate",
            "img2": "",
            "link": "#",
            "link2": "#",
        },
        {
            "n": 0,
            "especifico": "order-md-2",
            "headline": "GARANTIA",
            "headline2": "Contacto",
            "content": "Servicio garantia y mantenimiento",
            "content2": "",
            "ico": "fa-handshake",
            "img2": "",
            "link": "#",
            "link2": "#",
        },
]
featurette = [
        # "especifico":"order-md-2",
        {
            "n": "featurette_0",
            "especifico": "order-md-2",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "",
            "content2": "",
            "img": "multi-storey-car-park-1271919_640.jpg",
            "img2": "",
            "link": links[1],
            "link2": "#",
        },
        {
            "n": "featurette_0",
            "especifico": "order-md-2",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "",
            "content2": "",
            "img": "multi-storey-car-park-1271919_640.jpg",
            "img2": "",
            "link": "https://kcjysmt9s7.execute-api.eu-west-1.amazonaws.com/dev/recarga",
            "link2": "#",
        },
        {
            "n": "featurette_1",
            "especifico": "order-md-2",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "",
            "content2": "",
            "img": "multi-storey-car-park-1271919_640.jpg",
            "img2": "",
            "link": "https://kcjysmt9s7.execute-api.eu-west-1.amazonaws.com/dev/recarga",
            "link2": "#",
        },
        {
            "n": "featurette_2",
            "especifico": "order-md-2",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "",
            "content2": "",
            "img": "multi-storey-car-park-1271919_640.jpg",
            "img2": "",
            "link": "https://kcjysmt9s7.execute-api.eu-west-1.amazonaws.com/dev/recarga",
            "link2": "#",
        },
        {
            "n": "featurette_3",
            "especifico": "order-md-2",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "",
            "content2": "",
            "img": "multi-storey-car-park-1271919_640.jpg",
            "img2": "",
            "link": "https://kcjysmt9s7.execute-api.eu-west-1.amazonaws.com/dev/recarga",
            "link2": "#",
        },
]
cards = [
        # "especifico":"active",
        {
            "n": "cards_0",
            "especifico": "active",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "holla caracola",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": "",
            "link2": "#",
        },
        {
            "n": "cards_1",
            "especifico": "active",
            "headline": "Contacto",
            "headline2": "Contacto",
            "content": "holla caracola",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": links[2],
            "link2": "#",
        },

]
menu = [
        # "especifico":"active",
        {
            "datos": "featurette",
            "plantilla":"Cards.html",
            "n": "navbar_2",
            "especifico": "",
            "headline": "MOVES III",
            "headline2": "Ayudas del 70 % para autónomos, particulares Comunidades de propietarios y administración sinactividad económica",
            "content": "Cards.html",
            "content2": "",
            "img": "2021-05-30_19-38.png",
            "img2": "",
            "link": "https://kcjysmt9s7.execute-api.eu-west-1.amazonaws.com/dev/recarga",
            "link2": "#",
        },

        {
            "datos": "cards",
            "plantilla":"Cards.html",
            "n": "navbar_1",
            "especifico": "",
            "headline": "COLECTIVO",
            "headline2": "Instalamos su Punto de Recarga en comunidades, hoteles, y  otros aparcamientos colectivos",
            "content": "CardsXL.html",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": "https://ivehiculoelectrico.com/blog/ITC-BT%2052/5.REQUISITOS%20GENERALES%20DE%20LA%20INSTALACION/",
            "link2": "#",
        },
        {
            "datos": "cardsxl",
            "plantilla":"Cards.html",
            "n": "navbar_3",
            "especifico": "",
            "headline": "SERVICIOS",
            "headline2": "Quieres asociarte a IVE ?",
            "content": "featurette.html",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": "https://ivehiculoelectrico.com/blog/ITC-BT%2052/5.REQUISITOS%20GENERALES%20DE%20LA%20INSTALACION/",
            "link2": "#",
        },
        {
            "datos": "cards",
            "plantilla":"Cards.html",
            "n": "navbar_4",
            "especifico": "",
            "headline": "BLOG",
            "headline2": "Contacto",
            "content": "Cards.html",
            "content2": "",
            "img": "electric-car-4381728_640.jpg",
            "img2": "",
            "link": "https://kcjysmt9s7.execute-api.eu-west-1.amazonaws.com/dev/recarga",
            "link2": "#",
        },
        {
            "datos": "cards",
            "plantilla":"Cards.html",
            "n": "navbar_5",
            "especifico": "active",
            "headline": "",
            "headline2": "INFRAESTRUCTURA RECARGA VEHICULO ELECTRICO",
            "content": "Cards.html",
            "content2": "",
            "img": "2021-05-30_19-38.png",
            "img2": "",
            "link": "https://kcjysmt9s7.execute-api.eu-west-1.amazonaws.com/dev/recarga",
            "link2": "#",
        },

]
# para anadirle el orden que se necesita en el carousel
o = -1
for i in menu:
    o = o + 1
    i["o"] = str(o)
# ===============================================================

pag = {
        "title": "INFRAESTRUCTURA RECARGA VEHICULO ELECTRICO",
        "logo": "",
}


@app.route("/", methods=["GET", "POST"])
def recarga():



    return render_template(
        "index.html",

        pag=pag,
        cards=cards,
        cardsxl=cardsxl,
        marketing=marketing,
        featurette=featurette,
        menu=menu,
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        cli(app, base_url="https://asolear.com")
    else:
        app.run(debug=True, host="0.0.0.0", port=5500)
