import subprocess


def git_commit_and_push():
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Commit message'])
    subprocess.run(['git', 'push', 'origin', 'master'])


if __name__ == '__main__':
    git_commit_and_push()
