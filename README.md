# API de Recomendação de Papers

Este repositório contém uma API desenvolvida com FastAPI para recomendar papers científicos com base em uma consulta de texto. A API utiliza um modelo de recomendação baseado em TF-IDF para calcular a relevância dos documentos com base na entrada do usuário.

## Base de Dados

A base de dados utilizada para recomendação de papers é derivada de um conjunto de dados contendo informações sobre artigos científicos, como título, autores, resumo (abstract), e outras informações relevantes. Para esta aplicação, apenas os seguintes campos foram mantidos:

- **`cord_uid`**: Identificador único do documento.
- **`title`**: Título do paper.
- **`abstract`**: Resumo do paper (usado para calcular a relevância).
- **`publish_time`**: Data de publicação.
- **`authors`**: Lista de autores do paper.
- **`journal`**: Jornal ou conferência onde o paper foi publicado.
- **`url`**: Link para o paper original.

Os dados foram filtrados para garantir que apenas documentos com resumos preenchidos estejam presentes, e o conjunto de dados foi limitado a 10.000 linhas para otimizar o desempenho.

## Como Rodar a API

### Pré-requisitos

- Python 3.x instalado
- Pip instalado (geralmente já vem com o Python)

### Passos para Rodar

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/Guilherme-s-m/Covid-Articles-AP.git
   cd nome-do-repositorio
   ```

2. **Torne o Script Executável e Instale as Dependências:**

   Use o script `start_unix.sh` para instalar as dependências e rodar a API. Para isso, torne o script executável e execute-o:

   ```bash
   chmod +x start_unix.sh
   ./start_unix.sh
   ```

   Este script irá:
   - Instalar todas as dependências listadas no arquivo `requirements.txt`.
   - Executar a API utilizando o Uvicorn na porta 3942.

3. **Acesse a API:**

   A API estará disponível em: `http://10.103.0.28:3942`.

### Documentação Interativa

Uma documentação interativa da API está disponível em: `http://10.103.0.28:3942/docs`.

## Casos de Uso

Aqui estão três exemplos de uso para testar a API:

### 1. Retornando 10 Documentos

- **Descrição:** Este caso de uso retorna uma lista completa de 10 documentos mais relevantes para a consulta dada.
- **URL:** [http://10.103.0.28:3942/query?query=deep+learning](http://10.103.0.28:3942/query?query=deep+learning)
- **Explicação:** A consulta "deep learning" é ampla e popular, gerando muitos resultados relevantes. Por isso, a API retorna o número máximo de documentos permitidos (10), garantindo que o usuário obtenha uma lista diversificada de papers relevantes sobre o tema.

### 2. Retornando Entre 1 a 9 Documentos

- **Descrição:** Este caso de uso retorna entre 1 e 9 documentos, mostrando que a API pode lidar com consultas menos comuns ou mais específicas.
- **URL:** [http://10.103.0.28:3942/query?query=Zebrafish%20and%20Medaka](http://10.103.0.28:3942/query?query=Zebrafish%20and%20Medaka)
- **Explicação:** A consulta "Zebrafish and Medaka" é mais específica e restrita, resultando em menos documentos que atendem aos critérios de relevância. Dependendo do conteúdo da base de dados, a API pode retornar de 1 a 9 documentos.

### 3. Retornando Algo Não Óbvio

- **Descrição:** Este caso de uso demonstra um resultado menos esperado, onde a consulta não parece diretamente relacionada aos documentos retornados, mas ainda pode fornecer insights valiosos.
- **URL:** [http://10.103.0.28:3942/query?query=quantum+mechanics+influence+on+machine+learning](http://10.103.0.28:3942/query?query=quantum+mechanics+influence+on+machine+learning)
- **Explicação:** A consulta "quantum mechanics influence on machine learning" é interdisciplinar e incomum, o que pode levar a resultados não óbvios. A maioria dos papers pode não abordar diretamente a interseção exata entre esses campos, mas documentos relacionados que exploram aspectos avançados de algoritmos de aprendizado de máquina ou teoria quântica podem ser recomendados, oferecendo uma perspectiva inovadora que não é imediatamente evidente.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias.
