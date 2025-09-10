Advanced Usage
==============

This guide covers advanced features and patterns for using the GitHub Discussions GraphQL Client effectively.

Async Support
-------------

The client provides async/await support for non-blocking operations:

.. code-block:: python

   import asyncio
   from github_discussions import AsyncGitHubDiscussionsClient

   async def main():
       async with AsyncGitHubDiscussionsClient(token="your_token") as client:
           # All operations are now async
           discussions = await client.get_discussions("owner", "repo")
           comments = await client.get_discussion_comments(discussion_id)

           # Create multiple discussions concurrently
           tasks = []
           for i in range(5):
               task = client.create_discussion(
                   repository_id="repo_id",
                   category_id="category_id",
                   title=f"Discussion {i}",
                   body=f"Content for discussion {i}"
               )
               tasks.append(task)

           results = await asyncio.gather(*tasks)
           print(f"Created {len(results)} discussions")

   asyncio.run(main())

Pagination Handling
-------------------

Handle large result sets with automatic pagination:

.. code-block:: python

   # Automatic pagination iterator
   all_discussions = []
   for page in client.get_discussions_paginated("owner", "repo"):
       all_discussions.extend(page)
       print(f"Loaded page with {len(page)} discussions")

   print(f"Total discussions: {len(all_discussions)}")

   # Manual pagination control
   cursor = None
   has_next_page = True

   while has_next_page:
       result = client.get_discussions(
           "owner", "repo",
           first=50,
           after=cursor
       )

       # Process the page
       for discussion in result.nodes:
           print(discussion.title)

       # Update pagination state
       has_next_page = result.page_info.has_next_page
       cursor = result.page_info.end_cursor

Error Handling and Retry Logic
-------------------------------

Comprehensive error handling with automatic retries:

.. code-block:: python

   from github_discussions import (
       GitHubDiscussionsClient,
       RateLimitError,
       AuthenticationError,
       NotFoundError,
       NetworkError,
       GitHubGraphQLError
   )

   client = GitHubDiscussionsClient(
       token="your_token",
       max_retries=3,
       retry_backoff=2.0
   )

   def handle_errors(func):
       def wrapper(*args, **kwargs):
           try:
               return func(*args, **kwargs)
           except RateLimitError as e:
               print(f"Rate limited. Reset at: {e.reset_at}")
               # Wait or implement backoff strategy
               time.sleep(60)
               return func(*args, **kwargs)
           except AuthenticationError as e:
               print(f"Authentication failed: {e}")
               # Refresh token or re-authenticate
           except NotFoundError as e:
               print(f"Resource not found: {e}")
               # Handle 404 errors
           except NetworkError as e:
               print(f"Network error: {e}")
               # Retry or handle network issues
           except GitHubGraphQLError as e:
               print(f"GraphQL error: {e}")
               # Handle GraphQL-specific errors
           except Exception as e:
               print(f"Unexpected error: {e}")
               # Handle other exceptions

       return wrapper

   @handle_errors
   def safe_get_discussions(owner, repo):
       return client.get_discussions(owner, repo)

Rate Limit Management
---------------------

Monitor and manage GitHub API rate limits:

.. code-block:: python

   # Check current rate limit status
   status = client.get_rate_limit_status()
   print(f"Limit: {status.limit}")
   print(f"Remaining: {status.remaining}")
   print(f"Used: {status.used}")
   print(f"Reset at: {status.reset_at}")

   # Implement rate limit aware operations
   def rate_limit_aware_operation():
       while True:
           try:
               return client.get_discussions("owner", "repo")
           except RateLimitError as e:
               # Calculate wait time
               reset_time = datetime.fromisoformat(e.reset_at.replace('Z', '+00:00'))
               wait_seconds = (reset_time - datetime.now(timezone.utc)).total_seconds()

               if wait_seconds > 0:
                   print(f"Rate limited. Waiting {wait_seconds} seconds...")
                   time.sleep(wait_seconds)
               else:
                   # Reset time has passed, retry immediately
                   continue

Custom GraphQL Operations
-------------------------

Execute complex custom GraphQL queries:

.. code-block:: python

   # Multi-repository query
   query = """
   query($org: String!) {
       organization(login: $org) {
           repositories(first: 10) {
               nodes {
                   name
                   discussions(first: 5) {
                       nodes {
                           title
                           author {
                               login
                           }
                       }
                   }
               }
           }
       }
   }
   """

   result = client.execute_query(query, variables={"org": "my-organization"})

   # Process nested results
   for repo in result["data"]["organization"]["repositories"]["nodes"]:
       print(f"Repository: {repo['name']}")
       for discussion in repo["discussions"]["nodes"]:
           print(f"  Discussion: {discussion['title']}")

Batch Operations
----------------

Perform multiple operations efficiently:

.. code-block:: python

   import asyncio
   from typing import List, Dict

   async def batch_create_discussions(
       client: AsyncGitHubDiscussionsClient,
       discussions_data: List[Dict]
   ) -> List:
       """Create multiple discussions concurrently."""
       tasks = []
       for data in discussions_data:
           task = client.create_discussion(**data)
           tasks.append(task)

       return await asyncio.gather(*tasks, return_exceptions=True)

   async def batch_process_comments(
       client: AsyncGitHubDiscussionsClient,
       discussion_ids: List[str]
   ) -> Dict[str, List]:
       """Get comments for multiple discussions."""
       tasks = [
           client.get_discussion_comments(discussion_id)
           for discussion_id in discussion_ids
       ]

       results = await asyncio.gather(*tasks, return_exceptions=True)

       return dict(zip(discussion_ids, results))

Advanced Search and Filtering
-----------------------------

Use GitHub's search capabilities:

.. code-block:: python

   # Note: This would require extending the client with search methods
   # Example of how search might be implemented

   def search_discussions(query: str, **filters):
       """Search discussions with advanced filters."""
       search_query = f"repo:owner/repo {query}"

       if "author" in filters:
           search_query += f" author:{filters['author']}"

       if "created" in filters:
           search_query += f" created:{filters['created']}"

       if "is" in filters:
           search_query += f" is:{filters['is']}"

       # This would call GitHub's search API
       return client.search_discussions(search_query)

Monitoring and Logging
-----------------------

Add comprehensive logging to your operations:

.. code-block:: python

   import logging
   import time

   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)

   class MonitoredGitHubClient(GitHubDiscussionsClient):
       def _make_request(self, query, variables=None):
           start_time = time.time()
           logger.info(f"Making GraphQL request: {query[:50]}...")

           try:
               result = super()._make_request(query, variables)
               duration = time.time() - start_time
               logger.info(".2f")
               return result
           except Exception as e:
               duration = time.time() - start_time
               logger.error(".2f")
               raise

   # Use the monitored client
   client = MonitoredGitHubClient(token="your_token")

Configuration Management
-------------------------

Configure the client for different environments:

.. code-block:: python

   import os
   from typing import Optional

   class GitHubClientConfig:
       def __init__(
           self,
           token: Optional[str] = None,
           base_url: str = "https://api.github.com/graphql",
           timeout: float = 30.0,
           max_retries: int = 3,
           retry_backoff: float = 2.0
       ):
           self.token = token or os.getenv("GITHUB_TOKEN")
           self.base_url = os.getenv("GITHUB_API_URL", base_url)
           self.timeout = float(os.getenv("GITHUB_TIMEOUT", timeout))
           self.max_retries = int(os.getenv("GITHUB_MAX_RETRIES", max_retries))
           self.retry_backoff = float(os.getenv("GITHUB_RETRY_BACKOFF", retry_backoff))

       def create_client(self):
           if not self.token:
               raise ValueError("GitHub token is required")

           return GitHubDiscussionsClient(
               token=self.token,
               base_url=self.base_url,
               timeout=self.timeout,
               max_retries=self.max_retries,
               retry_backoff=self.retry_backoff
           )

   # Usage
   config = GitHubClientConfig()
   client = config.create_client()
