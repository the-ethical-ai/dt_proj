FROM python:3.10.6-buster

WORKDIR /api/fast.py

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY darktriad darktriad
COPY setup.py  setup.py
RUN pip install .

EXPOSE 8000

CMD uvicorn darktriad.api.fast:app --host 0.0.0.0 --port $PORT
