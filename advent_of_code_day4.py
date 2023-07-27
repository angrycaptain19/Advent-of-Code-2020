input_file_name = "advent_of_code_day4_input.txt"

necessary_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

def passport_check(passport, necessary_fields):
  passport_status = "Valid"
  for field in necessary_fields:
    if field not in passport:
      passport_status = "Invalid"
  return passport_status

def part_1_passport_check_all(input_field, necessary_fields, optional_fields):
  #Open input file and chunk out what is a passport
  input = open(input_field, "r")
  current_passport = {}
  valid_passport_count = 0
  for row in input:
    if len(row) < 2 :
      #Analyse the current passport
      passport_status = passport_check(current_passport, necessary_fields)
      if passport_status == "Valid":
        valid_passport_count += 1
      #Reset out the current passport
      current_passport = {}
    else:
      row_entries = row.split()
      for field in row_entries:
        parsed_fields = field.split(":")
        current_passport[parsed_fields[0]] = parsed_fields[1]
  return valid_passport_count

part_1_answer = part_1_passport_check_all(input_file_name, necessary_fields, optional_fields)

print(f"In part one there were {part_1_answer} valid passports")

def passport_check_part_2(passport, necessary_fields):
  passport_status = "Valid"
  for field in necessary_fields:
    if field not in passport:
      passport_status = "Invalid"
      print("Invalid because of missing fields")
  if passport_status == "Valid":
    birth_year = passport["byr"]
    expiration_year = passport["eyr"]
    issue_year = passport["iyr"]
    height = passport["hgt"]
    hair_color = passport["hcl"]
    eye_color = passport["ecl"]
    passport_id = passport["pid"]
    passport_status = birth_year_validation(birth_year, passport_status)
    passport_status = expiration_year_validation(expiration_year, passport_status)
    passport_status = issue_year_validation(issue_year, passport_status)
    passport_status = height_validation(height, passport_status)
    passport_status = hair_color_validation(hair_color, passport_status)
    passport_status = eye_color_validation(eye_color, passport_status)
    passport_status = passport_id_validation(passport_id, passport_status)
  return passport_status

def birth_year_validation(birth_year, current_passport_status):
  passport_status = current_passport_status
  birth_year = int(birth_year)
  if birth_year > 2002 or birth_year < 1920:
    passport_status = "Invalid"
  print(f"Birth year is {passport_status}")
  return passport_status

def issue_year_validation(issue_year, current_passport_status):
  passport_status = current_passport_status
  issue_year = int(issue_year)
  if issue_year > 2020 or issue_year < 2010:
    passport_status = "Invalid"
  print(f"Issue year is {passport_status}")
  return passport_status

def expiration_year_validation(expiration_year, current_passport_status):
  passport_status = current_passport_status
  expiration_year = int(expiration_year)
  if expiration_year > 2030 or expiration_year < 2020:
    passport_status = "Invalid"
  print(f"Expiration year is {passport_status}")
  return passport_status

def height_validation(height, current_passport_status):
  passport_status = current_passport_status
  if "cm" in height:
    cm_position = height.find("cm")
    height_in_cm = int(height[:cm_position])
    if height_in_cm < 150 or height_in_cm > 193:
      passport_status = "Invalid"
  elif "in" in height:
    inch_position = height.find("in")
    height_in_inches = int(height[:inch_position])
    if height_in_inches < 59 or height_in_inches > 76:
      passport_status = "Invalid"
  else:
    passport_status = "Invalid"
  print(f"Height is {passport_status}")
  return passport_status

def hair_color_validation(hair_color, current_passport_status):
  passport_status = current_passport_status
  if len(hair_color) == 7 and hair_color[0] != "#" or len(hair_color) != 7:
    passport_status = "Invalid"
  else:
    valid_color_keys = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    for character in range(1,len(hair_color),1):
      if hair_color[character] not in valid_color_keys:
        passport_status = "Invalid"
  print(f"Hair color is {passport_status}")
  return passport_status

def eye_color_validation(eye_color, current_passport_status):
  passport_status = current_passport_status
  valid_colors = ["amb","blu","brn","gry","grn","hzl","oth"]
  if eye_color not in valid_colors:
    passport_status = "Invalid"
  print(f"Eye color is {passport_status}")
  return passport_status

def passport_id_validation(passport_id, current_passport_status):
  passport_status = current_passport_status
  if len(passport_id) != 9:
    passport_status = "Invalid"
  else:
    valid_numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for character in passport_id:
      if character not in valid_numbers:
        passport_status = "Invalid"
  print(f"Passport_id is {passport_status}")
  return passport_status

def part_2_passport_check_all(input_field, necessary_fields, optional_fields):
  #Open input file and chunk out what is a passport
  input = open(input_field, "r")
  current_passport = {}
  valid_passport_count = 0
  for row in input:
    if len(row) < 2 :
      #Analyse the current passport
      print(current_passport)
      passport_status = passport_check_part_2(current_passport, necessary_fields)
      if passport_status == "Valid":
        valid_passport_count += 1
      #Reset out the current passport
      current_passport = {}
    else:
      row_entries = row.split()
      for field in row_entries:
        parsed_fields = field.split(":")
        current_passport[parsed_fields[0]] = parsed_fields[1]
  return valid_passport_count

part_2_answer = part_2_passport_check_all(input_file_name, necessary_fields, optional_fields)

print(f"In part two there were {part_2_answer} valid passports")