from config.weibo_config import SUPPORT_MODEL
from driver.weibo_driver import WeiBoDriver


def get_extract(name):
    if name not in SUPPORT_MODEL:
        raise NameError('not supported model')
    if name == "weibo":
        return WeiBoDriver()

    assert 0, "Bad shape creation: " + name
