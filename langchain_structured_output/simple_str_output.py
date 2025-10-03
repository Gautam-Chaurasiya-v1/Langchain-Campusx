from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatOpenAI()

#Schema
class Review(TypedDict):
    summary:str
    sentiment:str

#invoke structred
structured_model = chatModel.with_structured_output(Review)

#invoke model
review = "The XYZ Phone 12 Pro has a stunning display, smooth performance, and excellent cameras. Battery life is solid, but the phone feels a bit heavy and the price is high. Overall, it’s a great choice if you want premium quality."

result = structured_model.invoke(review)

print(result)