input = "advent_of_code_day8_input.txt"

instructions = []

def convert_input_to_instructions(input_file):
  input = open(input_file, "r")
  for row in input:
    instructions.append(row)
  return instructions


def part_1_solution(input):
  instructions = convert_input_to_instructions(input)
  accumulator_value = 0
  read_instructions = []
  current_position = 0
  while current_position not in read_instructions:
    current_instruction = instructions[current_position]
    instruction_type = current_instruction[:3]
    cleaned_operator = current_instruction[3:].strip()
    direction = cleaned_operator[0]
    operator_value = int(cleaned_operator[1:])
    if instruction_type == "acc":
      if direction == "+":
        accumulator_value += operator_value
      else:
        accumulator_value -= operator_value
      current_position += 1
      read_instructions.append(current_position - 1)
    elif instruction_type == "jmp":
      if direction == "+":
        current_position += operator_value
        read_instructions.append(current_position - operator_value)
      else:
        current_position -= operator_value
        read_instructions.append(current_position + operator_value)
    elif instruction_type == "nop":
      current_position += 1
      read_instructions.append(current_position - 1)
  return accumulator_value

part_one_output = part_1_solution(input)

print(part_one_output)
    

def part_2_solution(input):
  instructions = []
  instructions = convert_input_to_instructions(input)
  for i in range(len(instructions)):
    instruction = instructions[i]
    instruction_type = instruction[:3]
    temporary_instructions = []
    temporary_instructions = instructions
    if instruction_type == "jmp":
      temp_instruction = "nop"
    elif instruction_type == "nop":
      temp_instruction = "jmp"
    else:
      temp_instruction = "acc"
    temporary_instructions[i] = temp_instruction + instruction[3:]
    loop_status, accumulator_value = part_2_loop(temporary_instructions)
    if loop_status == "Fixed":
      valid_accumulator_value = accumulator_value
    else:
      temporary_instructions[i] = instruction_type + instruction[3:]
  return valid_accumulator_value


def part_2_loop(instructions):
  accumulator_value = 0
  read_instructions = []
  current_position = 0
  while True:
    current_instruction = instructions[current_position]
    instruction_type = current_instruction[:3]
    cleaned_operator = current_instruction[3:].strip()
    direction = cleaned_operator[0]
    operator_value = int(cleaned_operator[1:])
    if instruction_type == "acc":
      if direction == "+":
        accumulator_value += operator_value
      else:
        accumulator_value -= operator_value
      current_position += 1
      if current_position in read_instructions:
        loop_status = "Infinite"
        break
      elif current_position >= len(instructions):
        loop_status = "Fixed"
        break
      read_instructions.append(current_position - 1)
    elif instruction_type == "jmp":
      if direction == "+":
        current_position += operator_value
        if current_position in read_instructions:
          loop_status = "Infinite"
          break
        elif current_position >= len(instructions):
          loop_status = "Fixed"
          break
        read_instructions.append(current_position - operator_value)
      else:
        current_position -= operator_value
        if current_position in read_instructions:
          loop_status = "Infinite"
          break
        elif current_position >= len(instructions):
          loop_status = "Fixed"
          break
        read_instructions.append(current_position + operator_value)
    elif instruction_type == "nop":
      current_position += 1
      if current_position in read_instructions:
        loop_status = "Infinite"
        break
      elif current_position >= len(instructions):
        loop_status = "Fixed"
        break
      read_instructions.append(current_position - 1)
  return loop_status, accumulator_value

part_two_output = part_2_solution(input)
print("part 2 solution is %s" % part_two_output)
    