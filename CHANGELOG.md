# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-XX

### Added
- Initial release of GitHub Discussions GraphQL client
- Support for querying discussions, comments, and categories
- Full CRUD operations for discussions and comments
- Rate limit handling and error management
- Async client support with `AsyncGitHubDiscussionsClient`
- Comprehensive type hints and Pydantic models
- Unit tests with pytest
- Documentation and examples
- Support for GitHub Enterprise Server

### Features
- **Discussion Management**: Get, create, update, and delete discussions
- **Comment Management**: Add, update, delete comments; mark as answers
- **Category Support**: Retrieve discussion categories
- **Pinned Discussions**: Get and manage pinned discussions
- **Pagination**: Automatic handling of paginated responses
- **Authentication**: Support for personal access tokens and GitHub Apps
- **Error Handling**: Specific exceptions for different error types
- **Rate Limiting**: Automatic rate limit detection and handling

### Technical Details
- **Python Version**: 3.8+
- **Dependencies**: requests, pydantic, typing-extensions
- **Optional Dependencies**: aiohttp (for async support)
- **License**: MIT

## Types of changes
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` in case of vulnerabilities
