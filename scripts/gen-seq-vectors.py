num_vectors = 1000

print "# Exhaustive test vector for sequencer."
print "# Automatically generated."
print "<PinDef>"
print "A13,A14,A18,Q7,Q8,Q9,Q10,Q11,Q12,Q16,Q15,Q14,Q13"
print "</PinDef>"
print "<TestVector>"

def bit(x, n):
  return str((x >> n) & 1)

def print_row(clock, reset_n, run_in, digits, dp, d):
  s = str(clock) + str(reset_n) + " "
  s += str(run_in) + " "
  s += str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3]) + str(digits[4]) + " "
  s += str(1-dp) + " "
  s += bit(d, 3) + bit(d, 2) + bit(d, 1) + bit(d, 0)
  print s

print "# initialisation"
print_row(0, 0, 0, [1,0,0,0,0], 1, 0)
print_row(0, 1, 0, [1,0,0,0,0], 1, 0)
print_row("C", 1, 0, [0,1,0,0,0], 0, 0)
print_row("C", 1, 0, [0,0,0,1,0], 0, 0)
print_row("C", 1, 0, [0,0,1,0,0], 1, 0)

digit1 = digit2 = digit3 = digit4 = 0
n = 2

for i in range(num_vectors/4):
  n += 1
  if n > 4:
    n = 0
    digit4 += 1
    if digit4 > 9:
      digit4 = 0
      digit3 += 1
      if digit3 > 9:
        digit3 = 0
        digit2 += 1
        if digit2 > 5:
          digit2 = 0
          digit1 += 1
          if digit1 > 9:
            digit1 = 0
  print "# stopwatch display = %d%d%d%d" % (digit1, digit2, digit3, digit4)
  print_row("C", 1, 1, [1,0,0,0,0], 1, digit1)
  print_row("C", 1, 1, [0,1,0,0,0], 0, digit2)
  print_row("C", 1, 1, [0,0,0,1,0], 0, digit4)
  print_row("C", 1, 1, [0,0,1,0,0], 1, digit3)

print "# test RunIn = 0"
print_row("C", 1, 0, [1,0,0,0,0], 1, digit1)
print_row("C", 1, 0, [0,1,0,0,0], 0, digit2)
print_row("C", 1, 0, [0,0,0,1,0], 0, digit4)
print_row("C", 1, 0, [0,0,1,0,0], 1, digit3)

print "</TestVector>"