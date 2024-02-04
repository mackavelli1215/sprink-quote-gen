from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv

load_dotenv()

def generate_quote(labor_costs, materials_costs):
    llm = ChatOpenAI(temperature = 0.3)

    prompt_template_name = PromptTemplate(
        input_variables=['labor_costs', 'materials_costs'],
        template="Add the {labor_costs} and the {materials_costs} and then add a 50 percent gross margin to produce a final quotation price for a sprinkler service."
    )

    quote_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    response = quote_chain({'labor_costs': labor_costs, 'materials_costs': materials_costs})
    return response 

if __name__ == "__main__":
    print(generate_quote(678, 745))

