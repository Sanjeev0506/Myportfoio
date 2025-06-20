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
st.set_page_config(
    page_title="Sanjeev - Resume Portfolio",
    page_icon="🧑‍💻",
    layout="wide"
)

# --- Sidebar ---
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📁 Projects", "📫 Contact"])

# --- Header Section ---
if page == "🏠 Home":
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(profile_image, width=150)
    with col2:
        st.title("Sanjeev")
        st.subheader("Aspiring Cloud Engineer | Python Enthusiast | Intern @ AMCAP BIZON")
        st.write("Welcome to my portfolio! I'm passionate about cloud computing, Python development, and building intelligent apps with AI.")
        st.download_button(
            label="📄 Download My Resume",
            data=PDFbyte,
            file_name="Sanjeev_Resume.pdf",
            mime="application/pdf",
        )

    st.markdown("---")
    st.header("🧠 Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.write("- 🐍 Python (Streamlit,APIs)")
        st.write("- ☁️ AWS (Cloud Practitioner)")
        st.write("- 🛠️ Tools: Git, VS Code, Packet Tracer")
    with col2:
        st.write("- 🌐 Web Basics: HTML, CSS, JS")
        st.write("- 🧠 Problem Solving & Aptitude")
        st.write("- 🔧 Linux, Networking")

    st.markdown("---")
    st.header("🎓 Education")
    st.write("**B.Tech Electronics and Communincation Engineering*, AVV 2026 ")
    st.write("Relevant Courses: Data Structures, Networking, Cloud Basics")

# --- Projects Section ---
elif page == "📁 Projects":
    st.header("🛠️ My Projects")

    with st.expander("🧳 AI Trip Planner"):
        st.write("A smart travel assistant using Python + Streamlit to plan trips, estimate budget, and recommend hotels.")
        st.markdown("[🔗 View Project Repo](https://github.com/your-username/ai-trip-planner)")

    with st.expander("🏥 Hospital Network Simulation"):
        st.write("Designed and simulated a secure hospital network using VLANs, inter-VLAN routing, ACLs, and server configurations.")
        st.markdown("[🔗 View Report/Code](https://github.com/your-username/hospital-network-project)")

# --- Contact Section ---
elif page == "📫 Contact":
    st.header("📫 Let's Connect!")

    st.write("📧 Email: [sanjeevb0506@gmail.com](mailto:sanjeevb0506@gmail.com)")
    st.write("💼 LinkedIn: [linkedin.com/in/yourname](https://www.linkedin.com/in/sanjeevb1412/)")
    st.write("🐙 GitHub: [github.com/your-Sanjeev0506](https://github.com/Sanjeev0506)")

    st.markdown("---")
    st.markdown("Feel free to reach out for collaboration, questions, or opportunities! ✨")
