from fabric.api import *

import os 

ENV = 'api_dev' # Choices ['uat','production','development', 'api_dev']


#ENV = 'production'
SERVERS = {
    'development': '172.16.12.10',
    'api_dev': '172.16.12.10',
    'uat': '103.95.197.103',
    'production' : '103.95.197.103'
}
BRANCH = {
    'development': 'develop',
    'api_dev': 'api',
    'uat': 'uat',
    'production': 'production'
}

USERS = {
    'development': 'adminvn',
    'api_dev': 'adminvn',
    'production': 'ubuntu',
    'uat': 'ubuntu'
}

PASSWORDS = {
    'development': 'Abc@123',
    'api_dev': 'Abc@123',
    'uat': 'ThangNguyen@@123',
    'production': 'ThangNguyen@@123'
}

VIRTUAL_ENVS = {
    'development': 'source /home/adminvn/envs_root/metiz_env/bin/activate',
    'api_dev': 'source /home/adminvn/envs_root/metiz_api_env/bin/activate',
    'uat': 'source /home/ubuntu/envs_root/metiz_uat_env/bin/activate',
    'production': 'source /home/ubuntu/envs_root/metiz_env//bin/activate'
}

PATHS = {
    'development': '/home/adminvn/sites/metiz',
    'api_dev': '/home/adminvn/sites/metiz_api/metiz',
    'uat': '/home/ubuntu/projects/metiz',
    'production': '/home/ubuntu/projects/production/metiz'
}

PROCESS_ID = {
    'development': '/tmp/metiz_web.pid',
    'api_dev': '/tmp/metiz_api.pid',
    'uat': '/tmp/metiz_uat_web.pid',
    'production': '/tmp/metiz_web.pid'
}

CRON_MOVIE = {
    'uat': 'bash /home/ubuntu/projects/metiz/websites/config/cronjobs/script_cron_movies.sh',
    'production': 'bash /home/ubuntu/projects/metiz/websites/config/cronjobs/production/script_cron_movies.sh'
}

env.hosts = [SERVERS[ENV]]
env.user = USERS[ENV]
env.password = PASSWORDS[ENV]
env.activate = VIRTUAL_ENVS[ENV]


PROJECT_PATH = PATHS[ENV]
DEBUG = True

VERBOSITY = ('', '') if DEBUG else ('-q', '-v 0')

def restart_app_server():
    """ Restarts remote nginx and uwsgi.4
    """
    sudo("uwsgi --reload /tmp/metiz_web.pid")

def deploy():
    with cd(PROJECT_PATH):
        run('git checkout %s'%BRANCH[ENV])
        run('git fetch {0} origin {1}'.format('' , BRANCH[ENV]))
        run('git reset --hard origin/%s'%BRANCH[ENV])
        # run('git reset --hard origin/master')
        run('find . -name "*.pyc" -exec rm -rf {} \;')
        
        with cd('websites'):
            with prefix(env.activate):
                run('pip install -r ../requirements.txt')
                run('python manage.py collectstatic --noinput')
                run('python manage.py migrate')

                if ENV == "development" or ENV == "api_dev":
                    sudo('su -s /bin/bash www-data -c "%s;%s" '%(env.activate,"uwsgi --reload %s"%PROCESS_ID[ENV]))
                elif ENV == 'uat':
                    sudo('systemctl restart uwsgi_metiz_uat')
                elif ENV == 'production':
                    sudo('systemctl restart uwsgi_metiz')

def synchronize():
    with cd(PROJECT_PATH):
        with cd('websites'):
            with prefix(env.activate):
                run('python manage.py sync_movie')


def synchronize_test():
    run("ls -al")


        

