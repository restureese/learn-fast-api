import datetime
import json
from bson import ObjectId
from uuid import UUID

class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		if isinstance(o, datetime.datetime):
			return o.strftime("%Y-%m-%d %H:%M:%S")
		if isinstance(o, datetime.date):
			return o.strftime("%Y-%m-%d")
		if isinstance(o, UUID):
			return o.hex
		return json.JSONEncoder.default(self, o)