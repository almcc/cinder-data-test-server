from invoke import task

SOURCE_FILES = 'cars/ core/'


@task
def lint_flake8(ctx):
    """Run the flake8 linter."""
    print('Flake8 report:')
    ctx.run('flake8 {src}'.format(src=SOURCE_FILES))


@task
def lint_pylint(ctx):
    """Run the pylint linter."""
    print('Pylint report:')
    ctx.run('pylint --rcfile=tox.ini {src}'.format(src=SOURCE_FILES))


@task(lint_flake8, lint_pylint)
def lint(ctx):
    """Run the linter tools against the source."""


@task
def sync_venv(ctx):
    """Sync the local pip environment with requirements.txt."""
    ctx.run('pip-sync requirements.txt requirements-dev.txt')


@task
def update_requirements(ctx):
    """Update the requirements.txt to reflect the available lastest packages."""
    ctx.run('pip-compile --upgrade --output-file requirements.txt requirements.in')
    ctx.run('pip-compile --upgrade --output-file requirements-dev.txt requirements-dev.in')


@task(update_requirements, sync_venv)
def changed_requirements(ctx):
    """Update the requirements.txt file and sync the environment."""
    pass


@task
def bump_version(ctx, part, confirm=False):
    """Bump the package version."""
    if confirm:
        ctx.run('bumpversion {part}'.format(part=part))
    else:
        ctx.run('bumpversion --dry-run --allow-dirty --verbose {part}'.format(part=part))
        print('Add "--confirm" to actually perform the bump version.')


@task
def build(ctx):
    """Build the docker image ready to release."""
    ctx.run('docker build -t almcc/cinder-data-test-server:latest .')


@task(build)
def release(ctx):
    """Build and release the docker image."""
    ctx.run('docker push almcc/cinder-data-test-server:latest')
