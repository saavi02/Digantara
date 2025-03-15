# Digantara

This project implements three algorithms as REST APIs using FastAPI in Python:
- **Binary Search**: Find an element in a sorted array.
- **Quick Sort**: Sort an array.
- **BFS (Breadth-First Search)**: Traverse a graph from a given starting node.

Each API call is logged in `api_logs.json`.

##  Project Files

### **1️⃣ `binary_search.py`**
This file contains the **Binary Search Algorithm**, which searches for a target value in a sorted list. 
- **Function:** `binary_search(arr, target)`
- **Parameters:**
  - `arr` (List[int]): A sorted list of integers.
  - `target` (int): The number to search for.
- **Returns:** The index of the target if found, otherwise `-1`.

### **2️⃣ `quick_sort.py`**
This file implements the **Quick Sort Algorithm**, which sorts an array.
- **Function:** `quick_sort(arr)`
- **Parameters:**
  - `arr` (List[int]): The unsorted list.
- **Returns:** A sorted version of the list.

### **3️⃣ `bfs.py`**
This file contains the **Breadth-First Search (BFS) Algorithm**, which traverses a graph from a given starting node.
- **Function:** `bfs(graph, start_node)`
- **Parameters:**
  - `graph` (Dict[str, List[str]]): An adjacency list representation of a graph.
  - `start_node` (str): The node to start traversal from.
- **Returns:** A list of nodes in BFS order.

---

## 🚀 Setup & Installation

### **1. Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### **2. Run the API Server**
```bash
uvicorn main:app --reload
```
The API will start at `http://127.0.0.1:8000/`.

---



