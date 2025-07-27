import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Your Name - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
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
    }
    
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #2E86AB;
    }
    
    .contact-form {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    
    .download-button {
        background-color: #2E86AB;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        text-decoration: none;
        display: inline-block;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def create_download_link(file_path, download_filename):
    """Create a download link for files"""
    try:
        with open(file_path, "rb") as f:
            bytes_data = f.read()
        b64 = base64.b64encode(bytes_data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{download_filename}" class="download-button">📄 Download Resume</a>'
        return href
    except (FileNotFoundError, OSError):
        return '''
        <div style="padding: 1rem; background-color: #fff3cd; border-radius: 8px; border-left: 4px solid #ffc107;">
            <p style="margin: 0; color: #856404;">
                📄 <strong>Resume Download:</strong> Add your resume.pdf file to the assets folder to enable download functionality.
            </p>
        </div>
        '''

def main():
    # Header Section
    st.markdown("""
    <div class="main-header">
        <h1>👨‍💻 John Doe</h1>
        <h3>Full Stack Developer & Data Scientist</h3>
        <p>Passionate about creating innovative solutions and turning data into insights</p>
    </div>
    """, unsafe_allow_html=True)

    # Profile Picture and Quick Stats
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        try:
            profile_img = Image.open("assets/profile.jpg")
            st.image(profile_img, width=300, caption="Profile Picture")
        except (FileNotFoundError, OSError):
            # Display a placeholder if image is not found
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background-color: #f0f2f6; border-radius: 10px; margin: 1rem 0;">
                <div style="font-size: 4rem;">👨‍💻</div>
                <p style="color: #666; margin-top: 1rem;">Profile Picture</p>
                <small style="color: #999;">Add your profile.jpg to the assets folder</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("### 📊 Quick Stats")
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    with stat_col1:
        st.markdown("""
        <div class="stats-card">
            <h3>5+</h3>
            <p>Years Experience</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stat_col2:
        st.markdown("""
        <div class="stats-card">
            <h3>20+</h3>
            <p>Projects Completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stat_col3:
        st.markdown("""
        <div class="stats-card">
            <h3>10+</h3>
            <p>Technologies</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stat_col4:
        st.markdown("""
        <div class="stats-card">
            <h3>100%</h3>
            <p>Client Satisfaction</p>
        </div>
        """, unsafe_allow_html=True)

    # About Me Section
    st.markdown('<h2 class="section-header">🙋‍♂️ About Me</h2>', unsafe_allow_html=True)
    
    about_col1, about_col2 = st.columns([2, 1])
    
    with about_col1:
        st.markdown("""
        Welcome to my portfolio! I'm a passionate Full Stack Developer and Data Scientist with over 5 years of experience 
        in creating innovative web applications and extracting meaningful insights from complex datasets.

        **🎓 Education:**
        - Master's in Computer Science - Stanford University (2019)
        - Bachelor's in Software Engineering - UC Berkeley (2017)

        **💼 Background:**
        I've worked with startups and Fortune 500 companies, helping them build scalable applications and implement 
        data-driven solutions. My expertise spans from frontend development with modern frameworks to backend systems 
        and machine learning models.

        **🎯 Interests:**
        - Artificial Intelligence & Machine Learning
        - Web Development & Cloud Computing  
        - Open Source Contributions
        - Photography & Travel
        """)
    
    with about_col2:
        st.markdown("### 🏆 Achievements")
        st.markdown("""
        - 🥇 Best Innovation Award 2023
        - 📱 Published 3 mobile apps
        - 🌟 5k+ GitHub stars
        - 📝 Tech blogger with 50k+ readers
        - 🎤 Speaker at 10+ conferences
        """)

    # Skills Section
    st.markdown('<h2 class="section-header">💪 Skills</h2>', unsafe_allow_html=True)
    
    skill_col1, skill_col2, skill_col3 = st.columns(3)
    
    with skill_col1:
        st.markdown("#### 💻 Technical Skills")
        technical_skills = [
            "Python", "JavaScript", "React", "Node.js", "Django", "Flask",
            "PostgreSQL", "MongoDB", "AWS", "Docker", "Kubernetes"
        ]
        for skill in technical_skills:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with skill_col2:
        st.markdown("#### 🔬 Research & Analytics")
        research_skills = [
            "Machine Learning", "Deep Learning", "Data Analysis", "Statistics",
            "TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn"
        ]
        for skill in research_skills:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with skill_col3:
        st.markdown("#### 🤝 Soft Skills")
        soft_skills = [
            "Team Leadership", "Project Management", "Communication",
            "Problem Solving", "Critical Thinking", "Adaptability"
        ]
        for skill in soft_skills:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

    # Projects Section
    st.markdown('<h2 class="section-header">🚀 Featured Projects</h2>', unsafe_allow_html=True)
    
    # Project 1
    proj_col1, proj_col2 = st.columns([1, 2])
    
    with proj_col1:
        try:
            project1_img = Image.open("assets/project1.jpg")
            st.image(project1_img, caption="E-commerce Platform")
        except (FileNotFoundError, OSError):
            # Display a placeholder image
            st.markdown("""
            <div style="text-align: center; padding: 3rem 1rem; background-color: #f0f2f6; border-radius: 8px; margin: 1rem 0;">
                <div style="font-size: 3rem;">🛒</div>
                <p style="color: #666; margin: 0.5rem 0;">E-commerce Platform</p>
            </div>
            """, unsafe_allow_html=True)
    
    with proj_col2:
        st.markdown("""
        <div class="project-card">
            <h3>🛒 E-commerce Platform</h3>
            <p><strong>Technologies:</strong> React, Node.js, MongoDB, Stripe API</p>
            <p>A full-stack e-commerce solution with advanced features including real-time inventory management, 
            payment processing, and admin dashboard. Implemented responsive design and optimized for mobile devices.</p>
            <p><strong>Key Features:</strong></p>
            <ul>
                <li>User authentication and authorization</li>
                <li>Shopping cart and wishlist functionality</li>
                <li>Payment gateway integration</li>
                <li>Order tracking and management</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Project 2
    proj2_col1, proj2_col2 = st.columns([2, 1])
    
    with proj2_col1:
        st.markdown("""
        <div class="project-card">
            <h3>📊 Data Analytics Dashboard</h3>
            <p><strong>Technologies:</strong> Python, Streamlit, Plotly, Pandas</p>
            <p>An interactive dashboard for business intelligence that processes large datasets and provides 
            real-time insights through dynamic visualizations. Features include data filtering, export capabilities, 
            and automated reporting.</p>
            <p><strong>Key Features:</strong></p>
            <ul>
                <li>Real-time data processing</li>
                <li>Interactive charts and graphs</li>
                <li>Automated report generation</li>
                <li>Multi-format data export</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with proj2_col2:
        try:
            project2_img = Image.open("assets/project2.jpg")
            st.image(project2_img, caption="Analytics Dashboard")
        except (FileNotFoundError, OSError):
            # Display a placeholder image
            st.markdown("""
            <div style="text-align: center; padding: 3rem 1rem; background-color: #f0f2f6; border-radius: 8px; margin: 1rem 0;">
                <div style="font-size: 3rem;">📊</div>
                <p style="color: #666; margin: 0.5rem 0;">Analytics Dashboard</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Project 3
    proj3_col1, proj3_col2 = st.columns([1, 2])
    
    with proj3_col1:
        try:
            project3_img = Image.open("assets/project3.jpg")
            st.image(project3_img, caption="AI Chatbot")
        except (FileNotFoundError, OSError):
            # Display a placeholder image
            st.markdown("""
            <div style="text-align: center; padding: 3rem 1rem; background-color: #f0f2f6; border-radius: 8px; margin: 1rem 0;">
                <div style="font-size: 3rem;">🤖</div>
                <p style="color: #666; margin: 0.5rem 0;">AI Chatbot</p>
            </div>
            """, unsafe_allow_html=True)
    
    with proj3_col2:
        st.markdown("""
        <div class="project-card">
            <h3>🤖 AI-Powered Chatbot</h3>
            <p><strong>Technologies:</strong> Python, TensorFlow, NLP, Flask</p>
            <p>An intelligent chatbot system using natural language processing and machine learning. 
            Capable of handling customer queries, providing product recommendations, and learning from interactions.</p>
            <p><strong>Key Features:</strong></p>
            <ul>
                <li>Natural language understanding</li>
                <li>Context-aware responses</li>
                <li>Multi-language support</li>
                <li>Continuous learning capability</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Resume Download Section
    st.markdown('<h2 class="section-header">📄 Resume</h2>', unsafe_allow_html=True)
    
    resume_col1, resume_col2 = st.columns([2, 1])
    
    with resume_col1:
        st.markdown("""
        Download my detailed resume to learn more about my experience, education, and accomplishments. 
        The resume includes comprehensive information about my technical skills, work history, and notable projects.
        """)
        
        # Create download link
        download_link = create_download_link("assets/resume.pdf", "John_Doe_Resume.pdf")
        st.markdown(download_link, unsafe_allow_html=True)
    
    with resume_col2:
        st.info("💡 **Tip:** Keep your resume updated regularly and tailor it for specific opportunities!")

    # Contact Section
    st.markdown('<h2 class="section-header">📬 Contact Me</h2>', unsafe_allow_html=True)
    
    contact_col1, contact_col2 = st.columns([1, 1])
    
    with contact_col1:
        st.markdown("### 📞 Get In Touch")
        st.markdown("""
        **📧 Email:** john.doe@email.com  
        **📱 Phone:** +1 (555) 123-4567  
        **🌐 LinkedIn:** [linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)  
        **💻 GitHub:** [github.com/johndoe](https://github.com/johndoe)  
        **🐦 Twitter:** [@johndoe](https://twitter.com/johndoe)
        
        **📍 Location:** San Francisco, CA  
        **🕒 Availability:** Open to new opportunities
        """)
    
    with contact_col2:
        st.markdown("### 💌 Send a Message")
        
        # Contact Form using FormSubmit
        st.markdown("""
        <div class="contact-form">
            <form action="https://formsubmit.co/your-email@email.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="_next" value="https://yourdomain.com/thanks.html">
                
                <div style="margin-bottom: 1rem;">
                    <label for="name" style="display: block; margin-bottom: 0.5rem; font-weight: bold;">Name:</label>
                    <input type="text" name="name" required style="width: 100%; padding: 0.75rem; border: 1px solid #ddd; border-radius: 5px;">
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label for="email" style="display: block; margin-bottom: 0.5rem; font-weight: bold;">Email:</label>
                    <input type="email" name="email" required style="width: 100%; padding: 0.75rem; border: 1px solid #ddd; border-radius: 5px;">
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label for="subject" style="display: block; margin-bottom: 0.5rem; font-weight: bold;">Subject:</label>
                    <input type="text" name="subject" required style="width: 100%; padding: 0.75rem; border: 1px solid #ddd; border-radius: 5px;">
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label for="message" style="display: block; margin-bottom: 0.5rem; font-weight: bold;">Message:</label>
                    <textarea name="message" rows="5" required style="width: 100%; padding: 0.75rem; border: 1px solid #ddd; border-radius: 5px; resize: vertical;"></textarea>
                </div>
                
                <button type="submit" style="background-color: #2E86AB; color: white; padding: 0.75rem 1.5rem; border: none; border-radius: 25px; cursor: pointer; font-size: 1rem;">
                    Send Message 📨
                </button>
            </form>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <p>© 2024 John Doe. Built with ❤️ using Streamlit</p>
        <p>Thank you for visiting my portfolio!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
