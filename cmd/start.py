import os, sys, time

PROJECT_BASE = '/home/ubuntu/projects/jieermei'

def main():
    '''启动临时任务'''
    os.system(f'cd {PROJECT_BASE}')
    ret = os.system(f'nohup python3 ./main.py >> ./log/main.log &')
    if ret == 0:
        print('task start successed!')
    else:
        raise Exception('task start failed!')

if __name__ == '__main__':
    main()