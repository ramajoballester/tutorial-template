# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'numpydoc',
    'sphinx.ext.autodoc.typehints',
    'myst_parser',      # For markdown support
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
    'sphinx.ext.viewcode',
    'sphinx_markdown_tables',
    'sphinx.ext.napoleon',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
# html_theme = 'pytorch_sphinx_theme'

# html_theme_options = {
#     'navigation_with_keys': True
# }

html_theme_options = {

}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Configure autodoc to generate documentation for both class and module docstrings
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}


# add_module_names = False

# The suffix(es) of source filenames (not needed with MyST ?).
# You can specify multiple suffix as a list of string:
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
# }
