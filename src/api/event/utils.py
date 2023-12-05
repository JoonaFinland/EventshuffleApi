from typing import List, Dict, Any

def transform_votes(votes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    transformed_data = []
    for vote_entry in votes:
        for date in vote_entry["date"]:
            existing_entry = next((entry for entry in transformed_data if entry["date"] == date), None)
            if existing_entry:
                existing_entry["people"].append(vote_entry["voter_name"])
            else:
                transformed_data.append({"date": date, "people": [vote_entry["voter_name"]]})

    return transformed_data

def get_suitable_dates(votes: List[Dict[str, Any]]) -> List[str]:
    # get all the unique voter names from each date entry
    all_voters = get_unique_voters(votes)
    suitable_dates = []

    for date_entry in votes:
        if list(set(date_entry["people"])) == all_voters:
            suitable_dates.append({
                "date":date_entry["date"],
                "people": list(set(date_entry["people"]))})

    return suitable_dates

def get_unique_voters(votes: List[Dict[str, Any]]) -> List[str]:
    all_voters = list(set(voter for date in votes for voter in date["people"]))
    return all_voters