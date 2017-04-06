#!/usr/bin/env python
import sys
id = {}
class Reducer(object):
	def __init__(self, stream):
		self.stream = stream

	def emit(self, key, value):
		sys.stdout.write("{0}\t{1}\n".format(key, value))
	def reduce(self):

		for a, w, cnt in self:
			cnt = int(cnt)
			if a in id.keys():

				if w in id[a].keys():
					id[a][w] += cnt
				else:
					id[a][w]=cnt
			else:
				id[a]={w:cnt}
		for k in id.keys():
			self.emit(k,id[k])

	def __iter__(self):
		for line in self.stream:
			try: #this is important
				parts = line.split('\t')
				yield parts[0], parts[1], parts[2]
			except:
				continue
if __name__ == "__main__":
	reducer = Reducer(sys.stdin)
	reducer.reduce()
