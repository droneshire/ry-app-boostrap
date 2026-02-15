import unittest

from ry_app_bootstrap.version import get_version


class BasicTest(unittest.TestCase):
    def test_missing_version_file_returns_empty(self) -> None:
        self.assertEqual(get_version('/tmp/definitely-missing-version-file'), '')
