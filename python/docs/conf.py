# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xmf'
copyright = '2025, Lei Huang'
author = 'Lei Huang and Ruochen Xu'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # For automatic documentation generation
    'sphinx.ext.napoleon',  # For Google/NumPy docstrings
    'sphinx.ext.viewcode',  # Add links to source code
    'sphinx.ext.autosummary',  # to generate function lists/tables

    'sphinxcontrib.matlab',  # For MATLAB domain support
    'sphinx_gallery.gen_gallery', # For generating example galleries
]

sphinx_gallery_conf = {
    # Path to your example scripts
    'examples_dirs': 'examples',       # <-- folder with example .py scripts
    # Path to where gallery pages will be generated
    'gallery_dirs': 'auto_examples',   # <-- generated output
    'filename_pattern': r'.*\.py',     # run all .py scripts
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'

# -- Options for MATLAB domain -----------------------------------------------
this_dir = os.path.dirname(os.path.abspath(__file__))
matlab_src_dir = os.path.abspath(os.path.join(this_dir, '..','..'))
