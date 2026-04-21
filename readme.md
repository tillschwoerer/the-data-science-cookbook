# The Data Science Cookbook

This repository is a collaborative project created for the purpose of learning about Git and Github, with special focus on collaborative workflows. 

Each participant will contribute to our collaborative Cookbook by providing a single recipe of some food that he or she likes. The goal is to learn how to use Git and Github effectively, while also creating a useful resource for everyone involved. 

Every time a recipe is added, the cookbook will be automatically built and deployed as a Jupyter Book using Github Actions.

[![Deploy Jupyter Book](https://github.com/tillschwoerer/the-data-science-cookbook/actions/workflows/deploy.yml/badge.svg)](https://github.com/tillschwoerer/the-data-science-cookbook/actions/workflows/deploy.yml)



# Contribution Guidelines

## Initialization

- Each of the course participants will be added as a **collaborator** to the repository in the beginning of our class. Please please provide me with your github username or the email address that you used for your Github account.
- **Clone the central repo** to your local machine.

## Adding a recipe

- **Branch**: Create a branch for your specific contribution and switch to it. Name it according to the recipe that you are providing, e.g., `git branch pasta` and `git switch pasta`. All changes that you implement should be carried out inside your branch.
- **Develop**: Inside the `recipe/yyyy-semester` directory create a subdirectory with the name of your recipe (e.g. `pasta`). Then add a file called `recipe.md` and fill it with life. For a more consistent appearance, follow the format specified in `template.md` and add information about ingredients and cooking instructions. Add also additional information, such as cooking time, an image of the dish, or personal hints and tricks. The template serves as a guide, but feel free to adapt it to your needs. If you add an image, store it in your directory with the name (e.g. `image.jpg`) and link to it from your markdown file.
- **Commit**: Commit your changes regularly with descriptive commit messages. For example, `git commit -m "Add ingredients for pasta"`. Each recipe should have at least three commits.
- **Push**: Push your branch to the central repository. If you are pushing your branch for the first, you need to use the --set-upstream flag, e.g., `git push --set-upstream origin pasta`. For follow-up pushes, you can simply use `git push`. 
- **Submit a Pull Request**: Open your branch on Github, and make a pull request to the main branch.

## Review Process

- **Pull requests** must be reviewed by at least 2 people before they can be merged into the main branch. Conversely, each participant must review at least 2 pull requests from other participants. Look out for reviews that do not yet have sufficient approvals, and volunteer to review it.
- **Reviewers** should check for completeness and formal correctness, but can also ask for more personal touches, images, or additional hints and tricks. Don't treat the review as a mere formality. Serious code reviews make a big difference - and so do serious recipe reviews. The more feedback you provide, the better the final cookbook will be, and the more you will learn about the review process.
- **Recipe authors** should carefully consider the feedback provided by the reviewers, and implement the requested changes, or engage in a further discussion with the reviewers. 
- **Merging**: once your recipe has received **at least two approvals**, you may merge your own branch into the main branch. 
- **Conflicts**: In this simple setup, conflicts are unlikely, since everyone is working on a separate file. However, should any merge conflict arise, then of course try to resolve the conflict.