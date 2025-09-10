Error Handling
==============

The GitHub Discussions GraphQL Client provides comprehensive error handling with specific exception types for different error scenarios.

Exception Hierarchy
-------------------

All exceptions inherit from the base :exc:`GitHubGraphQLError` class:

.. code-block:: python

   from github_discussions import GitHubGraphQLError

   # Base exception for all GitHub GraphQL errors
   try:
       client.get_discussions("invalid", "repo")
   except GitHubGraphQLError as e:
       print(f"GitHub error: {e}")

Specific Exception Types
------------------------

RateLimitError
~~~~~~~~~~~~~~

Raised when you exceed GitHub's rate limits.

.. code-block:: python

   from github_discussions import RateLimitError

   try:
       discussions = client.get_discussions("owner", "repo", first=100)
   except RateLimitError as e:
       print(f"Rate limit exceeded!")
       print(f"Limit: {e.limit}")
       print(f"Remaining: {e.remaining}")
       print(f"Reset at: {e.reset_at}")

       # Wait until reset
       import time
       from datetime import datetime
       reset_time = datetime.fromisoformat(e.reset_at.replace('Z', '+00:00'))
       wait_seconds = (reset_time - datetime.now()).total_seconds()
       if wait_seconds > 0:
           time.sleep(wait_seconds)

AuthenticationError
~~~~~~~~~~~~~~~~~~~

Raised when authentication fails.

.. code-block:: python

   from github_discussions import AuthenticationError

   try:
       client = GitHubDiscussionsClient(token="invalid_token")
       discussions = client.get_discussions("owner", "repo")
   except AuthenticationError as e:
       print(f"Authentication failed: {e}")
       # Token might be expired or invalid

NotFoundError
~~~~~~~~~~~~~

Raised when a requested resource doesn't exist.

.. code-block:: python

   from github_discussions import NotFoundError

   try:
       discussion = client.get_discussion("owner", "nonexistent-repo", number=1)
   except NotFoundError as e:
       print(f"Resource not found: {e}")
       # Repository or discussion doesn't exist

NetworkError
~~~~~~~~~~~~

Raised for network-related issues.

.. code-block:: python

   from github_discussions import NetworkError

   try:
       discussions = client.get_discussions("owner", "repo")
   except NetworkError as e:
       print(f"Network error: {e}")
       # Connection issues, timeouts, etc.

GitHubGraphQLError
~~~~~~~~~~~~~~~~~~

Raised for GraphQL-specific errors.

.. code-block:: python

   from github_discussions import GitHubGraphQLError

   try:
       result = client.execute_query("invalid { graphql query }")
   except GitHubGraphQLError as e:
       print(f"GraphQL error: {e}")
       print(f"Error details: {e.errors}")

Error Handling Patterns
-----------------------

Retry Pattern
~~~~~~~~~~~~~

Implement retry logic for transient errors:

.. code-block:: python

   import time
   from github_discussions import (
       GitHubDiscussionsClient,
       RateLimitError,
       NetworkError
   )

   def retry_on_error(func, max_retries=3, backoff_factor=2):
       """Decorator to retry operations on transient errors."""
       def wrapper(*args, **kwargs):
           last_exception = None

           for attempt in range(max_retries):
               try:
                   return func(*args, **kwargs)
               except (RateLimitError, NetworkError) as e:
                   last_exception = e
                   if attempt < max_retries - 1:
                       wait_time = backoff_factor ** attempt
                       print(f"Attempt {attempt + 1} failed: {e}")
                       print(f"Retrying in {wait_time} seconds...")
                       time.sleep(wait_time)
                   else:
                       print(f"All {max_retries} attempts failed")
                       raise last_exception
               except (AuthenticationError, NotFoundError):
                   # Don't retry these errors
                   raise

       return wrapper

   @retry_on_error
   def get_discussions_safe(owner, repo):
       return client.get_discussions(owner, repo)

Circuit Breaker Pattern
~~~~~~~~~~~~~~~~~~~~~~~

Prevent cascading failures:

.. code-block:: python

   import time
   from enum import Enum

   class CircuitState(Enum):
       CLOSED = "closed"
       OPEN = "open"
       HALF_OPEN = "half_open"

   class CircuitBreaker:
       def __init__(self, failure_threshold=5, recovery_timeout=60):
           self.failure_threshold = failure_threshold
           self.recovery_timeout = recovery_timeout
           self.failure_count = 0
           self.last_failure_time = None
           self.state = CircuitState.CLOSED

       def call(self, func, *args, **kwargs):
           if self.state == CircuitState.OPEN:
               if self._should_attempt_reset():
                   self.state = CircuitState.HALF_OPEN
               else:
                   raise Exception("Circuit breaker is OPEN")

           try:
               result = func(*args, **kwargs)
               self._on_success()
               return result
           except Exception as e:
               self._on_failure()
               raise e

       def _should_attempt_reset(self):
           if self.last_failure_time is None:
               return True
           return time.time() - self.last_failure_time >= self.recovery_timeout

       def _on_success(self):
           self.failure_count = 0
           self.state = CircuitState.CLOSED

       def _on_failure(self):
           self.failure_count += 1
           self.last_failure_time = time.time()

           if self.failure_count >= self.failure_threshold:
               self.state = CircuitState.OPEN

Context Manager Pattern
~~~~~~~~~~~~~~~~~~~~~~~

Use context managers for automatic error handling:

.. code-block:: python

   from contextlib import contextmanager
   from github_discussions import GitHubGraphQLError

   @contextmanager
   def github_error_handler():
       """Context manager for handling GitHub API errors."""
       try:
           yield
       except RateLimitError as e:
           logger.warning(f"Rate limit hit: {e}")
           # Implement rate limit handling
       except AuthenticationError as e:
           logger.error(f"Authentication failed: {e}")
           # Handle auth issues
       except NotFoundError as e:
           logger.info(f"Resource not found: {e}")
           # Handle missing resources
       except NetworkError as e:
           logger.error(f"Network error: {e}")
           # Handle network issues
       except GitHubGraphQLError as e:
           logger.error(f"GraphQL error: {e}")
           # Handle GraphQL errors

   # Usage
   with github_error_handler():
       discussions = client.get_discussions("owner", "repo")

Logging and Monitoring
----------------------

Set up comprehensive logging:

.. code-block:: python

   import logging
   import sys

   # Configure logging
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       handlers=[
           logging.StreamHandler(sys.stdout),
           logging.FileHandler('github_client.log')
       ]
   )

   logger = logging.getLogger(__name__)

   class LoggingGitHubClient(GitHubDiscussionsClient):
       """Client with enhanced logging capabilities."""

       def _make_request(self, query, variables=None):
           logger.info(f"Making GraphQL request: {query[:100]}...")

           try:
               result = super()._make_request(query, variables)
               logger.info("Request successful")
               return result
           except GitHubGraphQLError as e:
               logger.error(f"GraphQL error: {e}")
               raise
           except Exception as e:
               logger.error(f"Unexpected error: {e}")
               raise

Custom Error Classes
--------------------

Create custom error handling for your application:

.. code-block:: python

   from github_discussions import GitHubGraphQLError

   class DiscussionNotFoundError(GitHubGraphQLError):
       """Raised when a discussion is not found."""
       pass

   class PermissionDeniedError(GitHubGraphQLError):
       """Raised when user lacks permissions."""
       pass

   def handle_github_errors(func):
       """Decorator to convert GitHub errors to custom errors."""
       def wrapper(*args, **kwargs):
           try:
               return func(*args, **kwargs)
           except GitHubGraphQLError as e:
               error_message = str(e).lower()

               if "not found" in error_message:
                   raise DiscussionNotFoundError(str(e)) from e
               elif "permission" in error_message or "forbidden" in error_message:
                   raise PermissionDeniedError(str(e)) from e
               else:
                   raise

       return wrapper

   @handle_github_errors
   def get_discussion_safe(client, owner, repo, number):
       return client.get_discussion(owner, repo, number)

Error Recovery Strategies
-------------------------

Implement different recovery strategies:

.. code-block:: python

   from typing import Callable, Any
   import random
   import time

   class ErrorRecovery:
       """Handles different error recovery strategies."""

       @staticmethod
       def exponential_backoff(attempt: int, base_delay: float = 1.0) -> float:
           """Calculate delay with exponential backoff and jitter."""
           delay = base_delay * (2 ** attempt)
           jitter = random.uniform(0.1, 1.0) * delay
           return delay + jitter

       @staticmethod
       def linear_backoff(attempt: int, delay: float = 1.0) -> float:
           """Calculate delay with linear backoff."""
           return delay * (attempt + 1)

       @staticmethod
       def retry_with_strategy(
           func: Callable,
           max_attempts: int = 3,
           strategy: str = "exponential",
           **kwargs
       ) -> Any:
           """Retry function with specified backoff strategy."""
           last_exception = None

           for attempt in range(max_attempts):
               try:
                   return func()
               except (RateLimitError, NetworkError) as e:
                   last_exception = e

                   if attempt < max_attempts - 1:
                       if strategy == "exponential":
                           delay = ErrorRecovery.exponential_backoff(attempt)
                       elif strategy == "linear":
                           delay = ErrorRecovery.linear_backoff(attempt)
                       else:
                           delay = 1.0

                       print(f"Attempt {attempt + 1} failed, retrying in {delay:.2f}s")
                       time.sleep(delay)
                   else:
                       raise last_exception

Best Practices
--------------

1. **Always handle specific exceptions** rather than catching generic Exception
2. **Implement retry logic** for transient errors (RateLimitError, NetworkError)
3. **Don't retry** authentication or permission errors
4. **Log errors appropriately** with context information
5. **Use circuit breakers** to prevent cascading failures
6. **Monitor error rates** and set up alerts for unusual patterns
7. **Provide meaningful error messages** to users
8. **Test error scenarios** in your application
