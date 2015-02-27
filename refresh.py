#!/usr/bin/env python

from cobra.subscriptions import Subscriptions
from cobra.entry import EntryDAO

# get feeds
feeds = Subscriptions('subscriptions.xml').get_feeds()

# connect to db
entries = []
for feed in feeds:
    for entry in feed.entries:
        entries.append({
            'feedTitle': feed.title,
            'htmlUrl': feed.htmlUrl,
            'xmlUrl': feed.xmlUrl,
            'title': entry.title,
            'link': entry.link,
            'date': entry.date
        })

entry_dao = EntryDAO()
entry_dao.clear()
entry_dao.insert(entries)
entry_dao.index()