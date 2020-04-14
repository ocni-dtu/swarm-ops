__author__ = "Christian Kongsgaard"
__license__ = 'MIT'
import git
import git.remote


def check_for_updates(path):
    """Check for updates in the git repo"""

    repo = get_repo(path)
    remote = repo.remotes[0]
    pull = remote.pull()

    return pull


def get_repo(path):
    repo = git.Repo(path)

    return repo
