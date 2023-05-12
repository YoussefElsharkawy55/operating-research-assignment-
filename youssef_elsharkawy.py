
def main():
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))
    alloc = []
    max = []
    avail = []
    need = []
    sequence = []
    for i in range(n):
        alloc.append([0] * m)
        max.append([0] * m)
        need.append([0] * m)
    print("Enter allocation matrix: ")
    for i in range(n):
        for j in range(m):
            alloc[i][j] = int(input())
    print("Enter maximum matrix: ")
    for i in range(n):
        for j in range(m):
            max[i][j] = int(input())
    print("Enter available matrix: ")
    for i in range(m):
        avail.append(int(input()))
    # n = 5
    # m = 3
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]
    print("Allocation matrix is: ")
    for i in range(n):
        for j in range(m):
            print(alloc[i][j], end=" ")
        print()
    print("Maximum matrix is: ")
    for i in range(n):
        for j in range(m):
            print(max[i][j], end=" ")
        print()
    print("Need matrix is: ")
    for i in range(n):
        for j in range(m):
            print(need[i][j], end=" ")
        print()
    print("Available matrix is: ")
    for i in range(m):
        print(avail[i], end=" ")
    print()
    for i in range(n):
        for j in range(m):
            if need[i][j] > avail[j]:
                break
        else:
            sequence.append(i)
            for k in range(m):
                avail[k] += alloc[i][k]
    print("Safe sequence is: ", sequence)


if __name__ == "__main__":
    main()


    