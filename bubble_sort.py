# Bubble sort
def sort_element(element):
    for i in range(len(element)-1):
        for j in range(len(element)-1-i):
            sort = False
            if element[j] > element[j+1] or element[j] == element[j+1]:
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp
                sort = True
        if not sort:
            break

if __name__ == "__main__":
    elements = [2,43,5,524,23,4,345,45,3,4,4,6,4,6]
    sort_element(elements)
    print(elements)