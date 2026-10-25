# Mkdocs tips &amp; tricks

## Check Content Formatting

There have been some differences in how certain IDE's such as Visual Studio (VS) code and MkDocs
render Markdown. What this means is that when creating a page in Forensics Wiki, some content looks
fine in VS code but then once committed to Github the content is not displaying properly. To ensure
content is formatted correctly, you could use a local MkDocs install which has a built in
development server. Follow the steps below to install MkDocs. Steps 1 and 2 are optional.

### Install MkDocs

Step 1. Setup a Python environment

```bash
python3 -m venv mkdocs
```

Step 2. Activate Python environment

```bash
source mkdocs/bin/activate
```

Step 3. Install MkDocs on your system.

```bash
pip3 install mkdocs-material mkdocs-redirects mkdocs-title-casing-plugin
```

### Run MkDocs

Next, we want MkDocs to load all of the pages of the Forensics Wiki. MkDocs needs two things to be
able to run and load the Forensics Wiki pages.

* It will need a `docs` directory which holds all of Forensics Wiki pages.
* It will the `mkdocs.yml` configuration file. This is the configuration that tells MkDocs how to
  structure the site such as the structure of the menus.

Both of the previous items are located in the root directory of the repository. To run MkDocs
development server follow the steps below:

Step 1. Change to the root of the repository. For example, if you cloned the repository to your
home directory.

```bash
cd ~/wiki
```

Step 2. Start local MkDocs server

```bash
mkdocs serve
```

Step 3. Open your browser and visit <http://127.0.0.1:8000/your_doc_name>

## Tags

### Linking to a tag

To link to a tag, e.g. the "Concept" tag:

```text
https://forensics.wiki/tags/#tag:concept
```

### Including a tag as content

Forensics Wiki uses Material for MkDocs which supports generating a list of articles with a
specific tag as part of its content as following:

```html
<!-- material/tags { include: ["File Formats"] } -->
```

Which generates the list under "File formats documented in this wiki" in
[File formats](https://forensics.wiki/file_formats/).
