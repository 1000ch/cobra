__author__ = '1000ch'

import xml.etree.ElementTree as etree
from cobra.models.feed import Feed


class Subscriptions:

    def __init__(self, opml):
        self.xml = etree.parse(opml)
        self.root = self.xml.getroot()

    def get_feeds(self):
        feeds = []
        for element in self.root.getiterator():
            if element.tag == 'outline':
                feed = Feed(element.attrib['title'], element.attrib['htmlUrl'], element.attrib['xmlUrl'])
                feeds.append(feed)

        return feeds