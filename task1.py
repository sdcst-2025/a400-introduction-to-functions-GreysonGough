"""
Create a program with 3 function definitions:
function A prints the message "Hello"
function B prints the message "How are you"
function C prints the message "Hi"

Ask the user to enter a letter from A to C
Execute the function of the letter they use.
"""



def A():
    print("Hello")
def B():
    print("How are you")

def C():
    print("Hi")

def main():
    functions_map = {"A":A, "B":B, "C":C}
    user_input = input("choose 'A', 'B', or 'C' ")

    if user_input in functions_map:
        
        func_to_call = functions_map[user_input]
            
        func_to_call()
    else:
        print("Invalid choice. Please enter A, B, or C.")

if __name__ == "__main__":
    main()

