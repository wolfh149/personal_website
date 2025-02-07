""" This is the main file for the website.
     It is intended to be the home page, navigation, and conductor 
     between sub-pages.
"""
import base64
import streamlit as st # type: ignore ##What does this do?? Question for Geoff
import fitz  # PyMuPDF # type: ignore



# Page Configuration
st.set_page_config(page_title="Home_Page", page_icon=":house:", layout="centered") 
page = st.sidebar.radio 


# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Resume", "Projects", "Contact"))

# Home Page
if page == "Home":
    st.title("Welcome to My Personal Website")
    
    #sets the text for the body of the website
    body_text = """Hi, I'm Harrison. This website is where I'm currently hosting projects and is intended to be a sandbox.    
    Use the navigation bar on the left to look around."""
    st.write(body_text)
    main_image = st.image("/Users/harrisonwolf/Code Projects/HW Website/hwMainPhoto.JPG")    
#write the text to the website 
   
   ## st.write(main_image)


elif page == "Resume":
    st.title("Resume")
    st.write("Check out my resume below:")

    # File path
    resume_path = "HarrisonWolf_Resume_2025 Website.pdf"

    # Convert PDF to images
    doc = fitz.open(resume_path)
    images = []
    for page in doc:
        pix = page.get_pixmap()
        img = pix.tobytes("png")  # Convert to PNG bytes
        images.append(img)

    # Display all pages as images
    for img in images:
        st.image(img, use_container_width=True)

    # Full-Screen Download Button
    with open(resume_path, "rb") as pdf_file:
        st.download_button(
            label="Download My Resume as a PDF",
            data=pdf_file,
            file_name="HarrisonWolf_Resume_2025 Website.pdf",
            mime="application/pdf",
        )
    
## Projects Page
elif page == "Projects":
    st.title("Projects")
    st.write("Here are some of my projects:")
    st.write("Food Truck Scraper - WIP")
    st.write("Datenight - WIP")

## Contact Page
elif page == "Contact":
    st.title("Contact")
    st.write("Get in touch with me:")
    st.write("""
             • Email: harrisonfwolf@gmail.com  
             • Cell: (407)-221-0264  
             • LinkedIn: https://www.linkedin.com/in/wolfh149/
             """
            )
    