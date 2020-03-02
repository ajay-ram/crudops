from flask import Flask, jsonify, abort, request
from models import db,Employee, employee_schema,employees_schema


app = Flask(__name__)

app.config.from_pyfile('settings.py')
db.init_app(app)


@app.route('/employee', methods=['POST'])
def add_employee():
    name = request.json['emp_name']
    role = request.json['emp_role']
    salary = float(request.json['emp_salary'])
    emp = Employee(name, role, salary)
    db.create_all()
    db.session.add(emp)
    db.session.commit()
    # Init schema
    return jsonify(employee_schema.dump(emp))


@app.route('/employee/', methods=['GET'])
def get_employee():
    obj=Employee.query.all()
    result = employees_schema.dump(obj)
    return jsonify({'employee_data': result})


@app.route('/employee/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    obj=Employee.query.get(id)
    return jsonify({'employee_data': employee_schema.dump(obj)})


@app.route('/employee/id=<int:id>', methods=['DELETE'])
def delete_employee(id):
    # data = request.json['id']
    # id = int(data['id'])
    obj = Employee.query.get(int(id))
    if obj:
        ret = employee_schema.dump(obj)
        db.session.delete(obj)
        db.session.commit()
        return jsonify({'employee_data': employee_schema.dump(obj)})
    else:
        return jsonify('no employee found')


@app.route('/employee', methods=['PUT'])
def update_employee():
    data = request.json['id']
    id = int(data['id'])
    obj = Employee.query.get(id)
    name = data.get('emp_name','')
    role = data.get('emp_role','')
    salary = data.get('emp_salary','')
    if name:
        obj.emp_name = name
    # print(name)
    if role:
        obj.emp_role = role
    # print(role)
    if salary:
        obj.emp_salary = salary
    # print(str(salary))
    obj = db.session.merge(obj)
    db.session.commit()
    return jsonify({'employee_data': employee_schema.dump(obj)})


if __name__ == "__main__":
    app.run(debug=True)