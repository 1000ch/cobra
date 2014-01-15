__author__ = '1000ch'

import os
import pymongo

class Store:

  def __init__(self):
    url = os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017')
    self.connection = pymongo.Connection(url)
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