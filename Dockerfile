FROM python:3.11-slim-bookworm
ARG OPENAI_API_KEY_ARG

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV OPENAI_API_KEY=$OPENAI_API_KEY_ARG

# EXPOSE 8000

CMD [ "python3", "main.py"]