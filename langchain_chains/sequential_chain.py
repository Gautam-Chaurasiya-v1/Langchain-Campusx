from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# prompt

prompt = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

# model 
model = ChatOpenAI()

# parser 
parser = StrOutputParser()

# prompt 2 
prompt2 = PromptTemplate(
  template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
 )

# chain -> prompt + model + parser + prompt2 + model + parser
chain = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'employment in India'})

print(result)

chain.get_graph().print_ascii()