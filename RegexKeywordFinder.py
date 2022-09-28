from re import search

class GetCountOfRowsContainingKeyword:

    def __init__(self, keyword):
        self.keyword = keyword
    
    def countRows(self):
        count = 0
        try:
            with open("Test File.txt") as file:
                for row in file:
                    if search(keyword, row):
                        count+=1
            file.close()
        except Exception as e:
            print(e)
        return count

while True:

    print("\nPress '1' to Search a Keyword")
    print("Press '0' to Exist")
    user_pressed = input()

    if user_pressed == '1':
        print("\nSearch Keyword in Rows\n")
        print("Enter your Keyword:")
        keyword = input()
        
        NumberOfRowsContainingKeyword = GetCountOfRowsContainingKeyword(keyword)
        
        output = str(NumberOfRowsContainingKeyword.countRows())+" "+"rows constains"+" "+"'"+keyword+"'"+" "+"keyword"
        print(output)

    elif user_pressed == '0':
        break
    
    else:
        print("\nWrong Response: Please only press 1 or 0, Try again")
    print()
