import package02.A.module
import package02.B.module

a = 5
b = 10

print(package02.A.module.do_something(a, b))
print(package02.A.module.name())

print(package02.B.module.do_something(a, b))
print(package02.B.module.name())
