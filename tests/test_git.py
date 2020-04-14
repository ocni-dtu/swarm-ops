from src.git import check_for_updates

__author__ = "Christian Kongsgaard"
__license__ = 'MIT'


def test_pull_repo():
    """
    Pull repo
    Pull repo without password
    Pull repo with password and username
    Pull repo without repo
    """
    pass


def test_check_for_updates(repo_updates):
    """
    Check repo with updates
    Check repo without updates
    Check repo with updates but not to stacks
    """

    path = repo_updates
    updates = check_for_updates(path)

    assert updates
