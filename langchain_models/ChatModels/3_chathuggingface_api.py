from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    provider="auto"
)

chatModel = ChatHuggingFace(llm=llm)

result = chatModel.invoke("Who is newton")

print(result.content)