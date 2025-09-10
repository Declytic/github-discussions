Data Models
===========

Pydantic models used by the GitHub Discussions GraphQL Client.

Discussion Models
-----------------

.. automodule:: github_discussions.base_client
   :members:
   :undoc-members:
   :show-inheritance:

Rate Limit Models
-----------------

.. autoclass:: github_discussions.base_client.RateLimitStatus
   :members:
   :undoc-members:
   :show-inheritance:

Pagination Models
-----------------

The client uses cursor-based pagination with the following structure:

.. code-block:: python

   # PageInfo structure
   page_info = {
       "has_next_page": bool,
       "has_previous_page": bool,
       "start_cursor": str,
       "end_cursor": str
   }

   # Paginated result structure
   result = {
       "nodes": [Discussion, ...],
       "page_info": page_info,
       "total_count": int
   }

Model Validation
----------------

All models include automatic validation:

.. code-block:: python

   from github_discussions import GitHubDiscussionsClient
   from pydantic import ValidationError

   client = GitHubDiscussionsClient(token="your_token")

   try:
       discussions = client.get_discussions("owner", "repo")
       # All discussion objects are validated Pydantic models
       for discussion in discussions:
           print(f"Title: {discussion.title}")
           print(f"Author: {discussion.author.login}")
           print(f"Created: {discussion.created_at}")
   except ValidationError as e:
       print(f"Data validation error: {e}")

Custom Model Usage
------------------

You can extend the models or create custom ones:

.. code-block:: python

   from pydantic import BaseModel
   from typing import Optional
   from datetime import datetime

   class CustomDiscussion(BaseModel):
       id: str
       title: str
       body: str
       created_at: datetime
       author_login: str
       comment_count: int
       custom_field: Optional[str] = None

   # Use with custom GraphQL queries
   query = """
   query($owner: String!, $repo: String!) {
       repository(owner: $owner, name: $repo) {
           discussions(first: 10) {
               nodes {
                   id
                   title
                   body
                   createdAt
                   author {
                       login
                   }
                   comments {
                       totalCount
                   }
               }
           }
       }
   }
   """

   result = client.execute_query(query, variables={"owner": "octocat", "repo": "Hello-World"})

   # Parse into custom models
   discussions = [
       CustomDiscussion(
           id=node["id"],
           title=node["title"],
           body=node["body"],
           created_at=node["createdAt"],
           author_login=node["author"]["login"],
           comment_count=node["comments"]["totalCount"]
       )
       for node in result["data"]["repository"]["discussions"]["nodes"]
   ]

Model Serialization
-------------------

Models can be easily serialized to JSON:

.. code-block:: python

   import json
   from github_discussions import GitHubDiscussionsClient

   client = GitHubDiscussionsClient(token="your_token")
   discussions = client.get_discussions("owner", "repo")

   # Serialize to JSON
   json_data = json.dumps([d.dict() for d in discussions], indent=2, default=str)

   # Deserialize from JSON
   import json
   from github_discussions.base_client import Discussion

   discussion_data = json.loads(json_data)
   discussions = [Discussion(**data) for data in discussion_data]

Field Types
-----------

Common field types used in models:

- ``str``: String fields
- ``int``: Integer fields
- ``bool``: Boolean fields
- ``datetime``: ISO 8601 datetime strings (parsed automatically)
- ``Optional[T]``: Optional fields that may be None
- ``List[T]``: Lists of other model types
- ``Dict[str, Any]``: Dictionary fields

All datetime fields are automatically parsed from ISO 8601 strings to Python datetime objects.
