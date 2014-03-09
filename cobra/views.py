__author__ = '1000ch'

import flask
from cobra import app
from cobra.subscriptions import Subscriptions
from cobra.entry import EntryDAO

@app.route('/')
def show_entries():

  # dao
  entryDao = EntryDAO()

  # get entries from db
  entries = entryDao.findall()
  feeds = []
  for entry in entries:
    if not entry['feedTitle'] in feeds:
      feeds.append(entry['feedTitle'])

  top_entries = entryDao.find({}, 0, 20)

  return flask.render_template('index.html', entries = top_entries, feeds = feeds)

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

  entryDao = EntryDAO()
  entryDao.clear()
  entryDao.insert(list)
  entryDao.index()

  return flask.redirect('/')

@app.route('/clear')
def clear_entries():
  entryDao = EntryDAO()
  entryDao.clear()

  return flask.redirect('/')