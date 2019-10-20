student_basic_info = [
    (1, "6662118001", "张三"),
    (2, "6662118002", "李四"),
    (3, "6662118051", "王五"),
    (4, "6662118052", "赵六")
]

student_class_info = [
    ("6662118001", "计算机201班"),
    ("6662118002", "计算机202班"),
    ("6662118051", "计算机202班"),
    ("6662118052", "计算机203班")
]

L = [student_basic_info[x]+(student_class_info[x][1],) for x in range(0,4)]
for info in L:
    print(info)