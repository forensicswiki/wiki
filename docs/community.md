# How to Contribute

The Forensics Wiki has moved to GitHub, which has required some changes in the contributing process.

In order to add or update a page, you will need to create or edit a
[Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
file. You can do this in multiple ways, but the general flow is to:

* Copy (or "fork") the [Forensics Wiki](https://github.com/forensicswiki/wiki) GitHub project. You
  can then download ("clone") this copy to your computer to work on, or edit.
* Make your additions or edits to an article's Markdown file, such as: "plaso.md".
* Contribute your changes back to the main Forensics Wiki project for review, also referred to as
  submitting a "pull request". This will trigger some automated validation.
* A maintainer will review your changes, request edits if necessary, and once everything looks
  good, add it to the site ("merge" it)

GitHub has some excellent documentation on
[contributing to projects](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)
if you'd like a more detailed explanation.

The naming, content, style, and tagging conventions for articles are documented in the
[style guide](https://github.com/forensicswiki/wiki/blob/main/style_guide.md).

## Example Using the Command Line

Step 1. Fork the Forensics Wiki project

Step 2. Clone the fork and set Forensics Wiki as the upstream

```bash
git clone https://github.com/[your-github-user-id]/wiki.git
cd wiki
git remote add upstream https://github.com/forensicswiki/wiki.git
```

Step 3. Create a branch for new articles or article updates

```bash
git checkout -b [article-branch-name]
```

Step 4. Make your changes to the Markdown file(s) and push changes to your repository.

```bash
git push origin [article-branch-name]
```

Step 5. Checklist before creating a PR

Make sure your changes contain digital forensic relevant information, e.g. when listing tools
include forensics relevant tradeoffs. For more detail see the style guide.

Step 6. Create PR for review

<!-- ## TODO: Example Using the GitHub Web UI -->

## Check Content Formatting

There have been some differences in how certain IDE's such as Visual Studio code and mkdocs
render Markdown. What this means is that when creating a page in Forensicswiki, some content looks
fine in VS code but then once committed to Github the content is not displaying properly. To ensure
content is formatted correctly, you could use a local mkdocs install which has a built in
development server. Follow the steps below to install mkdocs. Steps 1 and 2 are optional.

### Install mkdocs

Step 1. Setup a Python environment

```bash
python3 -m venv mkdocs
```

Step 2. Activate Python environment

```bash
source mkdocs/bin/activate
```

Step 3. Install mkdocs on your system.

```bash
pip3 install mkdocs-material mkdocs-redirects mkdocs-title-casing-plugin
```

### Run mkdocs

Next, we want mkdocs to load all of the pages of the Forensics Wiki. Mkdocs needs two things to be
able to run and load the Forensics Wiki pages.

* It will need a `docs` directory which holds all of Forensics Wiki pages.
* It will the `mkdocs.yml` configuration file. This is the configuration that tells mkdocs how to
  structure the site such as the structure of the menus.

Both of the previous items are located in the root directory of the repository. To run mkdocs
development server follow the steps below:

Step 1. Change to the root of the repository. For example, if you cloned the repository to your
home directory.

```bash
cd ~/wiki
```

Step 2. Start local mkdocs server

```bash
mkdocs serve
```

Step 3. Open your browser and visit <http://127.0.0.1:8000/your_doc_name>

## Suggesting New Tags

There might be an article that does not fit well within the tagging guidelines in the style guide.
If you want to suggest a new tag, please open a
[GitHub Issue](https://github.com/forensicswiki/wiki/issues).
