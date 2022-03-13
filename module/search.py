import requests

def search(nickname):
    us = open("list.txt", "r")
    user=nickname
    print("Inizio la ricerca del nick " + nickname)
    for line in us:
        url = "https://tmi.twitch.tv/group/user/"+line.lower()[:-1]+"/chatters"
        r=requests.get(url).json()
        chat=r.get('chatters')['viewers']
        if(user in chat):
            print(user + " sta guardando " + line[:-1])
    us.close()