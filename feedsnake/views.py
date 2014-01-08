__author__ = '1000ch'

import flask
from feedsnake import application
from feedsnake.subscriptions import Subscriptions

@application.route('/')
def show_entries():
  return 'Feedsnake.'

@application.route('/update')
def update_entries():
  feeds = Subscriptions('app.static/subscriptions.xml')
  entries = feeds.getEntries()
  return 'Updated entries.'