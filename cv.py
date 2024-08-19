import streamlit as st
from streamlit_star_rating import st_star_rating
import feedparser
import re

def show_about_me():
    st.title(":blue[About Me]")
    col1, col2 = st.columns(2, gap="small",vertical_alignment="center")

    with col1:
        st.image("pp2.jpg",width=280)
    with col2:
        st.title("İbrahim Enes Ulusoy",anchor=False)
        st.write("Experienced and passionate about Python, data science, machine learning and computer vision. There are projects that constantly improve themselves in these areas through various bootcamps and develop various projects in these areas and are still developing. I am constantly improving my skills in AI technologies and follow the latest trends in this field.")


def show_skills():
    st.title(":blue[Skills]")
    skills = {
        "Python": 5,
        "Data Science": 4,
        "Machine Learning": 4,
        "Deep Learning":4,
        "Computer Vision": 4,
        "SQL": 4,
        "Git ve GitHub": 5,
        "Streamlit":5,
        "Django":4,
        "C++": 3,
        "Docker": 3,
        "Java":3
    }

    # Sütunları oluştur
    col1, col2 = st.columns(2)

    # İlk 5 yeteneği birinci sütuna, sonraki 5 yeteneği ikinci sütuna yerleştir
    with col1:
        for skill, rating in list(skills.items())[:6]:
            st_star_rating(label=f"{skill}", maxValue=5, defaultValue=rating, key=f"{skill}_rating_col1", read_only=True )

    with col2:
        for skill, rating in list(skills.items())[6:]:
            st_star_rating(label=f"{skill}", maxValue=5, defaultValue=rating, key=f"{skill}_rating_col2", read_only=True)


def contact_form():
    with st.form("contact form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_input("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.success("Message successfuly sent!")

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

def show_contact_me():
    # İletişim Bilgileri Bölümü
    st.title(":blue[Contact Me]")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/ibrahim-enes-ulusoy-9646551b9/")
        st.link_button("Buy Me Coffee","https://buymeacoffee.com/ibrahimenesulusoy")
    with col2:
        st.link_button("GitHub", "https://github.com/Enes-CE")
        st.link_button("Kaggle","https://www.kaggle.com/brahimenesulusoy")
    with col3:
        if st.button("Contact Me"):
            show_contact_form()
        st.link_button("HackerRank","https://www.hackerrank.com/profile/c_enes_eng")


def show_experiences():
    st.title(":blue[Experiences]")

    st.subheader("Mentor & Community Lead - Global AI Hub", divider=True)
    st.markdown(":gray[Aug 2022 - Currently]")
    st.write("As a dedicated volunteer, I serve as both a mentor and community lead in an education-focused community centered around AI and related technologies. My responsibilities include guiding participants through various AI-related training programs, providing technical support, and conducting key educational sessions. I collaborate with fellow mentors to foster an inclusive learning environment, empowering participants to develop their skills and grow in the AI field.")

    st.subheader("Instructor - Smartpro Technology", divider=True)
    st.markdown(":gray[Aug 2023 - Nov 2023]")
    st.write("During my time as a Python instructor at a corporate company, I successfully delivered Python Data Science and Machine Learning courses. My priorities were to teach students how to effectively use the Python programming language and help them enhance their skills in data analysis, machine learning, and artificial intelligence. I supported their learning through the creation of educational materials, practical exercises, and real-world projects. Additionally, I organized individual and group work to answer students' questions, monitor their progress, and evaluate their development. Through this experience, I enabled students to build a strong foundation in Python and data science, and assisted them in understanding real-world applications.")

    st.subheader("Python Developer - Detaysoft", divider=True)
    st.markdown(":gray[Jan 2022 - Jan 2023]")
    st.write("In image processing projects, I analyzed visual data using advanced algorithms and feature extraction methods. I worked on subjects such as object detection, image classification and image segmentation, and produced solutions to real-world problems. At the same time, I created prediction models by processing large data sets in data science projects and extracting meaningful information.")


def medium():
    # Medium RSS Feed'inizi alın
    rss_url = "https://medium.com/feed/@enes-ulusoy"  # Kullanıcı adınızı buraya ekleyin

    # RSS Feed'i Parse Edin
    feed = feedparser.parse(rss_url)

    # En son yazıyı alın
    if feed.entries:
        latest_post = feed.entries[0]
        title = latest_post.title
        link = latest_post.link
        published = latest_post.published
        summary = latest_post.summary

        # Görsel URL'sini almak için özet (summary) kısmında img etiketini arayın
        img_url = None
        img_match = re.search(r'<img src="(.*?)"', summary)
        if img_match:
            img_url = img_match.group(1)

        # Medya Formatında Gösterim
        st.header(":gray[Medium'daki Son Yazım]")

        st.markdown(f"### [{title}]({link})")
        st.write(f"*Yayın Tarihi: {published}*")
    else:
        st.write("Medium hesabınızda şu anda gösterilecek bir yazı bulunmamaktadır.")

def footer():
    # Footer
    st.write("© 2024 [İbrahim Enes Ulusoy]. Tüm hakları saklıdır.")

show_about_me()
show_skills()
show_experiences()
medium()
show_contact_me()
footer()

