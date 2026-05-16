import tkinter as tk
from tkinter import ttk
import random
import pygame

from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort


class SortingVisualizer:

    def __init__(self):

        # ---------------- MAIN WINDOW ---------------- #

        self.root = tk.Tk()

        self.root.title("Divide and Conquer Sorting Visualizer")

        self.root.geometry("1200x700")

        self.root.configure(bg="#121212")

        #----------------- SOUNDS ---------------- #

        pygame.mixer.init()

        self.tick_channel = pygame.mixer.Channel(0)

        self.complete_channel = pygame.mixer.Channel(1)

        self.tick_sound = pygame.mixer.Sound("assets/sounds/tick.wav")

        self.complete_sound = pygame.mixer.Sound("assets/sounds/complete.wav")

        self.tick_sound.set_volume(0.2)

        self.complete_sound.set_volume(0.8)

        # ---------------- VARIABLES ---------------- #

        self.array = []

        self.array_size = tk.IntVar(value=50)

        self.speed = tk.IntVar(value=50)

        self.selected_algorithm = tk.StringVar(value="Merge Sort")

        self.generator = None

        self.is_sorting = False

        self.paused = False

        self.steps = 0

        self.comparisons = 0

        # ---------------- CONTROL FRAME ---------------- #

        control_frame = tk.Frame(
            self.root,
            bg="#1E1E1E",
            height=100
        )

        control_frame.pack(fill=tk.X, padx=10, pady=10)

        # ---------------- ALGORITHM DROPDOWN ---------------- #

        tk.Label(
            control_frame,
            text="Algorithm",
            bg="#1E1E1E",
            fg="white",
            font=("Arial", 11, "bold")
        ).grid(row=0, column=0, padx=10)

        algorithm_menu = ttk.Combobox(
            control_frame,
            textvariable=self.selected_algorithm,
            values=["Merge Sort", "Quick Sort"],
            state="readonly",
            width=15
        )

        algorithm_menu.grid(row=1, column=0, padx=10)

        # ---------------- ARRAY SIZE SLIDER ---------------- #

        tk.Label(
            control_frame,
            text="Array Size",
            bg="#1E1E1E",
            fg="white",
            font=("Arial", 11, "bold")
        ).grid(row=0, column=1, padx=10)

        size_slider = tk.Scale(
            control_frame,
            from_=10,
            to=150,
            orient=tk.HORIZONTAL,
            variable=self.array_size,
            bg="#1E1E1E",
            fg="white",
            troughcolor="#00ADB5",
            highlightthickness=0,
            command=self.update_array_size
        )

        size_slider.grid(row=1, column=1, padx=10)

        # ---------------- SPEED SLIDER ---------------- #

        tk.Label(
            control_frame,
            text="Speed",
            bg="#1E1E1E",
            fg="white",
            font=("Arial", 11, "bold")
        ).grid(row=0, column=2, padx=10)

        speed_slider = tk.Scale(
            control_frame,
            from_=1,
            to=200,
            orient=tk.HORIZONTAL,
            variable=self.speed,
            bg="#1E1E1E",
            fg="white",
            troughcolor="#00ADB5",
            highlightthickness=0
        )

        speed_slider.grid(row=1, column=2, padx=10)

        # ---------------- GENERATE BUTTON ---------------- #

        generate_button = tk.Button(
            control_frame,
            text="Generate Array",
            command=self.generate_array,
            bg="#00ADB5",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=15
        )

        generate_button.grid(row=1, column=3, padx=10)

        # ---------------- START BUTTON ---------------- #

        start_button = tk.Button(
            control_frame,
            text="Start Sorting",
            command=self.start_sorting,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=15
        )

        start_button.grid(row=1, column=4, padx=10)

        # ---------------- PAUSE BUTTON ---------------- #

        pause_button = tk.Button(
            control_frame,
            text="Pause",
            command=self.pause_sorting,
            bg="#FF9800",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=15
        )

        pause_button.grid(row=1, column=5, padx=10)

        # ---------------- RESUME BUTTON ---------------- #

        resume_button = tk.Button(
            control_frame,
            text="Resume",
            command=self.resume_sorting,
            bg="#2196F3",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=15
        )

        resume_button.grid(row=1, column=6, padx=10)

        # ---------------- RESET BUTTON ---------------- #

        reset_button = tk.Button(
            control_frame,
            text="Reset",
            command=self.reset_array,
            bg="#F44336",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=15
        )

        reset_button.grid(row=1, column=7, padx=10)

        # ---------------- CANVAS ---------------- #

        self.canvas = tk.Canvas(
            self.root,
            width=1100,
            height=500,
            bg="#1E1E1E",
            highlightthickness=0
        )

        self.canvas.pack(pady=20)

        # ---------------- INFO LABEL ---------------- #

        self.info_label = tk.Label(
            self.root,
            text="""
            Algorithm: Merge Sort
            Time Complexity: O(n log n)
            Steps: 0
            Comparisons: 0
            Status: Ready
            """,
            bg="#121212",
            fg="white",
            font=("Arial", 12, "bold")
        )

        self.info_label.pack()

        # Initial array
        self.generate_array()

    # ---------------- GENERATE ARRAY ---------------- #

    def generate_array(self):

        self.array = [
            random.randint(20, 450)
            for _ in range(self.array_size.get())
        ]

        self.draw_array(
            ["#00ADB5"] * len(self.array)
        )

    # ---------------- DRAW ARRAY ---------------- #

    def draw_array(self, colors):

        self.canvas.delete("all")

        canvas_width = 1100

        canvas_height = 500

        bar_width = canvas_width / len(self.array)

        for i, value in enumerate(self.array):

            x0 = i * bar_width

            y0 = canvas_height - value

            x1 = (i + 1) * bar_width

            y1 = canvas_height

            self.canvas.create_rectangle(
                x0,
                y0,
                x1,
                y1,
                fill=colors[i],
                outline=""
            )

        self.root.update_idletasks()

    # ---------------- UPDATE ARRAY SIZE ---------------- #

    def update_array_size(self, event):
        self.generate_array()

    # ---------------- GET COMPLEXITY ---------------- 
    
    def get_complexity(self):
        
        algorithm = self.selected_algorithm.get()
        
        if algorithm == "Merge Sort":
            
            return "O(n log n)"
        
        elif algorithm == "Quick Sort":
            
            return "Average: O(n log n)"
        
        return "Unknown"

    # ---------------- START SORTING ---------------- #

    def start_sorting(self):

        if self.is_sorting:
            return

        self.is_sorting = True

        self.paused = False

        self.steps = 0

        self.comparisons = 0

        algorithm = self.selected_algorithm.get()

        # Merge Sort
        if algorithm == "Merge Sort":

            self.generator = merge_sort(
                self.array,
                0,
                len(self.array) - 1
            )

        # Quick Sort
        elif algorithm == "Quick Sort":

            self.generator = quick_sort(
                self.array,
                0,
                len(self.array) - 1
            )

        self.animate()

    # ---------------- ANIMATION LOOP ---------------- #

    def animate(self):

        if self.paused:
            return

        try:

            arr, colors = next(self.generator)

            self.draw_array(colors)

            if self.steps % 12 == 0:

                if not self.tick_channel.get_busy():

                    self.tick_channel.play(self.tick_sound)

            self.steps += 1

            self.comparisons += 1

            self.info_label.config(

                text=f"""
            Algorithm: {self.selected_algorithm.get()}
            Time Complexity: {self.get_complexity()}
            Steps: {self.steps}
            Comparisons: {self.comparisons}
            Status: Sorting...
            """

            )

            delay = self.speed.get()

            self.root.after(delay, self.animate)

        except StopIteration:

            self.draw_array(
                ["#9C27B0"] * len(self.array)
            )

            self.is_sorting = False

            self.tick_channel.stop()

            self.complete_channel.play(
                self.complete_sound
            )

            self.info_label.config(
                text=f"""
            Algorithm: {self.selected_algorithm.get()}
            Time Complexity: {self.get_complexity()}
            Steps: {self.steps}
            Comparisons: {self.comparisons}
            Status: Completed
            """
            )

    # ---------------- PAUSE SORTING ---------------- #

    def pause_sorting(self):

        self.paused = True

    # ---------------- RESUME SORTING ---------------- #

    def resume_sorting(self):

        if self.is_sorting:

            self.paused = False

            self.animate()

    # ---------------- RESET ARRAY ---------------- #

    def reset_array(self):
        self.is_sorting = False

        self.paused = False

        self.steps = 0

        self.comparisons = 0

        self.generate_array()

        self.info_label.config(
            text=f"""
        Algorithm: {self.selected_algorithm.get()}
        Time Complexity: {self.get_complexity()}
        Steps: 0
        Comparisons: 0
        Status: Ready
        """
        )
    # ---------------- RUN APP ---------------- #

    def run(self):

        self.root.mainloop()