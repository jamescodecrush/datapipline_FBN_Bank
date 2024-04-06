FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt 
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt


COPY . .

CMD [ "python", "./data_instance.py" ]
