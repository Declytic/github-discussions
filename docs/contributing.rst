Contributing
============

We welcome contributions to the GitHub Discussions GraphQL Client! This guide will help you get started.

Development Setup
-----------------

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:

   .. code-block:: bash

      git clone https://github.com/your-username/github-discussions.git
      cd github-discussions

3. **Create a virtual environment**:

   .. code-block:: bash

      pipenv install --dev
      pipenv shell

4. **Install pre-commit hooks**:

   .. code-block:: bash

      pre-commit install

5. **Verify setup**:

   .. code-block:: bash

      make test

Development Workflow
--------------------

1. **Create a feature branch**:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

2. **Make your changes** following our coding standards
3. **Write tests** for your changes
4. **Run the test suite**:

   .. code-block:: bash

      make test

5. **Run linting and formatting**:

   .. code-block:: bash

      make lint
      make format

6. **Build documentation** (if you made changes):

   .. code-block:: bash

      make docs

7. **Commit your changes**:

   .. code-block:: bash

      git add .
      git commit -m "Add your descriptive commit message"

8. **Push to your fork**:

   .. code-block:: bash

      git push origin feature/your-feature-name

9. **Create a Pull Request** on GitHub

Coding Standards
----------------

Code Style
~~~~~~~~~~

- Follow **PEP 8** style guidelines
- Use **Black** for code formatting (88 character line length)
- Use **isort** for import sorting
- Use **flake8** for linting

Type Hints
~~~~~~~~~~

- Use type hints for all function parameters and return values
- Use ``typing`` module for complex types
- Document types in docstrings using Google/NumPy style

.. code-block:: python

   from typing import List, Optional, Dict, Any
   from datetime import datetime

   def get_discussions(
       self,
       owner: str,
       repo: str,
       first: Optional[int] = None,
       after: Optional[str] = None
   ) -> List[Discussion]:
       """Get discussions for a repository.

       Args:
           owner: Repository owner
           repo: Repository name
           first: Number of discussions to return
           after: Cursor for pagination

       Returns:
           List of discussion objects
       """
       pass

Documentation
~~~~~~~~~~~~~

- Write comprehensive docstrings for all public methods
- Update documentation for any API changes
- Add examples for new features
- Keep README updated

Testing
-------

Test Structure
~~~~~~~~~~~~~~

- Unit tests go in ``tests/`` directory
- Test files should be named ``test_*.py``
- Test classes should be named ``Test*``
- Test methods should be named ``test_*``

Writing Tests
~~~~~~~~~~~~~

.. code-block:: python

   import pytest
   from github_discussions import GitHubDiscussionsClient

   class TestGitHubDiscussionsClient:
       def test_get_discussions_success(self, client, mock_response):
           """Test successful discussion retrieval."""
           # Arrange
           expected_discussions = [...]

           # Act
           result = client.get_discussions("owner", "repo")

           # Assert
           assert len(result) == len(expected_discussions)
           assert result[0].title == expected_discussions[0]["title"]

       def test_get_discussions_not_found(self, client):
           """Test handling of non-existent repository."""
           with pytest.raises(NotFoundError):
               client.get_discussions("nonexistent", "repo")

Test Coverage
~~~~~~~~~~~~~

- Aim for high test coverage (>90%)
- Test both success and failure scenarios
- Test edge cases and error conditions
- Mock external API calls

Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   make test

   # Run with coverage
   make test-cov

   # Run specific test
   pytest tests/test_client.py::TestGitHubDiscussionsClient::test_get_discussions

Submitting Changes
------------------

Pull Request Guidelines
~~~~~~~~~~~~~~~~~~~~~~~

- **Title**: Use descriptive, imperative titles (e.g., "Add rate limit handling")
- **Description**: Explain what the change does and why it's needed
- **Tests**: Include tests for new functionality
- **Documentation**: Update docs if needed
- **Breaking Changes**: Clearly mark any breaking changes

Checklist
~~~~~~~~~

Before submitting your PR:

- [ ] Code follows style guidelines (Black, isort, flake8)
- [ ] Type hints are used throughout
- [ ] Docstrings are comprehensive and follow Google style
- [ ] Tests are written and passing
- [ ] Documentation is updated
- [ ] Commit messages are descriptive
- [ ] No linting errors
- [ ] Code is compatible with supported Python versions (3.8+)

Review Process
~~~~~~~~~~~~~~

1. **Automated Checks**: GitHub Actions will run tests and linting
2. **Code Review**: Maintainers will review your code
3. **Feedback**: Address any requested changes
4. **Approval**: Once approved, your PR will be merged

Reporting Issues
----------------

Bug Reports
~~~~~~~~~~~

When reporting bugs, please include:

- **Python version**: ``python --version``
- **Package version**: ``pip show github-discussions``
- **Operating system**: Windows/Linux/macOS version
- **Steps to reproduce**: Minimal code example
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Error messages**: Full traceback if applicable

Feature Requests
~~~~~~~~~~~~~~~~

For feature requests, please:

- **Describe the problem** you're trying to solve
- **Explain your proposed solution**
- **Consider alternatives** you've thought about
- **Include examples** of how the feature would be used

Getting Help
------------

- **Documentation**: Check the :doc:`../index` first
- **Issues**: Search existing GitHub issues
- **Discussions**: Use GitHub Discussions for questions
- **Discord/Slack**: Join our community chat (if available)

License
-------

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.
