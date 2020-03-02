from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from marshmallow import Schema, fields


db = SQLAlchemy()


# Product Class/Model
class Employee(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  emp_name = db.Column(db.String(100))
  emp_role = db.Column(db.String(200))
  emp_salary = db.Column(db.Float)

  def __init__(self, emp_name, emp_role, emp_salary):
    self.emp_name = emp_name
    self.emp_role = emp_role
    self.emp_salary = emp_salary
  
  @classmethod
  def emp_json(self):
    ret={}
    ret['id']=self.id
    ret['emp_name']=self.emp_name
    ret['emp_role']=self.emp_role
    ret['emp_salary']=self.emp_salary
    return ret


# Product Schema
class EmployeeSchema(Schema):
  class Meta:
    fields = ('id', 'emp_name', 'emp_role', 'emp_salary')

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)