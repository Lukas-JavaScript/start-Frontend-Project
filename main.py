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
print(f"Project '{name}' created successfully.")
with open('index.html', 'w') as f:
    f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
</head>
<body>
    <h1>Welcome to {name}</h1>
</body>
</html>
""")
    f.close()
with open('style.css', 'w') as f:
    f.close()
with open('script.js', 'w') as f:
    f.close()
os.system('git add .')
os.system('git commit -m "Initial commit"')
print("Created index.html, style.css, and script.js files.")
