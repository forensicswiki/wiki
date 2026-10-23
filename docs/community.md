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
include forensics relevant tradeoffs. Make sure any external links you add are publicly
accessible. Links with signup or paywalls, or that are geo-restricted, will be removed.
For more detail see the style guide.

Step 6. Create PR for review

<!-- ## TODO: Example Using the GitHub Web UI -->

## Suggesting New Tags

There might be an article that does not fit well within the tagging guidelines in the style guide.
If you want to suggest a new tag, please open a
[GitHub Issue](https://github.com/forensicswiki/wiki/issues).
