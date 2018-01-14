# coding=GB18030
# 2017/12/18 by cyxn2760
from __future__ import unicode_literals

from symbolic_differentiation_of_prefix_expressions import diff


class CNull(object):
	pass


def assert_equals(val, expected, msg):
	if val != expected:
		raise Exception(msg)


def expect(val, msg):
	if not val:
		raise Exception('expect failed', msg)


Test = CNull()
test = CNull()
test.assert_equals = assert_equals
test.expect = expect
Test.describe = lambda *args: None


def testThis(config, n=1, val=0):
	for msg, expected, inp in config:
		msg, expected, inp = (s.format(val) for s in (msg, expected, inp))
		for _ in range(n - 1): inp = diff(inp)
		test.assert_equals(diff(inp), expected, msg)


Test.describe("Sample tests")

config = [("constant should return 0", "0", "5"),
          ("x should return 1", "1", "x"),
          ("x+x should return 2", "2", "(+ x x)"),
          ("x-x should return 0", "0", "(- x x)"),
          ("2*x should return 2", "2", "(* x 2)"),
          ("x/2 should return 0.5", "0.5", "(/ x 2)"),
          ("x^2 should return 2*x", "(* 2 x)", "(^ x 2)"),
          ("cos(x) should return -1 * sin(x)", "(* -1 (sin x))", "(cos x)"),
          ("sin(x) should return cos(x)", "(cos x)", "(sin x)"),
          ("tan(x) should return 1 + tan(x)^2", "(+ 1 (^ (tan x) 2))", "(tan x)"),
          ("exp(x) should return exp(x)", "(exp x)", "(exp x)"),
          ("ln(x) should return 1/x", "(/ 1 x)", "(ln x)")]

testThis(config)
print("<COMPLETEDIN::>")

Test.describe("Sample tests")

config = [("x+(x+x) should return 3", "3", "(+ x (+ x x))"),
          ("(x+x)-x should return 1", "1", "(- (+ x x) x)"),
          ("2*(x+2) should return 2", "2", "(* 2 (+ x 2))"),
          ("2/(1+x) should return -2/(1+x)^2", "(/ -2 (^ (+ 1 x) 2))", "(/ 2 (+ 1 x))"),
          ("cos(x+1) should return -1 * sin(x+1)", "(* -1 (sin (+ x 1)))", "(cos (+ x 1))"),
          ("sin(x+1) should return cos(x+1)", "(cos (+ x 1))", "(sin (+ x 1))"),
          ("sin(2*x) should return 2*cos(2*x)", "(* 2 (cos (* 2 x)))", "(sin (* 2 x))"),
          ("tan(2*x) should return 2 * (1 + tan(2*x)^2)", "(* 2 (+ 1 (^ (tan (* 2 x)) 2)))", "(tan (* 2 x))"),
          ("exp(2*x) should return 2*exp(2*x)", "(* 2 (exp (* 2 x)))", "(exp (* 2 x))")]

testThis(config)

result = diff("(cos (* 2 x))")
test.expect(result in ("(* 2 (* -1 (sin (* 2 x))))", "(* -2 (sin (* 2 x)))"),
            "Expected (* 2 (* -1 (sin (* 2 x)))) or (* -2 (sin (* 2 x))) but got " + result)

print("<COMPLETEDIN::>")

Test.describe("Second derivatives")

config = [("Second deriv. sin(x) should return -1 * sin(x)", "(* -1 (sin x))", "(sin x)"),
          ("Second deriv. exp(x) should return exp(x)", "(exp x)", "(exp x)")]

testThis(config, 2)

result = diff(diff("(^ x 3)"))
test.expect(result in ("(* 3 (* 2 x))", "(* 6 x)"), "Expected (* 3 (* 2 x)) or (* 6 x) but got " + result)
