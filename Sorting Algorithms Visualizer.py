import tkinter as tk
from tkinter import ttk
import random
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.array = []
        
        # Create and pack the canvas to draw the array
        self.canvas = tk.Canvas(root, width=800, height=400, bg='white')
        self.canvas.pack()

        # Create a frame to hold the control buttons and complexity label
        self.control_frame = ttk.Frame(root)
        self.control_frame.pack()

        # Create and place buttons for each sorting algorithm and to generate a new array
        self.bubble_sort_btn = ttk.Button(self.control_frame, text="Bubble Sort", command=self.bubble_sort)
        self.bubble_sort_btn.grid(row=0, column=0, padx=5, pady=5)

        self.selection_sort_btn = ttk.Button(self.control_frame, text="Selection Sort", command=self.selection_sort)
        self.selection_sort_btn.grid(row=0, column=1, padx=5, pady=5)

        self.insertion_sort_btn = ttk.Button(self.control_frame, text="Insertion Sort", command=self.insertion_sort)
        self.insertion_sort_btn.grid(row=0, column=2, padx=5, pady=5)

        self.merge_sort_btn = ttk.Button(self.control_frame, text="Merge Sort", command=lambda: self.merge_sort(0, len(self.array) - 1))
        self.merge_sort_btn.grid(row=0, column=3, padx=5, pady=5)

        self.quick_sort_btn = ttk.Button(self.control_frame, text="Quick Sort", command=lambda: self.quick_sort(0, len(self.array) - 1))
        self.quick_sort_btn.grid(row=0, column=4, padx=5, pady=5)

        self.generate_btn = ttk.Button(self.control_frame, text="Generate Array", command=self.generate_array)
        self.generate_btn.grid(row=0, column=5, padx=5, pady=5)

        # Create and place a label to display the time complexity
        self.complexity_label = ttk.Label(self.control_frame, text="Time Complexity: ")
        self.complexity_label.grid(row=1, column=0, columnspan=6, pady=5)

        # Generate the initial array
        self.generate_array()

    def generate_array(self, size=50):
        """Generate a new random array and draw it on the canvas."""
        self.array = [random.randint(1, 400) for _ in range(size)]
        self.draw_array()

    def draw_array(self, color_array=None):
        """Draw the array on the canvas."""
        self.canvas.delete("all")
        c_width = 800
        c_height = 400
        x_width = c_width / len(self.array)
        offset = 10
        spacing = 2

        for i, height in enumerate(self.array):
            x0 = i * x_width + offset + spacing
            y0 = c_height - height
            x1 = (i + 1) * x_width + offset
            y1 = c_height
            if color_array:
                color = color_array[i]
            else:
                color = "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.root.update_idletasks()

    def swap(self, i, j):
        """Swap two elements in the array and update the canvas."""
        self.array[i], self.array[j] = self.array[j], self.array[i]
        self.draw_array(['red' if x == i or x == j else 'blue' for x in range(len(self.array))])
        time.sleep(0.1)

    def update_complexity_label(self, complexity):
        """Update the time complexity label with the given complexity."""
        self.complexity_label.config(text=f"Time Complexity: {complexity}")

    def bubble_sort(self):
        """Perform bubble sort on the array with visual updates."""
        self.update_complexity_label("O(n^2)")
        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.swap(j, j + 1)

    def selection_sort(self):
        """Perform selection sort on the array with visual updates."""
        self.update_complexity_label("O(n^2)")
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.swap(i, min_idx)

    def insertion_sort(self):
        """Perform insertion sort on the array with visual updates."""
        self.update_complexity_label("O(n^2)")
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                self.draw_array(['red' if x == j or x == j + 1 else 'blue' for x in range(len(self.array))])
                time.sleep(0.1)
                j -= 1
            self.array[j + 1] = key
            self.draw_array()

    def merge_sort(self, start, end):
        """Perform merge sort on the array with visual updates."""
        if start < end:
            self.update_complexity_label("O(n log n)")
            mid = (start + end) // 2
            self.merge_sort(start, mid)
            self.merge_sort(mid + 1, end)
            self.merge(start, mid, end)

    def merge(self, start, mid, end):
        """Merge two halves of the array with visual updates."""
        left = self.array[start:mid + 1]
        right = self.array[mid + 1:end + 1]
        k = start
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                self.array[k] = left[i]
                i += 1
            else:
                self.array[k] = right[j]
                j += 1
            k += 1
            self.draw_array(['green' if x >= start and x <= end else 'blue' for x in range(len(self.array))])
            time.sleep(0.1)

        while i < len(left):
            self.array[k] = left[i]
            i += 1
            k += 1
            self.draw_array(['green' if x >= start and x <= end else 'blue' for x in range(len(self.array))])
            time.sleep(0.1)

        while j < len(right):
            self.array[k] = right[j]
            j += 1
            k += 1
            self.draw_array(['green' if x >= start and x <= end else 'blue' for x in range(len(self.array))])
            time.sleep(0.1)

    def quick_sort(self, start, end):
        """Perform quick sort on the array with visual updates."""
        if start < end:
            self.update_complexity_label("O(n log n)")
            pivot_index = self.partition(start, end)
            self.quick_sort(start, pivot_index - 1)
            self.quick_sort(pivot_index + 1, end)

    def partition(self, start, end):
        """Partition the array for quick sort with visual updates."""
        pivot = self.array[end]
        i = start - 1

        for j in range(start, end):
            if self.array[j] < pivot:
                i += 1
                self.swap(i, j)
        self.swap(i + 1, end)
        return i + 1

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
    