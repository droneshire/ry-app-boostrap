from ry_app_bootstrap.version import get_version


def test_missing_version_file_returns_empty() -> None:
    assert get_version("/tmp/definitely-missing-version-file") == ""
