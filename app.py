import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, filename="output.mp3", language="hi", slow=True):
    try:
        # Initialize gTTS object with Hindi language and slow speed
        tts = gTTS(text=text, lang=language, slow=slow)
        # Save the audio file
        tts.save(filename)
        st.success(f"Audio file saved as {filename}")
        return filename
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit app
st.title("Hindi Text-to-Speech Converter")

# Input text from user
text_input = st.text_area("Enter your Hindi text:",
    "राजा पोरस को सिकंदर ने पकड़ लिया और उसकी सेना ने अंततः आत्मसमर्पण कर दिया।")

# Set speech speed option
slow_speech = st.checkbox("Slow speech for more impact", value=True)

# Button to convert text to speech
if st.button("Convert to Speech"):
    if text_input.strip() == "":
        st.warning("Please enter some text to convert.")
    else:
        audio_file = text_to_speech(text_input, filename="impressive_hindi_audio.mp3", slow=slow_speech)
        if audio_file:
            # Display audio player
            st.audio(audio_file, format="audio/mp3")
            st.success("Speech successfully generated!")

            # Provide download link
            with open(audio_file, "rb") as file:
                st.download_button(
                    label="Download Audio File",
                    data=file,
                    file_name="impressive_hindi_audio.mp3",
                    mime="audio/mp3"
                )

# Display instructions
st.write("""
### Instructions:
- Enter your Hindi text in the input box.
- Check the 'Slow speech' option for a more impressive effect.
- Click 'Convert to Speech' to generate the audio.
""")
