import ctypes

_cbasic = ctypes.CDLL('cbasic.so')
_cbasic.cfunction.argtypes = (ctypes.c_uint8)

class basic:
	def __init__(self, newmessage):
		self.message = newmessage

	def outputTheMessage(self):

		print(self.message)

		_cbasic.cfunction(5)

		print("B")

"""
_geohash = ctypes.CDLL('libgeohash.so')
_geohash.geohash_fast_encode.argtypes = (GeoHashRange, GeoHashRange, ctypes.c_double, ctypes.c_double, ctypes.c_uint8,
                                         ctypes.POINTER(GeoHashBits))
"""
