def selection_sort(numlist):
  for i in range(len(numlist)):
    min_index = i
    
    for j in range(i + 1, len(numlist)):
      if numlist[j] < numlist[min_index]:
        min_index = j

    numlist.insert(i, numlist[min_index])
    numlist.pop(min_index + 1)
        
  return numlist

def main():
  unsorted = [1, 3, 7, 31, 25, 64, 33, 7, 19, 83, 16, 13, 10, 56, 74, 7, 6]
  print(f"Unsorted: {unsorted}")
  print(f"Sorted:   {selection_sort(unsorted)}")

if __name__ == "__main__":
  main()