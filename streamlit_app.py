import os
import streamlit as st
import google.generativeai as genai
import tweepy  # Add other social media libraries

# Configure Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 2500,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(model_name="gemini-1.5-pro-002", generation_config=generation_config)
chat_session = model.start_chat(history=[])

# Social Media API Setup (OAuth tokens, keys, etc.)
# Replace with appropriate setup and tokens for each platform
twitter_auth = tweepy.OAuthHandler(os.environ["TWITTER_CONSUMER_KEY"], os.environ["TWITTER_CONSUMER_SECRET"])
twitter_auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN"], os.environ["TWITTER_ACCESS_SECRET"])
twitter_api = tweepy.API(twitter_auth)

# Streamlit UI
st.title("Social Media Content Generator and Poster")

# Input for content generation
user_input = st.text_area("Describe your content idea:")

if st.button("Generate Content"):
    response = chat_session.send_message(user_input)
    generated_content = response.text
    st.write("Generated Content:")
    st.write(generated_content)

# Posting buttons
if st.button("Post to Twitter"):
    try:
        twitter_api.update_status(generated_content)
        st.success("Posted to Twitter!")
    except Exception as e:
        st.error(f"Failed to post to Twitter: {e}")

# Repeat similar blocks for other social media platforms...
