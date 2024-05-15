# goal of this program is to make a list which contains places in teh world that I'd like to see, then modify/sort them using the list functions given in the list chapter of the Python Crash Course, second edition book
# creating inital list of locations
locations = ['Beijing, China', 'Honolulu, Hawaii', 'Tokyo, Japan', 'Rome, Italy', 'Paris, France']


print(f"This is the orginal locations list\n {locations}")
print(f"\nThis is the sorted list\n {sorted(locations)}")
print(f"\nThis is the original list again\n{locations}")
print(f"\nThis is the original list, but it's been reverse sorted\n{sorted(locations, reverse=True)}")
print(f"\nThis is the orginal locations list\n {locations}")
locations.reverse()
print(f"\nTHis is a list reversed using the reverse function\n{locations}")
locations.reverse()
print(f"\nThis is the orginal locations list which has been re-reversed to be original again\n{locations}")
locations.sort()
print(f"\nThis is the sorted list using the sort function\n{locations}")
locations.sort(reverse=True)
print(f"\nThis is the sorted list which has been reverse sorted using reverse = true on the sort function\n{locations}")
print("\nEnd Program, we hope you enjoyed this")
