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
    # Add 'PlayerLine' column and fill with 0
    my_df['PlayerLine'] = 0
    my_df.drop('Scene', inplace=True, axis=1)
    
    # Group by Act, Scene, and Player
    grouped = my_df.groupby(['Act', 'Player'])
    
    # count lines per player per act and store in 'PlayerLine' column
    my_df['PlayerLine'] = grouped['Line'].transform('count')
    
    # Add 'PlayerPercent' column and fill with 0
    my_df['PlayerPercent'] = 0
    
    # Calculate percentage of lines per player per act
    my_df['PlayerPercent'] = my_df['PlayerLine']/grouped['PlayerLine'].transform('sum') * 100
    my_df.drop('Line', inplace=True, axis=1)
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
    other_df = pd.DataFrame(columns=['Act', 'Player', 'PlayerLine', 'PlayerPercent'])
    
    # Find the top 5 players with the most lines in the play
    top_players = my_df.groupby(['Player'])['PlayerLine'].sum().sort_values(ascending=False).head(5).index.tolist()
    top_players_df = my_df[my_df['Player'].isin(top_players)]
    top_players_df = top_players_df.drop_duplicates()
    
    # Sum the total lines in the play
    total_lines = my_df['PlayerLine'].sum()
    # Iterate through each act
    for act in my_df['Act'].unique():
        # Get all players who are not in the top 5 players
        other_players = my_df[~my_df['Player'].isin(top_players) & (my_df['Act'] == act)]
        other_players = other_players.drop_duplicates()
        
        # Sum the lines and percentages for all players who are not in the top 5
        line_count = other_players['PlayerLine'].sum()
        percent_count = line_count / total_lines * 100
        
        # Append the data for the 'OTHER' player for this act to the new dataframe
        other_df = other_df.append({'Act': act, 'Player': 'OTHER', 'PlayerLine': line_count, 'PlayerPercent': percent_count}, ignore_index=True)
    
    # Append the new dataframe to the original dataframe
    top_players_df = top_players_df.groupby(['Act','Player'], as_index=False).sum()
    my_df = pd.concat([top_players_df, other_df], ignore_index=True)
    my_df = my_df.sort_values('Act')
    my_df = my_df.rename(columns={"PlayerLine": "LineCount", "PlayerPercent": "LinePercent"})
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    my_df['Player'] = my_df['Player'].str.title()
    return my_df
