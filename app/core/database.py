from pymongo import MongoClient, DESCENDING, ASCENDING
import datetime


class DB(object):
	''' Class for connect to mongodb '''

	URI = "mongodb://localhost:27017"

	@staticmethod
	def init():
		client = MongoClient(DB.URI)
		DB.DATABASE = client['development']

	@staticmethod
	def insert(collection, data):
		data['created_at'] = datetime.datetime.now()
		return DB.DATABASE[collection].insert_one(data)

	@staticmethod
	def find(collection):
		query = {'delete_at':{'$exists':False}}
		return DB.DATABASE[collection].find(query)

	@staticmethod
	def find_one(collection, query):
		query['delete_at'] = {'$exists':False}
		return DB.DATABASE[collection].find_one(query)

	@staticmethod
	def find_all(collection, query):
		query['delete_at'] = {'$exists':False}
		return DB.DATABASE[collection].find(query).limit(250)

	@staticmethod
	def update(collection, query, new_query):
		new_query['update_at'] = datetime.datetime.now()
		query['delete_at'] = {'$exists':False}
		return DB.DATABASE[collection].update_one(query, {'$set':new_query})

	@staticmethod
	def delete_one(collection,query):
		new_query = {
			'delete_at':datetime.datetime.now()
		}
		return DB.DATABASE[collection].find_one_and_update(query,{'$set':new_query})

	@staticmethod
	def delete_all(collection, query):
		new_query = {
			'delete_at':datetime.datetime.now()
		}
		return DB.DATABASE[collection].update_many(query,{'$set':new_query})

	@staticmethod
	def find_pagination(collection, page, size):
		skips = size * (page - 1)
		query = {
			'delete_at' : {'$exists':False}
		}
		return DB.DATABASE[collection].find(query,sort=[('created_at', DESCENDING)]).skip(skips).limit(size)

	@staticmethod
	def find_paginate(collection, query,page,size):
		query['delete_at'] = {'$exists':False}
		return DB.DATABASE[collection].find(query,sort=[('created_at', DESCENDING)],skip=page,limit=size)

	@staticmethod
	def aggregate(collection, pipeline):
		return DB.DATABASE[collection].aggregate(pipeline)

