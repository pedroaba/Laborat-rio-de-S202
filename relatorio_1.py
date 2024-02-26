from typing import List


class Teacher:
    def __init__(self, name: str):
        self.name = name

    def teach_class(self, subject: str) -> str:
        return f"O professor {self.name} está ministrando uma aula sobre {subject}."


class Student:
    def __init__(self, name: str):
        self.name = name

    def presence(self) -> str:
        return f"O aluno {self.name} está presente."


class Class:
    def __init__(self, teacher: Teacher, subject: str):
        self.teacher = teacher
        self.students: List[Student] = []
        self.subject = subject

    def add_student(self, student: Student):
        self.students.append(student)

    def list_presence(self) -> str:
        presence_list = ""

        for student in self.students:
            presence_list += f"{student.presence()}\n"
        return presence_list


if __name__ == "__main__":
    teacher = Teacher("Lucas")
    student1 = Student("Maria")
    student2 = Student("Pedro")

    _class = Class(teacher, "Programação Orientada a Objetos")
    _class.add_student(student1)
    _class.add_student(student2)

    print(_class.list_presence())
