from bs4 import BeautifulSoup
import requests

def scrap21():

    # scrap = requests.get("https://www.nfl.com/stats/team-stats/offense/rushing/2023/reg/all")
    # sou = BeautifulSoup(scrap.text, "html.parser")
    # teams = sou.findAll('div', attrs= {'class':'d3-o-club-fullname'})

    # for team in teams:
    #     print(team.text)

    playersInBoth = []



    scraper = requests.get("https://www.detroitlions.com/team/stats/2021/PRE")
    soup = BeautifulSoup(scraper.text, "html.parser")

    #stats = soup.findAll('h3', attrs= {'class':'nfl-o-teamstats_title'})
    players = soup.findAll('span', attrs= {'class':'nfl-o-roster__player-name'})

    # for player in players:
    #     print(player.text)



    scrape = requests.get("https://www.detroitlions.com/team/stats/2023/PRE")
    soupy = BeautifulSoup(scrape.text, "html.parser")

    #stats = soup.findAll('h3', attrs= {'class':'nfl-o-teamstats_title'})
    plays = soupy.findAll('span', attrs= {'class':'nfl-o-roster__player-name'})

    # for play in plays:
    #     print(play.text)

    for player in players:
        # temp = player.text
        for play in plays:
            if player == play:
                playerExists = play.text in playersInBoth
                if playerExists == False:
                    playersInBoth.append(play.text)
                    # if temp != play.text:
                    print(play.text)
    
    print("\n")
                
def scrapJermar():
    scrap = requests.get("https://en.wikipedia.org/wiki/Jermar_Jefferson")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapCraig():
    scrap = requests.get("https://en.wikipedia.org/wiki/Craig_Reynolds_(American_football)")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapJason():
    scrap = requests.get("https://en.wikipedia.org/wiki/Jason_Cabinda")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapBrock():
    scrap = requests.get("https://en.wikipedia.org/wiki/Brock_Wright")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapJalen():
    scrap = requests.get("https://en.wikipedia.org/wiki/Jalen_Reeves-Maybin")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapAnthony():
    scrap = requests.get("https://en.wikipedia.org/wiki/Anthony_Pittman")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapJulian():
    scrap = requests.get("https://en.wikipedia.org/wiki/Julian_Okwara")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapWill():
    scrap = requests.get("https://en.wikipedia.org/wiki/Will_Harris_(American_football)")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapIfeatu():
    scrap = requests.get("https://en.wikipedia.org/wiki/Ifeatu_Melifonwu")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

def scrapJack():
    scrap = requests.get("https://en.wikipedia.org/wiki/Jack_Fox_(American_football)")
    sou = BeautifulSoup(scrap.text, "html.parser")

    boxes = sou.findAll('th', attrs= {'class':'infobox-label'})
    infos = sou.findAll('td', attrs= {'class':'infobox-data'})

    
    for box, info in zip(boxes,infos):
        # if draft.text == 'NFL draft':
        print(box.text + info.text)

    print("\n")

scrap21()
scrapJermar()
scrapCraig()
scrapJason()
scrapBrock()
scrapJalen()
scrapAnthony()
scrapJulian()
scrapWill()
scrapIfeatu()
scrapJack()




