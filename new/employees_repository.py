from database import get_connection
from validation import validate_employee

def add_employee(id,username,salary,department_id):
    validate_employee(id,salary,department_id)

    conn=get_connection()
    cursor=conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO employees (id,username,salary,department_id) VALUES (:1,:2,:3,:4)",
            (id,username,salary,department_id)
        )
        conn.commit()
        print(f"{username} əlavə edildi")
        return True
    except Exception as e:
        print("Xeta: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_all_employees():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT id,username,salary,department_id FROM employees")
    employees=cursor.fetchall()

    print("\n--- Bütün işçilər---")
    for emp in employees:
        print(f"ID:{emp[0]}, Ad:{emp[1]},Maas:{emp[2]},Şöbə:{emp[3]}")
    cursor.close()
    conn.close()
    return employees

def get_employees_above_500():
    conn=get_connection()
    cursor=conn.cursor() 

    cursor.execute("""
        SELECT id,username,salary,department_id
        FROM employees
        WHERE salary > 500
        ORDER BY salary DESC 
""")      
    employees=cursor.fetchall()
    print("\n---Maası 500-den yuxari olanlar---")
    for emp in employees:
       print(f"ID:{emp[0]}, Ad:{emp[1]},Maas:{emp[2]},Şöbə:{emp[3]}")
    cursor.close()
    conn.close()
    return employees   
    