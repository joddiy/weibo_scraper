from src.driver import weibo_driver


class WeiboExtract(object):
    def __init__(self):
        driver = weibo_driver()
        driver.run()

    # Create based on class name:

    def run(type):
        a = 1
