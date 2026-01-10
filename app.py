import streamlit as st

st.set_page_config(page_title="Judy Zhao", page_icon="📊", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Experience", "Projects", "Skills", "Contact"])

# HOME PAGE
if page == "Home":
    st.title("Hi, I'm Judy 👋")
    st.write("""
    I'm a business and finance student with interests in data analysis, financial markets, 
    and understanding how businesses make decisions.  
    This site is where I share my experience, projects, and what I'm learning.
    """)
    st.image("https://via.placeholder.com/800x200?text=Your+Hero+Banner+Here", use_container_width=True)

# EXPERIENCE PAGE
elif page == "Experience":
    st.title("Experience")
    with st.expander("💼 Finance / Business Roles"):
        st.write("""
        **Role Name** — Company  
        *Month Year – Month Year*  
        - Bullet point describing what you did  
        - Another bullet point  
        """)

    with st.expander("🛠 Other Work"):
        st.write("""
        **Job Title** — Company  
        *Month Year – Month Year*  
        - Bullet point  
        - Bullet point  
        """)

# PROJECTS PAGE
elif page == "Projects":
    st.title("Projects")
    st.write("Here are a few things I’ve worked on:")

    st.subheader("📊 Project Name")
    st.write("""
    Short description of what the project was about.
    - What tools you used  
    - What you learned  
    """)

# SKILLS PAGE
elif page == "Skills":
    st.title("Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Finance")
        st.write("- Financial analysis\n- Budgeting\n- Forecasting")

    with col2:
        st.subheader("Tools & Tech")
        st.write("- Excel / Sheets\n- Python\n- Tableau\n- SQL")

# CONTACT PAGE
elif page == "Contact":
    st.title("Contact")
    st.write("📧 Email: judyzhaoyu@gmail.com")
    st.write("🔗 LinkedIn: https://linkedin.com/in/yourprofile")
