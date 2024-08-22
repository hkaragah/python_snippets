from data_structure import Stack
import os

def binary(num):
    if num == 0:
        return '0'
    
    stack = Stack()  
    while num > 0:
        stack.push(str(num % 2))
        num = num // 2
        
    binary = ''
    while not stack.isEmpty():
        binary += stack.pop()
    
    return binary


def main():
    os.system('cls')
    try:
        num = int(input('Enter a positive integer:'))
    except:
        pass
    else:
        print(f'{num} >> {binary(num)}')
        

if __name__ == '__main__':
    main()