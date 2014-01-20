__author__ = '1000ch'

import flask
from feedsnake import application
from feedsnake.subscriptions import Subscriptions
from feedsnake.store import Store

@application.route('/')
def show_entries():

  # get entries from db
  entries = Store().all()
  return flask.render_template('index.html', entries = entries)

@application.route('/update')
def update_entries():

  # get subscriptions
  feeds = Subscriptions('feedsnake/static/subscriptions.xml')
  entries = feeds.get_entries()

  # connect to db
  list = []
  for i, entry in enumerate(entries):
    dic = {}
    dic['title'] = entry.title
    dic['link'] = entry.link
    if entry.get('published') is not None:
      dic['published'] = entry.published
    elif entry.get('pubDate') is not None:
      dic['published'] = entry.pubDate
    list.append(dic)

  store = Store()
  store.clear()
  result = store.insert(list)

  return flask.redirect('/')