from bs4 import BeautifulSoup
import requests

def the_artist():
    artist = input("Enter an artists name: ")
    new_artist = artist.replace("&", "and")
    new_artist =  "".join(c for c in new_artist if c not in "~`!@#$%^*()_+={}[]'|\:;?/.,<>`")
    new_artist = new_artist.replace(" ", "-")
    return new_artist

def the_song():
    song = input("Enter a song by the artist: ")
    new_song = song.replace("&", "and")
    new_song =  "".join(c for c in new_song if c not in "~`!@#$%^*()_+={}[]'|\:;?/.,<>`")
    new_song = new_song.replace(" ", "-")
    return new_song

def main():
    artist = the_artist()
    artist = artist.lower()
    song = the_song()
    song = song.lower()
    url = "https://genius.com/" + artist + "-" + song + "-lyrics"

    try:
        page = requests.get(url)
        html = BeautifulSoup(page.text, "html.parser") # Extract the page's HTML as a string
        #Scrape the song lyrics from the HTML
        lyrics = html.find("div", class_="lyrics").get_text()
        print(lyrics)
    except:
        print("Error! Invalid Artist or song!")

main()
