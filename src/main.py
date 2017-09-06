import argparse

from extract.extract_factory import get_extract
from config import weibo_config


def parse_args():
    parser = argparse.ArgumentParser(description='WeiBo Scraper. Joddiy@qq.com')

    help_ = 'debug mode for develop. set 1 on, set 0 off.'
    parser.add_argument('-d', '--debug', default='1', help=help_)

    help_ = 'which model to select.'
    parser.add_argument('-m', '--model', default='weibo', help=help_)

    args_ = parser.parse_args()
    return args_


if __name__ == '__main__':
    args = parse_args()
    model = args.model
    if model not in weibo_config.SUPPORT_MODEL:
        print('model %s should be one of' % model, weibo_config.SUPPORT_MODEL)
    else:
        if args.debug == '1':
            extract = get_extract(model)
            extract.run()

        elif args.debug == '0':
            pass

        else:
            print('debug mode error, set 1 on, set 0 off.')
