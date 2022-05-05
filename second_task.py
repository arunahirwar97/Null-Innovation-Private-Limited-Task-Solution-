with open('input_files/second_task_test.txt') as f:
    lines = f.read()

counts = dict()
for i in lines.split():
    words = i.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
with open("output_file/result_second_file.txt","a") as f :
    for i,j in counts.items():
        f.write("{} -> {} \n".format(i ,j))
    f.close()