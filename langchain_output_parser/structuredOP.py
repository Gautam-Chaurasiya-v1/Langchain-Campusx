from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# endpoint
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

# model
chatModel = ChatHuggingFace(llm=llm)

# schema
schema = [
    ResponseSchema(name='fact1', description='fact 1 about the topic'),
    ResponseSchema(name='fact1', description='fact 1 about the topic'),
    ResponseSchema(name='fact1', description='fact 1 about the topic')
]

#parser
parser = StructuredOutputParser.from_response_schemas(schema)

#teemplate 
template = PromptTemplate(
    template='Give 3 facts about topic {topic} /n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


#chain
chain = template | chatModel | parser

result = chain.invoke({"topic":"astute observer"})

print(result)

# prompt = template.invoke({"topic":"astute observer"})
# print(prompt)

# result = chatModel.invoke(prompt)
# print(result.content)

# finalR = parser(result) # not callable
# print(finalR)

