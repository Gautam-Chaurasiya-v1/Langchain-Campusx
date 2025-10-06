from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# model

model = ChatOpenAI()

# parser
parser = StrOutputParser()

# chain
chain = prompt | model | parser 

result = chain.invoke({'topic':'astute observer'})

# print(result)

chain.get_graph().print_ascii()