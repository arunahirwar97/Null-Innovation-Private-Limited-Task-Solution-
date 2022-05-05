with open('input_files/first_task_test.txt') as f:
    lines = f.readlines()


with open("output_file/result_first_task.txt","a") as f :
    for i in lines:
        f.write(i.capitalize())
    f.close()