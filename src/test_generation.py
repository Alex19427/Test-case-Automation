import os

class TestCaseGeneration:
    def __init__(self,path_to_find):
        self.projects=[]
        self.path_to_find = path_to_find
        self.default_path = os.getcwd()

    def find_folders(self):
        for i in os.listdir(self.path_to_find):
            if i.endswith('_project'):
                self.projects.append(i)


    def generate_test_cases(self):
        self.find_folders()
        txt_path = '..' + '/' + 'texts'
        os.chdir(self.default_path)
        with open(os.path.join(txt_path,'test_template.txt'),'r') as f:
            lines = f.read()
        for i in self.projects:
            os.chdir(self.path_to_find + '/' + i)
            new_dir = os.getcwd()
            # print(new_dir)
            for j in os.listdir():
                os.chdir(self.path_to_find+'/'+i + '/' + 'data')
                for k in os.listdir():
                    dfile = []
                    if k.endswith('.csv') or k.endswith('.zip'):
                        dfile.append(k)
                os.chdir(new_dir)
                if j.startswith('q0') and not j.endswith('.ipynb'):
                    os.chdir(self.path_to_find+'/' +i+'/' + j)
                    os.mkdir('tests')
                    os.chdir('tests')
                    #             os.mkdir('try_test1')
                    #             os.chdir('try_test1')

                    with open('test.py', 'w') as f:
                        new_content = lines.format(module=j, datafile=dfile[0])
                        f.write(new_content)
        os.chdir(self.path_to_find)



#ta = TestCaseGeneration(r'C:/Users/Alex/Desktop/Greyatom/Project/Z_project')
#ta.generate_test_cases()
