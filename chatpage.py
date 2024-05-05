import streamlit as st
#from test import generate_response
from openaigenerator import gpt_reply
from txtai import Embeddings
master_brain_path = f'/home/rajat/apps/jobtask/moviemaster'

prompt_engineering =  'You are a movie recommendation system , from the prompt list down 2-3  movies that are relevant to user query'
def main():
    # Set page title and page icon
    st.set_page_config(page_title="Movie Recommendation System", page_icon=":speech_balloon:")

    # Title and subtitle
    st.title("Movie Recommendation System")


    # Checkboxes for selecting genres
    st.write("Select genres:")
    selected_genres = st.multiselect(
        "Genres:",
        ['drama', 'thriller', 'adult', 'documentary', 'comedy', 'crime', 'reality-tv', 'horror', 'sport', 'animation',
         'action', 'fantasy', 'short', 'sci-fi', 'music', 'adventure', 'talk-show', 'western', 'family', 'mystery',
         'history', 'news', 'biography', 'romance', 'game-show', 'musical', 'war']
    )

    # Text area for displaying chat messages
    chat_messages = st.empty()

    # Input box for typing messages
    message = st.text_area("Type your message here:")

    # Button to send message
    if st.button("Send", key="send_button"):
        if message:
            # Display the selected genres
            if selected_genres:
                genre_text = ", ".join(selected_genres)
                chat_messages.markdown(f"<span style='color:#888'>Selected genres: {genre_text}</span>", unsafe_allow_html=True)
            # Display the sent message with the user's name in bold
            chat_messages.markdown(f"**:** {message}", unsafe_allow_html=True)
            prompt_string = ''
            for x in selected_genres:
                embeddings = Embeddings(hybrid=True, keyword=True)
                embeddings.load(f'{master_brain_path}/{x}')
                result = str((embeddings.search(message, 4)[0]["text"]))

                prompt_string+=result
            print("prompt given to ------------------------------------------")
            print(prompt_string)
            output = gpt_reply(prompt_engineering+message+prompt_string)
            st.write(output)


if __name__ == "__main__":
    main()
