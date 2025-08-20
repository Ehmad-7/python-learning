import sqlite3

conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 time TEXT NOT NULL
               )
               ''')

def list_videos():
  cursor.execute('SELECT * FROM videos')
  for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")

def add_video(video_name, time):
  cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (video_name, time))
  conn.commit()
  print("Video added successfully.")

def update_video(video_id, video_name, time):
  cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (video_name, time, video_id))
  conn.commit()
  if cursor.rowcount > 0:
    print("Video updated successfully.")
  else:
    print("Video not found.")

def delete_video(video_id):
  cursor.execute('DELETE FROM videos WHERE id = ?', (video_id,))
  conn.commit()
  if cursor.rowcount > 0:
    print("Video deleted successfully.")

def main():
  while True:
    print("\n Youtube Manager with db | Choose an option \n")
    print("1. List a favourite videos ")
    print("2. Add a youtube video ")
    print("3. Update a youtube video details ")
    print("4. Delete a youtube video ")
    print("5. Exit the app")
    choice=input("Enter your choice: ")

    if choice=='1':
      list_videos()
    elif choice=='2':
      video_name=input("Enter video name: ")
      time=input("Enter video time: ")
      add_video(video_name, time)
    elif choice=='3':
      video_id=input("Enter video ID to update: ")
      video_name=input("Enter new video name: ")
      time=input("Enter new video time: ")
      update_video(video_id, video_name, time)
    elif choice=='4':
      video_id=input("Enter video ID to delete: ")
      delete_video(video_id)
    elif choice=='5':
      print("Exiting the app...")
      break
    else:
      print("Invalid choice, please try again.") 
  
  conn.close()

if __name__=="__main__":
  main()