# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Path setup -----------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# Project information --------------------------------------------------------
project = 'loyverse'
copyright = '2020, Matteo Berchier'
author = 'Matteo Berchier'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# General configuration ------------------------------------------------------
# Extensions
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

# Autodoc configurations
autoclass_content = 'class'

# Napoleon configurations
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_use_admonition_for_examples = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '**.ipynb_checkpoints',
    '**.ipynb',
    'tests',
]


# HTML output options -----------------------------------------------------
# HTML theme
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    "css/custom.css",
]

# HTML Configuration of pydata_sphinx_theme ---------------------------------
html_logo = '_static/loyverse.png'
html_favicon = '_static/favicon.ico'

html_context = {
    'github_user': 'matteobe',
    'github_repo': 'loyverse',
    'github_version': 'master',
    'doc_path': 'docs/source/'
}

# HTML theme options --------------------------------------------------------
html_theme_options = {
    'github_url': 'https://github.com/matteobe/loyverse',
    'show_prev_next': False,
    'use_edit_page_button': True,
    'search_bar_text': 'Search the documentation...',
}

# If false, no module index is generated.
html_use_modindex = True
