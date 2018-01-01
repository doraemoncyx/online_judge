# coding=GB18030
# 2017/12/18 by cyxn2760
import re


# expr := "("func arg")" | "("op arg arg")"
# func := + - * / ^
# op := cos sin tan exp
# arg := x | expr

def pattern_parser(inStr, pos, rePattern=''):
	rePattern = re.compile('^(?P<tarStr>%s).*' % rePattern)
	result = rePattern.match(inStr, pos)
	if result:
		return result.groupdict()['tarStr'], None
	else:
		return '', None


def expr_parser(inStr, pos):
	originPos = pos
	# "("func arg")"
	retPos = pos
	while True:
		isDone = False
		if inStr[retPos] != '(':
			break
		retPos += 1
		break


def func_parser(inStr, pos):
	pass


def operator_parser(inStr, pos):
	pass


def arg_parser(inStr, pos):
	pass


class Expression(object):
	def __init__(self, exprStr):
		# exprStr may have extra ending contents, parse until match bracket is found

		pass

	def dump(self):
		return ''

	pass
