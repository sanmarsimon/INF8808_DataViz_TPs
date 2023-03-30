"""
    This file contains the functions to call when
    a click is detected on the map, depending on the context
"""
import dash_html_components as html


def no_clicks(style):
    """
    Deals with the case where the map was not clicked

    Args:
        style: The current display style for the panel
    Returns:
        title: The updated display title
        mode: The updated display title
        theme: The updated display theme
        style: The updated display style for the panel
    """
    return None, None, None, None


def map_base_clicked(title, mode, theme, style):
    """
    Deals with the case where the map base is
    clicked (but not a marker)

    Args:
        title: The current display title
        mode: The current display title
        theme: The current display theme
        style: The current display style for the panel
    Returns:
        title: The updated display title
        mode: The updated display title
        theme: The updated display theme
        style: The updated display style for the panel
    """
    return title, mode, theme, style


def map_marker_clicked(
    figure, curve, point, title, mode, theme, style
):  # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    """
    Deals with the case where a marker is clicked

    Args:
        figure: The current figure
        curve: The index of the curve containing the clicked marker
        point: The index of the clicked marker
        title: The current display title
        mode: The current display title
        theme: The current display theme
        style: The current display style for the panel
    Returns:
        title: The updated display title
        mode: The updated display title
        theme: The updated display theme
        style: The updated display style for the panel
    """
    new_title = figure["data"][curve]["customdata"][0][point]
    new_mode = figure["data"][curve]["customdata"][1][point]
    new_theme = figure["data"][curve]["customdata"][2][point]

    if new_theme is not None:
        new_theme = (
            html.Div(
                [
                    "Thématique:",
                    html.Ul(children=[html.Li(item) for item in new_theme.split("\n")]),
                ]
            ),
        )

    return (
        html.Div(new_title, style={"color": figure["data"][curve]["marker"]["color"]}),
        new_mode,
        new_theme,
        {
            "border": "1px solid black",
            "padding": "10px",
        },
    )
