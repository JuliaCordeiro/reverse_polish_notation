import constants

def reverse_polish_notation(output):
  polish = []
  stack = []

  output = output.replace(" ","").replace("(","")
  exp = output.split("=")[1]
  exp_end = len(exp)

  i_exp = 0

  while i_exp < exp_end:
    if exp[i_exp] not in constants.OPERATORS and exp[i_exp] != ")":
        if exp[i_exp] == 'B':
            if exp[i_exp+2].isnumeric():
                polish.append(exp[i_exp:i_exp+3])
                i_exp += 1
            else:
                polish.append(exp[i_exp:i_exp+2])  
        else:
            polish.append(exp[i_exp:i_exp+2])
        i_exp += 1
    else:
      if exp[i_exp] in constants.OPERATORS:
        stack.append(exp[i_exp])
      elif exp[i_exp] == ")":
        if stack:
          polish.append(stack.pop())
    i_exp += 1
  
  if stack:
    while len(stack) != 0:
      polish.append(stack.pop())

  return polish

print(reverse_polish_notation("o1 = (i1 ^ i2) | (o1 ^ i2)"))
