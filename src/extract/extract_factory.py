from src.extract.weibo_extract import WeiboExtract


class ExtractFactory(object):
    def factory(name):
        if name == "weibo":
            return WeiboExtract()

        assert 0, "Bad shape creation: " + name

    factory = staticmethod(factory)
