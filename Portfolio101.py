import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time
import math

# Page configuration
st.set_page_config(
    page_title="Your Name - Interactive Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

if 'show_animation' not in st.session_state:
    st.session_state.show_animation = False

# Custom CSS for modern styling and animations
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
        animation: fadeInDown 1s ease-out;
    }
    
    .section-header {
        color: #2E86AB;
        border-bottom: 2px solid #2E86AB;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }
    
    .skill-tag {
        background-color: #f0f2f6;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        margin: 0.25rem;
        display: inline-block;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }
    
    .skill-tag:hover {
        background-color: #2E86AB;
        color: white;
        transform: scale(1.05);
    }
    
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #2E86AB;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .interactive-button {
        background: linear-gradient(45deg, #2E86AB, #A23B72);
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-size: 1rem;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
    }
    
    .interactive-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(46, 134, 171, 0.4);
    }
    
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stats-card:hover {
        transform: scale(1.05);
    }
    
    .nav-button {
        background-color: #2E86AB;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 20px;
        cursor: pointer;
        margin: 0.25rem;
        transition: all 0.3s ease;
    }
    
    .nav-button:hover {
        background-color: #1a5f7a;
        transform: translateY(-2px);
    }
    
    .rotating-element {
        animation: rotate 4s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

def create_download_link(file_path, download_filename):
    """Create a download link for files"""
    try:
        with open(file_path, "rb") as f:
            bytes_data = f.read()
        b64 = base64.b64encode(bytes_data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{download_filename}" class="interactive-button">📄 Download Resume</a>'
        return href
    except (FileNotFoundError, OSError):
        return '''
        <div style="padding: 1rem; background-color: #fff3cd; border-radius: 8px; border-left: 4px solid #ffc107;">
            <p style="margin: 0; color: #856404;">
                📄 <strong>Resume Download:</strong> Add your resume.pdf file to the assets folder to enable download functionality.
            </p>
        </div>
        '''

def create_rotating_algorithm_viz():
    """Create an interactive rotating algorithm visualization"""
    st.markdown("### 🔄 Interactive Algorithm Visualization")
    
    # Algorithm selection
    algorithm = st.selectbox(
        "Choose Algorithm to Visualize:",
        ["Bubble Sort", "Binary Search Tree", "Spiral Matrix", "Fibonacci Spiral"]
    )
    
    if algorithm == "Bubble Sort":
        create_bubble_sort_animation()
    elif algorithm == "Binary Search Tree":
        create_bst_visualization()
    elif algorithm == "Spiral Matrix":
        create_spiral_matrix()
    elif algorithm == "Fibonacci Spiral":
        create_fibonacci_spiral()

def create_bubble_sort_animation():
    """Animated bubble sort visualization"""
    if st.button("🚀 Start Bubble Sort Animation", key="bubble_sort"):
        data = np.random.randint(1, 100, 10)
        chart_placeholder = st.empty()
        
        for i in range(len(data)):
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                
                # Create animated bar chart
                fig = px.bar(
                    x=list(range(len(data))), 
                    y=data,
                    title=f"Bubble Sort - Step {i * len(data) + j + 1}",
                    color=data,
                    color_continuous_scale="viridis"
                )
                fig.update_layout(showlegend=False, height=400)
                chart_placeholder.plotly_chart(fig, use_container_width=True)
                time.sleep(0.1)
        
        st.success("✅ Sorting Complete!")
        st.balloons()

def create_bst_visualization():
    """Interactive Binary Search Tree"""
    st.markdown("#### 🌳 Binary Search Tree Visualization")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎲 Generate Random Tree"):
            st.session_state.bst_nodes = np.random.randint(1, 50, 7)
    
    with col2:
        if st.button("🔄 Rotate Tree View"):
            st.session_state.tree_rotation = st.session_state.get('tree_rotation', 0) + 45
    
    # Create tree visualization
    nodes = st.session_state.get('bst_nodes', [25, 15, 35, 10, 20, 30, 40])
    
    # Create a simple tree layout
    fig = go.Figure()
    
    # Add nodes
    for i, node in enumerate(nodes):
        angle = (i * 360 / len(nodes)) + st.session_state.get('tree_rotation', 0)
        x = 2 * math.cos(math.radians(angle))
        y = 2 * math.sin(math.radians(angle))
        
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=40, color=node, colorscale='viridis'),
            text=[str(node)],
            textposition="middle center",
            name=f"Node {node}"
        ))
    
    fig.update_layout(
        title="Interactive Binary Search Tree",
        showlegend=False,
        height=400,
        xaxis=dict(showgrid=False, showticklabels=False),
        yaxis=dict(showgrid=False, showticklabels=False)
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_spiral_matrix():
    """Animated spiral matrix generation"""
    size = st.slider("Matrix Size", 3, 10, 5)
    
    if st.button("🌀 Generate Spiral Matrix", key="spiral"):
        matrix = np.zeros((size, size))
        
        # Spiral generation logic
        top, bottom, left, right = 0, size - 1, 0, size - 1
        num = 1
        
        placeholder = st.empty()
        
        while top <= bottom and left <= right:
            # Fill top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
                
                # Animate the filling
                fig = px.imshow(matrix, text_auto=True, aspect="auto", 
                               color_continuous_scale="viridis")
                fig.update_layout(title=f"Spiral Matrix Generation - Number {num-1}")
                placeholder.plotly_chart(fig, use_container_width=True)
                time.sleep(0.2)
            
            top += 1
            
            # Fill right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
                
                fig = px.imshow(matrix, text_auto=True, aspect="auto",
                               color_continuous_scale="viridis")
                fig.update_layout(title=f"Spiral Matrix Generation - Number {num-1}")
                placeholder.plotly_chart(fig, use_container_width=True)
                time.sleep(0.2)
            
            right -= 1
            
            # Fill bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                    
                    fig = px.imshow(matrix, text_auto=True, aspect="auto",
                                   color_continuous_scale="viridis")
                    fig.update_layout(title=f"Spiral Matrix Generation - Number {num-1}")
                    placeholder.plotly_chart(fig, use_container_width=True)
                    time.sleep(0.2)
                
                bottom -= 1
            
            # Fill left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                    
                    fig = px.imshow(matrix, text_auto=True, aspect="auto",
                                   color_continuous_scale="viridis")
                    fig.update_layout(title=f"Spiral Matrix Generation - Number {num-1}")
                    placeholder.plotly_chart(fig, use_container_width=True)
                    time.sleep(0.2)
                
                left += 1
        
        st.success("🎉 Spiral Matrix Complete!")

def create_fibonacci_spiral():
    """Interactive Fibonacci spiral"""
    if st.button("🌀 Generate Fibonacci Spiral", key="fibonacci"):
        fig = go.Figure()
        
        # Generate Fibonacci sequence
        fib = [1, 1]
        for i in range(8):
            fib.append(fib[-1] + fib[-2])
        
        # Create spiral
        theta = np.linspace(0, 4 * np.pi, 1000)
        r = np.exp(0.3 * theta)
        
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color='gold', width=3),
            name='Fibonacci Spiral'
        ))
        
        # Add Fibonacci numbers as points
        for i, num in enumerate(fib[:8]):
            angle = i * np.pi / 4
            radius = num / 5
            fig.add_trace(go.Scatter(
                x=[radius * np.cos(angle)],
                y=[radius * np.sin(angle)],
                mode='markers+text',
                marker=dict(size=15, color='red'),
                text=[str(num)],
                textposition="middle center",
                name=f"F({i}) = {num}"
            ))
        
        fig.update_layout(
            title="Interactive Fibonacci Spiral",
            showlegend=True,
            height=500,
            xaxis=dict(scaleanchor="y", scaleratio=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)

def create_interactive_skills():
    """Interactive skills section with progress bars and animations"""
    st.markdown('<h2 class="section-header">💪 Interactive Skills Dashboard</h2>', unsafe_allow_html=True)
    
    skills_data = {
        "Programming Languages": {"Python": 95, "JavaScript": 88, "Java": 82, "C++": 75},
        "Web Technologies": {"React": 90, "Node.js": 85, "Django": 88, "Flask": 80},
        "Data Science": {"Machine Learning": 92, "Data Analysis": 90, "Deep Learning": 85, "Statistics": 88},
        "Tools & Platforms": {"AWS": 80, "Docker": 85, "Git": 95, "Linux": 88}
    }
    
    selected_category = st.selectbox("Select Skill Category:", list(skills_data.keys()))
    
    # Animate skill bars
    for skill, level in skills_data[selected_category].items():
        st.markdown(f"**{skill}**")
        progress_placeholder = st.empty()
        
        # Animated progress bar
        for i in range(0, level + 1, 5):
            progress_placeholder.progress(i)
            time.sleep(0.05)
        
        st.markdown(f"Level: {level}%")
        st.markdown("---")

def navigation_sidebar():
    """Create interactive navigation sidebar"""
    st.sidebar.markdown("# 🧭 Navigation")
    
    # Navigation buttons
    pages = ["Home", "Projects", "Skills Lab", "Algorithms", "Contact"]
    
    for page in pages:
        if st.sidebar.button(f"📍 {page}", key=f"nav_{page}"):
            st.session_state.current_page = page
            st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🎮 Interactive Features")
    
    if st.sidebar.button("🎲 Random Color Theme"):
        colors = ["#667eea", "#f093fb", "#4facfe", "#43e97b", "#fa709a"]
        st.session_state.theme_color = np.random.choice(colors)
    
    if st.sidebar.button("🎆 Celebration Mode"):
        st.balloons()
        st.snow()

def render_home_page():
    """Render the home page with animations"""
    # Header Section with rotating element
    st.markdown(f"""
    <div class="main-header">
        <div class="rotating-element" style="display: inline-block; font-size: 2rem;">⚡</div>
        <h1>👨‍💻 John Doe</h1>
        <h3>Interactive Full Stack Developer & Data Scientist</h3>
        <p>Creating innovative solutions with interactive experiences</p>
    </div>
    """, unsafe_allow_html=True)

    # Profile Picture with hover effect
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        try:
            profile_img = Image.open("assets/profile.jpg")
            st.image(profile_img, width=300, caption="Profile Picture")
        except (FileNotFoundError, OSError):
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background-color: #f0f2f6; border-radius: 10px; margin: 1rem 0;" class="pulse-animation">
                <div style="font-size: 4rem;">👨‍💻</div>
                <p style="color: #666; margin-top: 1rem;">Profile Picture</p>
                <small style="color: #999;">Add your profile.jpg to the assets folder</small>
            </div>
            """, unsafe_allow_html=True)

    # Interactive Quick Stats
    st.markdown("### 📊 Interactive Stats Dashboard")
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    stats = [
        ("5+", "Years Experience", "💼"),
        ("20+", "Projects Completed", "🚀"),
        ("10+", "Technologies", "💻"),
        ("100%", "Client Satisfaction", "😊")
    ]
    
    for i, (stat_col, (number, text, emoji)) in enumerate(zip([stat_col1, stat_col2, stat_col3, stat_col4], stats)):
        with stat_col:
            if st.button(f"{emoji} {number}", key=f"stat_{i}"):
                st.balloons()
            st.markdown(f"<p style='text-align: center; margin-top: 0.5rem;'>{text}</p>", unsafe_allow_html=True)

def render_projects_page():
    """Render interactive projects page"""
    st.markdown('<h2 class="section-header">🚀 Interactive Project Showcase</h2>', unsafe_allow_html=True)
    
    project_tabs = st.tabs(["🛒 E-commerce", "📊 Analytics", "🤖 AI Chatbot"])
    
    with project_tabs[0]:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            try:
                project1_img = Image.open("assets/project1.jpg")
                st.image(project1_img, caption="E-commerce Platform")
            except (FileNotFoundError, OSError):
                st.markdown("""
                <div style="text-align: center; padding: 3rem 1rem; background-color: #f0f2f6; border-radius: 8px; margin: 1rem 0;" class="pulse-animation">
                    <div style="font-size: 3rem;">🛒</div>
                    <p style="color: #666; margin: 0.5rem 0;">E-commerce Platform</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 🛒 E-commerce Platform")
            st.markdown("**Technologies:** React, Node.js, MongoDB, Stripe API")
            
            if st.button("🚀 View Live Demo", key="demo1"):
                st.success("🎉 Demo launched! (This would open in a new tab)")
                st.balloons()
            
            if st.button("📋 View Code", key="code1"):
                st.info("📂 GitHub repository opened! (This would redirect to GitHub)")
            
            # Interactive feature showcase
            if st.button("⚡ Show Interactive Features", key="features1"):
                st.markdown("""
                **🔥 Interactive Features:**
                - Real-time cart updates
                - Dynamic product filtering
                - Live chat support
                - One-click checkout
                """)

    with project_tabs[1]:
        st.markdown("### 📊 Data Analytics Dashboard")
        
        # Create interactive demo
        if st.button("🎮 Launch Interactive Demo", key="analytics_demo"):
            # Generate sample data
            dates = pd.date_range('2024-01-01', periods=30, freq='D')
            data = np.random.randn(30).cumsum() + 100
            
            fig = px.line(x=dates, y=data, title="Sample Analytics Dashboard")
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            st.success("🎯 Interactive demo loaded!")

    with project_tabs[2]:
        st.markdown("### 🤖 AI-Powered Chatbot")
        
        if st.button("💬 Chat with AI Demo", key="chatbot_demo"):
            st.chat_message("assistant").write("Hello! I'm an AI assistant. How can I help you today?")
            
            user_input = st.chat_input("Type your message...")
            if user_input:
                st.chat_message("user").write(user_input)
                st.chat_message("assistant").write(f"Thanks for your message: '{user_input}'. This is a demo response!")

def render_skills_lab():
    """Interactive skills laboratory"""
    st.markdown('<h2 class="section-header">🧪 Interactive Skills Laboratory</h2>', unsafe_allow_html=True)
    
    # Skill categories with interactive elements
    skill_categories = st.tabs(["💻 Programming", "🔬 Data Science", "🎨 Creative", "🛠️ Tools"])
    
    with skill_categories[0]:
        st.markdown("### Programming Skills Assessment")
        
        languages = ["Python", "JavaScript", "Java", "C++", "Go"]
        selected_lang = st.selectbox("Test your knowledge in:", languages)
        
        if st.button(f"🎯 Take {selected_lang} Quiz", key=f"quiz_{selected_lang}"):
            st.markdown(f"""
            **{selected_lang} Knowledge Test:**
            
            **Question 1:** What is the time complexity of binary search?
            """)
            
            answer = st.radio("Choose your answer:", ["O(n)", "O(log n)", "O(n²)", "O(1)"], key="q1")
            
            if st.button("Submit Answer", key="submit_quiz"):
                if answer == "O(log n)":
                    st.success("🎉 Correct! You know your algorithms!")
                    st.balloons()
                else:
                    st.error("❌ Incorrect. The answer is O(log n)")

def render_algorithms_page():
    """Interactive algorithms page"""
    st.markdown('<h2 class="section-header">🔄 Interactive Algorithm Visualizations</h2>', unsafe_allow_html=True)
    
    create_rotating_algorithm_viz()

def render_contact_page():
    """Interactive contact page"""
    st.markdown('<h2 class="section-header">📬 Interactive Contact Hub</h2>', unsafe_allow_html=True)
    
    contact_col1, contact_col2 = st.columns([1, 1])
    
    with contact_col1:
        st.markdown("### 📞 Connect With Me")
        
        # Interactive contact buttons
        if st.button("📧 Send Email", key="email_btn"):
            st.success("✉️ Email client opened! (mailto:john.doe@email.com)")
        
        if st.button("💼 LinkedIn Profile", key="linkedin_btn"):
            st.success("🔗 LinkedIn opened in new tab!")
        
        if st.button("💻 GitHub Portfolio", key="github_btn"):
            st.success("🐱 GitHub profile opened!")
        
        if st.button("📱 Schedule Call", key="call_btn"):
            st.success("📅 Calendar booking opened!")
    
    with contact_col2:
        st.markdown("### 💌 Quick Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            
            submitted = st.form_submit_button("🚀 Send Message")
            
            if submitted:
                if name and email and message:
                    st.success("🎉 Message sent successfully!")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all fields")

def main():
    """Main application with navigation"""
    # Navigation sidebar
    navigation_sidebar()
    
    # Render current page
    if st.session_state.current_page == "Home":
        render_home_page()
    elif st.session_state.current_page == "Projects":
        render_projects_page()
    elif st.session_state.current_page == "Skills Lab":
        render_skills_lab()
    elif st.session_state.current_page == "Algorithms":
        render_algorithms_page()
    elif st.session_state.current_page == "Contact":
        render_contact_page()
    
    # Footer with interactive elements
    st.markdown("---")
    footer_col1, footer_col2, footer_col3 = st.columns(3)
    
    with footer_col1:
        if st.button("🎨 Change Theme"):
            st.success("🎨 Theme changed! (Demo)")
    
    with footer_col2:
        if st.button("📊 View Analytics"):
            st.info("📈 Portfolio analytics: 1,234 views this month!")
    
    with footer_col3:
        if st.button("💝 Give Feedback"):
            st.success("💌 Feedback form opened!")
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <p>© 2024 John Doe. Built with ❤️ using Streamlit</p>
        <p>✨ Interactive Portfolio - Click, Explore, Enjoy! ✨</p>
    </div>
    """, unsafe_allow_html=True)

# Required import for pandas (used in projects demo)
import pandas as pd

if __name__ == "__main__":
    main()
