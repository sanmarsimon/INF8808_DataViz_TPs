'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    # fig = go.Figure(go.Choroplethmapbox(geojson=montreal_data, locations=locations, z=z_vals, colorscale=colorscale, marker_opacity=0.2))
    # fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=9.5, mapbox_center = {"lat": 45.50884, "lon": -73.58781})

    # fig.add_trace(
    #     go.Choroplethmapbox(
    #         locations=locations,
    #         z=z_vals,
    #         geojson=montreal_data,
    #         colorscale=colorscale,
    #         marker_opacity=0.2,
    #         #hovertemplate=hover.get_hover_template()
    #     )
    # )

        # Create the base map
    # fig.add_trace(
    #     go.Choroplethmapbox(
    #         geojson=montreal_data,
    #         locations=locations,
    #         z=z_vals,
    #         colorscale=colorscale,
    #         marker_opacity=0.2,
    #         #hovertemplate=hover.get_hover_template(),
    #         showlegend=False,
    #     ),
    # )

    # # Set the map layout
    # fig.update_layout(
    #     mapbox_style="carto-positron",
    #     mapbox_zoom=10,
    #     mapbox_center={"lat": 45.522, "lon": -73.619},
    # )

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=montreal_data,
            locations=locations,
            featureidkey="properties.NOM",
            z=z_vals,
            zauto=True,
            colorscale=colorscale,
            showscale=False,
            marker_line_color='grey',
        )
    )

    fig.update_traces(hovertemplate=hover.map_base_hover_template())

    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    colors = {
        "Noyau villageois": "#636EFA",
        "Passage entre rues résidentielles": "#EF553B",
        "Rue bordant un bâtiment public ou institutionnel": "#00CC96",
        "Rue commerciale de quartier, d’ambiance ou de destination": "#AB63FA",
        "Rue en bordure ou entre deux parcs ou place publique": "#FFA15A",
        "Rue entre un parc et un bâtiment public ou institutionnel": "#19D3F3",
        "Rue transversale à une rue commerciale": "#FF6692",
    }

    for intervention, intervention_data in street_df.groupby(
        "properties.TYPE_SITE_INTERVENTION"
    ):
        fig.add_trace(
            go.Scattermapbox(
                lat=intervention_data["properties.LATITUDE"],
                lon=intervention_data["properties.LONGITUDE"],
                name=intervention,
                hovertemplate=hover.map_marker_hover_template(intervention),
                marker=go.scattermapbox.Marker(
                    size=20, color=colors[intervention]
                ),
                customdata=[
                    intervention_data["properties.NOM_PROJET"],
                    intervention_data["properties.MODE_IMPLANTATION"],
                    intervention_data["properties.OBJECTIF_THEMATIQUE"],
                ],
            )
        )

    return fig
