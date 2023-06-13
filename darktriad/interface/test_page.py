import streamlit as st
from darktriad.interface.result_page import result_page

if 'counter' not in st.session_state.keys():
   st.session_state.counter = 0

if 'answers' not in st.session_state.keys():
   st.session_state.answers = []
global answers
answers = st.session_state.answers
#
questions = ["It's not wise to tell your secrets.",
            "I like to use clever manipulation to get my way.",
            "Whatever it takes, you must get the important people on your side. ",
            "Avoid direct conflict with others because they may be useful in the future.",
            "It’s wise to keep track of information that you can use against people later.",
            "You should wait for the right time to get back at people. ",
            "There are things you should hide from other people because they don’t need to know.",
            "Make sure your plans benefit you, not others.",
            "Most people can be manipulated.",
            "People see me as a natural leader. ",
            "I hate being the center of attention.",
            "Many group activities tend to be dull without me.",
            "I know that I am special because everyone keeps telling me so. ",
            "I like to get acquainted with important people. ",
            "I feel embarrassed if someone compliments me.",
            "I have been compared to famous people. ",
            "I am an average person.",
            "I insist on getting the respect I deserve.",
            "I like to get revenge on authorities.",
            "I avoid dangerous situations.",
            "Payback needs to be quick and nasty. ",
            "People often say I’m out of control. ",
            "It’s true that I can be mean to others. ",
            "People who mess with me always regret it.",
            "I have never gotten into trouble with the law.",
            "I enjoy having sex with people I hardly know.",
            "I’ll say anything to get what I want.",
            "Are you a US citizen?"]
#
def update(select):
   answers.append(int(select))
   st.session_state.answers = answers
   st.session_state.counter += 1

global preds


def show_q_a(i):
   select = st.selectbox(
       f"{i+1})  {questions[i]}",
       ('Select a number', '1', '2', '3', '4', '5')
   )
   if select != 'Select a number':
       st.write('You selected:', select)
       if (i < 27):
           name = 'Continue'
           st.button(name, on_click=update, args=select,key='a43')

def show_text():
    # Add CSS styling
    st.markdown('<span style="font-size: 22px;">:red[1 - Strongly Disagree] &nbsp;&nbsp; :blue[2 - Disagree] &nbsp;&nbsp; :green[3 - Neutral] &nbsp;&nbsp; :orange[4 - Agree] &nbsp;&nbsp;  :violet[5 - Strongly Agree]</span>', unsafe_allow_html=True)
    st.markdown("Trust your instincts for the most accurate results.")
    st.markdown("Once you've finished answering all the questions, we'll generate your personalized Machiavellianism/Psychopathy/Narcissism score and compare it to the average score of other 2 traits.")
    st.markdown("Curious to see where you stand?")
    st.markdown("But wait, there's more! We'll also provide you with a predicted Machiavellianism/Psychopathy/Narcissism score based on your responses. Unleash your inner strategist and uncover the hidden aspects of your personality.")
    st.markdown("Ready to dive in? Begin the assessment now and unlock a fascinating glimpse into your Machiavellianism/Psychopathy/Narcissism score. Let's get started!")

def test_page():
    show_text()
    show_q_a(st.session_state.counter)
    st.markdown(f"You are at question: {st.session_state.counter+1} out of 28")
