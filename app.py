from fastapi import FastAPI, Query
import os
import uvicorn
from service import recommend_papers_from_csv  # Importa a função de recomendação do arquivo service.py

# Criação da aplicação FastAPI
app = FastAPI()

# Caminho para o arquivo CSV com dados limitados
CSV_PATH = "data/metadata_limited.csv"

@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):
    try:
        # Chamando a função de recomendação com a consulta do usuário
        recommendations = recommend_papers_from_csv(query)
        return {"results": recommendations, "message": "OK"}
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=3942, reload=True)

if __name__ == "__main__":
    run()
