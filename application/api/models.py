import flask


class Model1:
	var1 = 'var1'
	var2 = 'var2'

	def __init__(self, **kwargs):
		for k in kwargs:
			setattr(self, k, kwargs[k])

	def build_rest(self):
		"""
		Helper to build json
		"""
		return {
			"var1": self.var1,
			"var2": self.var2
		}
