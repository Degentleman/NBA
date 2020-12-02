#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:20:00 2018

@author: Degentleman
"""
import requests
import json
import pandas as pd
Team_Legend = pd.read_csv('NBA PBP - Team Legend.csv', delimiter = ',')

def GetDB(teamID):
    row = Team_Legend[(Team_Legend.TeamID == teamID)]
    team_name = row.Team.item()
    team_code = row.Code.item()
    mapping = {teamID:team_code}
    
    # Scrape URL for Team
    url = 'https://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2019-20&TeamID={team_id}'.format(team_id=teamID)
    headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true'
    }
    response = requests.get(url, headers = headers)
    
    if str(response) == '<Response [200]>':
    
        data = json.loads(response.content.decode())
        
        # Organize json data into DataFrame
        team_keys = list(data['resultSets'][0])
        coach_keys = list(data['resultSets'][1])
        team_dict = data['resultSets'][0]
        coach_dict = data['resultSets'][1]
        team_headers = team_dict[team_keys[1]]
        coach_headers = coach_dict[coach_keys[1]]
        team_data = team_dict[team_keys[2]]
        coach_data = coach_dict[coach_keys[2]]
        team_df = pd.DataFrame(data=team_data, columns=team_headers)
        coach_df = pd.DataFrame(data=coach_data, columns=coach_headers)
        
        new_df_cols = ['TeamID','PLAYER', 'HEIGHT', 'WEIGHT','POSITION', 'PLAYER_ID']
        
        player_df = team_df[new_df_cols]
        
        player_df = player_df.replace({'TeamID': mapping})
        
        new_col_head = ['Team', 'Player', 'Height', 'Weight','Position', 'PlayerID', ]
        
        player_df.columns = new_col_head
        
        return(team_name, team_code, team_df, coach_df, player_df)
