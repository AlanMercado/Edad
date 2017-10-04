import unittest
from edad import edad
# -*- coding: utf-8 -*-

class edadTest(unittest.TestCase):

	def setUp(self):
		self.edad=edad()

	def test_edad_no_existes(self):
		self.assertEquals(self.edad.edad(-1),"no existes")

	def test_edad_nino(self):
		self.assertEquals(self.edad.edad(5),"eres nino")

	def test_edad_adolecente(self):
		self.assertEquals(self.edad.edad(17),"eres adolecente")

	def test_edad_adulto(self):
		self.assertEquals(self.edad.edad(22),"eres adulto")

	def test_edad_adulto_mayor(self):
		self.assertEquals(self.edad.edad(88),"eres adulto mayor")

	def test_edad_mumm_ra(self):
		self.assertEquals(self.edad.edad(122),"eres mumm-ra")










if __name__ == '__main__':
	unittest.main()
