import configparser
import os


class GitRepository(object):
    """A git repository"""

    worktree = None
    gitdir = None
    conf = None

    def __init__(self, path, force=False):
        self.worktree = path
        self.gitdir = os.path.join(path, ".git")
        if not (force or os.path.isdir(self.gitdir)):
            raise Exception("Not a git repository: %s" % path)

        # Read configuartion file in .git/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")
        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("No configuration file in %s" % self.gitdir)
        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception("Unsupported repository format version %d" % vers)
