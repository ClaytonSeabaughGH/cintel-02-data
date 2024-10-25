import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

# Load data in with built in function
penguins_df = palmerpenguins.load_penguins()

#-----------------------
# Define User Interface
#------------------------

# Create Title
ui.page_opts(title="Clayton's Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="")
