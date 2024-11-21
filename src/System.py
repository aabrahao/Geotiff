import glob
import os

def pause():
    print("Press any key to continue...")
    input()

def list(pattern):
    return glob.glob(pattern)

def run(file):
    print('')
    print('###############################################')
    print(f'Running {file}...')
    print('')
    os.system(f'exec python3 {file}')
    print('Done!')