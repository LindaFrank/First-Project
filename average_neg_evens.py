def average_neg_evens(input_list):
    counts_loop = 0
    counts_even_negatives = 0
    sum_of_numbers_in_list = 0
    while counts_loop < len(input_list):
        if (input_list[counts_loop] % 2 ==0) and (input_list[counts_loop] < 0):
##            print(input_list[counts_loop], "is a negative even number in the list")
            sum_of_numbers_in_list += input_list[counts_loop]
##            print(sum_of_numbers_in_list)
            counts_even_negatives +=1
        counts_loop +=1
##        print(sum_of_numbers_in_list)
    return sum_of_numbers_in_list/counts_even_negatives

def main():
    input_list = [0,1,2,-2,-3,-4,3,4]
    print(average_neg_evens(input_list))
##    average_neg_evens(input_list)
main()
