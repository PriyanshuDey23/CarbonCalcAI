from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.llm import LLMChain
from CarbonCalcAI.prompt import *

# Load environment variables from .env file
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

def calculate_carbon_footprint(
    mode_of_transport,
    monthly_travel_distance,
    passenger_count,
    monthly_energy_usage,
    energy_source,
    dietary_habits,
    food_waste,
    weekly_waste_generation,
    disposal_method,
    living_area,
    heating_and_cooling_system,
):

    # Initialize the LLM model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", temperature=1,api_key=GOOGLE_API_KEY)

    # Set up the prompt template
    prompt = PromptTemplate(
        input_variables=[
            "mode_of_transport",
            "monthly_travel_distance",
            "passenger_count",
            "monthly_energy_usage",
            "energy_source",
            "dietary_habits",
            "food_waste",
            "weekly_waste_generation",
            "disposal_method",
            "living_area",
            "heating_and_cooling_system",
        ],
        template=PROMPT
    )

    # Create the LLM chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Generate and return the response
    return llm_chain.run(
        {
            "mode_of_transport": mode_of_transport,
            "monthly_travel_distance": monthly_travel_distance,
            "passenger_count": passenger_count,
            "monthly_energy_usage": monthly_energy_usage,
            "energy_source": energy_source,
            "dietary_habits": dietary_habits,
            "food_waste": food_waste,
            "weekly_waste_generation": weekly_waste_generation,
            "disposal_method": disposal_method,
            "living_area": living_area,
            "heating_and_cooling_system": heating_and_cooling_system,
        }
    )


