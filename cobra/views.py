__author__ = '1000ch'

import flask
from cobra import app
from cobra.subscriptions import Subscriptions
from cobra.store import Store

@app.route('/')
def show_entries():

  # get entries from db
  entries = Store().all()
  return flask.render_template('index.html', entries = entries)

@app.route('/update')
def update_entries():

  # get subscriptions
  feeds = Subscriptions('cobra/static/subscriptions.xml')
  entries = feeds.get_entries()

  # connect to db
  list = []
  for i, entry in enumerate(entries):

    dic = {}
    dic['title'] = entry.title
    dic['link'] = entry.link
    dic['summary'] = entry.summary
    if entry.get('published') is not None:
      dic['published'] = entry.published
    elif entry.get('pubDate') is not None:
      dic['published'] = entry.pubDate
    list.append(dic)

  store = Store()
  store.clear()
  result = store.insert(list)

  return flask.redirect('/')