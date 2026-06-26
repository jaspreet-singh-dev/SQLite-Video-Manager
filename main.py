import sqlite3
connection=sqlite3.connect("videos.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS videos(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT,
                Views INTEGER ,
                Category TEXT
                )""")
def add_videos():
    title=input("Enter Video title:")
    views=int(input("Enter the number of Views:"))
    category=input("Enter the Video category:")
    cursor.execute("INSERT INTO videos(Title,Views,Category) VALUES (?,?,?)"
                ,(title,views,category))
    
    connection.commit()
    print("✅ Video Added Successfully!")
def view_videos():
    cursor.execute("SELECT * FROM videos")
    rows=cursor.fetchall()
    for row in rows:
        print("ID:", row[0])
        print("Title:", row[1])
        print("Views:", row[2])
        print("Category:", row[3])
        print("-------------------")
    if len(rows)==0:
        print("Videos Not Available!")
def search_video():
    search=input("Enter the Video title to search:")
    cursor.execute("""SELECT * FROM videos
                WHERE Title=?"""
            ,(search,))
    rows=cursor.fetchall()
    for row in rows:
        print("ID:", row[0])
        print("Title:", row[1])
        print("Views:", row[2])
        print("Category:", row[3])
        print("-------------------")
    if len(rows)==0:
        print("Video Not Found!")

def update_video():
    id=int(input("Enter Video ID:"))
    views=int(input("Enter the latest views:"))
    cursor.execute("""
        UPDATE videos
        SET views=?
        WHERE ID=?
    """,(views,id))
    connection.commit()
    print("✅ Video Updated Successfully!")
def delete_video():
    id=int(input("Enter the Video ID you want to delete:"))
    cursor.execute("""
        DELETE FROM videos
        WHERE ID=?
    """,(id,))
    connection.commit()
    print("✅ Video Deleted Successfully!")

def analytics():
    cursor.execute("""SELECT COUNT(*) FROM videos;""")
    total=cursor.fetchone()[0]
    if total==0:
        print("No Videos Available!")
        return
    
    cursor.execute("""SELECT MAX(views) FROM videos;""")
    highest=cursor.fetchone()[0]
    cursor.execute("""SELECT MIN(views) FROM videos""")
    lowest=cursor.fetchone()[0]
    cursor.execute("""SELECT AVG(views) FROM videos;""")
    avg=cursor.fetchone()[0]
    cursor.execute("""SELECT SUM(views) FROM videos;""")
    calculated=cursor.fetchone()[0]
    print("Total Videos:",total)
    print("Total Views:",calculated)
    print("Highest Views:",highest)
    print("Lowest VIews:",lowest)
    if total!=0:
        print("Average Views:",round(avg,2))



while True:
    try:
        print("=====SQLite Video Manager=====")
        print("1.Add Video")
        print("2.View Videos")
        print("3.Search Video")
        print("4.Update Video")
        print("5.Delete Video")
        print("6.Analytics")
        print("7.Exit")
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            add_videos()
        elif choice==2:
            view_videos()
        elif choice==3:
            search_video()
        elif choice==4:
            update_video()
        elif choice==5:
            delete_video()
        elif choice==6:
            analytics()
        elif choice==7:
            print("ThankYou for using the program!")
            break
        else:
            print("Enter a Valid number!")
    except ValueError as e:
        print("Enter Numerics Only!",e)
connection.commit()
connection.close()