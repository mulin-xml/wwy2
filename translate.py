import os

files = os.listdir('uic')
for file in files:
    if file.endswith('.ui'):
        prefix = file.split('.')[0]
        print(prefix)
        os.system(f'pyside6-uic uic/{file} -o uic/{prefix}.py')
