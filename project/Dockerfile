FROM python:3.10

WORKDIR /web
COPY requirements.txt /web/requirements.txt

RUN  pip  install --no-cache-dir --upgrade -r /web/requirements.txt

COPY . /web

CMD bash -c "while true; do spleep 1; done"