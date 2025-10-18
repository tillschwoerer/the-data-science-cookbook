# The Data Science Cookbook

This repository is a collaborative project created for the purpose of learning about Git and Github, with special focus on collaborative workflows. 

Each participant will contribute to our collaborative Cookbook by providing a single recipe of some food that he or she likes. The goal is to learn how to use Git and Github effectively, while also creating a useful resource for everyone involved. 

Every time a recipe is added, the cookbook will be automatically built and deployed as a Jupyter Book using Github Actions. The final book can be accessed [here](https://tillschwoerer.github.io/the-data-science-cookbook).

[![Deploy Jupyter Book](https://github.com/tillschwoerer/the-data-science-cookbook/actions/workflows/deploy.yml/badge.svg)](https://github.com/tillschwoerer/the-data-science-cookbook/actions/workflows/deploy.yml)



## Contribution Guidelines

### Initialization

- Each of the course participants will be added as a **collaborator** to the repository in the beginning of our class. Please please provide me with your github username or the email address that you used for your Github account.
- **Clone the central repo** to your local machine.

### Making Contributions

- **Create a New Branch**: Create a branch for your specific contribution. Name it according to the recipe that you are providing, e.g., `git branch pasta`.
- **Switch to New Branch**: All changes that you implement should be carried out inside your branch. So, switch to your branch via, e.g. `git switch pasta`.
- **Create Markdown file**: Create a markdown file for your recipe and save it in the recipes folder. Name the file according to the dish that you are adding, e.g. `pasta.md`.
- **Edit the File**: Follow the format specified in `template.md` and add information about ingredients and cooking instructions. Add also additional information, such as cooking time, an image of the dish, or personal hints and tricks. The template serves as a guide, but feel free to adapt it to your needs. If you add an image, store it in the `images` folder and link to it from your markdown file.
- **Commit Your Changes**: Commit your changes regularly with descriptive commit messages. For example, `git commit -m "Add ingredients for pasta"`. Each recipe should have at least three commits.
- **Push Your Changes**: Push your branch to the central repository. If you are pushing your branch for the first, you need to use the --set-upstream flag, e.g., `git push --set-upstream origin pasta`. For follow-up pushes, you can simply use `git push`. 
- **Submit a Pull Request**: Go to the respective branch of the central repository, and make a pull request to the main branch for integration and review.

### Review Process and Merging
- Pull requests must be reviewed by at least 2 people before they can be merged into the main branch. 
- And conversely, each participant should review at least 2 pull requests from other participants. 
- Each participant should look out for reviews that do not yet have sufficient approvals, and volunteer to review it.
- Reviewers should check check for completeness, clarity, and formal correctness. However, you can also ask for more personal touches, images, or additional hints and tricks.
- Don't treat the review process as a mere formality. Instead, take it seriously: the reviewer should provide constructive feedback, and the author should carefully consider the reviewer's comments and suggestions, and update the file accordingly.
- Pull requests can be merged into the main branche once they have been approved by two participants.
- Note: In this simple setup, conflicts are unlikely, since everyone is working on a separate file. However, should any merge conflict arise, then try to resolve the conflict (either locally or on Github).