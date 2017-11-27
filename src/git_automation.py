import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell
import glob
import shutil

class GitAuto:
    def __init__(self, path, topic, filename,number_of_notebooks=1):
        self.topic = topic
        self.number_of_notebooks = number_of_notebooks
        self.path = path
        self.default_path = os.getcwd()
        self.filename = filename
        # self.lines

    def create(self):
        txt_path = '..'+'/'+'texts'
        with open(os.path.join(txt_path,'config.txt'), 'r') as f:
            self.lines = f.read()
        with open(os.path.join(txt_path,'try.py'), 'r') as f:
            self.notebook_lines = f.read()
        # print(lines.format(self=self))
        # lines.format(name,slide)
        os.chdir(self.path)
        os.mkdir(self.topic)
        os.chdir(self.topic)

        os.makedirs('images/icons')
        os.mkdir('data')
        os.mkdir('Notebooks')
        with open('README.md','w') as f:
            f.write('##' +  ' ' + self.topic)
        with open('config.json', 'w') as f:
            f.write(self.lines % (self.topic, self.filename))

    def notebooks(self):
        os.chdir('Notebooks')
        with open('config.json', 'w') as f:
                f.write(self.lines % (self.topic, self.filename))
        if self.number_of_notebooks == 1:
            nb = new_notebook()
            nb.cells.append(new_code_cell(self.notebook_lines))
            nbformat.write(nb, self.topic+'_'+self.filename + '.ipynb')
        else:
            for i in range(0, self.number_of_notebooks):
                nb = new_notebook()
                nb.cells.append(new_code_cell(self.notebook_lines))
                nbformat.write(nb,self.topic+'_'+self.filename+'%s' % i + '.ipynb')
               

    def create_icons(self):
        #print(os.getcwd())
        os.chdir(self.default_path)
        #os.chdir('..')
        src_dir = '..'+'/'+'icon'  # os.getcwd()
        dest_dir = self.path +'/' + self.topic +'/'+'images'+'/'+'icons'
        for filename in os.listdir(src_dir):
            if filename.endswith('.png'):
                print(filename)
                fullpath = os.path.join(src_dir, filename)
                shutil.copy(fullpath, dest_dir)

# ga = GitAuto('trial', 'logistic_regression_1', 'lec1',2)
# ga.create()
# ga.notebooks()
# ga.create_icons()