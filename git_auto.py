import os
from func import *
from dotenv import load_dotenv, find_dotenv

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)
USER = os.environ['USER']
ROOT = os.environ['ROOT_PATH']


if __name__ == '__main__':
    # print(USER, ROOT)
    os.chdir(ROOT)

    task = input("clone / push: ")

    if task == 'clone':
        clone_git(USER)

    elif task == 'push':
        push_git(USER)