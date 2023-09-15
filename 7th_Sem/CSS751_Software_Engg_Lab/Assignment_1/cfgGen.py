from pycfg.pycfg import PyCFG, CFGNode, slurp
import argparse
import tkinter as tk
from PIL import ImageTk, Image
import networkx as nx

def tarjan_scc(graph):
    index_counter = [0]
    stack = []
    lowlink = {}
    index = {}
    result = []

    def strongconnect(node):
        index[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)

        successors = graph.successors(node)
        for successor in successors:
            if successor not in index:
                strongconnect(successor)
                lowlink[node] = min(lowlink[node], lowlink[successor])
            elif successor in stack:
                lowlink[node] = min(lowlink[node], index[successor])

        if lowlink[node] == index[node]:
            connected_component = []
            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node:
                    break
            result.append(connected_component)

    for node in graph.nodes():
        if node not in index:
            strongconnect(node)

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pythonfile', help='The python file to be analyzed')
    args = parser.parse_args()
    arcs = []
    cfg = PyCFG()
    cfg.gen_cfg(slurp(args.pythonfile).strip())
    g = CFGNode.to_graph(arcs)
    g.draw(args.pythonfile + '.png', prog='dot')

    # Detect loops using Tarjan's algorithm.
    graph = nx.DiGraph(g)
    sccs = tarjan_scc(graph)
    has_loops = any(len(scc) > 1 for scc in sccs)

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Control Flow Graph")


    img1 = Image.open(str(args.pythonfile) + ".png")  # PIL solution
    img1 = img1.resize((800, 600), Image.LANCZOS)
    img = ImageTk.PhotoImage(img1)
    background = "gray"
    panel = tk.Label(root, height=600, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    nodes = g.number_of_nodes()  # no. of nodes.
    edges = g.number_of_edges()  # no. of Edges.
    complexity = edges - nodes + 2  # Cyclomatic complexity
    frame = tk.Frame(root, bg=background)
    frame.pack(side="bottom", fill="both", expand="yes")
    tk.Label(frame, text="Nodes = \t"+str(nodes), bg=background).pack()
    tk.Label(frame, text="Edges = \t"+str(edges), bg=background).pack()
    tk.Label(frame, text="Cyclo Complexity = \t" +
            str(complexity), bg=background).pack()
    tk.Label(frame, text="Number of bounded regions = \t" +
            str(complexity-1), bg=background).pack()
    tk.Label(frame, text="Number of independent paths = \t" +
            str(complexity), bg=background).pack()
    tk.Label(frame, text="Loops Detected = \t" + str(has_loops), bg=background).pack()
    root.mainloop() 
