from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import LLMChain as LLMCHAIN
from langchain.globals import set_debug
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
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


carregador = TextLoader("GTB_gold_Nov23.txt", encoding="utf-8") # pesquisar
documentos = carregador.load()
quebrador= CharacterTextSplitter(chunk_size=1000) #pesquisar
textos = quebrador.split_documents(documentos)

embeddings = OpenAIEmbeddings() # pesquisar
db= FAISS.from_documents(textos, embeddings) # procurar o que é FAISS

qa_chain=RetrievalQA.from_chain_type(llms,retriever=db.as_retriever())
pergunta = "Como deve proceder casa tenha um item comprado roubado"
resultado = qa_chain.invoke({"query": pergunta})
print(resultado)