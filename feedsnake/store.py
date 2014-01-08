__author__ = '1000ch'

import pymongo

class Store:

  def __init__(self):
    self.client = pymongo.MongoClient(conf.mongo['host'],conf.mongo['port'])