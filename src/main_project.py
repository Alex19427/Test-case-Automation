from git_project_generation import CreateProject
import os

#destination = r'C:/Users/Alex/Desktop/Greyatom/Project/Z_project'
#folder_names = ['data','images','q01_lliaear', 'q02_plot', 'q03_question3']
#name = ['linear_regression_project']
    
#folder = CreateProject(destination,name,folder_names)
#folder.createfolder()

class AutoProject(CreateProject):
	def __init__(self, paths, name, folder_names):
		super().__init__(paths, name, folder_names)
	
	def callproject(self):
		try:
			CreateProject.createfolder(self)
			print('---------------------------------------------------------------------')
			print(' ')
			print('the directory %s does not exist, Created and populated the directory'% self.name)
			print(' ')
			print('---------------------------------------------------------------------')
			print(' ')
		except:
			print('---------------------------------------------------------------------')
			print('')
			print('The directory %s already exists, listing the files in each subdirectory' % self.name)
			print(' ')
			print('---------------------------------------------------------------------')
			print(' ')
			os.chdir(self.paths)
			print(os.listdir())
			for i in os.listdir():
				if i.endswith('_project'):
					os.chdir(i)	
					print(os.listdir())
					os.chdir('..')
					
#AutoProject(destination,name,folder_names).callproject()



