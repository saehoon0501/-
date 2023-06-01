def quickSort(array, low, high):
    if low < high:
        pivot = array[low];
        i, j = low, high;

        while(i < j):
            while array[i] <= pivot:
                if i == high:
                    break;
                i+=1;
            while array[j] > pivot:
                j-=1;
            
            if i < j:
                array[i], array[j] = array[j], array[i];
    
        array[low], array[j] = array[j], array[low];

        quickSort(array, low, j-1);
        quickSort(array, j+1, high);
    return;

if __name__ == "__main__":
    # n = list(map(int, input().split(" ")));
    n = [4, 3, 1, 5, 7, 12, 10, 15]
    quickSort(n, 0, len(n)-1);
    print(n);