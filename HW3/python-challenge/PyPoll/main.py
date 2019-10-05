import csv

filepath = 'Resources/election_data.csv'

voter_id = []
county = []
candidate = []

with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile)
    for row in reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

votes = {}

for vote in candidate:
    if vote in votes:
        votes[vote] += 1
    else:
        votes.update({vote:0})
        
total_votes = len(candidate)

candidate_name = []
candidate_votes = []
vote_percents = []

for c in votes:
    candidate_name.append(c)
    candidate_votes.append(votes[c])
    vote_percents.append(round(100 * votes[c]/total_votes, 2))

winner = max(votes, key = votes.get)

output = 'Resources/output.csv'

with open(output, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Election Results'])
    writer.writerow(['----------------------------'])
    writer.writerow([f'Total Votes: {total_votes}'])
    writer.writerow(['----------------------------'])
    for i in range(0, len(votes)):
        writer.writerow([f'{candidate_name[i]}: {vote_percents[i]}% ({candidate_votes[i]})'])
    writer.writerow(['----------------------------'])
    writer.writerow(['Winner: {winner}'])
    

print('Election Results')
print('----------------------------')
print(f'Total Votes: {total_votes}')
print('----------------------------')
for i in range(0, len(votes)):
    print(f'{candidate_name[i]}: {vote_percents[i]}% ({candidate_votes[i]})')
print('----------------------------')
print(f'Winner: {winner}')
        
    