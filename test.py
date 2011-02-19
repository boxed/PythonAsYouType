def foo():
    eval(compile('global a;a = 2', '<string>', 'exec'))
    print a
foo()
print a
