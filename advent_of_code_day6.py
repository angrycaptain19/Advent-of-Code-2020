import numpy as np

input = "advent_of_code_day6_input.txt"

def part_one_customs_check(input_file):
  input = open(input_file, "r")
  current_group_unique_answers = []
  unique_answer_counts = []
  for row in input:
    row=row.strip()
    if len(row) < 1:
      unique_answer_counts.append(len(current_group_unique_answers))
      current_group_unique_answers = []
    else:
      for character in range(0, len(row), 1):
        if (row[character] != "" or row[character] != "\n"
            ) and row[character] not in current_group_unique_answers:
          current_group_unique_answers.append(row[character])
  return np.sum(unique_answer_counts)

print("The total number of unique answers in part one is %s" % part_one_customs_check(input))

def part_two_customs_check(input_file):
  # sourcery skip: inline-immediately-returned-variable, merge-nested-ifs
  input = open(input_file, "r")
  current_group_unanimous_answers = []
  unique_answer_counts = []
  group_row_counter = 0
  for row in input:
    row=row.strip()
    if len(row) < 1:
      unique_answer_counts.append(len(current_group_unanimous_answers))
      current_group_unanimous_answers = []
      group_row_counter = 0
    else:
      if group_row_counter == 0:
        for character in range(0, len(row), 1):
          if row[character] != "" or row[character] != "\n":
            current_group_unanimous_answers.append(row[character])
      else:
       #Defines the answers for an individual in a group who isn't the first to answer
        current_individual_answers = [
            row[character] for character in range(0, len(row), 1)
            if row[character] != "" or row[character] != "\n"
        ]
        #Need to create a temporary version of the group answers to iterate over
        answer_checker = 0
        while answer_checker < len(current_group_unanimous_answers):
          answer = current_group_unanimous_answers[answer_checker]
          if answer not in current_individual_answers:
            current_group_unanimous_answers.remove(answer)
          else:
            answer_checker += 1
      group_row_counter += 1
  print(unique_answer_counts)
  total_unique_answer_sum = np.sum(unique_answer_counts)
  return total_unique_answer_sum

print("The total number of unique answers in part two is %s" % part_two_customs_check(input))
