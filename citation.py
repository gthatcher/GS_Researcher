import serpapi

class MyCitation:
    def __init__(self):
        self.pArticleTitle = ""
        self.pArticleDOI = ""
        self.pArticleJournal = ""

    def scrapeScholar(self):
        SerapiSession.startsession
        serpapi.search()

class SerapiSession:
    def __init__(self):
        self.apikey = ""
        self.sessionID = ""


    def startsession(self):
         apikey = ""
         self.apikey = apikey
