print "# Exhaustive test vector for ALU."
print "# Automatically generated."
print "<PinDef>"
print "A4,A3,A8,A7,A6,A5,A12,A11,A10,A9,Q5,Q4,Q3,Q2"
print "</PinDef>"
print "<TestVector>"

def bit(x, n):
  return str((x >> n) & 1)

def print_row(f, x, y, xy):
  s = bit(f,1) + bit(f,0) + " "
  s += bit(x,3) + bit(x,2) + bit(x,1) + bit(x,0) + " "
  s += bit(y,3) + bit(y,2) + bit(y,1) + bit(y,0) + " "
  s += bit(xy,3) + bit(xy,2) + bit(xy,1) + bit(xy,0)
  print s

for x in range(16):
  for y in range(16):
    xy = (x + y) % 16
    print_row(0, x, y, xy)
    xy = (x - y + 16) % 16
    print_row(1, x, y, xy)
    xy = (2 * x) % 16
    print_row(2, x, y, xy)
    print_row(3, x, y, 0)

print "</TestVector>"
