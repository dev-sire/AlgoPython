import sys

def demonstrate_ref_counting():
  """
  Demonstrates how reference counting works in Python using sys.getrefcount().
  This function creates an integer object and tracks its reference count as it 
  is assigned to different variables.
  """
  
  x = 10
  print(f"Initial reference count of x: {sys.getrefcount(x)}") 
  y = x
  print(f"Reference count of x after assigning to y: {sys.getrefcount(x)}") 
  z = [x]
  print(f"Reference count of x after adding to list: {sys.getrefcount(x)}")
  del y
  print(f"Reference count of x after deleting y: {sys.getrefcount(x)}")
  del z
  print(f"Reference count of x after deleting z: {sys.getrefcount(x)}") 

if __name__ == "__main__":
  demonstrate_ref_counting()