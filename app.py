import streamlit as st
from CarbonCalcAI.helper import  calculate_carbon_footprint
from CarbonCalcAI.utils import *

# Set page configuration
st.set_page_config(
    page_title="Carbon Footprint Calculator",
    page_icon="🌿",
    layout="centered",  # Keeping original layout
    initial_sidebar_state="expanded",
)

# Title and subtitle with emojis
st.markdown(
    """
    # 🌱 **Carbon Footprint Calculator**
    ### Measure your environmental impact and get actionable insights! 
    💨 *Let's make the planet greener together!*
    """
)

# Add background image for the entire page
st.markdown(
    """
    <style>
    .reportview-container {
        background: url('https://images.unsplash.com/photo-1506748686213-b9c58d0587de?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDJ8fG5hdHVyZSUyMGJpbGx8ZW58MHx8fHwxNjg4NTA2NzI2&ixlib=rb-1.2.1&q=80') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True
)



# Add a stylish separator line for visual appeal
st.markdown("---")

# User interaction form
with st.sidebar:
    st.title(" 🖌️ **Fill out the details below:**")
    st.markdown("#### 🚗 **Transportation**")
    mode_of_transport = st.selectbox("How do you usually travel?", ["Car 🚗", "Bus 🚌", "Train 🚆", "Plane ✈️", "Other (please specify)"])
    mode_of_transport_custom = ""
    if mode_of_transport == "Other (please specify)":
        mode_of_transport_custom = st.text_input("Please specify your mode of transport:", placeholder="e.g., Bicycle, Boat")

    monthly_travel_distance = st.number_input("Distance traveled per month (km) 🛣", min_value=0)
    passenger_count = st.number_input("Number of passengers in vehicle 👥", min_value=1)

    st.markdown("#### 🔋 **Energy Usage**")
    monthly_energy_usage = st.number_input("Monthly energy consumption (kWh) 🔌", min_value=0)
    energy_source = st.selectbox(
        "Primary fuel source 🌌", ["Coal", "Natural Gas", "Oil", "Renewable Energy ♻️", "Other (please specify)"]
    )
    energy_source_custom = ""
    if energy_source == "Other (please specify)":
        energy_source_custom = st.text_input("Please specify your primary fuel source:", placeholder="e.g., Biomass, Hydrogen")

    st.markdown("#### 🍔 **Diet and Food Habits**")
    dietary_habits = st.selectbox(
        "Diet preference 🌶", ["Meat-based", "Vegetarian 🌱", "Vegan 🌿", "Flexitarian", "Other (please specify)"]
    )
    dietary_habits_custom = ""
    if dietary_habits == "Other (please specify)":
        dietary_habits_custom = st.text_input("Please specify your diet preference:", placeholder="e.g., Pescatarian")

    food_waste = st.number_input("Weekly food waste (kg) 🍲", min_value=0)

    st.markdown("#### 🗑 **Waste Management**")
    weekly_waste_generation = st.number_input("Weekly waste generation (kg) ♻", min_value=0)
    waste_disposal_method = st.selectbox(
        "Primary waste disposal method", ["Landfill", "Recycling ♻", "Composting 💦", "Incineration", "Other (please specify)"]
    )
    waste_disposal_custom = ""
    if waste_disposal_method == "Other (please specify)":
        waste_disposal_custom = st.text_input("Please specify your waste disposal method:", placeholder="e.g., Donation, Upcycling")

    st.markdown("#### 🏡 **Home or Office Details**")
    living_area = st.number_input("Square footage of your space 🏠", min_value=0)
    heating_and_cooling_system = st.selectbox(
        "Heating and cooling system ❄️", ["Gas", "Electric", "Heat Pump", "Other (please specify)"]
    )
    heating_custom = ""
    if heating_and_cooling_system == "Other (please specify)":
        heating_custom = st.text_input("Please specify your heating and cooling system:", placeholder="e.g., Solar, Geothermal")

# Handle form submission
if st.button("📊 Calculate Carbon Footprint"):
    with st.spinner("Calculating your carbon footprint... 🚀"):
        carbon_footprint = calculate_carbon_footprint(
            mode_of_transport,
            monthly_travel_distance,
            passenger_count,
            monthly_energy_usage,
            energy_source,
            dietary_habits,
            food_waste,
            weekly_waste_generation,
            waste_disposal_method,
            living_area,
            heating_and_cooling_system,
        )
        st.subheader("🌍 **Your Carbon Footprint**")
        st.write(carbon_footprint)
    

        # Create the DOCX file
        docx_file = create_docx(str(carbon_footprint))

        # Create download button for the DOCX file
        st.markdown("<hr style='border: 1px solid #388E3C;'>", unsafe_allow_html=True)
        st.download_button(
            label="Download Your Carbon Footprint Report 📥",
            data=docx_file,
            file_name="carbon_footprint_report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

