from bs4 import BeautifulSoup
import requests

def the_artist():
    list = []
    artist = input("Enter an artists name: ")
    for i in artist:
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

    #In the case of there being back to back spaces, remove one
    for i in range(len(list)-1):
        if(list[i] == " " and list[i+1] == " "):
            list.pop(i)

    #Combine list into string
    new_artist = ''.join(list)
    #Remove other necessary characters
    new_artist =  "".join(c for c in new_artist if c not in "!@#*(){}[]'|\:;?/,<>`")
    #Remove spaces at the beginning and end
    new_artist = new_artist.strip()
    #Turn remaining spaces into dashes
    new_artist = new_artist.replace(" ", "-")
    return new_artist

def the_song():
    list = []
    artist = input("Enter a song: ")
    for i in artist:
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

    #In the case of there being back to back spaces, remove one
    for i in range(len(list)-1):
        if(list[i] == " " and list[i+1] == " "):
            list.pop(i)

    #Combine list into string
    new_song = ''.join(list)
    #Remove other necessary characters
    new_song =  "".join(c for c in new_song if c not in "!@#*(){}[]'|\:;?/,<>`")
    #Remove spaces at the beginning and end
    new_song = new_song.strip()
    #Turn remaining spaces into dashes
    new_song = new_song.replace(" ", "-")
    return new_song

def main():
    artist = the_artist()
    artist = artist.lower()
    song = the_song()
    song = song.lower()
    url = "https://genius.com/" + artist + "-" + song + "-lyrics"
    #print(url)
    try:
        page = requests.get(url)
        #Extract the page's HTML as a string
        html = BeautifulSoup(page.text, "html.parser")
        #Scrape the song lyrics from the HTML
        lyrics = html.find("div", class_="lyrics").get_text()
        print(lyrics)
    except:
        print("Error! Invalid Artist or song!")

main()
