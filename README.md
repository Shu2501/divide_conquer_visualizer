# Divide and Conquer Sorting Visualizer

An interactive desktop application built using Python and Tkinter that visually demonstrates how Divide and Conquer sorting algorithms work through real-time animated bar visualization.

This project helps students understand recursive sorting techniques such as Merge Sort and Quick Sort by showing each comparison, partition, merge operation, and swap step visually.

---

# Features

- Merge Sort Visualization
- Quick Sort Visualization
- Real-Time Sorting Animation
- Adjustable Array Size
- Adjustable Sorting Speed
- Pause / Resume / Reset Controls
- Random Array Generation
- Color-Coded Sorting States
- Step Counter
- Comparison Counter
- Time Complexity Display
- Modern Dark-Themed UI

---

# Algorithms Implemented

## 1. Merge Sort

Merge Sort follows the Divide and Conquer approach:
1. Divide the array into smaller halves recursively.
2. Sort each half.
3. Merge the sorted halves together.

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

---

## 2. Quick Sort

Quick Sort works by:
1. Selecting a pivot element.
2. Partitioning elements around the pivot.
3. Recursively sorting left and right partitions.

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n²) |

---

# Technologies Used

- Python
- Tkinter
- Object-Oriented Programming
- Recursive Algorithms
- Generator Functions

---

# Project Structure

```plaintext
divide_conquer_visualizer/
│
├── algorithms/
│   ├── merge_sort.py
│   └── quick_sort.py
│
├── ui/
│   └── visualizer.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore