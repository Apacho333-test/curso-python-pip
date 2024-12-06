import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app =FastAPI()

@app.get("/") # un decorador, la ruta donde se ingresa a la web
def get_list():
    return[1,2,3,]

@app.get("/contact", response_class= HTMLResponse)
def get_list():
    #return{"name": "Platzi"} para cargar solo un texto el html (crear un servidor web con python) es para cargar una pagina completa y editarla
    return """<h1> Hola soy una pagina </h1>
<p> soy un parrafo </p>"""


def run():
    store.get_categories()

if __name__ ==   "__main__":
    run()

    