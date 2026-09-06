# importing whole file and not just a function:
from my_module_dir import my_module_file_1

my_module_file_1.hello_name('Aleks')  # Hello Aleks
my_module_file_1.hello_name()         # Hello Someone (default value)
