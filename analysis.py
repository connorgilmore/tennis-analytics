# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:46:07 2019

@author: Connor
"""
import pandas as pd

match_scores1 = pd.read_csv('C:/Users/Connor/Documents/Analytics Project/tennis/tennis-analytics/data/match_scores_1877-1967_unindexed.csv')
match_scores2 = pd.read_csv('C:/Users/Connor/Documents/Analytics Project/tennis/tennis-analytics/data/match_scores_1968-1990_unindexed.csv')
match_scores3 = pd.read_csv('C:/Users/Connor/Documents/Analytics Project/tennis/tennis-analytics/data/match_scores_1991-2016_unindexed.csv')
match_scores4 = pd.read_csv('C:/Users/Connor/Documents/Analytics Project/tennis/tennis-analytics/data/match_scores_2017_unindexed.csv')
tournaments = pd.read_csv('C:/Users/Connor/Documents/Analytics Project/tennis/tennis-analytics/data/tournaments_1877-2017_unindexed.csv')

match_scores1_df = pd.DataFrame(match_scores1)
match_scores2_df = pd.DataFrame(match_scores2)
match_scores3_df = pd.DataFrame(match_scores2)
match_scores4_df = pd.DataFrame(match_scores4)
all_matches_df = pd.concat([match_scores1_df, match_scores2_df, match_scores3_df,
                           match_scores4_df])
tournaments_df = pd.DataFrame(tournaments)