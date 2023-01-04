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
import os
import sys
from distutils.sysconfig import get_python_lib

import manim

sys.path.insert(0, os.path.abspath('.'))

if os.environ.get("READTHEDOCS") == "True":
    site_path = get_python_lib()
    ffmpeg_path = os.path.join(site_path, "imageio_ffmpeg", "binaries")
    print("########")
    print("good1")
    [ffmpeg_bin] = [
        file for file in os.listdir(ffmpeg_path) if file.startswith("ffmpeg-")
    ]
    print("########*****")
    print("good2")
    try:
        os.symlink(os.path.join(ffmpeg_path, ffmpeg_bin), os.path.join(ffmpeg_path, "ffmpeg"))
    except FileExistsError:
        print('File is already there!!!!!!!' )
    else:
        print('file created :)')
    print("good3")
    os.environ["PATH"] += os.pathsep + ffmpeg_path
    print("good4")

# -- Project information -----------------------------------------------------

project = 'FlyingFrames'
copyright = 'kolibril13'
author = 'kolibril13'

# The full version, including alpha/beta/rc tags


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'nbsphinx'
]
nbsphinx_allow_errors = True
pygments_style = "sphinx"
pygments_dark_style = "monokai"

autosummary_generate = False
add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_title = f"FlyingFrames v{manim.__version__}"
html_theme = 'furo'
html_logo = '_static/flyingframes_logo.png'
html_favicon = '_static/flyingframes_favicon.ico'


html_css_files = ["custom.css"]

if not os.path.exists('media/images'):
    os.makedirs('media/images')

if not os.path.exists('media/videos/480p30'):
    os.makedirs('media/videos/480p30')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'media/images', 'media/videos/480p30']