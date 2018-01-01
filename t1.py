# coding=utf-8
from __future__ import unicode_literals


def convert_thunder(url):
	# in : thunder://QUFodHRwOi8vZGwxMy5jdWRvd24uY29tLzNETUdBTUVfTGlmZV9pc19TdHJhbmdlX0JlZm9yZV90aGVfU3Rvcm0uQ0hTLkdyZWVuLnJhclpa
	import base64
	out = base64.decodebytes(url.replace('thunder://', '').encode('ascii'))[2:-2]
	print(out)


def main():
	import re
	p = re.compile('(?P<name1>(?P<name11>1)(?P<name12>2))(?P<name2>(?P<name21>3)(?P<name22>4))')
	r = p.match('1234')
	r.group()
	pass

if __name__ == '__main__':
	main()
