from package02.A import module as Amodule
from package02.B import module as Bmodule

a = 5
b = 10

print(Amodule.do_something(a, b))
print(Amodule.name())

print(Bmodule.do_something(a, b))
print(Bmodule.name())
