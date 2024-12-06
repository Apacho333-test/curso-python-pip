FROM python:3.10
# estoy partiendo el ambiente para ver solo esta version

WORKDIR /web-server
#Carpeta dentro del espacio de nombre app
COPY requirements.txt /web-server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web-server/requirements.txt

COPY . /web-server
#con el copy . estoy copiando todos los archivos a la carpeta nueva app

CMD {"uvicorn", "main:web-server","--host","0.0.0.0", "--port","80"}
#El comando lo lanza directamente a uvicorn para que quede en la web