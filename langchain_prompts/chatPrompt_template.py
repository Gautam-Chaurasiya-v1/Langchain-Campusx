from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    [
        ('system','You are an expert in {domain}'),
        ('human','Explain what is {topic} in simple terms')
    ]
)

prompt = chat_template.invoke({'domain':'cricket','topic':"lpw"})

print(prompt)