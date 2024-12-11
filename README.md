
# 🌱 **Carbon Footprint Calculator**

The **Carbon Footprint Calculator** is an interactive web application built using **Streamlit** that helps individuals and organizations measure their environmental impact. By providing key data on transportation, energy usage, dietary habits, waste management, and home/office details, users can get an estimate of their carbon footprint and discover actionable insights to reduce it.

This project integrates **Google's Generative AI**, powered by **Langchain** and **CarbonCalcAI**, to process the user inputs and generate personalized carbon footprint assessments.

---

## 🔧 **Technologies Used**

- **Streamlit**: Web app framework for building interactive and beautiful applications.
- **Langchain**: For integrating language models and prompting templates.
- **Google Gemini**: AI model used to calculate carbon footprint based on provided inputs.
- **Python**: The core language for the application.
- **docx**: Python library to generate downloadable Word reports.
- **dotenv**: To securely manage API keys and environment variables.

---

## 🚀 **Features**

- **User-Friendly Interface**: Interactive sidebar form for users to input relevant information about their lifestyle.
- **Carbon Footprint Calculation**: Real-time carbon footprint estimation based on transportation, energy usage, diet, waste generation, and home/office parameters.
- **Downloadable Report**: Provides a Word document report of the carbon footprint calculation for the user's records.
- **Data-Driven Insights**: Offers insights on how users can reduce their carbon footprint based on the results.

---

## 🛠 **Installation**

1. Clone the repository:

    ```bash
    git clone <repository_url>
    
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv python==3.10
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your **Google API Key**:

    ```
    GOOGLE_API_KEY=<your_google_api_key>
    ```

---

## ⚙️ **How It Works**

1. **Input Data**: The user fills out a form in the sidebar, providing details about their mode of transport, energy usage, diet, food waste, waste management practices, and home/office parameters.
2. **Carbon Footprint Calculation**: The user clicks "Calculate Carbon Footprint," and the application processes the inputs using Google's **Gemini 1.5** model and the **CarbonCalcAI** prompt.
3. **Results**: A summary of the user's carbon footprint is displayed on the main page, and they can download a Word report with the details.
4. **Actionable Insights**: The app offers suggestions for reducing carbon emissions based on the input data.

---

## 🖼️ **Demo**

### 🌍 **Home Page:**
A visually appealing, image-background page where users interact with the sidebar to input their data.

### 📊 **Results Page:**
After submitting the form, users see a detailed carbon footprint calculation and can download a Word report with the data.

---

---

## 🧑‍💻 **How to Use**

1. Launch the app:

    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to the local address provided by Streamlit (usually `http://localhost:8501`).
3. Fill out the form with the relevant details about your lifestyle.
4. Click on "Calculate Carbon Footprint" to get your environmental impact score.
5. Download your personalized carbon footprint report in Word format.

---

## 🌍 **Environmental Impact**

The goal of this project is to raise awareness about the environmental impact of everyday activities and empower users to make more sustainable choices. By measuring and understanding their carbon footprint, individuals and organizations can take actionable steps toward reducing their carbon emissions and contributing to a healthier planet.

---

## 📚 **Contributing**

We welcome contributions to improve the app! If you have suggestions or find any issues, feel free to create an issue or a pull request.

---

## 📑 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
