FROM python:3.10
# estoy partiendo el ambiente para ver solo esta version

WORKDIR /app
#Carpeta dentro del espacio de nombre app
COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app
#con el copy . estoy copiando todos los archivos a la carpeta nueva app

CMD bash -c "while true; do sleep 1; done"
#comando que mantiene en ejecucion constante el contenedor