import csv

# Load data from election_data.csv
file_path = "election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row

    # Loop through rows in the CSV
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # Update candidate's vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

        # Check for winner
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Print results to terminal
print("Election Results")
print("-" * 25)
print(f"Total Votes: {total_votes}")
print("-" * 25)

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-" * 25)
print(f"Winner: {winner['name']}")
print("-" * 25)

# Export results to a text file
output_file_path = "election_analysis_results.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-" * 25 + "\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-" * 25 + "\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    output_file.write("-" * 25 + "\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-" * 25 + "\n")

print(f"Results exported to {output_file_path}")
"""
Created on Tue Jan  9 21:08:41 2024

@author: wfede
"""

