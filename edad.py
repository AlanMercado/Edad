
# -*- coding: utf-8 -*-
#agrege algo2
class edad():
	def edad(self,num1):

		if type(num1) is str:
			return "no valido"
		
		elif num1<0:

			return "no existes"

		elif num1<13 and num1>=0:

			return "eres nino"

		elif num1>=13 and num1<18:
			return "eres adolecente"

		elif num1>=18 and num1<65:
			return "eres adulto"

		elif num1>=65 and num1<120:
			return "eres adulto mayor"

		else:
			return "eres mumm-ra"
