GitHub Discussions GraphQL Client
==================================

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

.. image:: https://badge.fury.io/py/github-discussions.svg
   :target: https://badge.fury.io/py/github-discussions
   :alt: PyPI version

A comprehensive Python package for interacting with GitHub Discussions using the GraphQL API.

This package provides a clean, type-safe interface for managing discussions, comments, and related functionality on GitHub.

Features
--------

🔐 **Secure Authentication**: Support for personal access tokens and GitHub Apps
📝 **Full Discussion Management**: Create, read, update, and delete discussions
💬 **Comment Management**: Handle discussion comments with full CRUD operations
🏷️ **Category Support**: Work with discussion categories
⭐ **Pin/Unpin Discussions**: Manage pinned discussions
🎯 **Answer Marking**: Mark comments as answers
📊 **Advanced Pagination**: Fixed cursor-based pagination with automatic iteration
🔍 **Search Integration**: Search discussions using GitHub's search API
🛡️ **Type Safety**: Full type hints and Pydantic models
⚡ **Async Support**: Optional async/await support
🧪 **Well Tested**: Comprehensive test coverage
🏗️ **Clean Architecture**: Refactored to eliminate code duplication between sync/async clients

Installation
------------

.. code-block:: bash

   pip install github-discussions

Quick Start
-----------

.. code-block:: python

   from github_discussions import GitHubDiscussionsClient

   # Initialize the client
   client = GitHubDiscussionsClient(token="your_github_token")

   # Get discussions for a repository
   discussions = client.get_discussions(
       owner="octocat",
       repo="Hello-World",
       first=10
   )

   # Create a new discussion
   discussion = client.create_discussion(
       repository_id="R_kgDOAHz1OX",
       category_id="DIC_kwDOAHz1OX4CW5wG",
       title="My New Discussion",
       body="This is the content of my discussion"
   )

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   getting_started
   authentication
   basic_usage
   advanced_usage
   error_handling

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   api/client
   api/async_client
   api/exceptions
   api/models

.. toctree::
   :maxdepth: 2
   :caption: Development:

   contributing
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
