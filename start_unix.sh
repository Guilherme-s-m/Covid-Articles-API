#!/bin/bash

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não está instalado. Por favor, instale o Python3 para continuar."
    exit
fi

# Verifica se o pip está instalado
if ! command -v pip3 &> /dev/null
then
    echo "pip3 não está instalado. Instalando pip3..."
    sudo apt-get install python3-pip -y
fi

# Instala as dependências do arquivo requirements.txt
echo "Instalando dependências..."
pip3 install -r requirements.txt

# Executa a API
echo "Executando a API..."
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
