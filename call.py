import requests

# def getTeamId(teamNumber):
#     # API endpoint
#     url = ("https://www.robotevents.com/api/v2/teams")
#
#     # Your API key
#     api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiZmExNTlkODcwYWRiZTU2MGNmMzQwNTU2ZmRmN2JiMjRmNjgwZWQ3ZDg5YWE5ZTdiZjQxMDNhMTZlZTBlNmNkODFkZDZiNDNkODJmYmNiYTYiLCJpYXQiOjE3MzY1MTcwOTIuMjcxNTA1MSwibmJmIjoxNzM2NTE3MDkyLjI3MTUwOCwiZXhwIjoyNjgzMjAxODkyLjI2NDk4Nywic3ViIjoiMTQyNTkwIiwic2NvcGVzIjpbXX0.lda8sp5OZ4ArofulBB13K-0638X0A2EyGAz8yAt6TG3pd-2Z9KxZH_xXv5ZMaEkeUAOiGp69NSlZznWqgiig49JIVlGVuSSqklHPxNlzlr8wEOu1nA8cW-iZdrUv2FRt-gj_TYaD1am1VxXGJA-K3AYqlK-16tgWBlCPrfOs3MiiGduPJPa0QEMvy5XPaGLTLViwuzHKMIQWD60qKwZakzbx7x5rWlluCwBoXcu6X7IbdmFgFiUeEqyBCs3JbIn52aEaWS9i7488WHGjhRmUSM-BB_odLVWAoVAYwJEajPO-jl820cFqm57Ul08gfUspGrPCsP2iW59OJhm2seMfPhkkOHH08YG_vhrRnN-xVnDy82MlVC3x0cvr6JyVk9AK49NbVhgw9C30V2S5wNrZnvJSrqVlql2L3yhufEvkJBkjIxWWC4Fw-idOvEezjCIoJ9ISf-Dd-gDIVLH3FDLSWMbLWEnV_dBmw25mM-zJUepA1eCACnlJdl0YgnVw6FeI7plsicpa3x7NG70MW_vB9CX9qLOIF8sQw3xX94Dnbwgq3XcUeCJ8geCSISCu4gr2SKz4PKk1hkumlUMHQvHISeKPDj7WsCmrb8l_CvWCSA3e13_Zp2iTTfx-Cq-NLUc6xYrm4AQ6ZnlADRcWllGI483uj-nTjNZWFOp1imOeSlo"
#
#     # Headers with the API key
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#         "Accept": "application/json"  # Explicitly request JSON
#     }
#
#     # Query parameters
#     params = {
#         "number[]": [teamNumber]
#     }
#
#     # Make the request
#     response = requests.get(url, headers=headers, params = params)
#
#     # Check response
#     #if response.status_code == 200:
#         #print(response.json())
#     #else:
#         #print(f"Error: {response.status_code}, {response.text}")
#
#     team_id = response.json()['data'][0]['id']
#     return(team_id)
#
# def getTeamScores(teamNumber):
#
#     teamId = teamNumber
#
#     # Your API key
#     api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiZmExNTlkODcwYWRiZTU2MGNmMzQwNTU2ZmRmN2JiMjRmNjgwZWQ3ZDg5YWE5ZTdiZjQxMDNhMTZlZTBlNmNkODFkZDZiNDNkODJmYmNiYTYiLCJpYXQiOjE3MzY1MTcwOTIuMjcxNTA1MSwibmJmIjoxNzM2NTE3MDkyLjI3MTUwOCwiZXhwIjoyNjgzMjAxODkyLjI2NDk4Nywic3ViIjoiMTQyNTkwIiwic2NvcGVzIjpbXX0.lda8sp5OZ4ArofulBB13K-0638X0A2EyGAz8yAt6TG3pd-2Z9KxZH_xXv5ZMaEkeUAOiGp69NSlZznWqgiig49JIVlGVuSSqklHPxNlzlr8wEOu1nA8cW-iZdrUv2FRt-gj_TYaD1am1VxXGJA-K3AYqlK-16tgWBlCPrfOs3MiiGduPJPa0QEMvy5XPaGLTLViwuzHKMIQWD60qKwZakzbx7x5rWlluCwBoXcu6X7IbdmFgFiUeEqyBCs3JbIn52aEaWS9i7488WHGjhRmUSM-BB_odLVWAoVAYwJEajPO-jl820cFqm57Ul08gfUspGrPCsP2iW59OJhm2seMfPhkkOHH08YG_vhrRnN-xVnDy82MlVC3x0cvr6JyVk9AK49NbVhgw9C30V2S5wNrZnvJSrqVlql2L3yhufEvkJBkjIxWWC4Fw-idOvEezjCIoJ9ISf-Dd-gDIVLH3FDLSWMbLWEnV_dBmw25mM-zJUepA1eCACnlJdl0YgnVw6FeI7plsicpa3x7NG70MW_vB9CX9qLOIF8sQw3xX94Dnbwgq3XcUeCJ8geCSISCu4gr2SKz4PKk1hkumlUMHQvHISeKPDj7WsCmrb8l_CvWCSA3e13_Zp2iTTfx-Cq-NLUc6xYrm4AQ6ZnlADRcWllGI483uj-nTjNZWFOp1imOeSlo"
#
#     # Headers with the API key
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#         "Accept": "application/json"  # Explicitly request JSON
#     }
#
#     url = ("https://www.robotevents.com/api/v2/teams/" + str(teamId) + "/matches")
#
#     # Make the request
#     response = requests.get(url, headers=headers)
#
#     # Check response
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print(f"Error: {response.status_code}, {response.text}")
#
#     return(response.json())

def getTeams(grade = "High School"):
    # API endpoint
    url = ("https://www.robotevents.com/api/v2/teams")

    # Your API key
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiZmExNTlkODcwYWRiZTU2MGNmMzQwNTU2ZmRmN2JiMjRmNjgwZWQ3ZDg5YWE5ZTdiZjQxMDNhMTZlZTBlNmNkODFkZDZiNDNkODJmYmNiYTYiLCJpYXQiOjE3MzY1MTcwOTIuMjcxNTA1MSwibmJmIjoxNzM2NTE3MDkyLjI3MTUwOCwiZXhwIjoyNjgzMjAxODkyLjI2NDk4Nywic3ViIjoiMTQyNTkwIiwic2NvcGVzIjpbXX0.lda8sp5OZ4ArofulBB13K-0638X0A2EyGAz8yAt6TG3pd-2Z9KxZH_xXv5ZMaEkeUAOiGp69NSlZznWqgiig49JIVlGVuSSqklHPxNlzlr8wEOu1nA8cW-iZdrUv2FRt-gj_TYaD1am1VxXGJA-K3AYqlK-16tgWBlCPrfOs3MiiGduPJPa0QEMvy5XPaGLTLViwuzHKMIQWD60qKwZakzbx7x5rWlluCwBoXcu6X7IbdmFgFiUeEqyBCs3JbIn52aEaWS9i7488WHGjhRmUSM-BB_odLVWAoVAYwJEajPO-jl820cFqm57Ul08gfUspGrPCsP2iW59OJhm2seMfPhkkOHH08YG_vhrRnN-xVnDy82MlVC3x0cvr6JyVk9AK49NbVhgw9C30V2S5wNrZnvJSrqVlql2L3yhufEvkJBkjIxWWC4Fw-idOvEezjCIoJ9ISf-Dd-gDIVLH3FDLSWMbLWEnV_dBmw25mM-zJUepA1eCACnlJdl0YgnVw6FeI7plsicpa3x7NG70MW_vB9CX9qLOIF8sQw3xX94Dnbwgq3XcUeCJ8geCSISCu4gr2SKz4PKk1hkumlUMHQvHISeKPDj7WsCmrb8l_CvWCSA3e13_Zp2iTTfx-Cq-NLUc6xYrm4AQ6ZnlADRcWllGI483uj-nTjNZWFOp1imOeSlo"

    # Headers with the API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"  # Explicitly request JSON
    }

    all_teams = []
    page = 1
    per_page = 999

    # for i in range(170):
    params = {
        "grade[]": "High School",
        #"country[]": "US",
        "per_page": per_page,
        "page": page,
        "program[]":1,
    }
    response = requests.get(url, headers=headers, params=params)
    # if response.status_code != 200:
    #     break
    data = response.json()
    teams = data.get('data', [])
    # if not isinstance(teams, list) or not teams:
    #     break

    # all_teams.extend(teams)

    # page += 1

    return teams
    # Query parameters

# def getTeamsFromEvent(eventId):
#     # API endpoint
#     url = ("https://www.robotevents.com/api/v2/events/" + eventId + "/teams")
#
#     # Your API key
#     api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiZmExNTlkODcwYWRiZTU2MGNmMzQwNTU2ZmRmN2JiMjRmNjgwZWQ3ZDg5YWE5ZTdiZjQxMDNhMTZlZTBlNmNkODFkZDZiNDNkODJmYmNiYTYiLCJpYXQiOjE3MzY1MTcwOTIuMjcxNTA1MSwibmJmIjoxNzM2NTE3MDkyLjI3MTUwOCwiZXhwIjoyNjgzMjAxODkyLjI2NDk4Nywic3ViIjoiMTQyNTkwIiwic2NvcGVzIjpbXX0.lda8sp5OZ4ArofulBB13K-0638X0A2EyGAz8yAt6TG3pd-2Z9KxZH_xXv5ZMaEkeUAOiGp69NSlZznWqgiig49JIVlGVuSSqklHPxNlzlr8wEOu1nA8cW-iZdrUv2FRt-gj_TYaD1am1VxXGJA-K3AYqlK-16tgWBlCPrfOs3MiiGduPJPa0QEMvy5XPaGLTLViwuzHKMIQWD60qKwZakzbx7x5rWlluCwBoXcu6X7IbdmFgFiUeEqyBCs3JbIn52aEaWS9i7488WHGjhRmUSM-BB_odLVWAoVAYwJEajPO-jl820cFqm57Ul08gfUspGrPCsP2iW59OJhm2seMfPhkkOHH08YG_vhrRnN-xVnDy82MlVC3x0cvr6JyVk9AK49NbVhgw9C30V2S5wNrZnvJSrqVlql2L3yhufEvkJBkjIxWWC4Fw-idOvEezjCIoJ9ISf-Dd-gDIVLH3FDLSWMbLWEnV_dBmw25mM-zJUepA1eCACnlJdl0YgnVw6FeI7plsicpa3x7NG70MW_vB9CX9qLOIF8sQw3xX94Dnbwgq3XcUeCJ8geCSISCu4gr2SKz4PKk1hkumlUMHQvHISeKPDj7WsCmrb8l_CvWCSA3e13_Zp2iTTfx-Cq-NLUc6xYrm4AQ6ZnlADRcWllGI483uj-nTjNZWFOp1imOeSlo"
#
#     # Headers with the API key
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#         "Accept": "application/json"  # Explicitly request JSON
#     }
#
#     params = {
#         "per_page": 9999
#     }
#
#     # Query parameters
#
#     # Make the request
#     response = requests.get(url, headers=headers, params=params)
#
#     # Check response
#     #if response.status_code == 200:
#         #print(response.json())
#     #else:
#         #print(f"Error: {response.status_code}, {response.text}")
#
#     teams = response.json()
#     return(teams)
#
# def getEvents():
#     # API endpoint
#     url = ("https://www.robotevents.com/api/v2/events")
#
#     # Your API key
#     api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiZmExNTlkODcwYWRiZTU2MGNmMzQwNTU2ZmRmN2JiMjRmNjgwZWQ3ZDg5YWE5ZTdiZjQxMDNhMTZlZTBlNmNkODFkZDZiNDNkODJmYmNiYTYiLCJpYXQiOjE3MzY1MTcwOTIuMjcxNTA1MSwibmJmIjoxNzM2NTE3MDkyLjI3MTUwOCwiZXhwIjoyNjgzMjAxODkyLjI2NDk4Nywic3ViIjoiMTQyNTkwIiwic2NvcGVzIjpbXX0.lda8sp5OZ4ArofulBB13K-0638X0A2EyGAz8yAt6TG3pd-2Z9KxZH_xXv5ZMaEkeUAOiGp69NSlZznWqgiig49JIVlGVuSSqklHPxNlzlr8wEOu1nA8cW-iZdrUv2FRt-gj_TYaD1am1VxXGJA-K3AYqlK-16tgWBlCPrfOs3MiiGduPJPa0QEMvy5XPaGLTLViwuzHKMIQWD60qKwZakzbx7x5rWlluCwBoXcu6X7IbdmFgFiUeEqyBCs3JbIn52aEaWS9i7488WHGjhRmUSM-BB_odLVWAoVAYwJEajPO-jl820cFqm57Ul08gfUspGrPCsP2iW59OJhm2seMfPhkkOHH08YG_vhrRnN-xVnDy82MlVC3x0cvr6JyVk9AK49NbVhgw9C30V2S5wNrZnvJSrqVlql2L3yhufEvkJBkjIxWWC4Fw-idOvEezjCIoJ9ISf-Dd-gDIVLH3FDLSWMbLWEnV_dBmw25mM-zJUepA1eCACnlJdl0YgnVw6FeI7plsicpa3x7NG70MW_vB9CX9qLOIF8sQw3xX94Dnbwgq3XcUeCJ8geCSISCu4gr2SKz4PKk1hkumlUMHQvHISeKPDj7WsCmrb8l_CvWCSA3e13_Zp2iTTfx-Cq-NLUc6xYrm4AQ6ZnlADRcWllGI483uj-nTjNZWFOp1imOeSlo"
#
#     # Headers with the API key
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#         "Accept": "application/json"  # Explicitly request JSON
#     }
#
#     params = {
#         "per_page":999,
#         "region": "Massachusetts",
#         "season[]":190,
#         "program":"V5RC"
#     }
#
#     # Query parameters
#
#     # Make the request
#     response = requests.get(url, headers=headers, params=params)
#
#     # Check response
#     #if response.status_code == 200:
#         #print(response.json())
#     #else:
#         #print(f"Error: {response.status_code}, {response.text}")
#
#     teams = response.json()
#     return(teams)
#
# def getEventIds():
#     ids = []
#     for event in getEvents().get('data'):
#         ids.append(event.get('id'))
#     return ids

# def get_match_scores(teamid):
#     matches = getTeamScores(teamid)
#     matches = matches.get('data')
#     match_scores = []
#     for match in matches:
#         temp_match_scores = []
#         match_info = match.get("alliances")[0:2]
#         for i in range(2):
#             temp_match_scores.append(match_info[i].get("score"))
#             temp_match_scores.append(match_info[i].get("teams")[0].get("team").get("name"))
#             temp_match_scores.append(match_info[i].get("teams")[1].get("team").get("name"))
#         match_scores.append(temp_match_scores)
#     return match_scores

def extract_id(data: dict) -> str:
    """
    Extracts and returns the string representation of the value
    associated with the key id in the provided dictionary.
    """
    return str(data.get("id", "Key not found"))


from pprint import pprint
import pandas as pd
# pprint(getTeamScores("25600Y"))
# print(getTeams().get('data'))
#for team in getTeams().get('data'):
    #for match in get_match_scores(team.get('id')):
        #if match not in match_scores:
            #match_scores.append(match)

#print(match_scores)

teamlist = getTeams()
pprint(teamlist)
teamIdList = []
for i in teamlist:
    teamIdList.append(extract_id(i))
pprint(teamIdList)


# import json
# #
# with open("teams_data.json", "w") as f:
#     json.dump(teamlist, f, indent=4)
# print(getEventIds())
# event_list = getEventIds()
#
# for i in event_list:
#     pprint(getTeamScores(str(i)))



# matches = getTeamScores("25600Y")
# matches = matches.get('data')
# for match in matches:
#     temp_match_scores = []
#     match_info = match.get("alliances")[0:2]
#     for i in range(2):
#         temp_match_scores.append(match_info[i].get("score"))
#         temp_match_scores.append(match_info[i].get("teams")[0].get("team").get("name"))
#         temp_match_scores.append(match_info[i].get("teams")[1].get("team").get("name"))
#     match_scores.append(temp_match_scores)

# match_scores = pd.DataFrame(match_scores, columns = ["bscore", "bteam1", "bteam2", "rscore", "rteam1", "rteam2"])
# match_scores.to_csv("match_scores")