'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    new_cleaned_list = my_df.groupby(['Act', 'Player']).size().reset_index(name='PlayerLine')
        
    new_cleaned_list['PlayerPercent'] = 100 * new_cleaned_list['PlayerLine'] / new_cleaned_list.groupby('Act')['PlayerLine'].transform('sum')
    
    my_df = new_cleaned_list.sort_values(by=['Act','PlayerLine'], ascending=[True,False])
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # Create a new dataframe for storing the grouped 'OTHER' players
    other_df = my_df.sort_values(by=['Act','PlayerLine'], ascending=[True,False])
    top_players = other_df.groupby(["Player"])["PlayerLine"].sum().sort_values(ascending=False).head(5).index.tolist()
    top_players_df = other_df[other_df["Player"].isin(top_players)]
    
    all_other_players = other_df[~other_df.index.isin(top_players_df.index)]
    
    all_other_players = all_other_players.groupby('Act').agg({
        'Player' : 'last',
        'PlayerLine' : 'sum',
        'PlayerPercent' : 'sum'
    }).reset_index()
    
    all_other_players['Player'] = 'OTHER'
    
    other_df = pd.concat([top_players_df, all_other_players])
    
    other_df = other_df.sort_values(by=['Act'], ascending=[True])
    
    other_df = other_df.rename(columns={"PlayerLine": "LineCount", "PlayerPercent": "LinePercent"})
    return other_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    my_df['Player'] = my_df['Player'].str.title()
    return my_df
