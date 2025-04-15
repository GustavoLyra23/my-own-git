import argparse
import sys
from repo import repo_create

argparser = argparse.ArgumentParser(description="....")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True
argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument(
    "path",
    metavar="directory",
    nargs="?",
    default=".",
    help="Where to create the repository.",
)


def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add":
            # cmd_add(args)
            pass
        case "cat-file":
            # cmd_cat_file(args)
            pass
        case "check-ignore":
            # cmd_check_ignore(args)
            pass
        case "checkout":
            # cmd_checkout(args)
            pass
        case "commit":
            # cmd_commit(args)
            pass
        case "hash-object":
            # cmd_hash_object(args)
            pass
        case "init":
            cmd_init(args)
        case "log":
            # cmd_log(args)
            pass
        case "ls-files":
            # cmd_ls_files(args)
            pass
        case "ls-tree":
            # cmd_ls_tree(args)
            pass
        case "rev-parse":
            # cmd_rev_parse(args)
            pass
        case "rm":
            # cmd_rm(args)
            pass
        case "show-ref":
            # cmd_show_ref(args)
            pass
        case "status":
            # cmd_status(args)
            pass
        case "tag":
            # cmd_tag(args)
            pass
        case _:
            print("Bad command.")


def cmd_init(args):
    repo_create(args.path)


if __name__ == "__main__":
    main(sys.argv[1:])
