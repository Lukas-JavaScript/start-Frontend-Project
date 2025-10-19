# Frontend Project Starter

This small script creates a directory for a frontend project, optionally initializes a Git repository, and generates standard files: `index.html`, `style.css` und `script.js`.

## Requirements
- Python 3.x installed
- Optional: Git installed (if you want to initialize a repository)

## Benutzung:
1. Install Python
2. Open a terminal in your project folder.
3. Run the script:
```bash
   python main.py
   ```
4. Follow the prompts:

#### Enter the project name
#### Initialize Git? (y/n, default: y)

###### A new directory with the specified name
###### Files inside the new directory:
###### index.html (Basis-HTML)
###### style.css (empty CSS-Datei)
###### script.js (empty JS-Datei)
###### Optional: a Git repository with an initial commit ("Initial commit")
## Notes:

The script executes system commands for Git (git init, git add ., git commit -m "Initial commit"). Make sure Git is available if you choose this option.
If a directory with the same name already exists, os.mkdir(name) will fail. You can modify the script to check for existing directories or overwrite them if needed.
