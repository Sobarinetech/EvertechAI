import streamlit as st
import google.generativeai as genai
import tweepy

# Configure the Gemini API securely from Streamlit's secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Set up Twitter API credentials using Tweepy
twitter_auth = tweepy.OAuthHandler(st.secrets["TWITTER_CONSUMER_KEY"], st.secrets["TWITTER_CONSUMER_SECRET"])
twitter_auth.set_access_token(st.secrets["TWITTER_ACCESS_TOKEN"], st.secrets["TWITTER_ACCESS_SECRET"])
twitter_api = tweepy.API(twitter_auth)

# Streamlit UI
st.title("Social Media Content Generator and Poster")
st.write("Generate content using AI and post it to Twitter in one click!")

# Prompt input field for content idea
user_input = st.text_input("Enter your content idea:", "Example: Tips on productivity")

# Button to generate response
if st.button("Generate Content"):
    try:
        # Load and configure the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate content based on the user's input
        response = model.generate_content(user_input)
        
        # Display the generated content
        generated_content = response.text
        st.write("Generated Content:")
        st.write(generated_content)
    except Exception as e:
        st.error(f"Failed to generate content: {e}")

# Button to post the generated content to Twitter
if st.button("Post to Twitter"):
    if 'generated_content' in locals() and generated_content:
        try:
            # Post generated content to Twitter
            twitter_api.update_status(generated_content)
            st.success("Posted to Twitter successfully!")
        except Exception as e:
            st.error(f"Failed to post to Twitter: {e}")
    else:
        st.warning("Please generate content before posting.")
