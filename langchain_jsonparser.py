from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain as LLMCHAIN
from langchain.chains import SimpleSequentialChain
from langchain.globals import set_debug
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
set_debug(True)

class Destino(BaseModel):
    cidade= Field('cidade a visitar')
    motivo= Field('motivo pelo qual é interessante visitar')

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

llms = ChatOpenAI(model='gpt-3.5-turbo',
                  temperature=0.5,
                  api_key=API_KEY)
parseador= JsonOutputParser(pydantic_object=Destino)
modelo_cidade= PromptTemplate(
    template="""Sugira uma cidade dado meu interesse por {interesse}.
    {formatacao_de_saida}
    """,
    input_variables=['interesse'],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()})
modelo_restaurantes= ChatPromptTemplate.from_template("Sugira restaurantes populares entre locais em {cidade}")
modelo_cultural= ChatPromptTemplate.from_template("Sugira atividades e locais culturais em {cidade}")



cadeia_cidade=LLMCHAIN(prompt=modelo_cidade, llm=llms)
cadeia_restaurantes=LLMCHAIN(prompt=modelo_restaurantes, llm=llms)
cadeia_cultural=LLMCHAIN(prompt=modelo_cultural, llm=llms)

cadeia=SimpleSequentialChain(chains=[cadeia_cidade,cadeia_restaurantes,cadeia_cultural], verbose=True)
resultado =cadeia.invoke('praias')
print(resultado)

"""
Este código é uma alternativa à classe LLMChain e SimpleSequentialChain, que serão depreciadas.  
Ele utiliza a estrutura de Runnables do LangChain para criar uma cadeia de execução mais modular e flexível.  
O código está comentado por padrão para evitar execução automática, mas pode ser descomentado conforme necessário.

Para testar, basta remover os comentários da seção correspondente. E comentar o codigo depreciado que começa na linha 82.
"""

'''  # Remova esta linha de comentário para ativar o código

# Importação das classes necessárias para a criação da cadeia de execução
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema import StrOutputParser

# Definição de diferentes cadeias que processam informações específicas
cadeia_cidade = modelo_cidade | llm | parseador
cadeia_restaurantes = modelo_restaurantes | llm 
cadeia_cultural = modelo_cultural | llm | StrOutputParser()

# Composição da cadeia principal, que agrega os diferentes fluxos de processamento
cadeia = (
    RunnablePassthrough() 
    | RunnablePassthrough.assign(cidade=cadeia_cidade) 
    | RunnablePassthrough.assign(restaurantes=cadeia_restaurantes) 
    | RunnablePassthrough.assign(cultura=cadeia_cultural)
)

# Executando a cadeia com um interesse específico
resultado = cadeia.invoke({"interesse": "praias"})

# Exibindo o resultado do fluxo cultural processado
print(resultado.get("cultura"))

# '''  # Remova esta linha de comentário para ativar o código