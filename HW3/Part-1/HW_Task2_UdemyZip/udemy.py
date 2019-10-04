import os
import csv

udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

s = "a b"
v = str.split(s)[0]
print(v)

with open(udemy_csv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        
        #convert length to int
        length_s = row[9]
        length_i = str.split(length_s)[0]
        length.append(length_i)
        
        review_percent.append(round(int(row[6])/int(row[5]), 2))

courses = zip(title, price, subscribers, reviews, length, review_percent)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    writer.writerows(courses)
