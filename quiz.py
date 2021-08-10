class Student:
    id=4
    name="moshe"
    def __init__(self,id=0,name="Moshe"):
        id=id
        name=name

if __name__=="__main__":
    a = Student(3, 'Yaakov')
    b = Student(4, 'TTO')
    a.id=5
    b.id=2
    students=[a,b]
    for student in students:

        for attr in student.__dict__:
            pass
            #print('d')
            #print(f'{attr} -> {getattr(student, attr)}')
    print(type(a).__name__)
    print('main')
    dicti=dict()
    dicti['ddd']=8
    dicti['cy']=3
    dicti['ccc'] = 2
    list=[3,2,5]
    re=sorted(list,key=list)
    print(re)
    result = sorted(dicti, key=dicti.get, reverse=True)[:2]
    print(result)
# class Student:
#     school = 'Forward Thinking'
#     address = '2626/Z Overlook Drive, COLUMBUS'
# student1 = Student()
# student2 = Student()
# student1.student_id = "V12"
# student1.student_name = "Ernesto Mendez"
# student2.student_id = "V12"
# student2.marks_language = 85
# student2.marks_science = 93
# student2.marks_math = 95
# students = [student1, student2]
# for student in students:
#     print('\n')
#     for attr in student.__dict__:
#         print(f'{attr} -> {getattr(student, attr)}')
