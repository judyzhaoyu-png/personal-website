import streamlit as st

st.set_page_config(page_title="Judy Zhao", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Experience", "Projects", "Skills", "Contact"])

# HOME PAGE
if page == "Home":
    st.title("Hi, I'm Judy 👋")
    st.write("""
    I'm a business and finance new grad, but this site exists because there is a real person behind these applications.
    """)

# EXPERIENCE PAGE
elif page == "Experience":
    st.title("Experience")
    with st.expander("Work Experience"):
        st.write("""
        **Server** - Lake Bonavista Retirement  
        *Dec 2025 - Present*  
        - Manage high-volume, time-sensitive service workflows for 200+ residents per shift, prioritizing tasks to ensure accuracy,
        efficiency, and consistent service delivery in a regulated environment
        - Another bullet point  
        """)

    with st.expander("🛠 Other Work"):
        st.write("""
        **Server** - Lake Bonavista Retirement  
        *Dec 2025 - Present*  
        - Manage high-volume, time-sensitive service workflows for 200+ residents per shift, prioritizing tasks to ensure accuracy, efficiency,
         and consistent service delivery in a regulated environment
        - Process and retain multiple concurrent, demonstrating strong short-term memory, attention to detail, and error prevention under pressure
        - Execute efficient task batching and time estimation by delivering multiple items per run, reducing delays and optimizing operational throughput
        - Continuously monitor service status and anticipate needs through real-time scanning of tables and dining areas, enabling proactive refills,
        timely dessert delivery, and issue prevention
        - Maintain accurate handling of dietary requirements, allergies, and special accommodations, reinforcing compliance standards 
        and minimizing operational and safety risk
        - Support team productivity by restocking supplies and assisting colleagues to ensure uninterrupted service flow and operational continuity
        - Navigate challenging client interactions with professionalism and emotional control, remaining calm and solution-oriented when residents experience confusion,
        sensory limitations, or sudden behavioral changes.
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
    st.write("🔗 LinkedIn: http://www.linkedin.com/in/judyzhaoyu")





