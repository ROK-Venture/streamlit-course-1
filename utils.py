import pandas as pd

def load_data():
    url = "https://api.iea.org/evs?parameters=EV%20sales&category=Historical&mode=Cars&csv=true"
    ev_df = pd.read_csv(url)
    ev_sales_df = ev_df[ev_df["parameter"] == "EV sales"]
    ev_sales_share_df = ev_df[ev_df["parameter"] == "EV sales share"]
    #drop the columns that are not needed from both dataframes category, mode, unit and build a filter where parameter is EV sales and EV sales share
    ev_sales_df = ev_sales_df.drop(columns=["category", "mode", "unit", "parameter"])
    ev_sales_share_df = ev_sales_share_df.drop(columns=["category", "mode", "unit", "parameter", "powertrain"])
    return ev_sales_df, ev_sales_share_df


def top10_sales_by_country(ev_sales_df, year=2023):
    # filter the df to only include the year 2023
    ev_sales_df_2023 = ev_sales_df[ev_sales_df["year"] == year]
    # drop the year column
    ev_sales_df_2023 = ev_sales_df_2023.drop(columns=["year"])
    # filter out regions that are not countries: World, OECD, G20, G7, EU, EU27, EU28, Rest of World, Europe, Asia, North America, South America, Africa, Middle East, Oceania
    ev_sales_df_2023 = ev_sales_df_2023[~ev_sales_df_2023["region"].isin(["World", "OECD", "G20", "G7", "EU", "EU27", "EU28", "Rest of World", "Europe", "Asia", "North America", "South America", "Africa", "Middle East", "Oceania"])]
    # aggregate the sales by region
    ev_sales_df_2023_agg = ev_sales_df_2023.groupby("region")["value"].sum().reset_index()
    #rename the region column to country
    ev_sales_df_2023_agg = ev_sales_df_2023_agg.rename(columns={"region": "country"})
    # rename the column value to sales
    ev_sales_df_2023_agg = ev_sales_df_2023_agg.rename(columns={"value": "sales"})
    #convert the sales column into millions
    ev_sales_df_2023_agg["sales_(m)"] = ev_sales_df_2023_agg["sales"] / 1000000
    #round the sales column to 2 decimal places
    ev_sales_df_2023_agg["sales_(m)"] = ev_sales_df_2023_agg["sales_(m)"].round(2)
    #drop the sales column
    ev_sales_df_2023_agg = ev_sales_df_2023_agg.drop(columns=["sales"])
    #sort the df by the sales column in descending order
    ev_sales_df_2023_agg = ev_sales_df_2023_agg.sort_values(by="sales_(m)", ascending=False)
    #reset the index and make it start from 1 
    ev_sales_df_2023_agg = ev_sales_df_2023_agg.reset_index(drop=True)
    ev_sales_df_2023_agg.index = ev_sales_df_2023_agg.index + 1
    # return the top 10 countries
    return ev_sales_df_2023_agg.head(10)


def create_sales_pie_chart(data_df):
    """
    Creates a pie chart visualization for EV sales by country.
    
    Args:
        data_df (DataFrame): DataFrame containing country and sales data
        
    Returns:
        dict: Plotly figure configuration for pie chart
    """
    return {
        "data": [{"type": "pie", 
                  "labels": data_df["country"], 
                  "values": data_df["sales_(m)"],
                  "hole": 0.4}],
        "layout": {
            "legend": {"orientation": "h", "y": -0.1, "x": 0.5, "xanchor": "center"},
            "margin": {"t": 30, "b": 80, "l": 40, "r": 40}
        }
    }
