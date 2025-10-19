import os

name = input("Enter the name for the project: ")
git = input("Do you want to initialize a git repository? (y/n) (default: y): ").lower()
os.mkdir(name)
os.chdir(name)
if git == '':
    git = 'y'
if git == 'y':
    os.system(f'git init')
else:
    pass

