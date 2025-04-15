import os
import configparser
from git_utils import repo_path, repo_dir, repo_file, repo_default_config
from GitRepository import GitRepository


def repo_create(path):
    """Create a new repository at path."""
    repo = GitRepository(path, True)
    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception(f"{path} is not a directory")
    if os.path.exists(repo.gitdir) and os.listdir(repo.gitdir):
        raise Exception(f"{path} is not empty")
    else:
        os.makedirs(repo.worktree)
    assert repo_dir(repo, "branches", mkdir=True)
    assert repo_dir(repo, "objects", mkdir=True)
    assert repo_dir(repo, "refs", "tags", mkdir=True)
    assert repo_dir(repo, "refs", "heads", mkdir=True)
    with open(repo_file(repo, "description"), "w") as f:
        f.write(
            "Unnamed repository; edit this file 'description' to name the repository.\n"
        )
    with open(repo_file(repo, "HEAD"), "w") as f:
        f.write("ref: refs/heads/master\n")
    with open(repo_file(repo, "config"), "w") as f:
        config = repo_default_config()
        config.write(f)
    return repo
