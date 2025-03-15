from fastapi import FastAPI
from typing import List, Dict
from binary_search import binary_search
from quick_sort import quick_sort
from bfs import bfs
import json
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

# Log file
LOG_FILE = "api_logs.json"

# Utility function to log API calls
def log_api_call(algorithm: str, input_data, output_data):
    log_entry = {"algorithm": algorithm, "input": input_data, "output": output_data}
    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

@app.get("/")
def home():
    return {"message": "Welcome to Digantara Backend Assignment API"}


class BinarySearchInput(BaseModel):
    arr: List[int]
    target: int

@app.post("/binary_search/")
def binary_search_api(input_data: BinarySearchInput):
    arr, target = input_data.arr, input_data.target
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return {"algorithm": "Binary Search", "result": mid}
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return {"algorithm": "Binary Search", "result": -1}

class QuickSortInput(BaseModel):
    arr: List[int]

def quick_sort(arr):
    """Sort an array using quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

@app.post("/quick_sort/")
def quick_sort_api(input_data: QuickSortInput):
    sorted_arr = quick_sort(input_data.arr)
    return JSONResponse(content={"algorithm": "Quick Sort", "sorted_array": sorted_arr}, media_type="application/json")


class BFSInput(BaseModel):
    graph: Dict[str, List[str]]
    start_node: str

def bfs(graph, start_node):
    """Perform BFS on a graph."""
    from collections import deque
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph.get(node, []))

    return visited

@app.post("/bfs/")
def bfs_api(input_data: BFSInput):
    result = bfs(input_data.graph, input_data.start_node)
    return {"algorithm": "BFS", "result": result}

@app.get("/logs/")
def get_logs():
    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
        return {"logs": logs}
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": "No logs found"}
