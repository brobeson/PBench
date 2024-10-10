"""Configuration file for the Sphinx documentation builder."""

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# pylint: disable=invalid-name
# cspell: words furo

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PBench"
project_copyright = "2024, brobeson"
author = "brobeson"
version = "0.0.0"
release = "0.0.0"
highlight_language = "python"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "furo"
html_static_path = ["_static"]
# https://pradyunsg.me/furo/customisation/
html_theme_options = {
    # "light_css_variables"
    # "dark_css_variables"
    # "sidebar_hide_name": True,     # Keep the name in the side bar
    # "navigation_with_keys": True,  # Don't see this doing anything
    # "top_of_page_buttons": ["edit", "view"],
    # "source_repository": "https://github.com/brobeson/PBench",
    # "source_branch": "14-configure-read-the-docs-project",
    # "source_directory": "docs/source/",
}
