FROM python:3-alpine

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt && \
    echo "INSTALLING OS PACKAGES" && \
    apk add --update wget curl zip unzip jq && \
    apk add git perl \
    && cd /tmp/ \
    && git clone https://github.com/jasonm23/cowsay.git \
    && cd cowsay && ./install.sh /usr/local \
    && cd .. \
    && rm -rf cowsay \
    && apk del git

WORKDIR /app/

COPY . ./

CMD ["python", "bio.py"]

EXPOSE 5000