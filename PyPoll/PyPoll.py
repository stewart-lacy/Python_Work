import os 
import csv 
file_to_load = "Resources/election_data.csv"
total_votes = 0 
list_of_candidates = []
candidate_votes = {}
winner_name= []
winner_votes = 0

with open(file_to_load) as poll_data: 
    reader = csv.DictReader(poll_data)
    first_row = next(reader)
    #vote count
    total_votes = total_votes + 1
    # list of candidates
    

    for row in reader: 
        #vote count
        total_votes = total_votes + 1 
        #List of candidate
        candidates = row["Candidate"]
        #To loop through the data to ensure 
        # that we append all names in that column 
        # and not ensure that they do not repeat themselves 
        if candidates not in list_of_candidates: 
            list_of_candidates.append(candidates)
            candidate_votes[candidates]=0
        candidate_votes[candidates] =  candidate_votes[candidates] + 1 
#to get winner you must loop to find the number of votes each candidate has 
for candidates in candidate_votes: 
                #getting all votes each canidate has 
                votes =  candidate_votes.get(candidates)
                #getting the % of votes 
                Percent_of_votes = float(votes)/float(total_votes) * 100
                # storing in the dict each candidate vote count and %
                candidate_votes[candidates] = candidate_votes[candidates], Percent_of_votes 
                #looping through to see which candidate has the most votes
                if (votes > winner_votes ): 
                    winner_votes = votes
                    winner_name = candidates

output_file = os.path.join("PyPoll_Solved.txt")
with open(output_file, "w", newline="") as txt_file:
    answer = (
     "\n Election Results\n"
     "\n ------------------------- \n"
     f"\n Total Votes : {total_votes:.2f}\n"
     "\n ------------------------- \n")
     
    print(answer)
    txt_file.write(answer)

    for candidates,t in candidate_votes.items():
        canidates_list = f"\n{candidates} {t[0]:2f} ({t[1]:2f})% \n"   
        print(canidates_list)
        txt_file.write(canidates_list )

    rest_of_data = ("\n ------------------------- \n"
    f"\n Winner: {winner_name}\n"
    "\n ------------------------- \n" )
    print(rest_of_data)
    txt_file.write(rest_of_data )





