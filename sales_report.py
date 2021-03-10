"""Generate sales report showing total melons each salesperson sold."""

# create empty list stored in the variable salespeople
salespeople = []
# create empty list stored in the variable melons_sold
melons_sold = []

# assign variable to file and opens file
f = open('sales-report.txt')
# create a for loop examining individual lines in file - look at each line in f
for line in f:
    # create variable 'line' and remove extra white space from right of line
    line = line.rstrip()
    # seprating/splitting line at each | and assign to variable 'entries'
    entries = line.split('|')

    # create variable 'salesperson' which assigns salesperson to the 0 index in entries
    salesperson = entries[0]
    # grab index 2 from entries convert to int and assignn to 'melons'
    melons = int(entries[2])

    # setting up start of a conditional if 'salesperson' is in the list 'salespeople'
    if salesperson in salespeople:
        # goinginto salespeople at index salesperson and assigning to the variable position
        position = salespeople.index(salesperson)
        
        # going in to list salsepeople and looking at the position/index of salesperson and adding number of melons at the same index in melons_sold
        # longhand - melons_sold[position] = melons_sold[position] + melons
        melons_sold[position] += melons
    # second half of conditional if salseperson doesnt exist in salespeople do this
    else:
        # add salesperosn to salespeople
        salespeople.append(salesperson)
        # add melons to melons_sold
        melons_sold.append(melons)

# find length of elements in salespeople list convert into a range which starts at index 0 
# creating indexed list
for i in range(len(salespeople)):
    # print formatted string with salesperson and melons matched by index number 
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# improvments: sort list for example to find top seller
# find total number of sales each person did
# implement dictionary

# refactored code provided by hackbright
# """Generate sales report showing total melons each salesperson sold."""


# def get_melons_sold_by_salesperson(log_file_path):
#     """Return a dictionary of {salesperson_name: melons_sold}.

#     Arguments:
#         log_file_path (str) - the path to a sales report log file

#     Return:
#         mels_by_sales (dict)
#     """

#     mels_by_sales = {}

#     with open(log_file_path) as f:
#         for line in f:
#             line = line.rstrip()

#             # Create a list of data and unpack its values
#             salesperson_name, total_dollars, melons_sold = line.split('|')

#             # Set or increment the salesperson's total melons sold
#             if salesperson_name in mels_by_sales:
#                 mels_by_sales[salesperson_name] += int(melons_sold)
#             else:
#                 mels_by_sales[salesperson_name] = int(melons_sold)

              # instead of if else statement we could do
              # mels_by_sales[salesperson_name] = mels_by_sales.get(salesperson_name, 0) + int(melons_sold)

#     return mels_by_sales


# def print_sales_report(melons_sold_by_salesperson):
#     """Print a report of salespeople and the total no. of melons they've sold.

#     Arguments:
#         melons_sold_by_salesperson (dict) - {salesperson_name: melons_sold}
#     """

#     for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
#         print(f'{salesperson_name} sold {melons_sold} melons')


# print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))