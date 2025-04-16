
matches = getTeamScores("25600Y")
matches = matches.get('data')
for match in matches:
    temp_match_scores = []
    match_info = match.get("alliances")[0:2]
    for i in range(2):
        temp_match_scores.append(match_info[i].get("score"))
        temp_match_scores.append(match_info[i].get("teams")[0].get("team").get("name"))
        temp_match_scores.append(match_info[i].get("teams")[1].get("team").get("name"))
    match_scores.append(temp_match_scores)

match_scores = pd.DataFrame(match_scores, columns = ["bscore", "bteam1", "bteam2", "rscore", "rteam1", "rteam2"])
match_scores.to_csv("match_scores")