PROMPT="""
Provide a detailed analysis and comprehensive report on the carbon footprint based on the following information:

Travel-Related Emissions
    - Mode of Transport: Specify your primary modes of travel (e.g., car, bus, train, plane): {mode_of_transport}
    - Monthly Travel Distance: What is your average distance traveled per month for each mode (in kilometers)? {monthly_travel_distance}
    - Passenger Count: How many passengers usually share your travel modes (if applicable)? {passenger_count}

Energy Consumption
    - Monthly Energy Usage: How much energy do you consume monthly (in kilowatt-hours, kWh)? {monthly_energy_usage}
    - Energy Source: Indicate your primary energy source (e.g., coal, natural gas, oil, solar, wind): {energy_source}

Food-Related Emissions
    - Dietary Habits: Describe your typical diet (e.g., meat-based, vegetarian, vegan, flexitarian): {dietary_habits}
    - Food Waste: How much food waste do you generate per week (in kilograms)? {food_waste}

Waste Management
    - Weekly Waste Generation: What is the total amount of waste you produce per week (in kilograms)? {weekly_waste_generation}
    - Disposal Methods: What is your primary method for waste disposal (e.g., landfill, recycling, composting, incineration)? {disposal_method}

Building and Infrastructure
    - Living/Work Area: What is the size of your home or office space (in square feet or square meters)? {living_area}
    - Heating and Cooling: Specify the type of heating and cooling systems you use (e.g., central air, heat pump, none): {heating_and_cooling_system}


Deliverables:

- Detailed Analysis: Provide a detailed analysis of greenhouse gas emissions based on the provided information.
- Total Carbon Footprint: Provide a clear numerical representation of the total carbon footprint in kg CO2e per year.
- Category Breakdown: Offer insights into emissions from travel, energy, food, waste, and infrastructure.
- Opinion and Suggestions: Provide an opinion on the largest contributor to the carbon footprint and suggest strategies for reduction.
- Comprehensive Report: Compile all the information into a comprehensive report

Note: Please use the provided information to generate a comprehensive report. If any information is missing, please make assumptions or provide recommendations for further data collection.

"""