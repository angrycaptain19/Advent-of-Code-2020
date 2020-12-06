import math
input = "advent_of_code_day_input.txt"

number_of_rows_on_plane = 128
number_of_columns_on_plane = 8
number_of_row_identities = 7
number_of_column_identities = 3

def identify_row(boarding_pass, number_of_rows_on_plane, number_of_row_identities):
  min_row = 0
  max_row = number_of_rows_on_plane
  for character in range(0, number_of_row_identities, 1):
    if boarding_pass[character] == "F":
      max_row = math.floor((min_row + max_row) / 2)
    elif boarding_pass[character] == "B":
      min_row = math.ceil((min_row + max_row) / 2)
    else: print("This is not a valid boarding pass")
  seat_row = min_row
  return seat_row

def identify_column(boarding_pass, number_of_columns_on_plane, number_of_row_identities, number_of_column_identities):
  min_column = 0
  max_column = number_of_columns_on_plane
  for character in range(number_of_row_identities, (number_of_row_identities + number_of_column_identities), 1):
    if boarding_pass[character] == "L":
      max_column = math.floor((min_column + max_column) / 2)
    elif boarding_pass[character] == "R":
      min_column = math.ceil((min_column + max_column) / 2)
    else: print("This is not a valid boarding pass")
  seat_column = min_column
  return seat_column

def seat_id(seat_row, seat_column):
  return seat_row * 8 + seat_column

def part_one(input_file):
  input = open(input_file, "r")
  max_seat_id = 0
  for ticket in input:
    ticket_row = identify_row(ticket, number_of_rows_on_plane, number_of_row_identities)
    ticket_column = identify_column(ticket, number_of_columns_on_plane, number_of_row_identities, number_of_column_identities)
    ticket_id = seat_id(ticket_row, ticket_column)
    if ticket_id > max_seat_id:
      max_seat_id = ticket_id
  return max_seat_id

part_one_solution = part_one(input)

print("The answer to part one is %s" % part_one_solution)

def part_two(input_file):
  input = open(input_file, "r")
  max_seat_id = 0
  min_seat_id = 1000
  seat_id_list = []
  for ticket in input:
    ticket_row = identify_row(ticket, number_of_rows_on_plane, number_of_row_identities)
    ticket_column = identify_column(ticket, number_of_columns_on_plane, number_of_row_identities, number_of_column_identities)
    ticket_id = seat_id(ticket_row, ticket_column)
    seat_id_list.append(ticket_id)
    if ticket_id > max_seat_id:
      max_seat_id = ticket_id
    if ticket_id < min_seat_id:
      min_seat_id = ticket_id
  your_seat = 0
  for seat in range(min_seat_id, max_seat_id, 1):
    if (seat - 1) in seat_id_list and (seat + 1) in seat_id_list and seat not in seat_id_list:
      your_seat = seat
  return your_seat

your_seat_ticket = part_two(input)

print("Your seat number is %s. Take your seat, its time to fly" % (your_seat_ticket))