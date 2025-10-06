from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv 
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Hugging endpoint
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)


# model 
chatModel = ChatHuggingFace(llm = llm)


parser = JsonOutputParser()

template = PromptTemplate(
    template='Write 5 skills about astute observer /n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

# prompt = template.invoke({})

# print(prompt)


chain = template | chatModel | parser

result = chain.invoke({})

print(result)