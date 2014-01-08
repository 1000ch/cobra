__author__ = '1000ch'

import flask
from feedsnake import application
from feedsnake.subscriptions import Subscriptions
from feedsnake.store import Store

@application.route('/')
def show_entries():
  return 'Feedsnake.'

@application.route('/update')
def update_entries():
  feeds = Subscriptions('feedsnake/static/subscriptions.xml')
  entries = feeds.get_entries()

  store = Store('192.168.0.1', 27017)
  for i, entry in enumerate(entries):
    dic = {'title': entry.title, 'link': entry.link, 'published': entry.published}
    result = store.insert(dic)
    print(result)

  return 'Updated entries.'