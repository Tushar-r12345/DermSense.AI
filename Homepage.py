from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "skin.jpg"
diagnoser_tool = current_dir / "pages" / "4_🔬_Diagnoser.py"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "DermSense.AI | Skin disease classifier"
PAGE_ICON = ":skin:"
PAGE_COLOR="dark"
NAME = "DermSense.AI"
DESCRIPTION = """
Transforming Skin Understanding with Machine Wisdom.
"""
EMAIL = "paltushar35@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/@Tushar_zi6ei",
    "LinkedIn": "https://www.linkedin.com/in/tushar-pal-7494b5203/",
    "GitHub": "https://github.com/Tushar-r12345",
    "Twitter": "https://twitter.com/Tushar48923527",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.title(NAME)
    st.write(DESCRIPTION)
    # st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
# st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})",unsafe_allow_html=True)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Our Vision")
st.write(
    """
- ✔️ Swift and accurate skin condition identification using machine learning
- ✔️ AI-powered virtual consultations for quick and convenient expert insights
- ✔️ Prioritizing user privacy and ensuring robust data security
- ✔️ Making advanced skincare insights available to a broad user base
- ✔️ Providing easy-to-understand information to enhance skin health awareness
- ✔️ Leading the charge in transforming skincare through innovative AI solutions
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("About Us")
st.write("---")

# --- JOB 1
st.write("🧬", "**About Us**")
st.write(
    """
- ► Empowering individuals to understand, embrace, and nurture their skin's unique story through the lens of artificial intelligence, fostering confidence and well-being. 
- ► Striving to redefine skincare through the power of artificial intelligence, unlocking the secrets of the skin to inspire self-care journeys and transform lives.
"""
)

# --- JOB 2
st.write('\n')
st.write("🔬", "**Advanced Classification Technology**")
st.write(
    """
- ► Develop a deep learning model that can classify images of skin into different categories, such as vitiligo, pigmentation issues, eczema, and normal skin. 
- ► Create a system that takes input images of affected skin areas and provides a probable diagnosis along with suggested treatments or skincare routines.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚑", "**Collaborative Approach**")
st.write(
    """
- ► Committed to continuous research and development, ensuring that the classification technology stays at the forefront of advancements in the field of dermatology.
- ► Integrating advanced classification technology seamlessly into user-friendly platforms, making it accessible and practical for both individuals and healthcare providers.
"""
)

# --- JOB 3
st.write('\n')
st.write("🩺", "**Advancing skin Health**")
st.write(
    """
- ► Advancing skin health with a commitment to user privacy, implementing robust security measures to safeguard sensitive information. 
- ► Advancing the beauty tech landscape by revolutionizing traditional skincare approaches, with a clear purpose of enhancing skin health and well-being.
- ► Bringing dermatology expertise to users through virtual consultations powered by artificial intelligence, ensuring quick and accessible insights.
"""
)

# Page layout
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Contact Us")
st.write("Please fill out the form below to get in touch with us.")

# Contact form fields
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
submitted = st.button("Submit")

# Form submission handling
if submitted:
    if name and email and message:
        # Perform desired action with the form data (e.g., send email, store in database, etc.)
        st.success("Thank you for your message. We will get back to you soon!")
    else:
        st.warning("Please fill in all the required fields.")



# Footer text and links
footer_text = "copyright © 2023, All rights reserved.Created by Tushar Pal (iam#11) ! This is prototype only"
footer_text2= "Follow us on : "
github_link = "https://github.com/Tushar-r12345"
twitter_link = "https://twitter.com/Tushar48923527"

# Display footer
# st.write("---")
# st.write(f"---\n{footer_text}\n[Twitter]({twitter_link}) | [Instagram]({instagram_link})")

st.write(footer_text)
# st.write("[Twitter](" + twitter_link + ") | [Instagram](" + instagram_link + ")")
st.write(f"---\n{footer_text2}\n[Twitter]({twitter_link})  |  [Github]({github_link})")
