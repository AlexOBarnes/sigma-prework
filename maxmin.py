#This function uses the sorted function on an inputted list of numbers
#Then returns a list of the largest and smallest numbers
def maxmin(num_list):
  sorted_num_list = sorted(num_list)
  minmax = [sorted_num_list[0],sorted_num_list[-1]]
  return minmax

#This function also returns a list of the largest and smallest numbers
#of a given list but does not use built in functions
def alt_maxmin(num_list):
  min = num_list[0]
  max = num_list[0]
  for num in num_list:
    if num < min:
      min = num
    elif num > max:
      max = num
  alt_maxmin = [min,max]
  return alt_maxmin

#Main body of code that takes the users input and creates a list of 
#integers
if __name__ == "__main__":
  print("Welcome! This program will tell you the highest number in an inputted array")
  num_list= input("Please enter a list of numbers separated by commas: ")
  joined_list = num_list.split(",")
  int_list = [eval(num) for num in joined_list]
  print(maxmin(int_list))
  print(alt_maxmin(int_list))