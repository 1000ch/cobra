__author__ = '1000ch'

import os
import pymongo
from urllib.parse import urlparse

class Store:

  def __init__(self):
    # get url string from env
    url = os.environ.get('MONGOHQ_URL')
    if url:
      connection = pymongo.Connection(url)
      self.db = connection[urlparse(url).path[1:]]
    else:
      print('hello')
      connection = pymongo.Connection('localhost', 27017)
      self.db = connection.db
      print('db is selected')

  def all(self):
    return self.db.entries.find()

  def find(self, condition):
    return self.db.entries.find(condition)

  def insert(self, object):
    result = self.db.entries.insert(object)
    return result

  def update(self, object):
    result = self.db.entries.save(object)
    return result

  def delete(self, object):
    result = self.db.entries.remove(object)
    return result

  def clear(self):
    result = self.db.entries.remove()
    return result