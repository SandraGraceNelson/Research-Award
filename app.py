import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_text(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    if sentiment_scores['neg'] > sentiment_scores['pos']:
        return "The text contains language associated with depression."
    else:
        return "The text does not contain language associated with depression."

def run_app():
    # Set page width and page title
    st.set_page_config(page_title="Depression Analysis App", page_icon=":smiley:", layout="wide")
    
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
    st.title("Depression Analysis App")
    st.markdown("*Analyze text to determine if it contains language associated with depression.*")

    # Create text input and analyze button
    text = st.text_area("Enter your text:", height=150)
    if st.button("Analyze"):
        result = analyze_text(text)
        st.write(result)

if __name__ == "__main__":
    run_app()
