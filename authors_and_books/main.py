from datalayer import insert_author, insert_book, get_all_authors, get_all_books, get_books_by_author
from database import create_tables

create_tables()

def menu():
    while True:
        print("\n" + "="*35)
        print("   KİTABXANA İDARƏETMƏ SİSTEMİ")
        print("="*35)
        print("1. Müəllifləri göstər")
        print("2. Kitabları göstər")
        print("3. Yeni müəllif əlavə et")
        print("4. Yeni kitab əlavə et")
        print("5. Müəllif adına görə kitabları axtar")
        print("0. Çıxış")
        
        choice = input("\nSeçiminizi edin: ").strip()

        if choice == '1':
            get_all_authors()
        
        elif choice == '2':
            get_all_books()
            
        elif choice == '3':
            name = input("Müəllifin adını daxil edin: ").strip()
            if name:
                insert_author(name)
            else:
                print("Xəta: Müəllif adı boş ola bilməz!")
            
        elif choice == '4':
            try:
                title = input("Kitabın adını daxil edin: ").strip()
                if not title:
                    print("Xəta: Kitab adı boş ola bilməz!")
                    continue
                
                price_input = input("Qiyməti daxil edin (məs: 15.50): ")
                price = float(price_input)
                
                # İstifadəçinin ID-ləri görməsi üçün əvvəlcə siyahını göstəririk
                get_all_authors()
                
                author_id_input = input("Müəllifin ID-sini daxil edin: ")
                author_id = int(author_id_input)
                
                insert_book(title, price, author_id)
            except ValueError:
                print("Xəta: Qiymət və ya ID üçün rəqəm daxil etməlisiniz!")
            
        elif choice == '5':
            author_name = input("Axtardığınız müəllifin tam adını yazın: ").strip()
            if author_name:
                get_books_by_author(author_name)
            else:
                print("Xəta: Axtarış üçün ad daxil edilməyib.")
            
        elif choice == '0':
            print("Proqramdan çıxılır... Sağ olun!")
            break
            
        else:
            print("Yanlış seçim! Zəhmət olmasa 0-5 arası rəqəm daxil edin.")

if __name__ == "__main__":
    menu()