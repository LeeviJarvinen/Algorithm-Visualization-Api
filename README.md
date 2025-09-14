# Algorithm Visualization API

A simple API built with FastAPI that provides visualization capabilities for common sorting and search algorithms. This project demonstrates the step-by-step execution of bubble sort, quicksort, linear search, and binary search algorithms.

## Features

- **Sorting Algorithms**:
  - Bubble Sort visualization
  - Quick Sort visualization
- **Search Algorithms**:
  - Linear Search visualization
  - Binary Search visualization
- Fast and lightweight API built with FastAPI
- Step-by-step algorithm execution tracking
- JSON responses for easy integration

## Requirements

- Python 3.7+
- FastAPI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LeeviJarvinen/Algorithm-Visualization-Api
cd algorithm-visualization-api/app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the development server:
```bash
fastapi dev main.py
```

2. The API will be available at `http://127.0.0.1:8000`

3. Access the interactive API documentation at `http://127.0.0.1:8000/docs`

## API Endpoints

### Sorting Algorithms

- **POST** `/sort/bubble` - Visualize bubble sort algorithm
- **POST** `/sort/quick` - Visualize quicksort algorithm

### Search Algorithms

- **POST** `/search/linear` - Visualize linear search algorithm
- **POST** `/search/binary` - Visualize binary search algorithm

## Example Usage

### Bubble Sort
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/sort/bubble" \
     -H "Content-Type: application/json" \
     -d '{"data": [64, 34, 25, 12, 22, 11, 90]}'
```

### Binary Search
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/search/binary" \
     -H "Content-Type: application/json" \
     -d '{"data": [1, 3, 5, 7, 9, 11, 13], "target": 7}'
```

## Response Format

All endpoints return JSON responses with the following structure:

```json
{
  "algorithm": "bubble_sort",
  "input": [64, 34, 25, 12, 22, 11, 90],
  "steps": [
    {
      "step": 1,
      "array": [34, 64, 25, 12, 22, 11, 90],
      "description": "Swapped 64 and 34"
    }
  ],
  "result": [11, 12, 22, 25, 34, 64, 90]
}
```
