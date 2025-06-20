import streamlit as st
from pathlib import Path
from PIL import Image

# --- Path settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile.jpg"

# --- Load resources ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_image = Image.open(profile_pic)

# --- Page Config ---
st.set_page_config(page_title="My Resume Portfolio", page_icon="📄", layout="wide")

# --- Sidebar ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# --- Header Section ---
if page == "Home":
    st.image(profile_image, width=150)
    st.title("Sanjeev ")
    st.subheader(" Intern @ AMCAP BIZON")

    st.write("Welcome to my portfolio! I'm passionate about cloud computing, Python development, and building intelligent apps with AI.")
    st.download_button(
        label="📄 Download My Resume",
        data=PDFbyte,
        file_name="Sanjeev_Kumar_Resume.pdf",
        mime="application/pdf",
    )

    st.markdown("---")
    st.header("Skills")
    st.write("""
    - 🐍 Python (Streamlit, Pandas, APIs)
    - ☁️ AWS (Cloud Practitioner)
    - 🖥️ Web (HTML, CSS, JS Basics)
    - 🧠 Problem Solving & Aptitude
    - 🛠️ Tools: Git, VS Code, Cisco Packet Tracer
    """)

    st.markdown("---")
    st.header("Education")
    st.write("**B.Sc. [Your Major]**, [Your College] (YYYY - YYYY)")
    st.write("Relevant Courses: Data Structures, Networking, Cloud Basics")

# --- Projects Section ---
elif page == "Projects":
    st.header("My Projects")

    st.subheader("AI Trip Planner")
    st.write("A smart travel assistant using Python + Streamlit to plan trips, estimate budget, and recommend hotels.")
    st.markdown("[🔗 View Project Repo](https://github.com/your-username/ai-trip-planner)")

    st.subheader("Hospital Network Simulation")
    st.write("Designed and simulated a secure hospital network using VLANs, inter-VLAN routing, ACLs, and server configurations.")
    st.markdown("[🔗 View Report/Code](https://github.com/your-username/hospital-network-project)")

# --- Contact Section ---
elif page == "Contact":
    st.header("Let's Connect!")

    st.write("📧 Email: [your.email@example.com](mailto:your.email@example.com)")
    st.write("💼 LinkedIn: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)")
    st.write("🐙 GitHub: [github.com/your-username](https://github.com/your-username)")
