# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
from pathlib import Path

# Add the project root to the path so we can import the package
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

project = "GitHub Discussions GraphQL Client"
copyright = "2024, Bill Schumacher"
author = "Bill Schumacher"
release = "0.1.0"
version = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Core autodoc functionality
    "sphinx.ext.autosummary",  # Generate autosummary tables
    "sphinx.ext.viewcode",  # Add source code links
    "sphinx.ext.napoleon",  # Support for NumPy/Google style docstrings
    "sphinx.ext.intersphinx",  # Link to external documentation
    "sphinx.ext.todo",  # Support for todo items
    "sphinx_rtd_theme",  # Read the Docs theme
]

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
    "inherited-members": True,
    "show-inheritance": True,
}

# Configure autodoc to handle inheritance properly
autodoc_inherit_docstrings = True
autoclass_content = "both"

# Suppress warnings for duplicate object descriptions
suppress_warnings = ["ref.python"]

# Additional autodoc settings to reduce duplicates
autodoc_member_order = "bysource"

# Autosummary settings
autosummary_generate = True

# Napoleon settings for Google/NumPy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Intersphinx mapping for external documentation
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
    "pydantic": ("https://docs.pydantic.dev/latest/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "#2980B9",
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# -- Options for manual page output ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-manual-page-output

man_pages = [
    (
        "index",
        "githubdiscussions",
        "GitHub Discussions GraphQL Client Documentation",
        [author],
        1,
    )
]

# -- Options for Texinfo output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-texinfo-output

texinfo_documents = [
    (
        "index",
        "GitHubDiscussions",
        "GitHub Discussions GraphQL Client Documentation",
        author,
        "GitHubDiscussions",
        "A Python package for interacting with GitHub Discussions using GraphQL API.",
        "Miscellaneous",
    ),
]

# -- Extension configuration --------------------------------------------------

# Todo extension
todo_include_todos = True
