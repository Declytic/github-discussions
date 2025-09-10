Exceptions
==========

All exceptions raised by the GitHub Discussions GraphQL Client.

Base Exception
--------------

.. autoclass:: github_discussions.exceptions.GitHubGraphQLError
   :members:
   :undoc-members:
   :show-inheritance:

Specific Exceptions
-------------------

.. autoclass:: github_discussions.exceptions.RateLimitError
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: github_discussions.exceptions.AuthenticationError
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: github_discussions.exceptions.NotFoundError
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: github_discussions.exceptions.NetworkError
   :members:
   :undoc-members:
   :show-inheritance:

Exception Hierarchy
-------------------

::

   GitHubGraphQLError
   ├── RateLimitError
   ├── AuthenticationError
   ├── NotFoundError
   └── NetworkError

Usage Examples
--------------

.. code-block:: python

   from github_discussions import (
       GitHubDiscussionsClient,
       RateLimitError,
       AuthenticationError,
       NotFoundError,
       NetworkError,
       GitHubGraphQLError
   )

   client = GitHubDiscussionsClient(token="your_token")

   try:
       discussions = client.get_discussions("owner", "repo")
   except RateLimitError as e:
       print(f"Rate limit exceeded: {e}")
   except AuthenticationError as e:
       print(f"Authentication failed: {e}")
   except NotFoundError as e:
       print(f"Resource not found: {e}")
   except NetworkError as e:
       print(f"Network error: {e}")
   except GitHubGraphQLError as e:
       print(f"GraphQL error: {e}")

Exception Attributes
--------------------

All exceptions provide access to additional error information:

- ``message``: Human-readable error message
- ``errors``: Raw GraphQL errors (for GitHubGraphQLError)
- ``status_code``: HTTP status code (when applicable)
- ``response``: Raw HTTP response (when applicable)

RateLimitError Specific Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``limit``: Rate limit ceiling
- ``remaining``: Remaining requests
- ``reset_at``: Time when limit resets (ISO 8601 format)
