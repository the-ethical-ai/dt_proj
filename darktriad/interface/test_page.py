import streamlit as st

from questions import QUESTIONS

def update(select):
    st.session_state.answers.append(int(select))
    st.session_state["currentQuestion"] += 1

def show_q_a(i):
    if i < 28:
        st.write("Questions:")
        
        if i == 27:  # Check if it is the "Are you a US citizen?" question
            select = {"Yes": "1", "No": "0"}.get(st.selectbox(
                f"{i+1})  {QUESTIONS[i]}",
                ('Select an option', 'Yes', 'No')
            ), "0")
            
        else:
            select = st.selectbox(
                f"{i+1})  {QUESTIONS[i]}",
                ('Select a number', '1', '2', '3', '4', '5')
            )
        
        st.markdown(f"You are at question: {st.session_state['currentQuestion'] + 1} out of 28")
        
        if select != 'Select a number' and select != 'Select an option':
            st.write('You selected:', select)
            st.button('Submit Answer', on_click=update, args=select, key='a43')
    

def show_text():
  
    # Add CSS styling
    st.markdown("""<style>.big-font {font-size:22px !important;}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-font">Trust your instincts for the most accurate results.</p>', unsafe_allow_html=True)
    #st.markdown('<p class="big-font">Once you've finished answering all the questions, we'll generate your personalized Machiavellianism/Psychopathy/Narcissism score and compare it to the average score of other 2 traits.</p>', unsafe_allow_html=True)
    #st.markdown('<p class="big-font">Curious to see where you stand?</p>', unsafe_allow_html=True)
    #st.markdown('<p class="big-font">But wait, there's more! We'll also provide you with a predicted Machiavellianism/Psychopathy/Narcissism score based on your responses. Unleash your inner strategist and uncover the hidden aspects of your personality.</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">Ready to dive in? Begin the assessment now and unlock a fascinating glimpse into your Machiavellianism/Psychopathy/Narcissism score.</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">Let us get started.</p>', unsafe_allow_html=True)
    st.markdown('<span style="font-size: 22px;">:red[1 - Strongly Disagree] &nbsp;&nbsp; :blue[2 - Disagree] &nbsp;&nbsp; :green[3 - Neutral] &nbsp;&nbsp; :orange[4 - Agree] &nbsp;&nbsp;  :violet[5 - Strongly Agree]</span>', unsafe_allow_html=True)

def test_page():
    show_text()
    show_q_a(st.session_state["currentQuestion"])

    #st.write(answers)
