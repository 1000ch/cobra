__author__ = '1000ch'

import os
import pymongo
from urllib.parse import urlsplit

class Store:

  def __init__(self):
    # get url string from env
    url = os.environ.get('MONGOLAB_URI')
    if url:
      self.connection = pymongo.Connection(url)
    else:
      self.connection = pymongo.Connection('localhost', 27017)

    # authenticate
    #if '@' in url:
    #  parsed = urlsplit(url)
    #  user, password = parsed.netloc.split('@')[0].split(':')
    #  self.connection.authenticate(user, password)

    # get entries
    self.entries = self.connection.feedsnake.entries

  def all(self):
    return self.entries.find()

  def find(self, condition):
    return self.entries.find(condition)

  def insert(self, object):
    result = self.entries.insert(object)
    return result

  def update(self, object):
    result = self.entries.save(object)
    return result

  def delete(self, object):
    result = self.entries.remove(object)
    return result

  def clear(self):
    result = self.entries.remove()
    return result