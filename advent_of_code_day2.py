input = open("advent_of_code_day2_input.txt","r")

def parser(input_string):
  initial_parse = input_string.split(":")
  password_rule = initial_parse[0]
  test_password = initial_parse[1]
  rule_parse = password_rule.split(" ")
  number_range = rule_parse[0]
  letter = rule_parse[1]
  number_range_parse = number_range.split("-")
  lower_limit = int(number_range_parse[0])
  upper_limit = int(number_range_parse[1])

  return lower_limit, upper_limit, letter, test_password

def part_1_password_check(lower_bound, upper_bound, rule_letter, password_to_test):
  i = 0 
  letter_count = 0
  while i < len(password_to_test):
    if password_to_test[i] == rule_letter:
      letter_count = letter_count + 1
    i = i + 1
  if letter_count >= lower_bound and letter_count <= upper_bound:
    return True
  else:
    return False

def part_1_check_full_list():
  count_of_valid_passwords = 0
  for item in input:
    lower_limit, upper_limit, letter, test_password = parser(item)
    validation = part_1_password_check(lower_bound = lower_limit, upper_bound = upper_limit, rule_letter = letter, password_to_test = test_password)
    if validation == True:
      count_of_valid_passwords = count_of_valid_passwords + 1
  return count_of_valid_passwords



print("Part 1 results:")
print(part_1_check_full_list())

input = open("advent_of_code_day2_input.txt","r")

def part_2_password_check(lower_bound, upper_bound, rule_letter, password_to_test):
  if rule_letter == password_to_test[lower_bound]:
    first_condition = True 
  else:
    first_condition = False
  if rule_letter == password_to_test[upper_bound]:
    second_condition = True
  else:
    second_condition = False
  if first_condition == True and second_condition == True:
      return False
  elif first_condition == True and second_condition != True:
      return True
  elif first_condition != True and second_condition == True:
    return True
  else:
    return False
    

def part_2_check_full_list():
  count_of_valid_passwords = 0
  for item in input:
    lower_limit, upper_limit, letter, test_password = parser(item)
    validation = part_2_password_check(lower_bound = lower_limit, upper_bound = upper_limit, rule_letter = letter, password_to_test = test_password)
    if validation == True:
      count_of_valid_passwords = count_of_valid_passwords + 1
  return count_of_valid_passwords

print("Part 2 results:")
print(part_2_check_full_list())
                 
                 