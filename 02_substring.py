def count_substring(main_string, sub_string):
    count = main_string.count(sub_string)
    return count
if __name__ == "__main__":
    main_string = input("Enter the main string: ")
    sub_string = input("Enter the substring to count: ")
   result=count_substring(main_string,sub_string)  
   print(f"the substring{sub_string}occurs{result}time(s)in mainstring")   


