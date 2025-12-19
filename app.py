from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Initialize the app with external stylesheets
app = Dash(__name__)

# Load the data
df = pd.read_csv('pink_morsel_data.csv')

# Define color scheme
COLORS = {
    'primary': '#FF6B9D',      # Pink morsel theme color
    'secondary': '#4A90A4',    
    'background': '#1a1a2e',   # Dark background
    'card': '#16213e',         # Card background
    'text': '#ffffff',         
    'text_muted': '#a0a0a0',   
    'accent': '#e94560',       
    'gradient_start': '#0f3460',
    'gradient_end': '#16213e'
}

# App layout with modern styling
app.layout = html.Div(
    style={
        'minHeight': '100vh',
        'background': f'linear-gradient(135deg, {COLORS["gradient_start"]} 0%, {COLORS["gradient_end"]} 100%)',
        'padding': '40px 20px',
        'fontFamily': '"Inter", -apple-system, BlinkMacSystemFont, sans-serif'
    },
    children=[
        # Header section
        html.Div(
            style={
                'textAlign': 'center',
                'marginBottom': '40px'
            },
            children=[
                html.H1(
                    '🍬 Pink Morsel Sales Dashboard',
                    style={
                        'color': COLORS['primary'],
                        'fontSize': '2.8rem',
                        'fontWeight': '700',
                        'marginBottom': '10px',
                        'textShadow': '2px 2px 4px rgba(0,0,0,0.3)',
                        'letterSpacing': '-0.5px'
                    }
                ),
                html.P(
                    'Analyze regional sales performance over time',
                    style={
                        'color': COLORS['text_muted'],
                        'fontSize': '1.2rem',
                        'marginTop': '0'
                    }
                )
            ]
        ),
        
        # Main content card
        html.Div(
            style={
                'maxWidth': '1200px',
                'margin': '0 auto',
                'backgroundColor': COLORS['card'],
                'borderRadius': '20px',
                'padding': '30px',
                'boxShadow': '0 20px 60px rgba(0,0,0,0.3)',
                'border': f'1px solid rgba(255,255,255,0.1)'
            },
            children=[
                # Filter section
                html.Div(
                    style={
                        'marginBottom': '30px',
                        'padding': '20px',
                        'backgroundColor': 'rgba(255,255,255,0.05)',
                        'borderRadius': '12px',
                        'border': '1px solid rgba(255,255,255,0.1)'
                    },
                    children=[
                        html.Label(
                            '📍 Filter by Region',
                            style={
                                'color': COLORS['text'],
                                'fontSize': '1.1rem',
                                'fontWeight': '600',
                                'marginBottom': '15px',
                                'display': 'block'
                            }
                        ),
                        dcc.RadioItems(
                            id='region-filter',
                            options=[
                                {'label': '🌐 All Regions', 'value': 'all'},
                                {'label': '🔺 North', 'value': 'north'},
                                {'label': '▶️ East', 'value': 'east'},
                                {'label': '🔻 South', 'value': 'south'},
                                {'label': '◀️ West', 'value': 'west'}
                            ],
                            value='all',
                            inline=True,
                            style={
                                'display': 'flex',
                                'gap': '10px',
                                'flexWrap': 'wrap'
                            },
                            labelStyle={
                                'display': 'inline-flex',
                                'alignItems': 'center',
                                'padding': '12px 20px',
                                'backgroundColor': 'rgba(255,107,157,0.1)',
                                'borderRadius': '8px',
                                'color': COLORS['text'],
                                'cursor': 'pointer',
                                'transition': 'all 0.3s ease',
                                'border': '2px solid transparent',
                                'fontSize': '0.95rem',
                                'fontWeight': '500'
                            },
                            inputStyle={
                                'marginRight': '8px',
                                'accentColor': COLORS['primary']
                            }
                        )
                    ]
                ),
                
                # Graph section
                html.Div(
                    style={
                        'backgroundColor': 'rgba(255,255,255,0.02)',
                        'borderRadius': '12px',
                        'padding': '20px',
                        'border': '1px solid rgba(255,255,255,0.05)'
                    },
                    children=[
                        dcc.Graph(
                            id='sales-graph',
                            config={
                                'displayModeBar': True,
                                'displaylogo': False
                            }
                        )
                    ]
                ),
                
                # Footer info
                html.Div(
                    style={
                        'marginTop': '25px',
                        'textAlign': 'center',
                        'padding': '15px',
                        'borderTop': '1px solid rgba(255,255,255,0.1)'
                    },
                    children=[
                        html.P(
                            'Data source: Soul Foods Pink Morsel Sales Records • Last updated: 2022',
                            style={
                                'color': COLORS['text_muted'],
                                'fontSize': '0.85rem',
                                'margin': '0'
                            }
                        )
                    ]
                )
            ]
        )
    ]
)


# Callback to update the graph based on region selection
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Filter data based on selection
    if selected_region == 'all':
        filtered_df = df
        title = 'Sales Across All Regions'
    else:
        filtered_df = df[df['region'] == selected_region]
        title = f'Sales in {selected_region.capitalize()} Region'
    
    # Create the figure with consistent styling
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales',
        title=title,
        color='region' if selected_region == 'all' else None,
        color_discrete_map={
            'north': '#FF6B9D',
            'south': '#4ECDC4',
            'east': '#FFE66D',
            'west': '#95E1D3'
        }
    )
    
    # Style the figure
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family='"Inter", sans-serif',
            color='#ffffff'
        ),
        title=dict(
            font=dict(size=20, color='#FF6B9D'),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title='Date',
            gridcolor='rgba(255,255,255,0.1)',
            linecolor='rgba(255,255,255,0.2)',
            tickfont=dict(color='#a0a0a0')
        ),
        yaxis=dict(
            title='Sales ($)',
            gridcolor='rgba(255,255,255,0.1)',
            linecolor='rgba(255,255,255,0.2)',
            tickfont=dict(color='#a0a0a0')
        ),
        legend=dict(
            bgcolor='rgba(0,0,0,0.3)',
            bordercolor='rgba(255,255,255,0.2)',
            font=dict(color='#ffffff')
        ),
        hovermode='x unified',
        margin=dict(t=60, b=40, l=60, r=40)
    )
    
    # Add line styling
    fig.update_traces(
        line=dict(width=2.5),
        hovertemplate='<b>%{y:,.0f}</b> sales<extra></extra>'
    )
    
    return fig


if __name__ == '__main__':
    app.run(debug=True)