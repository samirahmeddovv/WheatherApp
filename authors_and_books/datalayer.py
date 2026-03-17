from database import get_connection
import oracledb

def insert_author(name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # :1 istifadə ediriksə, siyahı [name] şəklində ötürürük
        cursor.execute("INSERT INTO authors (name) VALUES (:1)", [name])
        conn.commit()
        print(f"Müəllif əlavə edildi: {name}")
    except Exception as e:
        print(f"Müəllif əlavə edilərkən xəta: {e}")
    finally:
        cursor.close()
        conn.close()

def insert_book(title, price, author_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Sıralı parametrlər
        cursor.execute("INSERT INTO books (title, price, author_id) VALUES (:1, :2, :3)", 
                       [title, price, author_id])
        conn.commit()
        print(f"Kitab əlavə edildi: {title}")
    except Exception as e:
        print(f"Kitab əlavə edilərkən xəta: {e}")
    finally:
        cursor.close()
        conn.close()

def get_books_by_author(author_name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT b.title, b.price 
            FROM books b
            JOIN authors a ON b.author_id = a.author_id
            WHERE a.name = :name
        """
        # Adlandırılmış parametr istifadəsi (dict kimi)
        cursor.execute(sql, {"name": author_name})
        rows = cursor.fetchall()
        
        print(f"\n{author_name} tərəfindən yazılan kitablar:")
        if not rows:
            print("Bu müəllifə aid kitab tapılmadı.")
        for row in rows:
            print(f"- {row[0]} (Qiymət: {row[1]} AZN)")
    except Exception as e:
        print(f"Məlumat oxunarkən xəta: {e}")
    finally:
        cursor.close()
        conn.close()

def get_all_authors():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT author_id, name FROM authors ORDER BY author_id")
        rows = cursor.fetchall()
        print("\n--- Bütün Müəlliflər ---")
        for row in rows:
            print(f"ID: {row[0]} | Ad: {row[1]}")
    except Exception as e:
        print(f"Müəlliflər alınarkən xəta: {e}")
    finally:
        cursor.close()
        conn.close()
    
def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT b.book_id, b.title, b.price, a.name 
            FROM books b 
            LEFT JOIN authors a ON b.author_id = a.author_id
            ORDER BY b.book_id
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\n--- Bütün Kitablar ---")
        for row in rows:
            print(f"ID: {row[0]} | Başlıq: {row[1]} | Qiymət: {row[2]} AZN | Müəllif: {row[3]}")
    except Exception as e:
        print(f"Kitablar alınarkən xəta: {e}")
    finally:
        cursor.close()
        conn.close()