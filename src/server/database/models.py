import peewee
import settings

db = peewee.SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Student(BaseModel):
    fullname = peewee.CharField(default='')
    birthday = peewee.DateTimeField(default='1970-01-01 00:00:00')
    phone = peewee.IntegerField(default=0)
    address = peewee.CharField(default='')
    class_relation = peewee.ForeignKeyField(related_name='students', default=0)
    password = peewee.CharField(default='')


class Staff(BaseModel):
    fullname = peewee.CharField(default='')
    birthday = peewee.DateTimeField(default='1970-01-01 00:00:00')
    phone = peewee.IntegerField(default=0)
    address = peewee.CharField(default='')
    power_level = peewee.IntegerField(default=1)
    password = peewee.CharField(default='')
    user_relation = peewee.ForeignKeyField(related_name='staff', default=0)


class Lesson(BaseModel):
    name = peewee.CharField(default='')
    length = peewee.IntegerField(default=0)


class Class(BaseModel):
    number = peewee.IntegerField(default=0)
    letter = peewee.CharField(default='')


class LessonTime(BaseModel):
    time_start = peewee.TimeField(default='00:00:00')
    time_end = peewee.TimeField(default='00:00:00')


class LessonTable(BaseModel):
    lesson_relation = peewee.ForeignKeyField(related_name='lesson_tables', default=0)
    teacher_relation = peewee.ForeignKeyField(related_name='lesson_tables', default=0)
    lesson_time_relation = peewee.ForeignKeyField(related_name='lesson_tables', default=0)


class Mark(BaseModel):
    mark = peewee.IntegerField(default=0)
    student_relation = peewee.ForeignKeyField(related_name='marks', default=0)
    lesson_relation = peewee.ForeignKeyField(related_name='marks', default=0)


class Visit(BaseModel):
    student_relation = peewee.ForeignKeyField(related_name='visits', default=0)
    datetime_enter = peewee.DateTimeField(default='1970-01-01 00:00:00')
    datetime_exit = peewee.DateTimeField(default='1970-01-01 00:00:00')


class Truancy(BaseModel):
    student_relation = peewee.ForeignKeyField(related_name='truanсies', default=0)
    lesson_relation = peewee.ForeignKeyField(related_name='truanсies', default=0)
    reason = peewee.CharField(default='')
    valid = peewee.BooleanField(default=False)


class Event(BaseModel):
    name = peewee.CharField(default='')
    datetime = peewee.DateTimeField(default='1970-01-01 00:00:00')
    description = peewee.CharField(default='')
    class_relation = peewee.ForeignKeyField(related_name='events', default=0)


db.create_tables([
    Student,
    Staff,
    Lesson,
    Class,
    LessonTime,
    LessonTable,
    Mark,
    Visit,
    Truancy,
    Event
])
