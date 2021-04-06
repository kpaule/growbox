FROM python:3.8.5

WORKDIR /flask-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./growbox ./growbox

CMD ["python", "-m", "growbox"]