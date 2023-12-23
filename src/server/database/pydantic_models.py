from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Student(BaseModelModify):
    fullname: str
    birthday: str
    phone: int
    address: str
    class_id: int
    password: str


class Staff(BaseModelModify):
    fullname: str
    birthday: str
    phone: int
    address: str
    power_level: int
    password: str


class Lesson(BaseModelModify):
    name: str
    length: int


class Class(BaseModelModify):
    number: int
    letter: str


class LessonTime(BaseModelModify):
    time_start: str
    time_end: str


class LessonTable(BaseModelModify):
    lesson_id: int
    teacher_id: int
    lesson_time_id: int


class Mark(BaseModelModify):
    mark: int
    student_id: int
    lesson_id: int


class Visit(BaseModelModify):
    student_id: int
    datetime_enter: str
    datetime_exit: str


class Truancy(BaseModelModify):
    student_id: int
    lesson_id: int
    reason: str
    valid: bool


class Event(BaseModelModify):
    name: str
    datetime: str
    description: str
    class_id: int
