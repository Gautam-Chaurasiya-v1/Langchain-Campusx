from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatOpenAI(model='gpt-4',temperature=1.5)

result = chatModel.invoke("What is the meaning of been absolute observer")

print(result.content)
