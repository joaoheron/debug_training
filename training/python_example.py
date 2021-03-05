import os
#### Imports syntax ###
# import datetime
# from datetime import timedelta
from datetime import timedelta as indicium

# days = indicium(days=2)
# print(str(days))

#### Import installed lib ####
from dataml_engine.engine.postgresql import PostrgesqlEngine

#### Import local packages ####
#### ABSOLUTE & RELATIVE IMPORTS EXAMPLES #### 
# show diferences on files located on another folder, and moving file
# from training.example_folder.another_python_example import arg_1
# from example_folder.another_python_example import arg_1
# from example_folder import simple_file
# from training.example_folder import simple_file

#### SCRIPT EXECUTION EXAMPLES ####
# from example_folder.another_python_example import arg_1 # Ok
# from training.example_folder.another_python_example import arg_1
# from models import Element # Ok
# from training.models import Element

#### MODULE EXECUTION EXAMPLES ####
# from training.example_folder.another_python_example import arg_1 # Ok
# from example_folder.another_python_example import arg_1
# from training.models import Element # Ok
# from models import Element

DB_URI = os.environ.get('DB_URI')
print("DB_URI is " + str(DB_URI))

print(__package__)

print(str(os.system('pwd')))

for i in range(5):
    print(f'Current index is {str(i)}')

a = 1 + 32
b = a + 2
c = a + b

postgres_engine = PostrgesqlEngine('app.yaml', 'example_data_catalog_folder')

print(str(c))
print("Sucessfull execution")
