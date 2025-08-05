import streamlit as st
import requests

# Configure the page
st.set_page_config(
    page_title="Website Mirror",
    page_icon="🌐",
    layout="wide"
)

# The website you want to mirror
WEBSITE_URL = "https://example.com"  # Replace with your target website

@st.cache_data(ttl=300)  # Cache for 5 minutes
def fetch_website(url):
    """Fetch website content"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"<h1>Error loading website</h1><p>{str(e)}</p>"

# Main app
st.title("🌐 Website Mirror")

# Fetch and display the website
with st.spinner("Loading website..."):
    website_content = fetch_website(WEBSITE_URL)

# Display the mirrored content
st.components.v1.html(website_content, height=800, scrolling=True)

# Optional: Show the source URL
st.info(f"Mirroring content from: {WEBSITE_URL}")
