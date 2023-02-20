'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import plotly.io as pio
import hover_template


def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    fig = px.imshow(data)
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Neighborhood',
        dragmode = False,
        coloraxis_colorbar_title_text = 'Trees',

        # Set the x-axis ticks to be the years in the dataset and display the year only
        xaxis = dict(
            tickmode = 'array',
            tickvals = data.columns,
            ticktext = data.columns.str.slice(0, 4) # Display only the year
        )
    )
    
    fig.update_traces(hovertemplate = hover_template.get_heatmap_hover_template())
    #fig.show()
    return fig
