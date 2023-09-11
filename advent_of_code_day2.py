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
  letter_count = sum(1 for i in range(len(password_to_test))
                     if password_to_test[i] == rule_letter)
  return letter_count >= lower_bound and letter_count <= upper_bound

def part_1_check_full_list():
  count_of_valid_passwords = 0
  for item in input:
    lower_limit, upper_limit, letter, test_password = parser(item)
    validation = part_1_password_check(lower_bound = lower_limit, upper_bound = upper_limit, rule_letter = letter, password_to_test = test_password)
    if validation == True:
      count_of_valid_passwords += 1
  return count_of_valid_passwords



print("Part 1 results:")
print(part_1_check_full_list())

input = open("advent_of_code_day2_input.txt","r")

def part_2_password_check(lower_bound, upper_bound, rule_letter, password_to_test):
  first_condition = rule_letter == password_to_test[lower_bound]
  second_condition = rule_letter == password_to_test[upper_bound]
  return (not first_condition
          or not second_condition) and (first_condition or second_condition)
    

def part_2_check_full_list():
  count_of_valid_passwords = 0
  for item in input:
    lower_limit, upper_limit, letter, test_password = parser(item)
    validation = part_2_password_check(lower_bound = lower_limit, upper_bound = upper_limit, rule_letter = letter, password_to_test = test_password)
    if validation == True:
      count_of_valid_passwords += 1
  return count_of_valid_passwords

print("Part 2 results:")
print(part_2_check_full_list())
                 
                 