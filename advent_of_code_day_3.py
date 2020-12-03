import numpy as np

input_file_name = "advent_of_code_day3_input.txt"

#Set the slope you're moving
moves_to_the_right = 3
moves_down = 1

#Defines what a tree is
tree = "#"


def tree_detector(position, new_row, current_tree_count, moves_to_the_right, moves_down):
  new_position = position + moves_to_the_right
  indexed_position = new_position
  while indexed_position > (len(new_row) - 2):
    indexed_position = indexed_position - (len(new_row) - 1)
  current_result = new_row[indexed_position]
  if current_result == tree:
    current_tree_count += 1
  return current_tree_count, new_position

def full_slope_run_part_1(input_file, moves_to_the_right, moves_down):
  input = open(input_file,"r")
  #Sets the count of trees encountered at 0 & starts you at the top left corner of the input
  tree_counter = 0 
  current_position = 0 
  rows = input.readlines()
  for i in range(0, len(rows), moves_down):
    if i >0: 
      row = rows[i]
      tree_counter, current_position = tree_detector(current_position, row, tree_counter, moves_to_the_right, moves_down)
  return tree_counter
  


part_1_trees_hit = full_slope_run_part_1(input_file_name, moves_to_the_right, moves_down)

print("In part 1 you encountered %s trees" % part_1_trees_hit)

#Takes the input slops in form [moves to the right, moves down]
slope_matrix = [[1,1], [3,1], [5,1], [7,1], [1,2]]

def full_slope_run_part_2(input_file, slope_matrix):
  #sets up an empty array for results of each run
  run_results = []
  run_counter = 0
  for run in slope_matrix:
    trees_hit = full_slope_run_part_1(input_file, run[0], run[1])
    run_results.append(trees_hit)
    run_counter += 1
    print("In part 2 run %s you encountered %s trees" % (run_counter, trees_hit))
  return run_results

part_2_results = np.prod(full_slope_run_part_2(input_file_name, slope_matrix))

print("The overall part 2 results are %s" % part_2_results)


