# Usa una base Ubuntu image
FROM ubuntu:20.04

# Imposta variabili di ambiente per evitare l'interazione durante l'installazione dei pacchetti
ENV DEBIAN_FRONTEND=noninteractive

# Installa dipendenze, X11 e Kivy
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    libglib2.0-0 \
    libmtdev-dev \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Installa Kivy e altre dipendenze Python
RUN pip3 install kivy requests

# Imposta la directory di lavoro
WORKDIR /app

# Copia il codice dell'applicazione nel container
COPY . /app

# Espone la porta per X11
EXPOSE 6000

# Comando per avviare l'applicazione
CMD ["python3", "main.py"]
