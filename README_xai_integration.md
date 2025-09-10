# xAI Function Calling Integration for GitHub Discussions

This integration provides xAI's function calling capabilities for GitHub Discussions, allowing Grok models to interact with GitHub Discussions through tool calls.

## 📦 Optional Dependencies

**xAI integration is optional** - the core GitHub Discussions functionality works without xAI dependencies.

### Required for xAI Integration:
```bash
pip install xai-sdk pydantic
```

### Checking Availability:
```python
import github_discussions

if github_discussions._XAI_AVAILABLE:
    print("✅ xAI integration available")
else:
    print("ℹ️  xAI dependencies not installed")
```

## 📁 Files

- `github_discussions/xai_function_calling.py` - Core integration module with tool definitions
- `github_discussions/xai_chat_integration.py` - Advanced conversational AI assistant
- `examples/xai_usage_example.py` - Example showing optional import usage
- `README_xai_integration.md` - This documentation

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install xai-sdk pydantic  # Optional: for xAI integration
```

### 2. Set Environment Variables

```bash
export XAI_API_KEY=your_xai_api_key_here
export GITHUB_TOKEN=your_github_personal_access_token
```

### 3. Basic Usage

```python
# Import from the main package (new location as of core integration)
from github_discussions.xai_function_calling import setup_github_discussions_tools
from xai_sdk import Client

# Setup xAI client
client = Client(api_key=os.getenv('XAI_API_KEY'))
chat = client.chat.create(model="grok-4")

# Setup GitHub tools
tools = setup_github_discussions_tools(token=os.getenv('GITHUB_TOKEN'))

# Add tools to chat
for tool_def in tools:
    chat.add_tool(tool_def)

# Now you can chat with function calling capabilities!
response = chat.send(user("Show me recent discussions in microsoft/vscode"))
```

## 🔍 Graceful Fallback

The integration handles missing dependencies gracefully:

```python
try:
    from github_discussions.xai_function_calling import setup_github_discussions_tools
    # Use xAI functionality
    tools = setup_github_discussions_tools(token)
except ImportError as e:
    print(f"xAI not available: {e}")
    # Fallback to core functionality
    from github_discussions import GitHubDiscussionsClient
    client = GitHubDiscussionsClient(token)
```

## Available Tools

| Tool | Description |
|------|-------------|
| `get_discussions` | Get discussions from a repository with filtering and pagination |
| `get_discussion` | Get a specific discussion by number |
| `create_discussion` | Create a new discussion in a repository |
| `add_discussion_comment` | Add a comment to an existing discussion |
| `get_discussion_comments` | Get comments from a discussion |
| `get_rate_limit` | Check GitHub API rate limit status |
| `get_discussion_categories` | Get discussion categories for a repository |

## Tool Parameters

### get_discussions
```json
{
  "owner": "microsoft",
  "repo": "vscode",
  "first": 10,
  "after": null,
  "category_id": null,
  "answered": null,
  "order_by": {"field": "UPDATED_AT", "direction": "DESC"}
}
```

### get_discussion
```json
{
  "owner": "microsoft",
  "repo": "vscode",
  "number": 123
}
```

### create_discussion
```json
{
  "repository_id": "R_kgDOAHz1OX4uYAah",
  "category_id": "DIC_kwDOAHz1OX4CW5wG",
  "title": "New Feature Request",
  "body": "I would like to request a new feature...",
  "client_mutation_id": null
}
```

### add_discussion_comment
```json
{
  "discussion_id": "D_kwDOAHz1OX4uYAah",
  "body": "This is my comment on the discussion",
  "reply_to_id": null
}
```

## Advanced Usage

### Conversational AI Assistant

Run the interactive chat assistant:

```bash
python examples/xai_chat_integration.py
```

This provides a full conversational interface where you can ask natural language questions like:

- "Show me the latest discussions in the facebook/react repository"
- "Get discussion #42 from vercel/next.js"
- "What are the discussion categories for microsoft/TypeScript?"
- "Check my GitHub API rate limit status"
- "Create a new discussion about performance issues"

### Custom Integration

For custom integrations, you can:

1. Import the tool functions directly:
```python
from examples.xai_function_calling import get_discussions_tool, GetDiscussionsRequest

# Create request
request = GetDiscussionsRequest(owner="microsoft", repo="vscode", first=5)
result = get_discussions_tool(request)
```

2. Create your own chat handler:
```python
from xai_sdk import Client
from examples.xai_function_calling import setup_github_discussions_tools

class MyGitHubAssistant:
    def __init__(self, xai_key, github_token):
        self.client = Client(api_key=xai_key)
        self.chat = self.client.chat.create(model="grok-4")

        # Setup tools
        tools = setup_github_discussions_tools(github_token)
        for tool in tools:
            self.chat.add_tool(tool)

    def ask(self, question):
        response = self.chat.send(user(question))
        return self._process_response(response)
```

## Error Handling

All tool functions return a standardized response format:

```json
{
  "success": true,
  "data": {...},
  "error": null
}
```

Or on error:

```json
{
  "success": false,
  "error": "Error message",
  "error_type": "ExceptionType"
}
```

## Authentication

### GitHub Token

You need a GitHub personal access token with the following permissions:
- `public_repo` - for public repositories
- `repo` - for private repositories
- `read:org` - for organization repositories

Create a token at: https://github.com/settings/tokens

### xAI API Key

Get your xAI API key from: https://console.x.ai/

## Rate Limiting

GitHub's GraphQL API has rate limits:
- 5,000 points per hour for authenticated requests
- 60 points per hour for unauthenticated requests

The `get_rate_limit` tool helps you monitor your usage.

## Examples

### Get Recent Discussions
```python
response = chat.send(user("Show me the 5 most recent discussions in microsoft/vscode"))
```

### Create a Discussion
```python
response = chat.send(user(
    "Create a new discussion in my-repo about 'API Documentation Updates' "
    "with category 'General' and body 'We need to update our API docs...'"
))
```

### Get Discussion Details
```python
response = chat.send(user("Get the details of discussion #123 from facebook/react"))
```

### Add a Comment
```python
response = chat.send(user(
    "Add a comment to discussion D_kwDOAHz1OX4uYAah saying "
    "'Great suggestion! I'll look into implementing this.'"
))
```

## Troubleshooting

### Common Issues

1. **"GitHub token not found"**
   - Ensure `GITHUB_TOKEN` environment variable is set
   - Verify the token has appropriate permissions

2. **"xAI API key not found"**
   - Ensure `XAI_API_KEY` environment variable is set
   - Check that your xAI account is active

3. **Rate limit exceeded**
   - Use the `get_rate_limit` tool to check your status
   - Wait for the reset time or use a different token

4. **Tool call failed**
   - Check the error message in the tool response
   - Verify repository names and IDs are correct
   - Ensure you have access to the repository

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

When adding new tools:

1. Create a Pydantic model for the request parameters
2. Implement the tool function with proper error handling
3. Add the tool definition to `setup_github_discussions_tools()`
4. Update this documentation

## License

This integration example follows the same license as the main GitHub Discussions package.
