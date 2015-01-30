import dateutil.parser
import feedparser
from cobra.models.entry import Entry


class Feed():

    def __init__(self, title, htmlUrl, xmlUrl):
        self.title = title
        self.htmlUrl = htmlUrl
        self.xmlUrl = xmlUrl
        self.entries = self.get_entries()

    def get_entries(self):
        entries = []
        data = feedparser.parse(self.xmlUrl)
        for i, entry in enumerate(data.entries):
            date = None
            if entry.get('published') is not None:
                date = dateutil.parser.parse(entry.published).strftime('%Y%m%d%H%M%S')
            elif entry.get('pubDate') is not None:
                date = dateutil.parser.parse(entry.pubDate).strftime('%Y%m%d%H%M%S')
            elif entry.get('updated') is not None:
                date = dateutil.parser.parse(entry.updated).strftime('%Y%m%d%H%M%S')

            entries.append(Entry(entry.title, entry.link, date))
            if i == 5:
                break
        return entries