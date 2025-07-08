from langchain_openai import ChatOpenAI
from operator import itemgetter
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain as LLMCHAIN
from langchain.chains import SimpleSequentialChain
from langchain.globals import set_debug
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
set_debug(True)


class Destino(BaseModel):
    cidade = Field("cidade a visitar")
    motivo = Field("motivo pelo qual é interessante visitar")


API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

llms = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, api_key=API_KEY)
parseador = JsonOutputParser(pydantic_object=Destino)
modelo_cidade = PromptTemplate(
    template="""Sugira uma cidade dado meu interesse por {interesse}.
    {formatacao_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)
modelo_restaurantes = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares entre locais em {cidade}"
)
modelo_cultural = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)
modelo_final = ChatPromptTemplate.from_messages(
   [
    ("ai", "Sugestão de viagem para a cidade: {cidade}")
    ("ai", "Restaurantes que você não pode perder: {restaurantes}")
    ("ai", "Atividades e Locais culturais recomendados: {locais_culturais}"),
    ("system", "Combine as informações das cadeias anteriores em 2 parágrafos coerentes.")
   ]
)
# O operador | conecta componentes sequencialmente
parte1 = modelo_cidade | llms | parseador
parte2 = modelo_restaurantes | llms | StrOutputParser()
parte3 = modelo_cultural | llms | StrOutputParser()
parte4= modelo_final | llms | StrOutputParser()
# A cadeia executa a parte 2 e a parte 3 em paralelo
# é colocado o resultado da parte 2 e parte 3 em variaveis pois sao necessarias para o modelo_final
cadeia = (parte1 | {"restaurantes": parte2 , "locais_culturais": parte3, "cidade": itemgetter("cidade")} | parte4)
resultado = cadeia.invoke({"interesse": "praias"})
print(resultado)
