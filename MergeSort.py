def mergeSort(array, aux, low, high):
    
    if low < high:
        median = (low+high)//2;
        mergeSort(array, aux, low, median);
        mergeSort(array, aux, median+1, high);
        merge(array, aux, low, high);
    
    return;

def merge(array, aux, low, high):
    for i in range(low, high+1):
        aux[i] = array[i];
    
    median = (low + high)//2;
    j, k = low, median+1;
    for i in range(low, high+1):
        if j > median:
            array[i] = aux[k];
            k+=1;
        elif k > high:
            array[i] = aux[j];
            j+=1;
        elif aux[j] <= aux[k]:
            array[i] = aux[j];
            j+=1;
        else:
            array[i] = aux[k];
            k+=1;
    return;
    
if __name__ == "__main__":
    # n = list(map(int, input().split(" ")));
    n = [10, 9 , 8 ,5, 4, 3, 2, 1];
    aux = [0] * len(n);
    mergeSort(n, aux, 0,len(n)-1);
    print(n);

