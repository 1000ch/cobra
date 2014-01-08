__author__ = '1000ch'

import pymongo

class Store:

  def __init__(self, host, port):
    self.client = pymongo.MongoClient(host ,port)
    self.entries = self.client.feedsnake.entries

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