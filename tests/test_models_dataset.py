import unittest
from orders_reporter.models import Manufacturer

class TestModels(unittest.TestCase):

	def __init__(iself):
		self.Instance = Manufacterer
	
	def test_data_vendor(self):
		self.assertRaises(self, TypeError, self.Instance.vendor, 1)

	def test_length(self):
		text = "test" * 200
		self.assertRaises(self,self.Instance.vendor, text)


if __name__ == "__main__":
	unittest.main()

