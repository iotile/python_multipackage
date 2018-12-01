"""Basic files like editor settings and gitignore."""

import logging
import os

class BasicSubsystem:
    """Basic managed files."""

    def __init__(self, repo):
        self._repo = repo
        self._logger = logging.getLogger(__name__)

    def update(self, options):
        """Update the basic subsystem."""

        self._repo.ensure_lines(".gitignore", [
            "workspace/",
            "*.egg-info/",
            "dist/*",
            "__pycache__",
            "*.pyc",
            ".pytest_cache/",
            "build/*"
        ])

        self._repo.ensure_template(".editorconfig", template="editorconfig")
        self._repo.ensure_lines("requirements_build.txt", [
            "requests ~= 2.20",
            "twine ~= 1.12",
            "pycryptodome ~= 3.7",
            "pytest ~= 4.0",
            "wheel >= 0.32"
        ], [
            r"^requests",
            r"^twine",
            r"^pycryptodome",
            r"^pytest",
            r"^wheel"
        ], multi=True)

        variables = {
            'options': options,
            'components': self._repo.components,
            'doc': options.get('documentation', {}),
        }


        self._repo.ensure_directory(self._repo.SCRIPT_DIR)
        self._repo.ensure_template(os.path.join(self._repo.MULTIPACKAGE_DIR, "components.txt"), template="components.txt", overwrite=False)
        self._repo.ensure_template(os.path.join(self._repo.SCRIPT_DIR, "release_by_name.py"), "release_by_name.py.tpl", variables)
        self._repo.ensure_template(os.path.join(self._repo.SCRIPT_DIR, "components.py"), "components.py.tpl", variables)
        self._repo.ensure_template(os.path.join(self._repo.SCRIPT_DIR, "tag_release.py"), "tag_release.py.tpl", variables)

        self._repo.ensure_script(os.path.join(self._repo.SCRIPT_DIR, "shared_errors.py"), "shared_errors.py")
        self._repo.ensure_script(os.path.join(self._repo.SCRIPT_DIR, "release_notes.py"), "release_notes.py")
        self._repo.ensure_script(os.path.join(self._repo.SCRIPT_DIR, "release_component.py"), "release_component.py")
