import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_sequence(n):
    sequence = collatz_sequence(n)
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, marker='o')
    plt.title(f'Collatz Conjecture Sequence for {n}')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.grid(True)
    
    # Set x-axis ticks to be only integer values
    plt.xticks(range(len(sequence)))
    
    st.pyplot(plt)

def collatz_tree(n):
    G = nx.DiGraph()
    G.add_node(n)
    nodes = [n]
    
    while nodes:
        current = nodes.pop(0)
        if current != 1:
            if current % 2 == 0:
                next_num = current // 2
            else:
                next_num = 3 * current + 1
            
            G.add_node(next_num)
            G.add_edge(current, next_num)
            nodes.append(next_num)
            
    return G

def hierarchical_layout(G, root):
    pos = {}
    level = 0
    next_level_nodes = [root]
    
    while next_level_nodes:
        current_level_nodes = next_level_nodes
        next_level_nodes = []
        for i, node in enumerate(current_level_nodes):
            pos[node] = (i, -level)
            next_level_nodes.extend(G.successors(node))
        level += 1
    
    return pos

def plot_collatz_tree(n):
    G = collatz_tree(n)
    pos = hierarchical_layout(G, n)
    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)
    plt.title(f'Collatz Conjecture Tree for {n}')
    plt.gca().invert_yaxis()  # Invert y-axis to make the root at the top
    
    st.pyplot(plt)

def main():
    st.title("Collatz Conjecture Visualizer")
    st.write('***')
    
    st.markdown("""
    ## What is the Collatz Conjecture?
    The **Collatz Conjecture** is a conjecture in mathematics that concerns sequences defined as follows:

    1. Start with any positive integer \\( n \\).
    2. Then each term is obtained from the previous term as follows:
       - If the previous term is even, the next term is one half of the previous term.
       - If the previous term is odd, the next term is \\( 3 * n + 1 \\).
    
    The conjecture is that no matter what value of \\( n \\) you start with, the sequence will always reach 1.

    Let's visualize the Collatz sequence and its tree for any given number.
    """)
    
    st.write('***')

    number = st.number_input("Enter a number:", min_value=1, step=1, value=1)
    
    if st.button("Visualize Sequence"):
        plot_collatz_sequence(number)
    
    if st.button("Visualize Tree"):
        plot_collatz_tree(number)

if __name__ == "__main__":
    main()