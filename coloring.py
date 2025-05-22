import networkx as nx
from itertools import permutations
import matplotlib.pyplot as plt

G = nx.complete_graph(4)
L = nx.line_graph(G)

nodes = list(L.nodes())
n = len(nodes)

min_sum = float('inf')
best_coloring = None

for p in permutations(range(1, n+1)):
	coloring = dict(zip(nodes, p))
	if all(coloring[u] != coloring[v] for u, v in L.edges()):
		total = sum(coloring.values())
	if total < min_sum:
		min_sum = total
	best_coloring = coloring

print("Գումարային քրոմատիկ թիվ:", min_sum)
print("Լավագույն ներկում:", best_coloring)

pos = nx.spring_layout(L, seed=42)
colors = [best_coloring[node] for node in L.nodes()]
labels = {node: f"{node}\n{best_coloring[node]}" for node in L.nodes()}

plt.figure(figsize=(8,6))
nx.draw(L, pos, with_labels=True, labels=labels, node_color=colors,
		cmap=plt.cm.Paired, node_size=1200, font_size=11,
		font_color='black', edge_color='gray', linewidths=1.5)
plt.title("L(K₄) գրաֆի լավագույն գումարային ներկում", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
