# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import sphinx_bootstrap_theme


# import os
# import sys

# sys.path.insert(0, os.path.abspath('.'))

# sys.path.append(os.path.abspath('_themes'))
# html_theme_path = ['_themes']

html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

bootswatch_theme = "sandstone"

html_theme = 'bootstrap'

html_short_title = 'CV'

html_logo = "../bunny.png"

# -- Project information -----------------------------------------------------

project = 'TW'
copyright = '2020, HB'
author = 'HB'

# The full version, including alpha/beta/rc tags
release = '0.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel', 'rst2pdf.pdfbuilder'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# pdf options

pdf_documents = [('index', u'Techwriter-CV', u'TechWriter-CV', u'Harrie'),]
  
  # index - master document
  # u1 - name of the generated pdf
  # u2 - title of the pdf
  # u3 - author name in the pdf

# Generate pdf
# sphinx-build -b pdf source build/pdf

# possible 
# html_theme_options = {
#    'canonical_url': 'http://www.technobunnies.com/',
#    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
#    'logo_only': False,
#   'display_version': True,
#    'prev_next_buttons_location': 'bottom',
#    'style_external_links': False,
#    'vcs_pageview_mode': '',
#    'style_nav_header_background': 'white',
    # Toc options
#    'collapse_navigation': True,
#    'sticky_navigation': True,
#    'navigation_depth': -1,
#    'includehidden': True,
#    'titles_only': False
#}

html_theme_options = {

# Fingers crossed we are playing with the right switches!
# From https://pypi.org/project/sphinx-bootstrap-theme/
# http://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html

    # HTML navbar class (Default: "navbar") to attach to <div>.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer".
    'source_link_position': "nav",

     'navbar_site_name': "Technical Writing CV in rST",

# Render the next and previous page links in navbar. (Default: true)
     'navbar_sidebarrel': True,

 # Render the current pages TOC in the navbar. (Default: true)
     'navbar_pagenav': True,

         # Currently, the supported themes are:
    # - Bootstrap 2: https://bootswatch.com/2
    # Bootstrap 3: https://bootswatch.com/3
    

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    # 'bootstrap_version': "3",
}
