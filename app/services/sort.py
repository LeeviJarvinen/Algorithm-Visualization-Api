from ..models.sort import NumRequest 

def bubble_sort(data: NumRequest):
    data = data.num
    initial_data = data.copy()
    steps = []
    n = len(data)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                steps.append({
                   "count": len(steps) + 1,
                    "action": f"swap {data[j]} and {data[j+1]}",
                    "array": data.copy(),
                    "compared_indices": [data[j], data[j+1]],
                })

        if not swapped:
            break

    return {
        "algorithm": "bubble_sort",
        "input": initial_data,
        "steps": steps,
        "result": data
    }

def quick_sort(data: NumRequest):
    data = data.num
    steps = []
    step_counter = 0
    
    stack = [(0, len(data) - 1)]
    result_array = data.copy()
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_pos = partition(result_array, low, high, steps, step_counter)
            step_counter = len(steps)
            
            stack.append((pivot_pos + 1, high)) 
            stack.append((low, pivot_pos - 1)) 
    
    return {
        "algorithm": "quick_sort",
        "input": data,
        "steps": steps,
        "final_result": result_array
    }

def partition(arr, low, high, steps, step_counter):
    pivot = arr[high]
    current_step = len(steps) + 1
    
    steps.append({
        "step": current_step,
        "action": f"Choose pivot: {pivot} at index {high}",
        "array": arr.copy(),
        "pivot_index": high,
        "pivot_value": pivot,
        "range": f"[{low}:{high}]"
    })
    
    i = low - 1
    
    for j in range(low, high):
        current_step = len(steps) + 1
        
        if arr[j] <= pivot:
            i += 1
            if i != j: 
                arr[i], arr[j] = arr[j], arr[i]
                steps.append({
                    "step": current_step,
                    "action": f"Swap {arr[i]} and {arr[j]} ({arr[i]} <= {pivot})",
                    "array": arr.copy(),
                    "swapped_indices": [i, j],
                    "pivot_value": pivot
                })
            else:
                steps.append({
                    "step": current_step,
                    "action": f"{arr[j]} <= {pivot} no swap",
                    "array": arr.copy(),
                    "element_index": j,
                    "pivot_value": pivot
                })
        else:
            steps.append({
                "step": current_step,
                "action": f"{arr[j]} > {pivot}, leave",
                "array": arr.copy(),
                "element_index": j,
                "pivot_value": pivot
            })
    
    pivot_final_pos = i + 1
    if pivot_final_pos != high:
        arr[pivot_final_pos], arr[high] = arr[high], arr[pivot_final_pos]
    
    current_step = len(steps) + 1
    steps.append({
        "step": current_step,
        "action": f"Place pivot {pivot} in final position {pivot_final_pos}",
        "array": arr.copy(),
        "pivot_final_position": pivot_final_pos,
        "partition_complete": True
    })
    
    return pivot_final_pos
