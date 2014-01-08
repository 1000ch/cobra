__author__ = '1000ch'

from app import app
from app.subscriptions import Subscriptions

@app.route('/')
def show_entries():
  return 'Feedsnake.'

@app.route('/update')
def update_entries():
  feeds = Subscriptions('app.static/subscriptions.xml')
  entries = feeds.getEntries()
  return 'Updated entries.'