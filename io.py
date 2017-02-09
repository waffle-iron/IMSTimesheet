#!/usr/bin/python3
# Bradley Taniguchi
# 2/2/17

import datetime
from constants import HEADER_TEXT
from constants import SPACER_TEXT

SPACING = [17, 7, 8, 8, 10, 5]
#TODO: Add dir specification
def write_to_file(entries, dir=".", filename="output.txt"):
    print("Writing to file: " + filename + " at dir " + dir)
    with open(filename,'w') as out:
        out.write(string_format(entries))

#TODO: Add dir specification
def read_config(dir=".", filename="config.txt"):
    print("Reading config file: " + filename)
    list = []
    with open(filename, newline='') as file:
        for line in file:
            if line[0] != '#': # are comments
                list.append(line.strip('\n'))

    return list

def string_format(entries):
    '''Creates a string that will be outputted to a file
    does all the hard work in terms of formatting. 
    This function expects a 2d array of entires in the format:
        NAME, INTIME, OUTIME, DATE, HOURS, IS_VALID'''
    users = []  # a list of names given
    user_times = dict()
    # get current date
    now = datetime.datetime.now()
    # format the current date
    date_string = now.strftime("%d/%m/%y")
    # print out header text 
    main_string = HEADER_TEXT 
    main_string += "*********************************DATE: " + date_string
    main_string += "*******************************\n"
    main_string += SPACER_TEXT
    main_string += "\n"
    # Define the sections to display
    main_string += "***" 
    main_string += "Name".rjust(SPACING[0], ' ') + " | "
    main_string += "Time In".rjust(SPACING[1], ' ') + " | "
    main_string += "Time Out".rjust(SPACING[2], ' ') + " | "
    main_string += "Date".rjust(SPACING[3], ' ') + " | "
    main_string += "Calc Hours".rjust(SPACING[4], ' ') + " | "
    main_string += "Valid".rjust(SPACING[5], ' ') + " ****"
    main_string += "\n"
    # now for the entries
    for entry in entries:
        # Handle calculating a users total time.
        if entry[0] in users:
            # then add their time to user_times
            user_times[entry[0]] + int(entry[4])
        else: 
            # this is a new user, create a user_time
            user_times[entry[0]] = 0 
        # add a side bar to left side
        main_string += "***"
        # now actual string formatting, add name and padding
        main_string += entry[0].rjust(SPACING[0], ' ')
        main_string += " | "
        
        # add Time in
        main_string +=entry[1].rjust(SPACING[1],' ') + " | "
        # add Time out
        main_string += entry[2].rjust(SPACING[2], ' ') + " | "
        # add Date
        main_string += entry[3].rjust(SPACING[3], ' ') + " | "

        #Add Times
        main_string += entry[4].rjust(SPACING[4], ' ') + " | "

        #Add Valid time
        main_string += entry[5].rjust(SPACING[5], ' ')
        
        #Add side bar to right side 
        main_string += "*****"

        main_string += "\n" 
    main_string += SPACER_TEXT
    return main_string

#test
print(read_config())
#entries = [["test1", "12:12", "12:35", "02/02/17", "2", " . "],
#        ["test2", "01:01", "00:00", "02/02/17", "3", " X "]]
#print(string_format(entries))