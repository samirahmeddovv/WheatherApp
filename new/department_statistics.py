import matplotlib.pyplot as plt
from database import get_connection

def department_statistics():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
        SELECT department_id, MIN(salary),MAX(salary)
        FROM employees
        GROUP BY department_id
""")
    
    departments=[]
    min_salaries=[]
    max_salaries=[]

    print("\n---Şöbə üzrə maaş statistikası---")
    for  row in cursor:
        print(f"Şöbə:{row[0]}, min maaş:{row[1]}, max maaş:{row[2]}")
        departments.append(row[0])
        min_salaries.append(row[1] if row[1] is not None else 0)
        max_salaries.append(row[2] if row[2] is not None else 0)
    cursor.close()
    conn.close()


    x=range(len(departments))  
    width=0.35
    plt.bar([i-width/2 for i in x],min_salaries,width=width,label='Min maas',color='blue')
    plt.bar([i+width/2 for i in x],max_salaries,width=width,label='Max maas',color='purple')  

    plt.xticks(list(x),departments)
    plt.xlabel('Şöbələr')
    plt.ylabel('Maas')
    plt.title("Hər şöbə üzrə min və max maaş")
    plt.legend()
    plt.tight_layout()
    plt.show()