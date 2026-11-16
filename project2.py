def find_num():
    
    
    UNITS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
    TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
    
    TENS = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
    
    SCALES = {
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
    1000000000000: "trillion"
}
    
    NUM_WORDS = {
    **UNITS,
    **TEENS,
    **TENS,
    **SCALES
}
    
    first_user = input("Enter Number: ").strip().lower().replace(" ", "-")
    second_user = input("Enter Number: ").strip().lower().replace(" ", "-")
    
    first_number = []
    second_number = []
    
    for i in first_user.split("-"):
        for key, value in NUM_WORDS.items():
            if value == i:
                first_number.append(key)
                break
            
    first_result = 0
    
    for v in first_number:
        first_result += v
    print(first_result)
            
            
        
    for j in second_user.split("-"):
        for key, value in NUM_WORDS.items():
            if value == j:
                second_number.append(key)
                break  
            
    second_result = 0
    
    for v in second_number:
        second_result += v
    print(second_result)
            

find_num()