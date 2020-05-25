import os, sys, time

USER = os.path.expanduser('~').split('/')[2]
PROJECT_BASE = os.path.expanduser('~/projects/jieermei')
PROJECT_NGINX_CONF = '/home/ubuntu/projects/jieermei/config/nginx.conf'
NGINX_CONF = '/etc/nginx/nginx.conf'

def main():
    os.system(f'cd {PROJECT_BASE}')
    arg = sys.argv[1]
    if arg == 'install-gunicorn':  # 安装 Gunicorn
        os.system('sudo apt-get install gunicorn3')
    elif arg == 'start-gunicorn':  # 启动 Gunicorn
        os.system('gunicorn3 -w4 main:app -b 0.0.0.0:8080')
    elif arg == 'install-nginx':   # 安装 Nginx
        os.system('sudo apt-get remove nginx')
        os.system('sudo apt-get install nginx')
        # os.system(f'sudo rm -rf {NGINX_CONF}')
        # os.system(f'sudo ln -s {PROJECT_NGINX_CONF} {NGINX_CONF}')
    elif arg == 'start-nginx':     # 启动 Nginx
        # os.system(f'sudo rm -rf {NGINX_CONF}')
        # os.system(f'sudo ln -s {PROJECT_NGINX_CONF} {NGINX_CONF}')
        os.system('sudo /etc/init.d/nginx start')
    elif arg == 'restart-nginx':
        # os.system(f'sudo rm -rf {NGINX_CONF}')
        # os.system(f'sudo ln -s {PROJECT_NGINX_CONF} {NGINX_CONF}')
        os.system('sudo service nginx restart')
    else:
        raise Exception(f'argv: {arg} is invalid!')



if __name__ == '__main__':
    main()


