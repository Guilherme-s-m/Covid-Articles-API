# Verificar se o Python está instalado
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Python não está instalado. Por favor, instale o Python para continuar."
    exit
}

# Instalar dependências do requirements.txt
Write-Output "Instalando dependências..."
pip install -r requirements.txt

# Executar a API
Write-Output "Executando a API..."
uvicorn app:app --host 0.0.0.0 --port 3942 --reload
