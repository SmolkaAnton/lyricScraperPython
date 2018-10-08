from bs4 import BeautifulSoup
import requests

def the_artist():
    artist = input("Enter an artists name: ")
    new_artist = artist.replace(" ", "-")
    return new_artist

def the_song():
    song = input("Enter a song by the artist: ")
    new_song = song.replace(" ", "-")
    print(new_song)
    return new_song

def main():
    #artist = the_artist()
    #song = the_song()
    #url = "https://genius.com/" + artist + "-" + song + "-lyrics"
    url = "https://genius.com/Kendrick-lamar-humble-lyrics"
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser") # Extract the page's HTML as a string

    # Scrape the song lyrics from the HTML
    lyrics = html.find("div", class_="lyrics").get_text()
    print(lyrics)

main()
