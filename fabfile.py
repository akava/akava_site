from fabric.api import *
import os

env.hosts = [os.environ['HOSTING']]

PROJECT_NAME = 'kavaleu_ru'
PROJECT_DIR = '~/' + PROJECT_NAME
DEV_DIR = '~/Projects/' + PROJECT_NAME


def run_in_virtualenv(command):
    run('source ~/.virtualenvs/%s/bin/activate && %s' %
        (PROJECT_NAME, command))


def deploy(switch='no'):
    with cd(PROJECT_DIR):
        if switch == 'push':
            local('git push')
        run('git pull')
        run_in_virtualenv('pip install -r requirements.txt')
        run_in_virtualenv('python manage.py syncdb')
        run_in_virtualenv('python manage.py migrate')
        run_in_virtualenv('python manage.py collectstatic --noinput')
        #run_in_virtualenv('python manage.py clear_cache')
        run('restart' + PROJECT_NAME)


def local_deploy():
    local('cd ' + DEV_DIR)
    local('python manage.py collectstatic --noinput')
    local('cp -ru %s %s/..' % (DEV_DIR, PROJECT_DIR))
    #local('rm -r %s/static' % (DEV_DIR,))
    run('restart' + PROJECT_NAME)


import settings
db_settings = settings.DATABASES['default']


def fetch_db():
    with cd(PROJECT_DIR):
        run('pg_dump %(NAME)s | gzip > ~/private/dump.sql.gz' % db_settings)
        get('~/private/dump.sql.gz', 'dump.sql.gz')
    local('./manage.py flush --noinput')
    local('gunzip -c dump.sql.gz | ./manage.py dbshell')
    local('rm dump.sql.gz')
