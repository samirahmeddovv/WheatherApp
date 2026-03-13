def validate_employee(id,salary,department_id):
    if id<=0:
        raise ValueError ("id 0-dan boyuk olmalidir")
    if salary<=0:
        raise ValueError("salary 0-dan boyuk olmalidir")
    if department_id<=0:
        raise ValueError ('department id 0-dan boyuk olmalidir')