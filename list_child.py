class MyList(list):
	def pack(self, obj):
		assert(isinstance(obj, dict) and "source" in obj)
		if len(self):
			last = self[-1]
			n = len(last)
			if n  == 3:
				self.append({"src0": obj["source"]})
			else:
				last["src{}".format(n)] = obj["source"]
		else:
			self.append({"src0": obj["source"]})
