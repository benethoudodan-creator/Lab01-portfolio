import streamlit as st

st.title("Portfolio Quiz")

st.write("""
Welcome to my portfolio quiz. This will really test your attention span and if actually read through the porfolio throughly.
Good Luck!👍
""")
#Multiple Choice
st.header("1.What instrument does Benet mainly play as a Band leader?")
st.image("Images/Drum-Play.jpeg", caption="Drums")
st.image("Images/Piano-Play.jpeg",caption="Piano")
st.image("Images/Bass-Play.jpeg", caption="Bass")
main_instrument = st.selectbox(
    "Choose one:",
    ["Drums", "Piano", "Bass"]

)
correct_instrument = "Piano"



st.header("2.What language is Benet the most fluent in speaking?")

most_fluent_language = st.radio(
    "Choose one:",
    ["English", "French", "Ewe", "Chinese"]
)

correct_language = "English"





st.header("3.What is Benet majoring in while at Georgia Tech?")

Major = st.radio(
    "Choose one:",
    ["Computer Science", "Computer Information Systems", "Psychology", "Computer Engineering"]

)    
correct_major = "Computer Engineering"
#Multi-Select
st.header("4.What courses are part of Benet's relevant coursework for this semester?")

relevant_coursework = st.multiselect(
    "Select Multiple Answers:",
    ["Math 1113", "CHEM 1310", "APPH 1040", "APPH 1050"]

 )
correct_answers = ["Math 1113", "CHEM 1310"]

#Number-Input
st.header("5.What is Benet's anticipated graduation date from Georgia Tech?")


graduation_date = st.number_input(
    "Type in a number:",
   
    

)
correct_date = "2029"
# submit button
if st.button("Submit"):
    score = 0

    if main_instrument == correct_instrument:
        st.success("Q1: Correct!")
        score += 1
    else:
        st.error(f"Q1: Not Quite. Correct answer is {correct_instrument}")

    if most_fluent_language == correct_language:
        st.success("Q2: Correct!")
        score += 1
    else:
        st.error(f"Q2: Not Quite. Correct answer is {correct_language}")

    if Major == correct_major:
        st.success("Q3: Correct!")
        score += 1
    else:
        st.error(f"Q3: Not Quite. Correct answer is {correct_major}")

    if set(relevant_coursework) == set(correct_answers):
        st.success("Q4: Correct!")
        score += 1
    else:
        st.error("Q4: Not Quite")

    if graduation_date == correct_date:
        st.success("Q5: Correct!")
    else:
        st.error(f"Q5: Not Quite. Correct answer is {correct_date}.")
        
        
    
if st.button("See My Results"):
    st.success("Thanks for completing the quiz!")
    
