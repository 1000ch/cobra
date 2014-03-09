#!/usr/bin/env python

from cobra.subscriptions import Subscriptions
from cobra.entry import EntryDAO

# get feeds
feeds = Subscriptions('cobra/static/subscriptions.xml').get_feeds()

# connect to db
list = []
for feed in feeds:
  for entry in feed.entries:
    dic = {}
    dic['feedTitle'] = feed.title
    dic['htmlUrl'] = feed.htmlUrl
    dic['xmlUrl'] = feed.xmlUrl
    dic['title'] = entry.title
    dic['link'] = entry.link
    dic['date'] = entry.date
    list.append(dic)

entryDao = EntryDAO()
entryDao.clear()
entryDao.insert(list)
entryDao.index()