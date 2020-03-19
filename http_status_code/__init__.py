from .errors import CodeAlreadyExistException

class StatusCode:
	available_codes = list()
	def __init__(self, code, message):
		self.code = code
		self.message = message

		if self.code in StatusCode.available_codes:
			raise CodeAlreadyExistException('The required code is already available in the standard code')

		StatusCode.available_codes.append(self.code)

	def update_msg(self, new_msg):
		self.message = str(new_msg)


from . import standard
