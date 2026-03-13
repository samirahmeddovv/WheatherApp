from database import create_tables
from employees_repository import add_employee, get_all_employees,get_employees_above_500
from department_statistics import department_statistics

create_tables()
def main():
    while True:
        print("\n--- İşçi İdarəetmə Sistemi---")
        print("1. İşçi əlavə et")
        print("2. Bütün işçiləri göstər")
        print("3.Maaşı 500-dən yuxarı olanları göstər")
        print("4. Şöbə statistikasını göstər")
        print("0.Çıxış")

        choice=input("Seçim:")
        if choice=='1':
            try:
                id=int(input("Isci ID"))
                username=input("Ad:")
                salary=float(input("Maas:"))
                department_id=int(input("Şöbə ID"))

                if add_employee(id,username,salary,department_id):
                    print("İşçi əlavə edildi")
                else:
                    print("İşçi əlavə etmək alınmadı") 
            except ValueError as e:
                print(f"Xəta:{e}") 
        elif choice=='2':
            get_all_employees()

        elif choice=='3':
            get_employees_above_500()
        elif choice=="4":
            department_statistics()
        elif choice=='0':
            print("Çıxış...")
            
        else:
            print("Yanlış seçim!")

main()                                            