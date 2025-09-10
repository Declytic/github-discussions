Getting Started
===============

Installation
------------

Install the GitHub Discussions GraphQL Client using pip:

.. code-block:: bash

   pip install github-discussions

For development installation with extra dependencies:

.. code-block:: bash

   git clone https://github.com/Declytic/github-discussions.git
   cd github-discussions
   pip install -e ".[dev]"

Requirements
------------

- Python 3.8 or higher
- A GitHub Personal Access Token with appropriate permissions

Basic Usage
-----------

Here's a simple example to get you started:

.. code-block:: python

   from github_discussions import GitHubDiscussionsClient

   # Initialize the client with your GitHub token
   client = GitHubDiscussionsClient(token="your_github_token_here")

   # Get discussions from a repository
   discussions = client.get_discussions("owner", "repo", first=5)

   for discussion in discussions:
       print(f"Discussion: {discussion.title}")
       print(f"Author: {discussion.author.login}")
       print(f"Comments: {discussion.comments_count}")
       print("---")

Next Steps
----------

- :doc:`authentication` - Learn about different authentication methods
- :doc:`basic_usage` - Explore basic operations
- :doc:`advanced_usage` - Discover advanced features
- :doc:`api/client` - Complete API reference
