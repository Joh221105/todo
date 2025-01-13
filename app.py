def add_task():
    task = input('Please enter the task you would like to add: ')
    foobar = open('tasks', 'a')
    foobar.write(f'{task}--*!->')   # adds task and unique split marker for later split
    foobar.close()


def remove_task(task_idx = 0):
    print_incompleted_task()
    if task_idx == 0:   # if the user is choosing to remove a task from menu  
        task_idx = int(input("Enter the task's number you would like to remove: "))
    task_list = get_incompleted_tasks()
    open('tasks', 'w').close()    # clears file of all tasks
    foobar = open('tasks', 'a')
    for index, task in enumerate(task_list):    # loops through task list, writing to task file, skipping the deleted task
        if index + 1 == task_idx:
            continue
        foobar.write(f'{task}--*!->')
    foobar.close()

def print_incompleted_task():
    result_list = get_incompleted_tasks()
    print('\n')
    print('<------------TASKS------------->')
    for i in range(len(result_list)):
        print(f'{i + 1}: {result_list[i]}')
        
def get_incompleted_tasks():
    foobar = open('tasks', 'r')
    result = foobar.read()
    foobar.close()
    result_list = result.split('--*!->')
    return [x for x in result_list if x]  # returns a list with all empty elements removed



def main():
    while True:
        print('\n<---------MENU_OPTIONS--------->')
        print('1: See ongoing tasks')
        print('2: Add a task')
        print('3: Remove/Complete a task')
        print('4: Exit app')
        
        choice = int(input('\nChoose an Option (1-4) from above: '))

        match choice:
            case 1:
                print_incompleted_task()
            case 2:
                add_task()
            case 3:
                remove_task()
            case 4:
                break


if __name__ == "__main__":
    main()