# Septic-Hooks

Pre-commit hooks useful for Septic development.

Pre-commit hooks automatically runs before a commit is made to git repository to perform ceratin tasks like formatting, testing etc.

## Setup

1. Follow installation guide for [pre-commit](https://pre-commit.com/#install) using pip. Verify the installation by running `pre-commit --version`.
2. In the root of the relevant repository add a file name `.pre-commit-config.yaml` and add the following content to the file:

```
repos:
  - repo: https://github.com/equinor/septic-hooks
    rev: v0.0.2
    hooks:
      - id: export-source-to-csv
```

3. Setup the git hook script for the repo by running `pre-commit install`
4. Run the git hooks against all files to generate the expected files by running `pre-commit run --all-files`.
5. Add generated data files (one csv file for each sheet in excel files used in scg) to source control (i.e. add them to a commit).

The git hook will now run each time a commit is made and generate csv files from the excel files that has been updated since last commit. If a change is detected to the generated files, the commit failes and you have to add the updated csv files before commiting again.
