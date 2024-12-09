import tkinter as tk
from tkinter import ttk
import time

class MapColoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Map Coloring CSP Solver")

        self.canvas = tk.Canvas(root, width=500, height=500, bg='white')
        self.canvas.pack(expand=True, fill='both')

        self.colors = ['red', 'green', 'blue']  

        self.regions = {
            'A': {'x': 50, 'y': 50},
            'B': {'x': 150, 'y': 50},
            'C': {'x': 250, 'y': 50},
            'D': {'x': 50, 'y': 150},
            'E': {'x': 150, 'y': 150},
            'F': {'x': 250, 'y': 150}
        }

        self.constraints = {
            'A': ['B', 'C'],
            'B': ['A', 'C', 'D', 'E'],
            'C': ['A', 'B', 'E', 'F'],
            'D': ['B', 'E'],
            'E': ['B', 'C', 'D', 'F'],
            'F': ['C', 'E']
        }

        self.colors_map = {}

        self.solve_btn = ttk.Button(root, text="Solve", command=self.solve_map_coloring)
        self.solve_btn.pack(pady=5)

    def solve_map_coloring(self):
      
        for region, neighbors in self.constraints.items():
            available_colors = [color for color in self.colors if color not in self.colors_map.values()]
            if available_colors:
                self.colors_map[region] = available_colors[0]  
            else:
                
                self.colors_map[region] = 'white'
        self.draw_map()
        self.root.update()  
        time.sleep(2) 

       
        self.colors_map = {} 
        self.backtrack(0)

       
        self.draw_map()

    def backtrack(self, region_index):
        if region_index == len(self.regions):
            return True  
        region = list(self.regions.keys())[region_index]
        for color in self.colors:
            if self.is_valid_coloring(region, color):
                self.colors_map[region] = color
                self.draw_map()
                self.root.update()  
                time.sleep(2)  
                if self.backtrack(region_index + 1):
                    return True
                self.colors_map.pop(region) 
        return False

    def is_valid_coloring(self, region, color):
        for neighbor in self.constraints[region]:
            if neighbor in self.colors_map and self.colors_map[neighbor] == color:
                return False
        return True

    def draw_map(self):
        self.canvas.delete("all")
        for region, coords in self.regions.items():
            color = self.colors_map.get(region, 'white')
            self.canvas.create_rectangle(coords['x'], coords['y'], coords['x'] + 80, coords['y'] + 80, fill=color)
            self.canvas.create_text(coords['x'] + 40, coords['y'] + 40, text=region, font=('Arial', 12))

def main():
    root = tk.Tk()
    app = MapColoringApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
