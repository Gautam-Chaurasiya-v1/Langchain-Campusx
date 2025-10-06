from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text-generation'
)

chatModel = ChatHuggingFace(llm = llm)

#1st prompt -> report
template = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)


#2nd prompt -> summarize

template2 = PromptTemplate(
    template='Write a 5 lines summary on the following text /n {text}',
    input_variables=['text']
)


# result 
chain = template | chatModel
# prompt = template.invoke({'topic':"astute observer"})
# result = chatModel.invoke(prompt)
result = chain.invoke({'topic':"astute observer"})

print(result.content)

prompt2 = template2.invoke({'text':result.content})
result2 = chatModel.invoke(prompt2)

print(result2.content)