from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
print(prompt)


API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

cliente = OpenAI(api_key=API_KEY)

resposta = cliente.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
)

print(resposta)

roteiro_viagem = resposta.choices[0].message.content
print(roteiro_viagem)
