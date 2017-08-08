from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/MuTunCN/My_blog.git"

env.user = 'mutun'
env.password = '7895123'

# 填写你自己的主机对应的域名
env.hosts = ['howyoudoin.site']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '29119'


def deploy():
    source_folder = '/home/mutun/sites/demo.howyoudoin.site/My_blog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-demo.howyoudoin.site')
    sudo('service nginx reload')