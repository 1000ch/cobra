__author__ = '1000ch'

import os
import pymongo
from urllib.parse import urlparse

class EntryDAO:

  def __init__(self):
    # get url string from env
    url = os.environ.get('MONGOHQ_URL')

    if url:
      client = pymongo.MongoClient(url)
      self.db = client[urlparse(url).path[1:]]
    else:
      client = pymongo.MongoClient('localhost', 27017)
      self.db = client.db

  def findall(self):
    cursor = self.db.entries.find().sort('date', pymongo.DESCENDING)
    return list(cursor)

  def find(self, condition, skip, limit):
    cursor = self.db.entries.find(condition).sort('date', pymongo.DESCENDING).skip(skip).limit(limit)
    return list(cursor)

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

  def index(self):
    result = self.db.entries.ensure_index([('date', pymongo.DESCENDING)])
    return result