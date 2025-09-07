from ..models.search import SearchRequest

def linear_search(data: SearchRequest):
    arr = data.data
    target = data.target
    steps = []
    result = ""

    for i in range(len(arr)):
        if i == len(arr) - 1:
            steps.append({
                "action": f"target {target} not found in array",
                "found": False
            })
            result = f"target {target} does not exist in array"
            break

        if arr[i] == target:
            steps.append({
                "step": len(steps) + 1,
                "action": f"{arr[i]} == {target}",
                "found": True
            })
            result = f"target {target} found at index {i}"
            break

        steps.append({
            "action": f"{arr[i]} == {target}",
            "found": False
        })


    return {
        "algorithm": "linear_search",
        "input": data.data,
        "steps": steps,
        "result": result
    }
    
def binary_search(data: SearchRequest):
    arr = data.data
    target = data.target
    steps = []
    partition = []
    result = []

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == arr[mid]:
            steps.append({
                "step": len(steps) + 1,
                "action": f"value is at index {mid}",
                "found": True
            })
            break 
        elif target < arr[mid]:
            high = mid - 1
            partition = arr[low:mid]
        else:
            low = mid + 1
            partition = arr[mid:high] 

        steps.append({
            "step": len(steps) + 1,
            "action": f"split array from index {mid}",
            "array": partition,
            "found": False
        })

    return {
        "algorithm": "binary_search",
        "input": data.data,
        "steps": steps,
        "result": result
        }
    





                
