#!/bin/bash
#
# Script to build an index.rst for sphinx-build -b linkcheck

cat >docs/index.rst <<EOT
ForensicsWiki linkcheck
=======================

.. toctree::
   :maxdepth: 1

EOT

(cd docs && ls -1 *.md | sed 's|\(.*\)\.md|   <\1>|' >> index.rst)

