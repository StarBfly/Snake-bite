exec("print(3)")
print(eval("sum([1,2])"))

input(">>>")

import ast
s = ast.literal_eval("[1,2]")
print(sum(s))

import code
help(code)

import codeop
help(codeop)
