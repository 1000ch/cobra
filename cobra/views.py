__author__ = '1000ch'

import flask
from cobra import app
from cobra.subscriptions import Subscriptions
from cobra.store import Store

@app.route('/')
def show_entries():

  # get entries from db
  entries = Store().findall()
  return flask.render_template('index.html', entries = entries)

@app.route('/update')
def update_entries():

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

  store = Store()
  store.clear()
  result = store.insert(list)

  return flask.redirect('/')

@app.route('/clear')
def clear_entries():
  store = Store()
  result = store.clear()

  return flask.redirect('/')