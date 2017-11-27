
from test_generation import TestCaseGeneration
import os
import shutil

#destination = r'C:/Users/Alex/Desktop/Greyatom/Project/Z_project'

class TestGeneration(TestCaseGeneration):
	def __init__(self,path_to_find):
		super().__init__(path_to_find)
		
	
	def calltestcase(self):
		present =None
		data = None
		os.chdir(self.path_to_find)
		for i in os.listdir():
			if i.endswith('_project'):
				os.chdir(os.path.join(i+'/'+'data'))
				data = os.listdir()
				os.chdir('..')
				for j in os.listdir():
					if j.startswith('q0') and not j.endswith('.ipynb'):
						os.chdir(self.path_to_find+'/' +i+'/' + j)
						if os.path.isdir('tests'):
							present =+ 1
							shutil.rmtree('tests')
							os.chdir('..')
						os.chdir('..')

			os.chdir(self.path_to_find)

		try:
			
			if present == None:
				print('There is not tests folder present, trying to create testcases')
			if data != None:
				TestCaseGeneration.generate_test_cases(self)
				print('---------------------------------------------------------------------')
				print(' ')
				print('the directory data exist, ')
				print(' ')
				print('---------------------------------------------------------------------')
				print(' ')
		except:
			print('---------------------------------------------------------------------')
			print('')
			print('Please check if data is present ') #and test folder is not already created
			print(' ')
			print('---------------------------------------------------------------------')
			print(' ')
			os.chdir(self.path_to_find)
			for i in os.listdir():
				if i.endswith('_project'):
					os.chdir(os.path.join(i+'/'+'data'))	
					os.chdir('..')

destination = '/Users/abhisheksubramanian/Desktop/test_automation'
TestGeneration(destination).calltestcase()