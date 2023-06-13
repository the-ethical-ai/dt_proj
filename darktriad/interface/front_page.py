import streamlit as st
#from darktriad.params import IMG_PATH

def front_page():
    # st.header("Page Front Content")
    # Graphic
    # title
    # intro
    show_initial_text()

def show_initial_text():
    st.subheader("Introducing the Psychopathy, Narcissism, Machiavellianism Assessment: Discover Your Personality Score!")
    st.markdown("""
        Our interactive web interface offers a quick and engaging way to assess your Machiavellian tendencies. No lengthy explanations or excessive reading required!
        Simply answer 28 questions by selecting a score from 1 to 5. It's as easy as giving your honest opinion.
    """)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    # Display an image from a file
    image_file = "../images/image_front.jpg"
    st.image(image_file, caption="Image Caption", use_column_width=True)
