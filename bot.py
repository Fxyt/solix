import register
import task
import mining
import os
import platform

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

def main():
    try:
        clear()
        print('1. register & refferer')
        print('2. login & clear task')
        print('3. mining')
        print('4. exit')
        menu = int(input('choose number: '))
        if menu == 1:
            register.run()
        elif menu == 2:
            task.run()
        elif menu == 3:
            mining.run()
        else:
            print('bye')
    except KeyboardInterrupt:
        print('exiting...')
    except ValueError:
        print('Invalid input. Please enter a number.')
    except Exception as e: 
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()