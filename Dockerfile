FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  python3 \
  python3-dev \
  netcat \
  python3-pip

WORKDIR /src

COPY ./src/ /src/

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "/src/entrypoint.sh" ]