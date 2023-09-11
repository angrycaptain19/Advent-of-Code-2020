input = "advent_of_code_day7_input.txt"

def bag_parser(input_row):
  parsed_row = input_row.split("contain")
  outer_bag = parsed_row[0]
  inner_bags = parsed_row[1].split(",")
  outer_bag = number_replacer(outer_bag)
  outer_bag = bags_to_bag(outer_bag)
  for bag in range(0, len(inner_bags), 1):
    inner_bags[bag] = number_replacer(inner_bags[bag])
    inner_bags[bag] = bags_to_bag(inner_bags[bag])
  return outer_bag, inner_bags

def number_replacer(bag_listing):
  bag_type_only = bag_listing
  bag_type_only = bag_type_only.replace(" 0 ","")    
  bag_type_only = bag_type_only.replace(" 1 ","")
  bag_type_only = bag_type_only.replace(" 2 ","")  
  bag_type_only = bag_type_only.replace(" 3 ","")  
  bag_type_only = bag_type_only.replace(" 4 ","")  
  bag_type_only = bag_type_only.replace(" 5 ","")  
  bag_type_only = bag_type_only.replace(" 6 ","")  
  bag_type_only = bag_type_only.replace(" 7 ","")  
  bag_type_only = bag_type_only.replace(" 8 ","")  
  bag_type_only = bag_type_only.replace(" 9 ","")  
  return bag_type_only

def bags_to_bag(bag_listing):
  # sourcery skip: inline-immediately-returned-variable
    no_s_bag = bag_listing.replace("bags", "bag")
    no_s_bag = no_s_bag.replace(".", "")
    no_s_bag = no_s_bag.replace("\n", "")
    no_s_bag = no_s_bag.replace("bag ", "bag")
    return no_s_bag

def bag_containment_rules(input_row, individual_target_bag):
  #Takes in a row of unparsed inputs and a target set of INNER bags. Outputs an updated set of INNER bags.
  outer_bag, inner_bags = bag_parser(input_row)
  if individual_target_bag in inner_bags:
    return outer_bag

def part_one_result(input_file):
  target_bags = ["shiny gold bag"]
  i = 0
  while i < len(target_bags):
    input = open(input_file, "r")
    for row in input:
      potential_outer_bag = bag_containment_rules(row, target_bags[i])
      if potential_outer_bag and potential_outer_bag not in target_bags:
        target_bags.append(potential_outer_bag)
        i = 0
    i += 1
  #Will be overcounting the potential results by one because of the inclusion of the shiny golden bag
  return len(target_bags) - 1

# part_one_answer = part_one_result(input)

# print("There are %s potential bags to hold your bag" % part_one_answer)

def part_2_number_replacer(bag_listing):
  bag_type_only = bag_listing
  bag_type_only = bag_type_only.replace(" 0 ","0")    
  bag_type_only = bag_type_only.replace(" 1 ","1")
  bag_type_only = bag_type_only.replace(" 2 ","2")  
  bag_type_only = bag_type_only.replace(" 3 ","3")  
  bag_type_only = bag_type_only.replace(" 4 ","4")  
  bag_type_only = bag_type_only.replace(" 5 ","5")  
  bag_type_only = bag_type_only.replace(" 6 ","6")  
  bag_type_only = bag_type_only.replace(" 7 ","7")  
  bag_type_only = bag_type_only.replace(" 8 ","8")  
  bag_type_only = bag_type_only.replace(" 9 ","9")  
  return bag_type_only

def part_2_bag_parser(input_row):
  parsed_row = input_row.split("contain")
  outer_bag = parsed_row[0]
  inner_bags = parsed_row[1].split(",")
  outer_bag = number_replacer(outer_bag)
  outer_bag = bags_to_bag(outer_bag)
  for bag in range(0, len(inner_bags), 1):
    inner_bags[bag] = part_2_number_replacer(inner_bags[bag])
    inner_bags[bag] = bags_to_bag(inner_bags[bag])
  return outer_bag, inner_bags

def part_2(input_file):
  input = open(input_file, "r")
  bag_matrix = []
  outer_bags = []
  for row in input:
    outer_bag, inner_bags = part_2_bag_parser(row)
    bag_matrix.append([outer_bag, inner_bags])
    if outer_bag not in outer_bags:
      outer_bags.append(outer_bag)
  bags_contained_by_outer_bag = {
      bag_set[0]: 1
      for bag_set in bag_matrix if " no other bag" in bag_set[1]
  }
  while len(bags_contained_by_outer_bag) < len(outer_bags):  
    for bag_set in bag_matrix:
      inner_bag_fully_defined = []
      for inner_bag in bag_set[1]:
        if bags_contained_by_outer_bag.get(inner_bag[1:]) is None: inner_bag_fully_defined.append(False)
        else:
          inner_bag_fully_defined.append(True)
      if all(inner_bag_fully_defined) and inner_bag_fully_defined:
        sub_bags = 0
        for sub_bag in bag_set[1]:
          sub_bags = sub_bags + int(sub_bag[0]) * bags_contained_by_outer_bag.get(sub_bag[1:])
        #The final 1 is to account for the bag itself    
        bags_contained_by_outer_bag[bag_set[0]] = sub_bags + 1
  #Need to then discount the shiny gold bag by 1 because we only care about the bags inside it      
  return bags_contained_by_outer_bag, (bags_contained_by_outer_bag.get("shiny gold bag") - 1)

# Need to structure part 2 as a dictionary of bags and number of bags contained inside. Start by finiding the "terminal" bags 
# (eg the bags that contain 0 other bags) and then build up from there. If the dictionary doesn't contain a given bags value and
# it can be fully calculated then it is appended in

overall_bags, bags_in_shiny_gold = part_2(input)

print(bags_in_shiny_gold)
