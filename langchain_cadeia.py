from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain as LLMCHAIN
from langchain.chains import SimpleSequentialChain
from langchain.globals import set_debug
from dotenv import load_dotenv
import os
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
set_debug(True)

modelo_cidade= ChatPromptTemplate.from_template("Sugira uma cidade dado meu interesse por {interesse}. A sua saída deve ser SOMENTE o nome da cidade. Cidade:")
modelo_restaurantes= ChatPromptTemplate.from_template("Sugira restaurantes populares entre locais em {cidade}")
modelo_cultural= ChatPromptTemplate.from_template("Sugira atividades e locais culturais em {cidade}")

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

llms = ChatOpenAI(model='gpt-3.5-turbo',
                  temperature=0.5,
                  api_key=API_KEY)
cadeia_cidade=LLMCHAIN(prompt=modelo_cidade, llm=llms)
cadeia_restaurantes=LLMCHAIN(prompt=modelo_restaurantes, llm=llms)
cadeia_cultural=LLMCHAIN(prompt=modelo_cultural, llm=llms)

cadeia=SimpleSequentialChain(chains=[cadeia_cidade, cadeia_restaurantes, cadeia_cultural], verbose=True)
resultado =cadeia.invoke('praias')
print(resultado)