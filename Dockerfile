FROM python:3

RUN git clone https://github.com/ralvarezum/2019-parcial-tateti
WORKDIR /2019-parcial-tateti

RUN pip install -r requirements.txt

CMD [ "python3", "test_tateti.py" ]