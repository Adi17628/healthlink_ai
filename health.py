import streamlit as st
from google import genai
from google.genai import types
import time
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="HealthLink AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .feature-card {
        background: #343a40;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .response-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 0 1.5rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# System prompt
prompt_system = """
# Combined Health & Medicine Assistant System Prompt

You are a helpful health assistant that provides both symptom guidance and medicine information. Always respond in 150-200 words using simple English and clear structure.

## Task Detection
**If user mentions symptoms:** Provide first aid recommendations
**If user mentions medicine name:** Explain medicine uses and conditions

## Format for SYMPTOM QUERIES

### 🚨 Immediate Steps
- List 2-3 urgent first aid actions
- Mention emergency signs if serious

### 🏠 Self-Care Tips  
- Provide 3-4 simple home remedies
- Include timeline (24-48 hours)

### ⚠️ See Doctor If
- Clear warning signs
- When to seek medical help

## Format for MEDICINE QUERIES

### 💊 [Medicine Name]
**What it does:** Simple explanation of how it works
**Treats:** Main conditions it's used for
**Form:** How it's taken (tablet/liquid/injection)

### ⚠️ Important Notes
- Common side effects (2-3 main ones)
- Key safety warnings
- When to avoid using it

## Writing Rules
- Use 6th-grade reading level
- Keep responses between 150-200 words
- Use bullet points for clarity
- Include emojis for visual structure
- Write in friendly, caring tone
- Always end with: "This is general information only. Consult your doctor for personalized medical advice."

## Safety First
- For emergencies: Start with "🚨 SEEK IMMEDIATE MEDICAL HELP"
- Never diagnose specific conditions
- Always recommend professional consultation when needed
- Focus on evidence-based information only
"""

# Initialize session state
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''

# Header
st.markdown("""
<div class="main-header">
    <div class="main-title">🏥 HealthLink AI</div>
    <div class="main-subtitle">Your Personal AI Health Assistant</div>
    <p style="margin-top: 1rem; font-size: 1rem;">Get instant health guidance and medicine information powered by advanced AI</p>
</div>
""", unsafe_allow_html=True)

# API Key input in sidebar
with st.sidebar:
    st.markdown("### 🔐 API Configuration")
    api_key = st.text_input(
        "Enter your Google Gemini API Key:",
        type="password",
        value=st.session_state.api_key,
        help="Get your API key from Google AI Studio"
    )
    if api_key:
        st.session_state.api_key = api_key
        st.success("✅ API Key configured!")
    
    st.markdown("---")
    st.markdown("""
    ### 📋 How to Use
    1. **Text Query**: Ask about symptoms or medicine names
    2. **Image Analysis**: Upload medical images for analysis
    3. Get instant AI-powered health guidance
    
    ### ⚠️ Important Notice
    This tool provides general information only and should not replace professional medical advice.
    """)

# Check if API key is provided
if not st.session_state.api_key:
    st.warning("⚠️ Please enter your Google Gemini API key in the sidebar to continue.")
    st.stop()

# Initialize Gemini client
@st.cache_resource
def init_gemini_client(api_key):
    return genai.Client(api_key=api_key)

try:
    client = init_gemini_client(st.session_state.api_key)
except Exception as e:
    st.error(f"❌ Failed to initialize Gemini client: {str(e)}")
    st.stop()

# Main content tabs
tab1, tab2 = st.tabs(["💬 Text Query", "📸 Image Analysis"])

with tab1:
    st.markdown("### Ask About Symptoms or Medicines")
    
    # Feature cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🩺 Symptom Analysis</h4>
            <p>Describe your symptoms and get first aid recommendations, self-care tips, and guidance on when to seek medical help.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>💊 Medicine Information</h4>
            <p>Enter a medicine name to learn about its uses, side effects, dosage forms, and important safety information.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Text input
    user_query = st.text_area(
        "What would you like to know?",
        placeholder="Examples:\n• I have a headache and feel nauseous\n• What is DOLO-650 used for?\n• I have a fever and body aches",
        height=100
    )
    
    if st.button("🔍 Get Health Guidance", type="primary", use_container_width=True):
        if user_query.strip():
            with st.spinner("🤔 Analyzing your query..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        config=types.GenerateContentConfig(
                            system_instruction=prompt_system
                        ),
                        contents=user_query
                    )
                    
                    st.markdown("""
                    <div class="response-container">
                        <h3>🤖 AI Health Assistant Response</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(response.text)
                    
                    # Warning box
                    st.markdown("""
                    <div class="warning-box">
                        <strong>⚠️ Medical Disclaimer:</strong> This information is for educational purposes only. 
                        Always consult with healthcare professionals for proper medical diagnosis and treatment.
                    </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"❌ Error generating response: {str(e)}")
        else:
            st.warning("⚠️ Please enter your health query.")

with tab2:
    st.markdown("### Upload Medical Images for Analysis")
    
    st.markdown("""
    <div class="feature-card">
        <h4>📱 Image Analysis Capabilities</h4>
        <p>Upload medical images such as skin conditions, rashes, wounds, or other visible symptoms. 
        Our AI will analyze the image and provide relevant health information.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a medical image",
        type=['png', 'jpg', 'jpeg', 'webp'],
        help="Supported formats: PNG, JPG, JPEG, WEBP"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        col1, col2 = st.columns([1, 2])
        
        with col1:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
        
        with col2:
            st.markdown("**Image Details:**")
            st.write(f"• **Filename:** {uploaded_file.name}")
            st.write(f"• **File Size:** {uploaded_file.size / 1024:.1f} KB")
            st.write(f"• **Image Format:** {image.format}")
            st.write(f"• **Image Size:** {image.size[0]} x {image.size[1]} pixels")
        
        # Analysis button
        if st.button("🔬 Analyze Image", type="primary", use_container_width=True):
            with st.spinner("🔍 Analyzing your medical image..."):
                try:
                    # Upload file to Gemini
                    file_data = uploaded_file.getvalue()
                    temp_file = io.BytesIO(file_data)
                    
                    # Create a temporary file for upload
                    import tempfile
                    import os
                    
                    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                        tmp_file.write(file_data)
                        tmp_file_path = tmp_file.name
                    
                    try:
                        # Upload to Gemini
                        my_file = client.files.upload(file=tmp_file_path)
                        
                        # Generate response
                        response = client.models.generate_content(
                            model="gemini-2.5-flash",
                            config=types.GenerateContentConfig(
                                system_instruction=prompt_system
                            ),
                            contents=[my_file, "Analyze this medical image and provide health guidance for any symptoms or conditions you can identify."]
                        )
                        
                        st.markdown("""
                        <div class="response-container">
                            <h3>🔬 Image Analysis Results</h3>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown(response.text)
                        
                        # Success box
                        st.markdown("""
                        <div class="success-box">
                            <strong>✅ Analysis Complete:</strong> The AI has analyzed your image and provided relevant health information.
                        </div>
                        """, unsafe_allow_html=True)
                        
                    finally:
                        # Clean up temporary file
                        os.unlink(tmp_file_path)
                        
                except Exception as e:
                    st.error(f"❌ Error analyzing image: {str(e)}")
    else:
        st.info("📤 Please upload a medical image to get started with image analysis.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><strong>HealthLink AI</strong> - Empowering Health Decisions with AI</p>
    <p>⚠️ This tool is for informational purposes only and does not replace professional medical advice, diagnosis, or treatment.</p>
    <p>Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.</p>
</div>
""", unsafe_allow_html=True)