Authentication
==============

The GitHub Discussions GraphQL Client supports multiple authentication methods to access GitHub's API.

Personal Access Token
---------------------

The most common authentication method is using a Personal Access Token (PAT).

Creating a Personal Access Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "GitHub Discussions API")
4. Select the following scopes:
   - ``repo`` - Full control of private repositories
   - ``public_repo`` - Access public repositories
   - ``read:org`` - Read org and team membership (if accessing org repos)
5. Click "Generate token"
6. **Important**: Copy the token immediately - you won't be able to see it again!

Using the Token
~~~~~~~~~~~~~~~

.. code-block:: python

   from github_discussions import GitHubDiscussionsClient

   # Initialize with personal access token
   client = GitHubDiscussionsClient(token="ghp_your_token_here")

GitHub App Authentication
-------------------------

For applications that need to act on behalf of an organization or handle multiple users, you can use GitHub App authentication.

.. code-block:: python

   from github_discussions import GitHubDiscussionsClient

   # Initialize with GitHub App token
   client = GitHubDiscussionsClient(
       token="installation_token_from_github_app",
       app_id="your_app_id"
   )

Token Security Best Practices
-----------------------------

1. **Never commit tokens to version control**
2. **Use environment variables** for storing tokens:

   .. code-block:: python

      import os
      from github_discussions import GitHubDiscussionsClient

      token = os.getenv("GITHUB_TOKEN")
      client = GitHubDiscussionsClient(token=token)

3. **Use token rotation** - regularly regenerate tokens
4. **Limit token scopes** - only grant necessary permissions
5. **Monitor token usage** - check GitHub's audit logs

Rate Limits
-----------

GitHub's GraphQL API has rate limits that vary by authentication method:

- **Personal Access Tokens**: 5,000 requests per hour
- **GitHub Apps**: 10,000 requests per hour per installation

The client automatically handles rate limiting and will retry requests when rate limited.

.. code-block:: python

   # Check current rate limit status
   status = client.get_rate_limit_status()
   print(f"Remaining: {status.remaining}, Reset: {status.reset_at}")

Error Handling
--------------

The client raises specific exceptions for authentication issues:

.. code-block:: python

   from github_discussions import GitHubDiscussionsClient, AuthenticationError

   try:
       client = GitHubDiscussionsClient(token="invalid_token")
       discussions = client.get_discussions("owner", "repo")
   except AuthenticationError as e:
       print(f"Authentication failed: {e}")
       # Handle authentication error
