import streamlit as st
import requests

def get_lyrics(artist, song_title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{song_title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["lyrics"]
    else:
        return "Lyrics not found for the given artist and song title."

def main():
    st.title("Lyrics Fetcher")

    artist = st.text_input("Enter the artist name:")
    song_title = st.text_input("Enter the song title:")

    if artist and song_title:
        if st.button("Get Lyrics"):
            lyrics = get_lyrics(artist, song_title)
            st.subheader(f"Lyrics for {song_title} by {artist}")
            st.write(lyrics)

if __name__ == "__main__":
    main()
