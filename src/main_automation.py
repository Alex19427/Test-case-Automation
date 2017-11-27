from main_lecture import CreateLecture
from main_project import AutoProject
#from main_test_generation import TestGeneration

destination = '/Users/abhisheksubramanian/Desktop/test_automation'
topic = 'linear_regression_in_class'
number_of_notebooks = 3
folder_names = ['data','images','q01_lliaear', 'q02_plot', 'q03_question3']
name = ['linear_regression_project']


CreateLecture(destination,topic,'lec1',number_of_notebooks).call()
AutoProject(destination,name,folder_names).callproject()
#TestGeneration(destination).calltestcase()


