AsyncGitHubDiscussionsClient
=============================

The asynchronous client for interacting with GitHub Discussions.

.. autoclass:: github_discussions.async_client.AsyncGitHubDiscussionsClient
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

Initialization
--------------

.. automethod:: github_discussions.async_client.AsyncGitHubDiscussionsClient.__init__
   :no-index:

Async Context Manager
---------------------

The async client must be used as an async context manager:

.. code-block:: python

   import asyncio
   from github_discussions import AsyncGitHubDiscussionsClient

   async def main():
       async with AsyncGitHubDiscussionsClient(token="your_token") as client:
           discussions = await client.get_discussions("owner", "repo")
           # Session is automatically closed

   asyncio.run(main())

Discussion Operations
---------------------

.. automethod:: github_discussions.base_client.BaseGitHubDiscussionsClient.get_discussions
   :no-index:

.. automethod:: github_discussions.base_client.BaseGitHubDiscussionsClient.get_discussion
   :no-index:

.. automethod:: github_discussions.base_client.BaseGitHubDiscussionsClient.create_discussion
   :no-index:

Comment Operations
------------------

.. automethod:: github_discussions.async_client.AsyncGitHubDiscussionsClient.get_discussion_comments
   :no-index:

.. automethod:: github_discussions.async_client.AsyncGitHubDiscussionsClient.add_discussion_comment
   :no-index:

Category Operations
-------------------

.. automethod:: github_discussions.async_client.AsyncGitHubDiscussionsClient.get_discussion_categories
   :no-index:

Pinned Discussions
------------------

.. automethod:: github_discussions.async_client.AsyncGitHubDiscussionsClient.get_pinned_discussions
   :no-index:

Utility Methods
---------------

.. automethod:: github_discussions.base_client.BaseGitHubDiscussionsClient.get_rate_limit_status
   :no-index:

.. automethod:: github_discussions.base_client.BaseGitHubDiscussionsClient.execute_query
   :no-index:

Async Iteration
---------------

The async client supports async iteration for paginated results:

.. code-block:: python

   async with AsyncGitHubDiscussionsClient(token="your_token") as client:
       async for page in client.get_discussions_paginated("owner", "repo"):
           for discussion in page:
               print(discussion.title)
