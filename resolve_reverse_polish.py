import constants

def resolve(notation, inputs, outputs, booleans):
  in_out = []
  
  index = 0
  notation_resolve = []

  while(index < len(notation)):
    if notation[index] not in constants.OPERATORS:
        address = int(notation[index][1])
        if notation[index][0] == 'I':
            notation_resolve.insert(index, inputs[address - 1])
        elif notation[index][0] == 'O':
            notation_resolve.insert(index, outputs[address - 1])
        elif notation[index][0] == 'B':
            if len(notation[index]) == 3:
                address = int(notation[index][1::])
            notation_resolve.insert(index, booleans[address - 1])
    else:
        notation_resolve.insert(index, notation[index])
    index += 1

  for item in notation_resolve:
    if item not in constants.OPERATORS:
      in_out.append(item)
    else:
      if item == constants.OPERATORS[2]:
        operand = in_out.pop()
        operation = not operand
        in_out.append(operation)
      else:
        frist_op = in_out.pop()
        second_op = in_out.pop()
        if item == constants.OPERATORS[0]:
          operation = frist_op and second_op
          in_out.append(operation)
        elif item == constants.OPERATORS[1]:
          operation = frist_op or second_op
          in_out.append(operation)

  return in_out[0]

notation = ['I1', 'B16', '^', 'O1', 'I2', '^', '|']
inputs = [True, False]
outputs = [True]
booleans = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

print(resolve(notation, inputs, outputs, booleans))
