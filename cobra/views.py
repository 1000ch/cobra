__author__ = '1000ch'

import flask
from cobra import app
from cobra.subscriptions import Subscriptions
from cobra.store import Store

@app.route('/')
def show_entries():

  # get entries from db
  entries = Store().findall()
  feeds = []
  for entry in entries:
    if not entry['feedTitle'] in feeds:
      feeds.append(entry['feedTitle'])

  return flask.render_template('index.html', entries = entries, feeds = feeds)

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
  store.insert(list)
  store.index()

  return flask.redirect('/')

@app.route('/clear')
def clear_entries():
  store = Store()
  store.clear()

  return flask.redirect('/')