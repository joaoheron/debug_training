import os
# import os as indicium
# from os import environ

# from another_python_example import arr_1
from training.example_folder.another_python_example import arr_1

# from training.models import elemento
import training.models.elemento
# from ..models import Element, elemento
from training import models

DB_URI_DEV = os.environ.get('DB_URI_DEV')
print("env var DB_URI_DEV is " + str(DB_URI_DEV))

print(__package__)

print(str(os.system('pwd')))

for i in range(5):
    print(f'Current index is {str(i)}')

a = 1 + 32
b = a + 2
c = a + b

print(str(c))
