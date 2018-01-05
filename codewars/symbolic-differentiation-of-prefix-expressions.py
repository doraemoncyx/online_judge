# coding=GB18030
# 2017/12/18 by cyxn2760
import re


# expr := "("func arg")" | "("op arg arg")"
# func := + - * / ^
# op := cos sin tan exp
# arg := x | digit | expr

def pattern_parser(inStr, pos, rePattern=''):
	rePattern = re.compile('^(?P<tarStr>%s).*' % rePattern)
	result = rePattern.match(inStr, pos)
	if result:
		return result.groupdict()['tarStr'], None
	else:
		return '', None


def expr_parser(inStr, pos):
	pass


def expr_parser1(inStr, pos):
	originPos = pos
	partOmit, obj = pattern_parser(inStr, pos, '\(')
	if len(partOmit) == 0:
		return '', None
	pos += len(partOmit)

	partFunc, objFunc = pattern_parser(inStr, pos)
	if len(partFunc) == 0:
		return '', None
	pos += len(partFunc)

	partOmit, obj = pattern_parser(inStr, pos, ' ')
	if len(partOmit) == 0:
		return '', None
	pos += len(partOmit)

	partArg, objArg = arg_parser(inStr, pos)
	if len(partArg) == 0:
		return '', None
	pos += len(partArg)

	partOmit, obj = pattern_parser(inStr, pos, '\)')
	if len(partOmit) == 0:
		return '', None
	pos += len(partOmit)

	exp = Expression()
	exp.func = objFunc
	exp.arg1 = objArg
	return inStr[originPos:pos], exp

def expr_parser2(inStr, pos):
	originPos = pos
	partOmit, obj = pattern_parser(inStr, pos, '\(')
	if len(partOmit) == 0:
		return '', None
	pos += len(partOmit)

	partFunc, objFunc = pattern_parser(inStr, pos)

	partOmit, obj = pattern_parser(inStr, pos, ' ')
	if len(partOmit) == 0:
		return '', None
	pos += len(partOmit)

	partArg, objArg = arg_parser(inStr, pos)
	if len(partArg) == 0:
		return '', None

	partOmit, obj = pattern_parser(inStr, pos, '\)')
	if len(partOmit) == 0:
		return '', None
	pos += len(partOmit)

	exp = Expression()
	exp.func = objFunc
	exp.arg1 = objArg
	return inStr[originPos:pos], exp


def func_parser(inStr, pos):
	pass


def operator_parser(inStr, pos):
	pass


def arg_parser(inStr, pos):
	pass


class Expression(object):
	def __init__(self):
		pass

	def dump(self):
		return ''
