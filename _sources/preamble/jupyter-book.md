# Jupyter Book

All recipes provided as markdown files are compiled into a Jupyter Book hosted under https://tillschwoerer.github.io/data-science-cookbook-ws25

Here I will explain, how this is achieved. 

## Steps to create a Jupyter Book manually

1. Install the Jupyter Book package using pip:
```bash
pip install jupyter-book
```
2. Create a configuration `_config.yml` file for the Jupyter Book, which contains settings for the book, such as the title and author.

3. Define the book's structure via a file named `_toc.yml` (table of contents). Note that the file names need to be provided without the extension (.md)

4. Write the content of the book in markdown files (this is what we are doing collaboratively). Each recipe is a separate markdown file, and the recipes are organized into folders according to the structure defined in `_toc.yml`.

5. We build the HTML files for the book in a folder named `_build/html` via: 

```bash
jupyter-book build .
```

Optionally, you can preview the book locally using:
```bash
start _build/html/index.html  # Windows
open _build/html/index.html   # MacOS
```

6. Activate Github Pages for the repository: on Github navigate to Settings -> Pages -> Deploy from a branch -> gh-pages

This will create a new branch named `gh-pages` in your repository, which will host the HTML files of your book.

7. We push the `_build/html` folder to the `gh-pages` branch of our Github repository. 
```bash
pip install ghp                     # Install the package ghp once
ghp-import -n -p -f _build/html     # Execute for push to gh-pages
```

Note: every time a new recipe is added, the book needs to be rebuilt and the updated HTML files need to be pushed to the `gh-pages` branch. Hence, the steps number 3 (update the table of contents), 5 (build the book), and 7 (push to gh-pages) would need to be repeated.

# Automating deployment via Github Actions

To avoid the manual steps of rebuilding and deploying the book every time a new recipe is added, we can automate this process using Github Actions.

This is achieved via (1) the workflow defined in the file `.github/workflows/deploy.yml` and (2) a small python script `scripts/generate_toc.py` that automatically updates generates the table of contents based on the markdown files in the `recipes` folder.


