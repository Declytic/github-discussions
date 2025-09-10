Basic Usage
===========

This guide covers the fundamental operations you can perform with the GitHub Discussions GraphQL Client.

Initializing the Client
-----------------------

First, import and initialize the client:

.. code-block:: python

   from github_discussions import GitHubDiscussionsClient

   # Initialize with your GitHub token
   client = GitHubDiscussionsClient(token="your_github_token")

Working with Discussions
------------------------

Getting Discussions
~~~~~~~~~~~~~~~~~~~

Retrieve discussions from a repository:

.. code-block:: python

   # Get the first 10 discussions
   discussions = client.get_discussions("octocat", "Hello-World", first=10)

   # Get discussions with specific category
   discussions = client.get_discussions(
       "octocat",
       "Hello-World",
       category_id="DIC_kwDOAHz1OX4CW5wG"
   )

   # Get a specific discussion by number
   discussion = client.get_discussion("octocat", "Hello-World", number=1)

Creating Discussions
~~~~~~~~~~~~~~~~~~~~

Create a new discussion:

.. code-block:: python

   discussion = client.create_discussion(
       repository_id="R_kgDOAHz1OX",  # Repository node ID
       category_id="DIC_kwDOAHz1OX4CW5wG",  # Category node ID
       title="My Discussion Title",
       body="This is the content of my discussion."
   )

Updating Discussions
~~~~~~~~~~~~~~~~~~~~

Modify an existing discussion:

.. code-block:: python

   updated = client.update_discussion(
       discussion_id="D_kwDOAHz1OX4uYAah",
       title="Updated Title",
       body="Updated content for the discussion."
   )

Deleting Discussions
~~~~~~~~~~~~~~~~~~~~

Remove a discussion:

.. code-block:: python

   client.delete_discussion("D_kwDOAHz1OX4uYAah")

Working with Comments
---------------------

Getting Comments
~~~~~~~~~~~~~~~~

Retrieve comments for a discussion:

.. code-block:: python

   comments = client.get_discussion_comments("D_kwDOAHz1OX4uYAah")

   # Get comments with pagination
   comments = client.get_discussion_comments(
       "D_kwDOAHz1OX4uYAah",
       first=20
   )

Adding Comments
~~~~~~~~~~~~~~~

Add a new comment to a discussion:

.. code-block:: python

   comment = client.add_discussion_comment(
       discussion_id="D_kwDOAHz1OX4uYAah",
       body="This is my comment on the discussion."
   )

   # Reply to a specific comment
   reply = client.add_discussion_comment(
       discussion_id="D_kwDOAHz1OX4uYAah",
       body="This is a reply to another comment.",
       reply_to_id="DC_kwDOAHz1OX4uYAah"
   )

Updating Comments
~~~~~~~~~~~~~~~~~

Modify an existing comment:

.. code-block:: python

   updated_comment = client.update_discussion_comment(
       comment_id="DC_kwDOAHz1OX4uYAah",
       body="Updated content for this comment."
   )

Deleting Comments
~~~~~~~~~~~~~~~~~

Remove a comment:

.. code-block:: python

   client.delete_discussion_comment("DC_kwDOAHz1OX4uYAah")

Managing Answers
----------------

Mark a comment as the answer:

.. code-block:: python

   client.mark_comment_as_answer("DC_kwDOAHz1OX4uYAah")

Unmark a comment as the answer:

.. code-block:: python

   client.unmark_comment_as_answer("DC_kwDOAHz1OX4uYAah")

Working with Categories
-----------------------

List discussion categories:

.. code-block:: python

   categories = client.get_discussion_categories("octocat", "Hello-World")

   for category in categories:
       print(f"Category: {category.name} - {category.description}")

Pinned Discussions
------------------

Get pinned discussions:

.. code-block:: python

   pinned = client.get_pinned_discussions("octocat", "Hello-World")

Pin a discussion:

.. code-block:: python

   client.pin_discussion("D_kwDOAHz1OX4uYAah")

Unpin a discussion:

.. code-block:: python

   client.unpin_discussion("D_kwDOAHz1OX4uYAah")

Custom GraphQL Queries
----------------------

Execute custom GraphQL queries:

.. code-block:: python

   custom_result = client.execute_query("""
       query($owner: String!, $repo: String!) {
           repository(owner: $owner, name: $repo) {
               discussions(first: 5) {
                   nodes {
                       id
                       title
                       createdAt
                       author {
                           login
                       }
                   }
               }
           }
       }
   """, variables={"owner": "octocat", "repo": "Hello-World"})

Context Manager
---------------

Use the client as a context manager for automatic cleanup:

.. code-block:: python

   with GitHubDiscussionsClient(token="your_token") as client:
       discussions = client.get_discussions("owner", "repo")
       # Client session is automatically closed
