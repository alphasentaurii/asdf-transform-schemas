# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.
# See astropy.sphinx.conf for which values are set there.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))
# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for astropy or Astropy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory (if "python setup.py build_sphinx" is used).
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.

import datetime
import os
import sys
from pathlib import Path

# Ensure documentation examples are determinstically random.
import numpy
import tomli
from pkg_resources import get_distribution

try:
    numpy.random.seed(int(os.environ["SOURCE_DATE_EPOCH"]))
except KeyError:
    pass

try:
    from sphinx_astropy.conf.v1 import *  # noqa
except ImportError:
    print("ERROR: the documentation requires the sphinx-astropy package to be installed")
    sys.exit(1)

# Get configuration information from `pyproject.toml`
with open(Path(__file__).parent.parent / "pyproject.toml", "rb") as configuration_file:
    conf = tomli.load(configuration_file)
configuration = conf["project"]

# -- General configuration ----------------------------------------------------

project = configuration["name"]
author = f"{configuration['authors'][0]['name']} <{configuration['authors'][0]['email']}>"
copyright = f"{datetime.datetime.now().year}, {configuration['authors'][0]}"

release = get_distribution(configuration["name"]).version
version = ".".join(release.split(".")[:2])

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.2'

intersphinx_mapping["pypa-packaging"] = ("https://packaging.python.org/en/latest/", None)  # noqa
intersphinx_mapping["asdf-astropy"] = ("https://asdf-astropy.readthedocs.io/en/latest/", None)  # noqa
intersphinx_mapping["pytest"] = ("https://docs.pytest.org/en/latest/", None)  # noqa

# Docs are hosted as a "subproject" under the main project's domain: https://www.asdf-format.org/projects
# This requires including links to main project (asdf-website) and the other asdf subprojects
# See https://docs.readthedocs.io/en/stable/guides/intersphinx.html#using-intersphinx
subprojects = {
    # main project
    "asdf-website": ("https://www.asdf-format.org/en/latest", None),
    # other subprojects
    "asdf": ("https://asdf.readthedocs.io/en/latest/", None),
    "asdf-coordinates-schemas": ("https://www.asdf-format.org/projects/asdf-coordinates-schemas/en/latest/", None),
    "asdf-standard": ("https://asdf-standard.readthedocs.io/en/latest/", None),
    "asdf-wcs-schemas": ("https://www.asdf-format.org/projects/asdf-wcs-schemas/en/latest/", None),
}

intersphinx_mapping.update(subprojects) # noqa

# To perform a Sphinx version check that needs to be more specific than
# major.minor, call `check_sphinx_version("x.y.z")` here.
# check_sphinx_version("1.2.1")

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns.append("_templates")  # noqa

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog += """"""  # noqa

# -- Project information ------------------------------------------------------

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# -- Options for HTML output ---------------------------------------------------

# A NOTE ON HTML THEMES
# The global astropy configuration uses a custom theme, 'bootstrap-astropy',
# which is installed along with astropy. A different theme can be used or
# the options for this theme can be modified by overriding some of the
# variables set in the global configuration. The variables set in the
# global configuration are listed below, commented out.

# Add any paths that contain custom themes here, relative to this directory.
# To use a different custom theme, add the directory containing the theme.
# html_theme_path = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes. To override the custom theme, set this to the
# name of a builtin theme or the name of a custom theme in html_theme_path.
html_theme = "furo"

html_static_path = ["_static"]

# Custom sidebar templates, maps document names to template names.
# Override default settings from sphinx_asdf / sphinx_astropy (incompatible with furo)
html_sidebars = {}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/images/favicon.ico"
html_logo = ""
html_theme_options = {
    "light_logo": "images/logo-light-mode.png",
    "dark_logo": "images/logo-dark-mode.png",
}

pygments_style = "monokai"
# NB Dark style pygments is furo-specific at this time
pygments_dark_style = "monokai"
# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = ''

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f"{project} v{release}"

# Output file base name for HTML help builder.
htmlhelp_basename = project + "doc"

# Render inheritance diagrams in SVG
graphviz_output_format = "svg"

graphviz_dot_args = [
    "-Nfontsize=10",
    "-Nfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Efontsize=10",
    "-Efontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Gbgcolor=white",
    "-Gfontsize=10",
    "-Gfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
]

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [("index", project + ".tex", project + " Documentation", author, "manual")]

latex_logo = "_static/images/logo-light.png"


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", project.lower(), project + " Documentation", [author], 1)]

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname("__file__")), "sphinxext"))
extensions += ["sphinx_asdf", "sphinx.ext.intersphinx", "sphinx.ext.extlinks"]  # noqa


def setup(app):
    app.add_css_file("custom.css")


# -- sphinx_asdf configuration ---------------------------------------------

# Top-level directory containing ASDF schemas (relative to current directory)
asdf_schema_path = "../resources/stsci.edu"
# This is the prefix common to all schema IDs in this repository
asdf_schema_standard_prefix = "schemas"
