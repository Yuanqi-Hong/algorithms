# define a function called get_mean
# this function is going to read in data.csv (put in the same directory)
# and print out the mean of all numbers in it
def get_mean():

  # import the csv library
  import csv

  # import the os library for path construction
  # ref: https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
  # basically, the following section of code creates the absolute path to our data file dynamically
  # so that we don't have to specify where the file is
  # we only have to put this .py file and data.csv in the same directory
  import os
  script_dir = os.path.split(os.path.abspath(__file__))[0]
  rel_path = "data.csv"
  abs_file_path = os.path.join(script_dir, rel_path)

  # using with statement to open the data file and name it 'data_csv'
  # when using a with statement we don't have to close the file manually
  with open(abs_file_path) as data_csv:
      
      # create a variable called 'data' to take the output of csv.reader
      # which is a reader object that iterates over lines in the data csv file
      data = csv.reader(data_csv, delimiter=',')
      
      # define a 'total' variable outside the for loop to record the sum of numbers
      # I don't call the variable 'sum' here to avoid conflicting with function names
      # even though it works just as fine
      total = 0
      # define an 'n' variable to count the numbers
      n = 0
      
      # the outer for loop iterates over each row in the csv file
      # although in this case there's only 1 row in the file
      for row in data:
          # the inner for loop iterates over each number in a given row
          for number in row:
              # each time a number gets iterated over,
              # 'sum' increases by the number (turned to integer) and 'n' increases by 1
              total += int(number)
              n += 1
      
      # print the mean of all numbers
      # note that the print is put outside the for loops
      # because we only want the result after all the numbers are iterated over
      print('The mean is', total/n)

# to have the .py file actually print out the mean, we have to call the function we just defined
get_mean()