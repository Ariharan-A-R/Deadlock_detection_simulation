import tkinter as tk
import networkx as nx
from tkinter import messagebox
import time

class ProcessSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Chandy-Misra-Haas Deadlock Detection Simulator")

        self.canvas = tk.Canvas(root, width=900, height=500, bg="#f0f0f0")
        self.canvas.pack()

        self.control_frame = tk.Frame(root, bg="#dcdcdc")
        self.control_frame.pack(fill=tk.X)

        self.status_label = tk.Label(root, text="Click to add processes. Click two nodes to assign path.", bg="white", font=("Arial", 11))
        self.status_label.pack(fill=tk.X)


        self.deadlock_button = tk.Button(self.control_frame, text="Detect Deadlock", font=("Arial", 12, "bold"),
                                         bg="#e74c3c", fg="white", command=self.detect_deadlock)
        self.deadlock_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.reset_button = tk.Button(self.control_frame, text="Reset", font=("Arial", 12, "bold"),
                                      bg="#636e72", fg="white", command=self.reset)
        self.reset_button.pack(side=tk.RIGHT, padx=10, pady=8)

        self.G = nx.DiGraph()
        self.positions = {}
        self.process_count = 0
        self.selected_nodes = []

        self.canvas.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        clicked_node = self.get_node_at(event.x, event.y)

        if not clicked_node:
            node_id = f'P{self.process_count}'
            self.positions[node_id] = (event.x, event.y)
            self.G.add_node(node_id)

            self.canvas.create_oval(event.x - 25, event.y - 25, event.x + 25, event.y + 25,
                                    fill="#3498db", outline="black", width=2, tags=node_id)
            self.canvas.create_text(event.x, event.y, text=node_id, font=("Arial", 14, "bold"),
                                    fill="white", tags=node_id)
            self.process_count += 1
        else:
            self.selected_nodes.append(clicked_node)
            if len(self.selected_nodes) == 2:
                self.create_edge(self.selected_nodes[0], self.selected_nodes[1])
                self.selected_nodes = []

    def get_node_at(self, x, y):
        for node, (nx, ny) in self.positions.items():
            if (nx - 25 <= x <= nx + 25) and (ny - 25 <= y <= ny + 25):
                return node
        return None

    def create_edge(self, node1, node2):
        if node1 != node2:
            x1, y1 = self.positions[node1]
            x2, y2 = self.positions[node2]

            if not self.G.has_edge(node1, node2):
                self.G.add_edge(node1, node2)

                if self.G.has_edge(node2, node1):
                    # Draw curved arrow
                    ctrl_x = (x1 + x2) / 2 + 40
                    ctrl_y = (y1 + y2) / 2 - 40
                    self.canvas.create_line(x1, y1, ctrl_x, ctrl_y, x2, y2,
                                            arrow=tk.LAST, fill="#e67e22", width=2, smooth=True)
                else:
                    # Straight arrow
                    self.canvas.create_line(x1, y1, x2, y2,
                                            arrow=tk.LAST, fill="#e67e22", width=2)

                self.status_label.config(text=f"Connected {node1} → {node2}")

    def run_simulation(self):
        try:
            execution_order = list(nx.topological_sort(self.G))
            messagebox.showinfo("Simulation", "Execution Order:\n" + " → ".join(execution_order))
        except nx.NetworkXUnfeasible:
            messagebox.showerror("Cycle Detected", "A cycle was found in the graph. Cannot determine execution order.")

    def detect_deadlock(self):
        if self.chandy_misra_haas():
            messagebox.showerror("Deadlock Detected", "A deadlock has been found in the system!")
        else:
            messagebox.showinfo("No Deadlock", "No deadlock detected.")

    def chandy_misra_haas(self):
        probes = set()
        for node in self.G.nodes:
            for neighbor in self.G.neighbors(node):
                probe = (node, node, neighbor)
                probes.add(probe)
                if self.simulate_probe(probe, probes):
                    return True
        return False

    def simulate_probe(self, probe, probes):
        initiator, sender, receiver = probe
        self.animate_message(probe)

        if receiver == initiator:
            return True  # Deadlock detected

        for neighbor in self.G.neighbors(receiver):
            new_probe = (initiator, receiver, neighbor)
            if new_probe not in probes:
                probes.add(new_probe)
                if self.simulate_probe(new_probe, probes):
                    return True
        return False

    def animate_message(self, probe):
        initiator, sender, receiver = probe
        x1, y1 = self.positions[sender]
        x2, y2 = self.positions[receiver]

        msg = self.canvas.create_text(x1, y1, text=f"({initiator},{sender},{receiver})", fill="red", font=("Arial", 10, "bold"))

        for step in range(20):
            new_x = x1 + (x2 - x1) * (step / 20)
            new_y = y1 + (y2 - y1) * (step / 20)
            self.canvas.coords(msg, new_x, new_y)
            self.root.update()
            time.sleep(0.05)

        self.canvas.delete(msg)
    def reset(self):
        self.canvas.delete("all")
        self.G.clear()
        self.positions.clear()
        self.selected_nodes.clear()
        self.process_count = 0
        self.status_label.config(text="Simulation reset. Start by clicking to create processes.")

if __name__ == "__main__":
    root = tk.Tk()
    sim = ProcessSimulation(root)
    root.mainloop()
