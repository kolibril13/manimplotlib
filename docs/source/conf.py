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
    # we need to add ffmpeg to the path
    ffmpeg_path = os.path.join(site_path, "imageio_ffmpeg", "binaries")
    # the included binary is named ffmpeg-linux..., create a symlink
    [ffmpeg_bin] = [
        file for file in os.listdir(ffmpeg_path) if file.startswith("ffmpeg-")
    ]
    os.symlink(
        os.path.join(ffmpeg_path, ffmpeg_bin), os.path.join(ffmpeg_path, "ffmpeg")
    )
    os.environ["PATH"] += os.pathsep + ffmpeg_path

# -- Project information -----------------------------------------------------

project = 'manimplotlib'
copyright = '2021, kolibril13'
author = 'kolibril13'

# The full version, including alpha/beta/rc tags
release = '4/2021'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'manim_directive',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

pygments_style = 'material'

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

# html_title = f"Manimplotlib v{manim_rubikscube.__version__}"
html_theme = 'furo'
#html_logo = '_static/logo.png'

html_css_files = ["custom.css"]

if not os.path.exists('media/images'):
    os.makedirs('media/images')

if not os.path.exists('media/videos/480p30'):
    os.makedirs('media/videos/480p30')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'media/images', 'media/videos/480p30']