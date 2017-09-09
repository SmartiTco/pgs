#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath('.'))


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'Seiya'
copyright = '2017'
author = 'Stanvah'

# The short X.Y version.
version = '0.1.0'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

language = None

# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

todo_include_todos = False

# a list of builtin themes.
html_theme = 'alabaster'

html_theme_options = {
    'github_user': 'blaringsilence',
    'github_repo': 'pegasus',
    'github_banner': 'true',
    'head_font_family':'Hagin Caps Medium'
}

html_logo = '_static/docs_logo.png'

html_static_path = ['_static']

htmlhelp_basename = 'Pegasusdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'PSeiya.tex', 'Seiya Documentation',
     'Stanvah', 'manual'),
]

man_pages = [
    (master_doc, 'seyia', 'Seyia Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Seiya', 'Seiya Documentation',
     author, 'Seiya', 'One line description of project.',
     'Miscellaneous'),
]
