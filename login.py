import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

from pixivpy2 import *

_USERNAME = "gm415579"
_PASSWORD = "qq321520"


def main():
	api = PixivAPI()
	api.login(_USERNAME, _PASSWORD)

if __name__ == '__main__':
	main()
