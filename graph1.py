import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(4)


mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
G = nx.relabel_nodes(G, mapping)

# Ստեղծում ենք գծային գրաֆ՝ L(K4)
L = nx.line_graph(G)

# Պատկերների չափս
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Գրաֆ K4-ի դասավորություն
pos_G = nx.spring_layout(G, seed=42)
nx.draw(G, pos_G, with_labels=True, node_color='skyblue', edge_color='gray',
        node_size=800, font_size=14, ax=axes[0])
axes[0].set_title("Լրիվ գրաֆ՝ K₄", fontsize=16)

# Գծային գրաֆ՝ L(K4)
pos_L = nx.spring_layout(L, seed=42)
nx.draw(L, pos_L, with_labels=True, node_color='lightgreen', edge_color='black',
        node_size=800, font_size=14, ax=axes[1])
axes[1].set_title("Գծային գրաֆ՝ L(K₄)", fontsize=16)

plt.tight_layout()
plt.show()
