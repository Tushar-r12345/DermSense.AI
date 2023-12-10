from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "vitiligo.jpg"
profile_pic2 = current_dir / "assets" / "eczema.jpeg"
profile_pic3 = current_dir / "assets" / "pigments.jpg"
profile_pic4 = current_dir / "assets" / "normal.jpg"

NAME = "Vitiligo"
DESCRIPTION = """
Vitiligo is a skin disorder characterized by the loss of pigmentation, leading to white patches on the skin.
"""
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

SOCIAL_MEDIA = {
    "Healthline": "https://www.healthline.com/health/cataract",
    "WebMD": "https://www.webmd.com/skin-health/cataracts/what-are-cataracts",
    "MSD ": "https://www.msdmanuals.com/en-in/professional/skin-disorders/cataract/cataract",
}



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.write('\n')
    st.write('\n')
    st.title(NAME)
    st.write(DESCRIPTION)
    # --- SOCIAL LINKS ---
    st.write('\n')
    # cols = st.columns(len(SOCIAL_MEDIA))
    # for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    #     cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Enlightenment")
st.write("----")
st.write(
    """
- ✔️ Definition: Vitiligo is a skin condition characterized by the loss of pigmentation, resulting in white patches on the skin.
- ✔️ Cause: The exact cause is unknown, but it is believed to involve a combination of genetic, autoimmune, and environmental factors.
- ✔️ Pigment Loss: Melanocytes, the cells responsible for producing melanin (skin pigment), are destroyed or become dysfunctional in affected areas.
- ✔️ Pigment Loss: White patches on the skin, often symmetrical, can appear anywhere on the body.
- ✔️ Treatment: There is no cure, but treatment options include topical corticosteroids, phototherapy, and in some cases, surgical procedures.
"""
)
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')


NAME = "Eczema"
DESCRIPTION = """
Eczema, or atopic dermatitis, is a chronic skin condition characterized by inflammation, itching, and redness.
"""
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic2 = Image.open(profile_pic2)

SOCIAL_MEDIA = {
    "Mayo Clinic": "https://www.mayoclinic.org/diseases-conditions/diabetic-retinopathy/symptoms-causes/syc-20371611",
    "Medscape": "https://emedicine.medscape.com/article/1225122-overview",
    "NHS": "https://www.nhs.uk/conditions/diabetic-retinopathy/",
}



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic2, width=230)

with col2:
    st.write('\n')
    st.write('\n')
    st.title(NAME)
    st.write(DESCRIPTION)
    # --- SOCIAL LINKS ---
    st.write('\n')
    # cols = st.columns(len(SOCIAL_MEDIA))
    # for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    #     cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Enlightenment")
st.write("----")
st.write(
    """
- ✔️ Definition: Eczema, or atopic dermatitis, is a chronic skin condition characterized by inflammation, itching, and redness.
- ✔️ Cause: Genetics, immune system dysfunction, and environmental factors contribute to eczema.
- ✔️ Symptoms: Itchy, inflamed skin with red patches, often accompanied by blisters or oozing.
- ✔️ Triggers: Allergens, irritants, stress, and temperature changes can trigger eczema flare-ups.
- ✔️ Treatment: Moisturizers, topical corticosteroids, antihistamines, and avoiding triggers are common management strategie
"""
)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')



NAME = "Pigments"
DESCRIPTION = """
Pigmentation in the skin is primarily due to melanin, produced by melanocytes in the epidermis.
"""
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic3 = Image.open(profile_pic3)

SOCIAL_MEDIA = {
    "Healthline": "https://www.healthline.com/health/glaucoma",
    "Webmd": "https://www.webmd.com/skin-health/glaucoma-skins",
    "MedlinePlus": "https://medlineplus.gov/ency/article/001620.htm",
}



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic3, width=230)

with col2:
    st.write('\n')
    st.write('\n')
    st.title(NAME)
    st.write(DESCRIPTION)
    # --- SOCIAL LINKS ---
    st.write('\n')
    # cols = st.columns(len(SOCIAL_MEDIA))
    # for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    #     cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Enlightenment")
st.write("----")
st.write(
    """
- ✔️ Melanin: Melanin is the pigment responsible for the color of the skin, hair, and skins.
- ✔️ Melanocytes: Specialized cells called melanocytes produce melanin in the skin.
- ✔️ Types of Melanin: Eumelanin (brown/black) and pheomelanin (red/yellow) are the two main types of melanin.
- ✔️ Function: Melanin protects the skin from the harmful effects of ultraviolet (UV) radiation and determines skin color.
- ✔️ Distribution: Melanin is unevenly distributed in the skin, with higher concentrations in areas exposed to sunlight.

"""
)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')


NAME = "Normal"
DESCRIPTION = """
Balanced and well-hydrated, normal skin typically has an even tone and texture.
"""
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic4 = Image.open(profile_pic4)

SOCIAL_MEDIA = {
    "Healthline": "https://www.healthline.com/health/how-far-can-the-human-skin-see",
    "Medline Plus": "https://medlineplus.gov/ency/imagepages/19511.htm",
    "myvision.org": "https://myvision.org/education/perfect-vision/",
}



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic4, width=230)

with col2:
    st.write('\n')
    st.write('\n')
    st.title(NAME)
    st.write(DESCRIPTION)
    # --- SOCIAL LINKS ---
    st.write('\n')
    # cols = st.columns(len(SOCIAL_MEDIA))
    # for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    #     cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Enlightenment")
st.write("----")
st.write(
    """
- ✔️ Structure: The skin is composed of three layers - epidermis, dermis, and subcutis (or hypodermis).
- ✔️ Functions: Protection against pathogens, regulation of body temperature, and sensation are primary functions of the skin.
- ✔️ Pigmentation: Normal skin color is determined by the amount and type of melanin present.
- ✔️ Texture: Smooth and elastic texture with a consistent color in the absence of skin conditions.
- ✔️ Maintenance: Regular cleansing, moisturizing, and protection from excessive sun exposure contribute to maintaining healthy skin.

"""
)


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


# Footer text and links
footer_text = "copyright © 2023, All rights reserved.Created by Tushar Pal (iam#11) ! This is prototype only"
footer_text2= "Follow us on : "
twitter_link = "https://twitter.com/Tushar48923527"
github_link = "https://github.com/Tushar-r12345"

# Display footer
# st.write("---")
# st.write(f"---\n{footer_text}\n[Twitter]({twitter_link}) | [Instagram]({instagram_link})")

st.write(footer_text)
# st.write("[Twitter](" + twitter_link + ") | [Instagram](" + instagram_link + ")")
st.write(f"---\n{footer_text2}\n[Twitter]({twitter_link})  |  [Github]({github_link})")