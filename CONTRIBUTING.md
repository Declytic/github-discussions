# Contributing to GitHub Discussions GraphQL Client

Thank you for your interest in contributing to the GitHub Discussions GraphQL client! This document provides guidelines and information for contributors.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- GitHub personal access token (for testing)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Declytic/github-discussions.git
cd github-discussions-graphql
```

2. Install the package in development mode with all dependencies:
```bash
make install-dev
# or
pip install -e ".[dev]"
```

3. Set up your GitHub token for testing:
```bash
export GITHUB_TOKEN="your_github_token_here"
```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Write clear, concise commit messages
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed

### 3. Code Quality

Run the quality checks:

```bash
make check
# or individually:
make format    # Format code
make lint      # Run linting
make test      # Run tests
```

### 4. Testing

#### Unit Tests
```bash
make test-unit
```

#### Integration Tests
```bash
make test-integration
```

#### All Tests with Coverage
```bash
make test-cov
```

### 5. Documentation

Update documentation for any new features:

```bash
make docs
```

## Code Style

This project uses:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

### Type Hints

All code should include comprehensive type hints:

```python
from typing import Optional, List, Dict

def get_discussions(
    self,
    owner: str,
    repo: str,
    first: int = 10
) -> List[Discussion]:
    # Implementation
    pass
```

### Error Handling

Use appropriate exception handling and provide meaningful error messages:

```python
try:
    result = self._make_request(query)
except requests.exceptions.Timeout:
    raise TimeoutError("Request timed out")
```

## Testing

### Writing Tests

- Place tests in the `tests/` directory
- Use descriptive test names: `test_get_discussions_success`
- Use pytest fixtures for common setup
- Mock external dependencies (HTTP requests, etc.)

### Test Structure

```python
import pytest
from unittest.mock import Mock, patch

class TestGitHubDiscussionsClient:
    @pytest.fixture
    def client(self):
        return GitHubDiscussionsClient(token="test_token")

    def test_get_discussions_success(self, client):
        # Test implementation
        pass

    @patch('requests.Session.post')
    def test_get_discussions_error(self, mock_post, client):
        # Test error handling
        pass
```

## Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch from `main`
3. **Make** your changes following the guidelines above
4. **Test** thoroughly
5. **Commit** with clear messages
6. **Push** to your fork
7. **Create** a Pull Request with:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Reference to any related issues
   - Screenshots/videos if UI changes

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
feat: add support for discussion categories
fix: handle rate limit errors properly
docs: update API reference
test: add integration tests for comments
```

## API Design Principles

### Method Naming
- Use descriptive names: `get_discussions`, `create_discussion`
- Follow REST-like conventions where appropriate
- Use consistent parameter ordering

### Error Handling
- Raise specific exceptions for different error types
- Include helpful error messages
- Preserve original error context when possible

### Type Safety
- Use Pydantic models for API responses
- Include comprehensive type hints
- Validate input parameters

## Performance Considerations

- Use connection pooling for HTTP requests
- Implement proper pagination handling
- Cache responses when appropriate
- Handle rate limits gracefully

## Security

- Never log sensitive information (tokens, passwords)
- Use HTTPS for all API calls
- Validate user input
- Follow GitHub's API best practices

## Questions?

If you have questions about contributing, please:

1. Check existing issues and documentation
2. Open a GitHub issue for discussion
3. Contact the maintainers

Thank you for contributing to the GitHub Discussions GraphQL client! 🎉
