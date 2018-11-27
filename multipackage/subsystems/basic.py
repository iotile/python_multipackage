"""Basic files like editor settings and gitignore."""

import logging

class BasicSubsystem:
    """Basic managed files."""

    def __init__(self, repo):
        self._repo = repo
        self._logger = logging.getLogger(__name__)

    def update(self, options):
        """Update the linting subsystem."""

        self._repo.ensure_lines(".gitignore", [
            "workspace/",
            "*.egg-info/",
            "dist/*",
            "__pycache__",
            "*.pyc"
        ])

        self._repo.ensure_template(".editorconfig", template="editorconfig")