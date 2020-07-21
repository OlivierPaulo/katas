def solve(arr):
    arr.sort()

    if arr[1] == arr[2]:
        return arr[1] + arr[0]//2
    
    elif arr[1] + arr[0] > arr[2]:
        if (arr[0] % 2 == 1 and arr[1] % 2 == 1) or (arr[1] % 2 == 1 and arr[2] % 2 == 1) or (arr[0] % 2 == 1 and arr[2] % 2 == 1):
            return arr[0]//2 + arr[1]//2 + arr[2]//2 + 1
    
        else:
            return arr[0]//2 + arr[1]//2 + arr[2]//2
    
    else:
        return arr[0]+arr[1]