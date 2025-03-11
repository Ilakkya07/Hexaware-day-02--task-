class CRUD:
    def __init__(self):
        self.arr = []  
    def create(self, value):
        self.arr.append(value)  
        print(f"{value} added successfully!")
    def read(self):
        if self.arr:
            print("Current Array:", self.arr)
        else:
            print("Array is empty!")
    def update(self, index, new_value):
        if 0 <= index < len(self.arr):  
            old_value = self.arr[index]
            self.arr[index] = new_value
            print(f"Updated index {index}: {old_value} → {new_value}")
        else:
            print("Invalid index!")
    def delete(self, index):
        if 0 <= index < len(self.arr):  
            removed_value = self.arr.pop(index)  
            print(f"Deleted {removed_value} from index {index}")
        else:
            print("Invalid index!")

crud = CRUD()
crud.create(10)
crud.create(20)
crud.create(30)
crud.read()
crud.update(1, 40)
crud.read()
crud.delete(2)
crud.read()


def linear_search(arr, target):
    for i in range(len(arr)):  
        if arr[i] == target:  
            return i
    return -1  
n = int(input("Enter the number of elements: "))  
arr = []  
print("Enter the elements:")
for i in range(n): 
    arr.append(int(input()))
target = int(input("Enter the element to search: "))
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the list")