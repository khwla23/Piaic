import csv
#with open ("competition.csv", "a") as f:
#    content_of_file = csv.writer(f, delimiter = ",")
#    year = input (" Enter the year:")
#    event = input (" Enter the event name:")
#    winner = input (" Enter the winner of the Event:")
#    content_of_file.writerow([year, event, winner])
         #>.............READING.....<#
with open ("competition.csv") as f:
    contents_of_f = csv.reader(f, delimiter = ",")
    potter_competitions = [] 
    for each_line in contents_of_f:
        potter_competitions += each_line


print(potter_competitions[1])        
 