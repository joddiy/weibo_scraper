from config.weibo_config import SUPPORT_MODEL
from extract.weibo_extract import WeiBoExtract


def get_extract(name):
    if name not in SUPPORT_MODEL:
        raise NameError('not supported model')
    if name == "weibo":
        return WeiBoExtract()

    assert 0, "Bad shape creation: " + name
