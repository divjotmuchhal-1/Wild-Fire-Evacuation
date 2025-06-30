import networkx as nx
import pandas as pd

def get_safest_path(start: str, end: str):
    df = pd.read_csv("data/roads.csv")
    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_edge(row["start"], row["end"], weight=row["distance"])

    try:
        return nx.shortest_path(G, source=start, target=end, weight="weight")
    except:
        return ["Route not found"]
