import csv

filepath = 'employee_data.csv'

eid = []
name = []
dob = []
ssn = []
state = []

with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile)
    for row in reader:
        eid.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
        
first_name = []
last_name = []

for n in name:
    s = n.split()
    first_name.append(s[0])
    last_name.append(s[1])
    
birthday = []    

for n in dob:
    s = n.split('-')
    birthday.append(f'{s[1]}/{s[2]}/{s[0]}')
    
ssn_modified = []
    
for n in ssn:
    s = n.split('-')
    ssn_modified.append(f'***-**-{s[2]}')
    
    
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

state_modified = []

for n in state:
    s = us_state_abbrev[n]
    state_modified.append(s)
    
output = 'output.csv'

with open(output, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    for i in range(0, len(eid)):
        writer.writerow([eid[i], first_name[i], last_name[i], birthday[i], ssn_modified[i], state_modified[i]])