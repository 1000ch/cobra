__author__ = '1000ch'

import xml.etree.ElementTree as etree
import feedparser

class Subscriptions:

  def __init__(self, opml):
    self.xml = etree.parse(opml)
    self.root = self.xml.getroot()

  def get_outlines(self):
    outlines = []
    for element in self.root.getiterator():
      if element.tag == 'outline':
        outlines.append(element.attrib['xmlUrl'])
    return outlines

  def get_entries(self):
    outlines = self.get_outlines()
    entries = []
    for outline in outlines:
      feed = feedparser.parse(outline)
      for i, entry in enumerate(feed.entries):
        entries.append(entry)
        if i == 5:
          break
    return entries