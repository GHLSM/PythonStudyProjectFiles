import os, sys
from src import core


sys.path.append(
    os.path.dirname(__file__)
)


if __name__ == '__main__':
    core.run()