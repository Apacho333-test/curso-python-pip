# El enviroment (env) es el espacio especifico en donde funcionan versiones especificas de aplicaciones, ej: en este env necesito matplotlib 3.5.0 pero en otro necesito la vrsion 3.6.0

# Sin embargo, si una persona nueva mira el ambiente, tendria que descargar todas las versiones en ese env. para facilitar la descarga,se guardan todas las versiones de forma automatica en un .txt que es el requirements.txt que es una copia de la funcion freeze en texto. a esto se le llama  descargar las dependencias
# Si esa persona nueva quiere el proyecto loideal es que la clone

```sh
git clone
cd app
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

