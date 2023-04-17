import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_text(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    if sentiment_scores['neg'] > sentiment_scores['pos']:
        return "Hey, they need some help asap. Be the support."
    else:
        return "Don't worry, they are perfectly alright."

def run_app():
    # Set page width and page title
    st.set_page_config(page_title="DepScan", page_icon=":smiley:", layout="wide")
    
    # Set background color
    page_bg = '''
    <style>
    body {
        background-color: #ff99cc;
        background-image: linear-gradient(315deg, #ff99cc 0%, #ffe8e8 74%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #363636;
    }
    </style>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)

    # Set app title and subtitle
    st.title("DepScan")
    st.markdown("*Do you find it difficult to understand the emotions of your loved ones? Don't worry, DepScan can help! Just input their text and DepScan will analyze it to determine if it contains language commonly associated with depression.*")
    st.markdown("*Time is of the essence when it comes to mental health, so don't hesitate to use DepScan.*")
    # Create text input and analyze button
    text = st.text_area("Enter text:", height=150)
    if st.button("Analyze"):
        result = analyze_text(text)
        st.write(result)

if __name__ == "__main__":
    run_app()
