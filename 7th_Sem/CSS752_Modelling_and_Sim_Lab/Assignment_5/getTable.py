def getTable():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    table = []
    print("\nTable Entry......")
    for a in range(r):
        tmp = []
        print(f"Enter values of row {a}: ")
        tmp = list(map(int, input().split()))

        if len(tmp) != c:
            print("Incorrect number of elements")
            exit(1)

        table.append(tmp)

    # supply = []
    # print("\nEnter the supply values:")
    # supply = list(map(int, input().split()))
    # if len(supply) != r:
    #     print("Incorrect number of elements")
    #     exit(1)

    # demand = []
    # print("\nEnter the demand values:")
    # demand = list(map(int, input().split()))
    # if len(demand) != c:
    #     print("Incorrect number of elements")
    #     exit(1)
    
    return table