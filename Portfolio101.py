import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import numpy as np
import time
import math
import pandas as pd

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
    
    .algorithm-viz {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 2px solid #2E86AB;
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
    """Create an interactive rotating algorithm visualization using Streamlit native components"""
    st.markdown("### 🔄 Interactive Algorithm Visualization")
    
    # Algorithm selection
    algorithm = st.selectbox(
        "Choose Algorithm to Visualize:",
        ["Bubble Sort", "Number Pattern", "Spiral Matrix", "Fibonacci Sequence"]
    )
    
    if algorithm == "Bubble Sort":
        create_bubble_sort_animation()
    elif algorithm == "Number Pattern":
        create_number_pattern()
    elif algorithm == "Spiral Matrix":
        create_spiral_matrix()
    elif algorithm == "Fibonacci Sequence":
        create_fibonacci_sequence()

def create_bubble_sort_animation():
    """Animated bubble sort visualization using Streamlit bar chart"""
    st.markdown('<div class="algorithm-viz">', unsafe_allow_html=True)
    
    if st.button("🚀 Start Bubble Sort Animation", key="bubble_sort"):
        data = np.random.randint(1, 100, 10)
        chart_placeholder = st.empty()
        progress_bar = st.progress(0)
        
        total_steps = 0
        n = len(data)
        
        # Calculate total steps for progress bar
        for i in range(n):
            for j in range(0, n - i - 1):
                total_steps += 1
        
        current_step = 0
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                
                # Create DataFrame for bar chart
                df = pd.DataFrame({
                    'Position': list(range(len(data))),
                    'Value': data
                })
                
                chart_placeholder.bar_chart(df.set_index('Position')['Value'])
                progress_bar.progress((current_step + 1) / total_steps)
                current_step += 1
                time.sleep(0.1)
        
        st.success("✅ Sorting Complete!")
        st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_number_pattern():
    """Interactive number pattern visualization"""
    st.markdown('<div class="algorithm-viz">', unsafe_allow_html=True)
    pattern_type = st.selectbox("Choose Pattern:", ["Pascal's Triangle", "Multiplication Table", "Prime Spiral"])
    
    if pattern_type == "Pascal's Triangle":
        rows = st.slider("Number of rows:", 3, 10, 5)
        if st.button("🔺 Generate Pascal's Triangle", key="pascal"):
            triangle = []
            for i in range(rows):
                row = [1] * (i + 1)
                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
                triangle.append(row)
            
            # Display triangle
            for i, row in enumerate(triangle):
                spaces = "   " * (rows - i - 1)
                numbers = "   ".join(f"{num:2d}" for num in row)
                st.code(f"{spaces}{numbers}")
    
    elif pattern_type == "Multiplication Table":
        size = st.slider("Table size:", 3, 12, 5)
        if st.button("✖️ Generate Table", key="mult_table"):
            # Create multiplication table
            data = []
            for i in range(1, size + 1):
                row = []
                for j in range(1, size + 1):
                    row.append(i * j)
                data.append(row)
            
            df = pd.DataFrame(data, 
                            index=[f"Row {i}" for i in range(1, size + 1)],
                            columns=[f"Col {j}" for j in range(1, size + 1)])
            st.dataframe(df, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_spiral_matrix():
    """Animated spiral matrix generation using DataFrame display"""
    st.markdown('<div class="algorithm-viz">', unsafe_allow_html=True)
    size = st.slider("Matrix Size", 3, 8, 4)
    
    if st.button("🌀 Generate Spiral Matrix", key="spiral"):
        matrix = np.zeros((size, size), dtype=int)
        
        # Spiral generation logic
        top, bottom, left, right = 0, size - 1, 0, size - 1
        num = 1
        
        placeholder = st.empty()
        progress = st.progress(0)
        total_elements = size * size
        
        while top <= bottom and left <= right:
            # Fill top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
                
                # Show current state
                df = pd.DataFrame(matrix)
                placeholder.dataframe(df, use_container_width=True)
                progress.progress(num / total_elements)
                time.sleep(0.3)
            
            top += 1
            
            # Fill right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
                
                df = pd.DataFrame(matrix)
                placeholder.dataframe(df, use_container_width=True)
                progress.progress(num / total_elements)
                time.sleep(0.3)
            
            right -= 1
            
            # Fill bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                    
                    df = pd.DataFrame(matrix)
                    placeholder.dataframe(df, use_container_width=True)
                    progress.progress(num / total_elements)
                    time.sleep(0.3)
                
                bottom -= 1
            
            # Fill left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                    
                    df = pd.DataFrame(matrix)
                    placeholder.dataframe(df, use_container_width=True)
                    progress.progress(num / total_elements)
                    time.sleep(0.3)
                
                left += 1
        
        st.success("🎉 Spiral Matrix Complete!")
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_fibonacci_sequence():
    """Interactive Fibonacci sequence with visualization"""
    st.markdown('<div class="algorithm-viz">', unsafe_allow_html=True)
    
    if st.button("🌀 Generate Fibonacci Sequence", key="fibonacci"):
        n = st.slider("Number of terms:", 5, 20, 10)
        
        # Generate Fibonacci sequence
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        
        # Display sequence with animation
        sequence_placeholder = st.empty()
        chart_placeholder = st.empty()
        
        for i in range(2, len(fib)):
            current_fib = fib[:i+1]
            
            # Show current sequence
            sequence_placeholder.write(f"**Fibonacci Sequence:** {current_fib}")
            
            # Create chart data
            df = pd.DataFrame({
                'Index': list(range(len(current_fib))),
                'Fibonacci': current_fib
            })
            
            chart_placeholder.line_chart(df.set_index('Index')['Fibonacci'])
            time.sleep(0.5)
        
        # Show golden ratio approximation
        if len(fib) > 2:
            ratios = [fib[i] / fib[i-1] for i in range(2, len(fib))]
            st.write(f"**Golden Ratio Approximation:** {ratios[-1]:.6f}")
            st.write(f"**Actual Golden Ratio:** {(1 + math.sqrt(5)) / 2:.6f}")
    
    st.markdown('</div>', unsafe_allow_html=True)

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
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{skill}**")
            st.progress(level / 100)
        with col2:
            st.metric("Level", f"{level}%")

def navigation_sidebar():
    """Create interactive navigation sidebar"""
    st.sidebar.markdown("# 🧭 Navigation")
    
    # Navigation buttons
    pages = ["🏠 Home", "🚀 Projects", "🧪 Skills Lab", "🔄 Algorithms", "📬 Contact"]
    
    for page in pages:
        page_name = page.split(" ", 1)[1]  # Remove emoji for session state
        if st.sidebar.button(page, key=f"nav_{page_name}"):
            st.session_state.current_page = page_name
            st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🎮 Interactive Features")
    
    if st.sidebar.button("🎲 Random Fact"):
        facts = [
            "🐍 Python was named after Monty Python!",
            "🌐 The first website is still online!",
            "💾 1 GB used to cost $10,000 in 1981!",
            "🤖 AI can now write poetry and code!",
            "🚀 There are over 8 billion devices connected to the internet!"
        ]
        st.sidebar.success(np.random.choice(facts))
    
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

    # About Me Section
    st.markdown('<h2 class="section-header">🙋‍♂️ About Me</h2>', unsafe_allow_html=True)
    
    about_col1, about_col2 = st.columns([2, 1])
    
    with about_col1:
        st.markdown("""
        Welcome to my interactive portfolio! I'm a passionate Full Stack Developer and Data Scientist with over 5 years of experience 
        in creating innovative web applications and extracting meaningful insights from complex datasets.

        **🎓 Education:**
        - Master's in Computer Science - Stanford University (2019)
        - Bachelor's in Software Engineering - UC Berkeley (2017)

        **💼 Background:**
        I've worked with startups and Fortune 500 companies, helping them build scalable applications and implement 
        data-driven solutions. My expertise spans from frontend development to backend systems and machine learning models.
        """)
    
    with about_col2:
        st.markdown("### 🏆 Achievements")
        achievements = [
            "🥇 Best Innovation Award 2023",
            "📱 Published 3 mobile apps",
            "🌟 5k+ GitHub stars",
            "📝 Tech blogger with 50k+ readers",
            "🎤 Speaker at 10+ conferences"
        ]
        
        for achievement in achievements:
            if st.button(achievement, key=f"achieve_{achievement}"):
                st.success(f"Thanks for your interest in: {achievement}")

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
                features = [
                    "✅ Real-time cart updates",
                    "✅ Dynamic product filtering", 
                    "✅ Live chat support",
                    "✅ One-click checkout"
                ]
                for feature in features:
                    st.write(feature)

    with project_tabs[1]:
        st.markdown("### 📊 Data Analytics Dashboard")
        
        # Create interactive demo
        if st.button("🎮 Launch Interactive Demo", key="analytics_demo"):
            # Generate sample data
            dates = pd.date_range('2024-01-01', periods=30, freq='D')
            data = np.random.randn(30).cumsum() + 100
            
            df = pd.DataFrame({'Date': dates, 'Value': data})
            st.line_chart(df.set_index('Date')['Value'])
            
            st.success("🎯 Interactive demo loaded!")

    with project_tabs[2]:
        st.markdown("### 🤖 AI-Powered Chatbot")
        
        if st.button("💬 Chat with AI Demo", key="chatbot_demo"):
            st.chat_message("assistant").write("Hello! I'm an AI assistant. How can I help you today?")
            
            user_input = st.chat_input("Type your message...")
            if user_input:
                st.chat_message("user").write(user_input)
                responses = [
                    f"Thanks for your message: '{user_input}'. That's interesting!",
                    f"I understand you mentioned '{user_input}'. How can I help with that?",
                    f"Great question about '{user_input}'! Let me think about that.",
                ]
                st.chat_message("assistant").write(np.random.choice(responses))

def render_skills_lab():
    """Interactive skills laboratory"""
    st.markdown('<h2 class="section-header">🧪 Interactive Skills Laboratory</h2>', unsafe_allow_html=True)
    
    create_interactive_skills()
    
    # Add interactive quiz section
    st.markdown("---")
    st.markdown("### 🎯 Quick Knowledge Quiz")
    
    questions = {
        "What is the time complexity of binary search?": {
            "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
            "correct": "O(log n)"
        },
        "Which Python framework is best for web development?": {
            "options": ["Django", "Flask", "FastAPI", "All are good choices"],
            "correct": "All are good choices"
        },
        "What does API stand for?": {
            "options": ["Application Programming Interface", "Advanced Program Integration", "Automated Process Integration", "Application Process Interface"],
            "correct": "Application Programming Interface"
        }
    }
    
    question = st.selectbox("Choose a question:", list(questions.keys()))
    answer = st.radio("Your answer:", questions[question]["options"])
    
    if st.button("Submit Answer", key="quiz_submit"):
        if answer == questions[question]["correct"]:
            st.success("🎉 Correct! Well done!")
            st.balloons()
        else:
            st.error(f"❌ Incorrect. The correct answer is: {questions[question]['correct']}")

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
        contact_methods = [
            ("📧 Send Email", "✉️ Email client opened! (mailto:john.doe@email.com)"),
            ("💼 LinkedIn Profile", "🔗 LinkedIn opened in new tab!"),
            ("💻 GitHub Portfolio", "🐱 GitHub profile opened!"),
            ("📱 Schedule Call", "📅 Calendar booking opened!")
        ]
        
        for button_text, success_msg in contact_methods:
            if st.button(button_text, key=f"contact_{button_text}"):
                st.success(success_msg)
    
    with contact_col2:
        st.markdown("### 💌 Quick Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.selectbox("Subject", ["General Inquiry", "Job Opportunity", "Collaboration", "Other"])
            message = st.text_area("Your Message")
            
            submitted = st.form_submit_button("🚀 Send Message")
            
            if submitted:
                if name and email and message:
                    st.success("🎉 Message sent successfully!")
                    st.balloons()
                    
                    # Show confirmation details
                    with st.expander("📋 Message Details"):
                        st.write(f"**Name:** {name}")
                        st.write(f"**Email:** {email}")
                        st.write(f"**Subject:** {subject}")
                        st.write(f"**Message:** {message}")
                else:
                    st.error("❌ Please fill in all required fields")

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
            themes = ["🌞 Light Mode", "🌙 Dark Mode", "🌈 Colorful", "💼 Professional"]
            st.success(f"🎨 Theme changed to: {np.random.choice(themes)}")
    
    with footer_col2:
        if st.button("📊 View Analytics"):
            st.info("📈 Portfolio analytics: 1,234 views this month!")
            
            # Show fake analytics
            with st.expander("📊 Detailed Analytics"):
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Views", "1,234", "12%")
                col2.metric("Unique Visitors", "892", "8%")
                col3.metric("Avg. Time", "3m 45s", "15%")
    
    with footer_col3:
        if st.button("💝 Give Feedback"):
            st.success("💌 Thank you for your interest in providing feedback!")
            
            with st.expander("💬 Quick Feedback"):
                rating = st.select_slider("Rate this portfolio:", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
                if st.button("Submit Rating"):
                    st.success(f"Thanks for the {rating} rating!")
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <p>© 2024 John Doe. Built with ❤️ using Streamlit</p>
        <p>✨ Interactive Portfolio - Click, Explore, Enjoy! ✨</p>
    </div>
    ""
