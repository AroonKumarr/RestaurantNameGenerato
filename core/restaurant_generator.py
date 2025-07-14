from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

# ✅ Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",   # or "gpt-4" if you have access
    temperature=0.7
)

def generate_restaurant_name_and_items(cuisine):
    # Prompt to generate restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.'
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Prompt to generate menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='Suggest a detailed menu (5–7 items) for a restaurant named "{restaurant_name}".'
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine both steps in sequence
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items'],
        verbose=True
    )

    return chain.invoke({'cuisine': cuisine})  # Using `.invoke()` to avoid deprecation warning
