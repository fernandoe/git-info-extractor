import os
import sys
import subprocess


def main():
    if len(sys.argv) == 1:
        print("Usage: python extractor.py /home/user")
    else:
        print("| Name | Repository | Branch |")
        print("| ---- | ---------- | ------ |")
        path = sys.argv[1]
        for name in os.listdir(path):
            try:
                repo_path = os.path.join(path, name)
                repository = subprocess.check_output(["git", "config", "--get", "remote.origin.url"], cwd=repo_path)
                repository = repository.decode("utf-8").strip()
            except subprocess.CalledProcessError:
                repository = "Not a git repository"

            try:
                branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_path)
                branch = branch.decode("utf-8").strip()
            except subprocess.CalledProcessError:
                branch = "Not a git repository"

            print("| {} | {} | {} |".format(name, repository, branch))


if __name__ == "__main__":
    main()
