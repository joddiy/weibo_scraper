import argparse

from src.extract.ExtractFactory import ExtractFactory


def parse_args():
    parser = argparse.ArgumentParser(description='WeiBo Scraper. Joddiy@qq.com')

    help_ = 'debug mode for develop. set 1 on, set 0 off.'
    parser.add_argument('-d', '--debug', default='1', help=help_)

    args_ = parser.parse_args()
    return args_


if __name__ == '__main__':
    args = parse_args()
    if args.debug == '1':
        extract = ExtractFactory.factory('weibo')
        extract.run()

    elif args.debug == '0':
        pass

    else:
        print('debug mode error, set 1 on, set 0 off.')
