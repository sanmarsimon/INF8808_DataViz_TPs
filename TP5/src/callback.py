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
    mode_new = figure["data"][curve]["customdata"][1][point]
    theme_new = figure["data"][curve]["customdata"][2][point]
    title_new = figure["data"][curve]["customdata"][0][point]

    if theme_new is not None:
        theme_new = (
            html.Div(
                [
                    "Thématique:",
                    html.Ul(children=[html.Li(item) for item in theme_new.split("\n")]),
                ]
            ),
        )

    return (
        html.Div(title_new, style={"color": figure["data"][curve]["marker"]["color"]}),
        mode_new,
        theme_new,
        {
            "border": "1px solid black",
            "padding": "10px",
        },
    )
