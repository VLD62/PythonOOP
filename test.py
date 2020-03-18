ARR_SIZE = 1000
REF = [1, 3, 4]
ARR = [0] * ARR_SIZE

def printCompositions(n, i):
    if (n == 0):
        printArray(ARR, i)
    elif(n > 0):
        for k in range(1, 4 + 1):
            if k in REF:
                ARR[i] = k
                printCompositions(n - k, i + 1)

def printArray(arr, arr_size):
        temp_list = []
        for i in range(arr_size):
            temp_list.append(ARR[i])
        if 3 in temp_list and 4 in temp_list and 1 in temp_list:
            print(temp_list)


if __name__ == "__main__":
    N = int(input())
    print(
        f"All the different ways the number {N} can be represented as the sum of 1,3 and 4 simultaneously are: ")
    printCompositions(N, 0)
    print(f"PTI4i KORONA GRIP VIRUS!")
