import os

from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0.9)


from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["food"],
    template="5 best resturants in bangalore for {food} along with the best time to visit?",
)
food = input("What food are you looking for? ")
print(llm(prompt.format(food="food")))

