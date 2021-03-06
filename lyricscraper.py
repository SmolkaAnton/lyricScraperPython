from bs4 import BeautifulSoup
import requests
import csv

def the_artist():
    artist = input("Enter an artists name: ")
    new_artist = clean_up_string(artist)
    return new_artist

def the_song():
    song = input("Enter the artist's song: ")
    new_song = clean_up_string(song)
    return new_song

def clean_up_string(str):
    list = []
    #Put the string into a list
    for i in str:
        list.append(i)

    #Will fix glitch with Songs/Artists beginning with &
    if(list[0]=="&"):
        list.pop(0)

    #Will replace characters with necessary replacements
    for i in list:
        if(i=="+"):
            list.remove(i)
    list = [w.replace('&', 'and') for w in list]
    list = [w.replace('$', '-') for w in list]
    list = [w.replace('.', '-') for w in list]
    list = [w.replace('&', 'and') for w in list]

    #Combine list into string
    new_string = ''.join(list)
    #Remove other necessary characters
    new_string =  "".join(c for c in new_string if c not in "!@#*(){}[]'|\:;?/,<>`")
    #Remove spaces at the beginning and end
    new_string = new_string.strip()
    #Turn remaining spaces into dashes
    new_string = new_string.replace(" ", "-")
    return new_string

def main():
    artist = the_artist()
    artist = artist.lower()
    song = the_song()
    song = song.lower()
    url = "https://genius.com/" + artist + "-" + song + "-lyrics"

    try:
        page = requests.get(url)
        #Extract the page's HTML as a string
        html = BeautifulSoup(page.text, "html.parser")
        #Scrape the song lyrics from the HTML
        lyrics = html.find("div", class_="lyrics").get_text()
        print(lyrics)

        #Export Artist, Song Title, and Lyrics to a .csv file
        with open('lyrics.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([artist, song, lyrics])
    except:
        print("Error! Invalid Artist or song!")

main()
