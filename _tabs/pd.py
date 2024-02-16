##生成一个学生管理系统的类

class student:
    def __init__(self,name,age,sex,score):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=score

    #student book info

    #write a method to print out what book does student checked out
    def print_info(self):
        print(f"name:{self.name},age:{self.age},sex:{self.sex},score:{self.score}")


## make a class of library system to manage books

class library:
    def __init__(self,name,address,phone,books):
        self.name=name
        self.address=address
        self.phone=phone
        self.books=books

    # a method to handle the books check in and checkout by student
    def check_in(self,student_name,book_name):
        if book_name in self.books:
            print(f"{student_name} checked in {book_name}")
        else:
            print(f"{book_name} is not in the library")


    # a method to handle the books checkout by student

    def  check_out(self,student_name,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"{student_name} checked out {book_name}")
        else:
            print(f"{book_name} is not in the library")

    # a method to print out the current books in the library
    def print_books(self):
        print(f"The books in the library are {self.books}")

#construct 3 instance of student and 3 instance of library

student1=student("zhangsan",20,"male",90)
student2=student("lisi",21,"female",80)
student3=student("wangwu",22,"male",70)

library1=library("shanghai", "shanghai", "123456789", ["python","java","c++"])
library2=library("beijing", "beijing", "123456789", ["c","c++","java"])
library3=library("guangzhou", "guangzhou", "123456789", ["c","c++","java"])

#w


def check_out_books():
    print("-----------all books in the library------------")
    
    # print all the book in 3 libraries
    library1.print_books()
    library2.print_books()
    library3.print_books()

    print("--------student check out books------------")

    library1.check_out("zhangsan","python")
    library1.check_out("lisi","java")
    library2.check_out("wangwu","c")
    library3.check_out("zhangsan","c++")
    library3.check_out("lisi","c")
    library3.check_out("wangwu","java")

    print("--------all books left in the library----------")
    library1.print_books()
    library2.print_books()
    library3.print_books()

    print("-----------student has books------------")

    #print all students book in hands
    for student in [student1,student2,student3]:
        student.print_info()

if __name__=="__main__":
    check_out_books()
  
     

