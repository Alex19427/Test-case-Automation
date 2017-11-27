from git_automation import GitAuto
import os



class CreateLecture(GitAuto):
	def __init__(self, path, topic, filename,number_of_notebooks=1):
		super().__init__(path, topic, filename,number_of_notebooks=1)

	def call(self):
		try:
			GitAuto.create(self)
			GitAuto.notebooks(self)
			GitAuto.create_icons(self)
			print('---------------------------------------------------------------------')
			print(' ')
			print('the directory {directory} does not exist, Created and populated the directory'.format(directory=self.topic))
			print(' ')
			print('---------------------------------------------------------------------')
			print(' ')

		except:
			print('---------------------------------------------------------------------')
			print('')
			print('The directory {directory} already exists, listing the files in each subdirectory'.format(directory=self.topic))
			print(' ')
			print('---------------------------------------------------------------------')
			print(' ')
			os.chdir(self.path+'/'+self.topic)
			print(os.listdir())
			for i in os.listdir():
				
				if not i.endswith('.json') and not i.endswith('.md') and not i.endswith('.DS_Store'):
					os.chdir(i)
					print(os.listdir())
					if os.path.exists('icons'):
						os.chdir('icons')
						print(os.listdir())
						os.chdir('..')
						
					#print(os.listdir())
					#os.chdir(i)
					
					os.chdir('..')



#CreateLecture(destination,topic,'lec1',number_of_notebooks).call()


