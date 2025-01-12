def add_task():
    task = input('Please enter the task you would like to add: ')
    foobar = open('tasks', 'a')
    foobar.write(f'{task}--*!->')
    foobar.close()


def remove_task():
    print("REMOVE A TASK")


def mark_task():
    print("MARK TASK AS COMPLETE")


def print_all_task():
    result_list = get_all_tasks()
    print('\n')
    print('<------------TASKS------------->')
    for i in range(len(result_list) - 1):
        print(f'{i + 1}: {result_list[i]}')

        
def get_all_tasks():
    foobar = open('tasks', 'r+')
    result = foobar.read()
    return result.split('--*!->')


def main():
    while True:
        print('\n<---------Menu Options--------->')
        print('1: See all tasks')
        print('2: Add task')
        print('3: Mark task as complete')
        print('4: Delete a task')
        print('5: Exit app')
        
        choice = int(input('\nChoose an Option (1-5) from above: '))

        match choice:
            case 1:
                print_all_task()
            case 2:
                add_task()
            case 3:
                mark_task()
            case 4:
                remove_task()
            case 5:
                break


if __name__ == "__main__":
    main()