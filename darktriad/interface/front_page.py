# page1.py
import streamlit as st

def front_page():
    st.header("Page Front Content")
    # Add content specific to Page 2
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

    st.markdown("1 - Strongly Disagree &nbsp;&nbsp; 2 - Disagree &nbsp;&nbsp;  3 - Neutral &nbsp;&nbsp;  4 - Agree &nbsp;&nbsp;  5 - Strongly Agree")

    st.markdown("Trust your instincts for the most accurate results.")
    st.markdown("Once you've finished answering all the questions, we'll generate your personalized Machiavellianism/Psychopathy/Narcissism score and compare it to the average score of other 2 traits.")
    st.markdown("Curious to see where you stand?")
    st.markdown("But wait, there's more! We'll also provide you with a predicted Machiavellianism/Psychopathy/Narcissism score based on your responses. Unleash your inner strategist and uncover the hidden aspects of your personality.")
    st.markdown("Ready to dive in? Begin the assessment now and unlock a fascinating glimpse into your Machiavellianism/Psychopathy/Narcissism score. Let's get started!")

    st.write(
        "<style>div.stButton > button {display: block; margin: 0 auto;}</style>",
        unsafe_allow_html=True
    )
