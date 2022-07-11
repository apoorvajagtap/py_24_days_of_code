def lsComprehensionCond():
    # result = [(int(num)*int(num)) for num in ls if int(num)%2 != 0]
    print(','.join([str(int(num)**2) for num in input("Enter the numbes: ").split(',') if int(num)%2 != 0]))

    # NORMAL METHOD
    # ls = input("Enter the numbers: ").split(',')
    #  result = []
    # for num in ls:
    #     num = int(num)
    #     if num % 2 != 0:
    #         result.append(num * num)
    # print(result)

def calNetAmount():
    transaction = {"D": 0, "W": 0}

    while True:
        line = input("Transaction: ").split()
        if line:
            transaction[line[0]] += int(line[1])
        else:
            break
    
    print(transaction["D"]-transaction["W"])

def main():
    ## square of each odd number in list using list comprehension
    #lsComprehensionCond()

    ## calculate the net amount in account (deposit vs withdrawal)
    calNetAmount()

if __name__ == "__main__":
    main()