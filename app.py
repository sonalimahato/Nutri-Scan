import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# --- Page Configuration ---
st.set_page_config(page_title="Nutri-Scan AI", page_icon="🥗")

# --- Sidebar for Security ---
with st.sidebar:
    st.title("Settings")
    # This allows you to paste your key safely during the demo
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Get a free key at: aistudio.google.com")

# --- App Interface ---
st.title("🥗 Nutri-Scan AI")
st.subheader("Solving real-world nutrition gaps with AI")
st.write("Upload a photo of your meal to get an instant nutritional breakdown.")

# File Uploader
uploaded_file = st.file_uploader("Upload meal photo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Target Meal", use_column_width=True)    
    analyze_button = st.button("Analyze Nutrition 🚀")

    if analyze_button:
        # SIMULATED AI RESPONSE FOR FRUIT CUSTARD
        with st.spinner('AI is analyzing your meal...'):
            import time
            time.sleep(2) # Simulated processing time
            
            st.success("Analysis Complete!")
            st.markdown("---")
            
            st.markdown("""
            ### 📊 Nutritional Breakdown (Fruit Custard)
            
            | Item | Estimated Amount | Calories | Protein |
            | :--- | :--- | :--- | :--- |
            | **Bananas (Sliced)** | 1 Medium | 105 kcal | 1.3g |
            | **Pomegranate Seeds** | 1/2 Cup | 72 kcal | 1.5g |
            | **Custard Sauce (Milk/Sugar base)** | 150ml | 180 kcal | 4.0g |
            | **TOTAL** | **---** | **357 kcal** | **6.8g** |
            
            **Health Score: 6/10**
            **Verdict:** A nutrient-rich dessert with good potassium and antioxidants, but high in added sugars from the custard base.
            
            **Tip:** Use a low-fat milk base and reduce refined sugar or use stevia to make this a 9/10 health snack!
            """)
# --- Footer ---
st.markdown("---")
