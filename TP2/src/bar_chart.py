'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # TODO : Update the template to include our new theme and set the title

    fig.update_layout(
        template=pio.templates['simple_white'],
        dragmode=False,
        barmode='relative',
        title='Lines per act',
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    fig = go.Figure(fig)  # conversion back to Graph Object
    # TODO : Update the figure's data according to the selected mode
    
    if mode == 'Count':
        y_data = 'LineCount'
    elif mode == 'Percent':
        y_data = 'LinePercent'
    else:
        raise ValueError("Invalid mode, please choose 'count' or 'percent'")
    print(data)
    Benvolio = data[data["Player"] == "Benvolio"]
    Juliet = data[data["Player"] == "Juliet"]
    Mercutio = data[data["Player"] == "Mercutio"]
    Nurse = data[data["Player"] == "Nurse"]
    Romeo = data[data["Player"] == "Romeo"]
    Others = data[data["Player"] == "Other"]
    fig.add_trace(go.Bar(name="Benvolio", x=Benvolio["Act"], y=Benvolio[y_data]))
    fig.add_trace(go.Bar(name="Juliet", x=Juliet["Act"], y=Juliet[y_data]))
    fig.add_trace(go.Bar(name="Mercutio", x=Mercutio["Act"], y=Mercutio[y_data]))
    fig.add_trace(go.Bar(name="Nurse", x=Nurse["Act"], y=Nurse[y_data]))
    fig.add_trace(go.Bar(name="Romeo", x=Romeo["Act"], y=Romeo[y_data]))
    fig.add_trace(go.Bar(name="Others", x=Others["Act"], y=Others[y_data]))
    fig.update_layout(barmode="stack")
    return update_y_axis(fig, mode)


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode
    fig = go.Figure(fig)
    if mode == 'Count':
        y_axis_title = 'Lines (Count)'
    elif mode == 'Percent':
        y_axis_title = 'Lines (%)'
    print(mode)
    
    fig.update_layout(yaxis_title=y_axis_title)
    return fig