from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"


modelo_do_prompt = PromptTemplate.from_template("Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}.")
prompt = modelo_do_prompt.format(numero_de_dias=numero_de_dias, 
                        numero_de_criancas=numero_de_criancas, 
                        atividade=atividade)

print(prompt)

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

llms = ChatOpenAI(model='gpt-3.5-turbo',
                  temperature=0.5,
                  api_key=API_KEY)

resposta = llms.invoke(prompt)
print(resposta.content)