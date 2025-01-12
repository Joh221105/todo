def add_task():
    task = input('Please enter the task you would like to add: ')
    foobar = open('tasks', 'a')
    foobar.write(f'{task}--*!->')   # adds task and unique split marker for later split
    foobar.close()


def remove_task():
    print_all_task()
    task_idx = int(input('Enter the task number you would like to remove: '))
    task_list = get_all_tasks()
    open('tasks', 'w').close()    # clears file of all tasks
    foobar = open('tasks', 'a')
    for index, task in enumerate(task_list):    # loops through task list, writing to task file, skipping the deleted task
        if index + 1 == task_idx:
            continue
        foobar.write(f'{task}--*!->')
    foobar.close()

def mark_task():
    print("MARK TASK AS COMPLETE")


def print_all_task():
    result_list = get_all_tasks()
    print('\n')
    print('<------------TASKS------------->')
    for i in range(len(result_list)):
        print(f'{i + 1}: {result_list[i]}')

        
def get_all_tasks():
    foobar = open('tasks', 'r')
    result = foobar.read()
    foobar.close()
    result_list = result.split('--*!->')
    return [x for x in result_list if x]  # returns a list with all empty elements removed


def main():
    while True:
        print('\n<---------MENU_OPTIONS--------->')
        print('1: See all tasks')
        print('2: Add a task')
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