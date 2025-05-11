import os
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI


# Carrega a API do google e a senha do banco de dados
load_dotenv(find_dotenv())
GOOGLE_KEY = os.environ.get('GOOGLE_API_KEY')
DB_PASSWORD = os.environ['DB_PASSWORD']


# Definir um template de prompt para gerar queries baseando nas tabelas
template = """
Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query
"""
prompt = ChatPromptTemplate.from_template(template)
prompt.format(schema='my schema', question="how many users are there?")


# Cria uma isntância de conexão com o banco de dados
db_uri = f"mysql+mysqlconnector://root:{DB_PASSWORD}@localhost:3306/chinook"
db = SQLDatabase.from_uri(db_uri)


# Retorna a estrutura da tabela
def get_schema(_):
    return db.get_table_info()

get_schema(None)


# Instancia do google gemini para geração
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# Cria uma cadeia de execução 
sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm 
    | StrOutputParser()
)

# Remove os markdowns para gerar as querys
def clean_sql_query(query):
    lines = query.strip().split('\n')
    cleaned_lines = []
    for line in lines:
        if line.strip().startswith('```') or line.strip() == 'sql':
            continue
        cleaned_lines.append(line)
    cleaned_query = '\n'.join(cleaned_lines).strip()
    return cleaned_query

# Executa a query no banco de dados
def run_query(query):
     cleaned_query = clean_sql_query(query)
     db.run(cleaned_query)
    

# Cadeia de execução para retornar o resultado
full_chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
        schema=get_schema,
        response = lambda variables: run_query(variables["query"])   
    )
    |prompt
    |llm
)


# Loop para interação do usuário
while True:
    q = int(input("Escolha uma opção:\n1. Inserir dados\n2 Consultar dados\n3. Deletar dados\n4. Atualizar dados\n" \
    "Outro número para sair\nOpção: "))

    match q:
        case 1:
            c = input("Digite o nome do artista que quer colocar no banco: ")
            resposta = full_chain.invoke({"question": f"Insert a new artist named: {c} into the artist table."})
            sql_query = clean_sql_query(resposta.content)
            result = db.run(sql_query)
            print(result)
        case 2:
            c = input("TDigite o que deseja saber do banco: ")
            resposta = full_chain.invoke({"question": c})
            sql_query = clean_sql_query(resposta.content)
            result = db.run(sql_query)
            print(result)
        case 3:
            c = input("Digite o que deseja deletar do banco: ")
            resposta = full_chain.invoke({"question": c})
            sql_query = clean_sql_query(resposta.content)
            result = db.run(sql_query)
            print(result)
        case 4:
            c = input("Type what you want to update in the database: ")
            resposta = full_chain.invoke({"question": c})
            sql_query = clean_sql_query(resposta.content)
            result = db.run(sql_query)
            print(result)
        case _:
            break