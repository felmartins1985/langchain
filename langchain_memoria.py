from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain as LLMCHAIN
from langchain.globals import set_debug
from langchain_core.output_parsers import  StrOutputParser
from dotenv import load_dotenv
import os
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
set_debug(True)


API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

llms = ChatOpenAI(model='gpt-3.5-turbo',
                  temperature=0.5,
                  api_key=API_KEY)

mensagens = [
        "Quero visitar um lugar no Brasil famoso por suas praias e cultura. Pode me recomendar?",
        "Qual é o melhor período do ano para visitar em termos de clima?",
        "Quais tipos de atividades ao ar livre estão disponíveis?",
        "Alguma sugestão de acomodação eco-friendly por lá?",
        "Cite outras 20 cidades com características semelhantes as que descrevemos até agora. Rankeie por mais interessante, incluindo no meio ai a que você já sugeriu.",
        "Na primeira cidade que você sugeriu lá atrás, quero saber 5 restaurantes para visitar. Responda somente o nome da cidade e o nome dos restaurantes.",
]


longa_conversa = ""
for mensagem in mensagens:
    longa_conversa= f"Usuário: {mensagem}\n"
    longa_conversa += f"IA:"

    modelo=PromptTemplate(template=longa_conversa, input_variables=[""])
    cadeia= modelo | llms| StrOutputParser()
    resposta = cadeia.invoke(input={}) # ver
    # print(resposta)
    longa_conversa += resposta + "\n"
    print