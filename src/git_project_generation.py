import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell

 
class CreateProject:  
    def __init__(self, paths, name, folder_names):
        self.folder_names = folder_names
        self.name = name
        self.paths = paths
    def createfolder(self):
        # Create folders in directory:
            for tocreate in self.name:
            #Create subfolders in directory:
                text_path = '..'+'/'+'texts'
                build_content =  open(os.path.join(text_path,'build.txt'), 'r').read()
                os.chdir(self.paths)
                for subfolder_name in self.folder_names:
                    os.makedirs(os.path.join(tocreate, subfolder_name))
                    os.chdir(tocreate)
                #Create readme 
                    with open('readme.md', 'w+') as f:
                        f.write(tocreate)
                    ques = []
                    for names in os.listdir('.'):
                        if names.startswith('q0') and not names.endswith('.ipynb'):
                            ques.append(names)
        			# Create json.config and notebook file :
                    content1 = '{ "notebook": { "folder": "%s" ' % (tocreate)
                    for assignment in ques:
                        os.chdir(assignment)
                        # Create readme and build.py in each assignment:
                        with open('build.py', 'w+') as f:
                            f.write(build_content.format(assignment=assignment))
                        with open('readme.md', 'w+') as f:
                            f.write(assignment) 
                        os.chdir('..')
                        content1 += ', "' + assignment + '": "' + assignment + '.ipynb"'
                        nb = new_notebook()
                        nb.cells.append(new_code_cell("%load "+ assignment+"/build.py"))
                        nbformat.write(nb, assignment +  '.ipynb')
                    content1 += "} }"
                    with open('config.json','w') as file_1:
                        file_1.write(content1)
                    os.chdir('..')
            os.chdir(self.paths)
            return os.listdir('.')

		
#if __name__ == '__main__':
#	CreateProject.main()