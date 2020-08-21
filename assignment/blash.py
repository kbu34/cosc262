def thing(s, blah=[]):
    blah.append(s)
    print(blah)

thing('x', ['hi'])
thing('y')
thing('z')

print()
def thing(s, blah=None):
    if blah is None:
        blah = []
    blah.append(s)
    print(blah)

thing('x', ['hi'])
thing('y')
thing('z')