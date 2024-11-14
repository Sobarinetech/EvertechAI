import streamlit as st
import google.generativeai as genai
import tweepy  # Add other social media libraries as needed
import os

# Configure Gemini API with Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Set generation configuration
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 2500,
    "response_mime_type": "text/plain",
}

# Set up Twitter API credentials
twitter_auth = tweepy.OAuthHandler(st.secrets["TWITTER_CONSUMER_KEY"], st.secrets["TWITTER_CONSUMER_SECRET"])
twitter_auth.set_access_token(st.secrets["TWITTER_ACCESS_TOKEN"], st.secrets["TWITTER_ACCESS_SECRET"])
twitter_api = tweepy.API(twitter_auth)

# Streamlit UI
st.title("Social Media Content Generator and Poster")

# Input for content generation
user_input = st.text_area("Describe your content idea:")

# Generate content when button is clicked
if st.button("Generate Content"):
    try:
        # Generate content without chat session
        response = genai.generate(prompt=user_input, **generation_config)
        generated_content = response.text
        st.write("Generated Content:")
        st.write(generated_content)
    except Exception as e:
        st.error(f"Failed to generate content: {e}")

# Social media posting
if st.button("Post to Twitter"):
    if 'generated_content' in locals() and generated_content:
        try:
            # Post to Twitter
            twitter_api.update_status(generated_content)
            st.success("Posted to Twitter successfully!")
        except Exception as e:
            st.error(f"Failed to post to Twitter: {e}")
    else:
        st.warning("Please generate content before posting.")

# Repeat similar blocks for other social media platforms as needed
