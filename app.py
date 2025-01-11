def add_task():
    print("ADD A TASK")

def remove_task():
    print("REMOVE A TASK")

def mark_task():
    print("MARK TASK AS COMPLETE")

def see_all_task():
    print("LISTING ALL TASKS")


def main():

    while True:
        print('\n Choose an Option (1-5) from below: \n')
        print('1: See all tasks')
        print('2: Add task')
        print('3: Mark task as complete')
        print('4: Delete a task')
        print('5: Exit app \n')
        
        choice = int(input())

        match choice:
            case 1:
                see_all_task()
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