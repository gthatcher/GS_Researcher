import serpapi

class MyCitation:
    def __init__(self):
        self.pArticleTitle = ""
        self.pArticleDOI = ""
        self.pArticleJournal = ""
class SerapiSession:
    def __init__(self):
        self.apikey=""
    def scrapeScholar(self):
        serpapi.search()