from tortoise.models import Model
from tortoise import fields


# 选课
class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    sno = fields.IntField(description="学号")
    # 一对多 班级与学生
    clazz = fields.ForeignKeyField("models.Clazz", related_name="students")

    # 多对多  学生与课程
    courses = fields.ManyToManyField("models.Course", related_name="students", description="学生选课表")


class Clazz(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="班级名称")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="课程名称")
    teacher = fields.ForeignKeyField("models.Teacher", related_name="teachers", description="课程讲师表")
    addr = fields.CharField(max_length=32,description="教室地址",default="")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="老师姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    tno = fields.IntField(description="老师编号")
