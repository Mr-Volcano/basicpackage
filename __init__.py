import ctypes

def get_library_path():
    for f in __loader__.contents():
        if f.endswith('.so'):
            return __loader__.resource_path(f)

_cbasic = ctypes.CDLL(get_library_path())
_cbasic.cfunction.argtypes = (ctypes.c_uint8)

class basic:
	def __init__(self, newmessage):
		self.message = newmessage

	def outputTheMessage(self):

		print(self.message)

		_cbasic.cfunction(5)

		print("B")
