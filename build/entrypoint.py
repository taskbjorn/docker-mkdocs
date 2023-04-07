'''Entrypoint module for the docker-breathe container
'''

import os
import subprocess
import time


def main():
    """Entrypoint main method.
    """
    # Parse the environment variables.
    git_user = os.environ.get('GIT_USER', 'git')
    git_server = os.environ.get('GIT_SERVER', 'github.com')
    git_port = os.environ.get('GIT_PORT', 22)
    git_repository = os.environ.get('GIT_REPOSITORY')
    git_username = os.environ.get('GIT_USERNAME')
    git_email = os.environ.get('GIT_EMAIL')
    git_pull_interval = os.environ.get('GIT_PULL_INTERVAL', 60.0)

    # Configure the system-wide Git options.
    subprocess.call(f'git config --global user.name {git_username}',
                    shell=True)
    subprocess.call(f'git config --global user.email {git_email}',
                    shell=True)
    subprocess.call('git config --global pull.rebase false',
                    shell=True)
    subprocess.call('git config --global --add safe.directory /repo',
                    shell=True)

    with os.scandir('/repo') as files:
        if not any(files):
            subprocess.call(
                f'git clone ssh://{git_user}@{git_server}:{git_port}/{git_username}/{git_repository}.git .',
                shell=True)
        else:
            subprocess.call('git pull',
                            shell=True)

    # Build the documentation.
    subprocess.call('mkdocs build -d /usr/share/nginx/html/',
                    shell=True)

    # Launch the NGINX web server.
    # This is a necessary step as we have overriden the default entrypoint for
    # the NGINX container.
    subprocess.call('nginx -g "daemon off;"',
                    shell=True)

    while True:
        subprocess.call('git pull',
                        shell=True)
        time.sleep(git_pull_interval)


if __name__ == '__main__':
    main()
