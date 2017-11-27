# Test-case-Automation

README
This is a repository to generate files for a lecture that which includes the data folder the images/icon folder and the Notebooks folder which contains the notebooks for a specific topic. Apart from this two json files are created one in the repository and the other in the notebook folder. Also, a README.md file is created.
What is this repository for?
Automate the git folder creation process
contains a class GitAuto with methods to create folders for Lecture.
contains a class CreateProject with methods to create folders for project.
How is this repository set up?
This repository contains three directories
texts: this repositories contains texts config.txt which are then written to config.json file and
try.py which is written to a cell of ipython notebook
icon : contains icons which are copied to images/icons
generation: this contains one class for now the GaAuto class in git_automation.py which is used to generate lecture notebooks. This also contains a class test_generation.py which is used to generate test cases by locating the folders that end with _project in the specified location.
build: this text file contains the contain the content for the build.py file
How to use it?
To use the code call the class with the following parameters
Lecture Generation
path : which specifies the path where the repo will be created.
the name of the topic which would be the topic for which the folder is created.
filename - the name of the lecture notebook to be created
the number_of_notebooks : the number of notebooks wiht the name filename to be created. Here the default is 1. If the value is chaged notebooks are formed as filename+0,filename+1 the list starts from 0.
Project Generation
path : which specifies the path where the repo will be created.
build_content : Content for the build.py
name : the name of the topic for which the folder to be created.
folder_names : the subfolders which needs to be created for that topic.
Test Generation
path_to_find : which specifies the path where the repo's are created. The test.py is created only when the data folder contains data. This is because the name of the data file is used in the path.
