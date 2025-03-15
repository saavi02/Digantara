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

##  API Endpoints & Sample Requests

### **1️⃣ Binary Search API**
**Endpoint:** `POST /binary_search/`
```json
{
    "arr": [1, 3, 5, 7, 9, 11],
    "target": 5
}
```
**Response:**
```json
{
    "algorithm": "Binary Search",
    "result": 2
}
```

### **2️⃣ Quick Sort API**
**Endpoint:** `POST /quick_sort/`
```json
{
    "arr": [3, 1, 4, 1, 5, 9, 2, 6]
}
```
**Response:**
```json
{
    "algorithm": "Quick Sort",
    "sorted_array": [1, 1, 2, 3, 4, 5, 6, 9]
}
```

### **3️⃣ BFS Traversal API**
**Endpoint:** `POST /bfs/`
```json
{
    "graph": { "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"], "D": ["B"], "E": ["B", "F"], "F": ["C"] },
    "start_node": "A"
}
```
**Response:**
```json
{
    "algorithm": "BFS",
    "result": ["A", "B", "C", "D", "E", "F"]
}
```

### **4️⃣ View API Logs**
**Endpoint:** `GET /logs/`
**Response:**
```json
{
    "logs": [
        {"algorithm": "Binary Search", "input": {"arr": [1, 3, 5], "target": 5}, "output": 2}
    ]
}
```


The API will start at `http://127.0.0.1:8000/`.

---



