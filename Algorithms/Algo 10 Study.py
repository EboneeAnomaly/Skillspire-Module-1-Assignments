#1. Create a for loop that will iterate from the front of the array to the back of the array
#2. Inside the loop we will swap the current value that is at the current index with the value next to it
# example [1,2] should be [2,1]
#3. After we have exited the loop we will pop off and return the last value in the array

def arrPopFront(arr):
    for i in range(0, len(arr)-1):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
    return arr.pop()

print(arrPopFront([1,2,3,4,5]))