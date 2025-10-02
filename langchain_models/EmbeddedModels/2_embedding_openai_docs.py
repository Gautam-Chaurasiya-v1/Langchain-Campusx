from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

docs = [
    "I am Human",
    "You are robot",
    "You are good"
]

result = embedding.embed_documents(docs)  

print(str(result))