GitHubDiscussionsClient
========================

The main synchronous client for interacting with GitHub Discussions.

.. autoclass:: github_discussions.client.GitHubDiscussionsClient
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

Initialization
--------------

.. automethod:: github_discussions.client.GitHubDiscussionsClient.__init__
   :no-index:

Discussion Operations
---------------------

.. automethod:: github_discussions.client.GitHubDiscussionsClient.get_discussions
   :no-index:

.. automethod:: github_discussions.client.GitHubDiscussionsClient.get_discussion
   :no-index:

.. automethod:: github_discussions.client.GitHubDiscussionsClient.create_discussion
   :no-index:

Comment Operations
------------------

.. automethod:: github_discussions.client.GitHubDiscussionsClient.get_discussion_comments
   :no-index:

.. automethod:: github_discussions.client.GitHubDiscussionsClient.add_discussion_comment
   :no-index:

Category Operations
-------------------

.. automethod:: github_discussions.client.GitHubDiscussionsClient.get_discussion_categories
   :no-index:

Pinned Discussions
------------------

.. automethod:: github_discussions.client.GitHubDiscussionsClient.get_pinned_discussions
   :no-index:

Utility Methods
---------------

.. automethod:: github_discussions.client.GitHubDiscussionsClient.get_rate_limit_status
   :no-index:

.. automethod:: github_discussions.client.GitHubDiscussionsClient.execute_query
   :no-index:

Context Manager
---------------

The client can be used as a context manager for automatic resource cleanup:

.. code-block:: python

   with GitHubDiscussionsClient(token="your_token") as client:
       discussions = client.get_discussions("owner", "repo")
       # Session is automatically closed
