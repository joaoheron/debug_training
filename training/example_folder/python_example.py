#### Imports syntax ###

import os
# from os import environ
# import os as indicium

#### Import installed lib ####

from dataml_engine.engine.postgresql import PostrgesqlEngine

#### Import local files ####

# from another_python_example import arr_1
from training.example_folder.another_python_example import arr_1
from training.models import elemento
# import training.models.elemento
# from ..models import Element, elemento
from training import models

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
