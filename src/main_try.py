try:
    from git_project_generation import CreateProject
except Exception as e:
    print(e)
import os

destination = '/Users/abhisheksubramanian/Desktop/test_automation'
folder_names = ['data', 'images', 'q01_lliaear', 'q02_plot', 'q03_question3']
name = ['linear_regression_project']


class AutoProject(CreateProject):
    def __init__(self, paths, naam, folder_naam):
        super().__init__(paths,naam,folder_naam)

    def call(self):
        try:

            CreateProject.createfolder(self)

            print('---------------------------------------------------------------------')
            print(' ')
            print('the directory %s does not exist, Created and populated the directory' % name)
            print(' ')
            print('---------------------------------------------------------------------')
            print(' ')
        except:
            print('---------------------------------------------------------------------')
            print('')
            print('The directory %s already exists, listing the files in each subdirectory' % name)
            print(' ')
            print('---------------------------------------------------------------------')
            print(' ')
            os.chdir(destination)
            print(os.listdir())
            for i in os.listdir():
                if i.endswith('_project'):
                    os.chdir(i)
                    print(os.listdir())
                    os.chdir('..')


AutoProject(destination, name, folder_names).call()
