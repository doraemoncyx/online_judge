# coding=GB18030
# 2017/12/18 by cyxn2760
from __future__ import unicode_literals
import re
import copy


# expr := "("func expr")" | "("op expr expr")" |  x | digit
# func := + - * / ^
# op := cos sin tan exp


def read_char(parserState, tarChar):
	inStr = parserState['str']
	pos = parserState['pos']
	if inStr[pos] == tarChar:
		parserState['pos'] += 1
		return 1
	else:
		return 0


def pattern_parser(parserState, tarPtn):
	inStr = parserState['str']
	pos = parserState['pos']
	rePattern = re.compile('^(?P<tarStr>%s).*' % tarPtn)
	result = rePattern.match(inStr, pos)
	if result:
		s = result.groupdict()['tarStr']
		parserState['pos'] += len(s)
		return len(s)
	else:
		return 0


def expr_parser(parserState):
	inStr = parserState['str']
	originPos = parserState['pos']
	l = read_char(parserState, '(')
	if l:
		funcLen = func_parser(parserState)
		if funcLen:
			funcStr = inStr[parserState['pos'] - funcLen:parserState['pos']]
			l = read_char(parserState, ' ')
			if not l:
				parserState['pos'] = originPos
				return 0, None
			argLen, argObj = expr_parser(parserState)
			if not argLen:
				parserState['pos'] = originPos
				return 0, None
			l = read_char(parserState, ')')
			if not l:
				parserState['pos'] = originPos
				return 0, None
			obj = Expression()
			obj.func = funcStr
			obj.args = [argObj, ]
			return parserState['pos'] - originPos, obj

		opLen, opObj = operator_parser(parserState)
		if opLen:
			opStr = inStr[parserState['pos'] - funcLen:parserState['pos']]
			l = read_char(parserState, ' ')
			if not l:
				parserState['pos'] = originPos
				return 0, None
			arg1Len, arg1Obj = expr_parser(parserState)
			if not arg1Len:
				parserState['pos'] = originPos
				return 0, None
			l = read_char(parserState, ' ')
			if not l:
				parserState['pos'] = originPos
				return 0, None
			arg2Len, arg2Obj = expr_parser(parserState)
			if not arg2Len:
				parserState['pos'] = originPos
				return 0, None
			l = read_char(parserState, ')')
			if not l:
				parserState['pos'] = originPos
				return 0, None
			obj = Expression()
			obj.op = opStr
			obj.args = [arg1Obj, arg2Obj]
			return parserState['pos'] - originPos, obj
	if read_char(parserState, 'x'):
		obj = Expression()
		obj.args = ['x']
		return 1, obj
	digitLen = pattern_parser(parserState, '[0-9]+')
	if digitLen:
		digitStr = inStr[parserState['pos'] - digitLen:parserState['pos']]
		obj = Expression()
		obj.args = [int(digitStr)]
		return len(digitStr), obj


def func_parser(parserState):
	for item in '+-*/^':
		if read_char(parserState, item):
			return 1
	return 0


def operator_parser(parserState):
	for item in ('cos', 'sin', 'tan', 'exp'):
		l = pattern_parser(parserState, item)
		if l:
			return l
	return 0


def arg_parser(parserState):
	inStr = parserState['str']
	pos = parserState['pos']
	if read_char(parserState, 'x'):
		obj = Expression()
		obj.args = ['x']
		return 1, obj
	digitLen = pattern_parser(parserState, '[0-9]+')
	if digitLen:
		digitStr = inStr[parserState['pos'] - digitLen:parserState['pos']]
		obj = Expression()
		obj.args = [int(digitStr)]
		return len(digitStr), obj
	exprLen, exprObj = expr_parser(parserState)
	if exprLen:
		return exprLen, exprObj
	return 0, None


class Expression(object):
	def __init__(self):
		self.func = None
		self.op = None
		self.args = []
		pass

	def diff(self):
		pass

	def dump(self):
		return ''


def diff(inStr):
	parserState = {'str': inStr, 'pos': 0}
	exprLen, exprObj = expr_parser(parserState)
	pass
