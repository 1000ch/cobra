__author__ = '1000ch'

import flask
from feedsnake import application
from feedsnake.subscriptions import Subscriptions
from feedsnake.store import Store

@application.route('/')
def show_entries():
  return 'Under development...'

@application.route('/update')
def update_entries():
  feeds = Subscriptions('feedsnake/static/subscriptions.xml')
  entries = feeds.get_entries()

  store = Store()
  for i, entry in enumerate(entries):
    dic = {'title': entry.title, 'link': entry.link, 'published': entry.published}
    result = store.insert(dic)

  return 'Updated entries.'