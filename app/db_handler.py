import sqlite3

def insert_resume(data):
    if data is not None:
        try:
            conn = sqlite3.connect("../resume_data.db")
            cursor = conn.cursor()

            cursor.execute(''' 
                INSERT INTO resumes (`name`, `email`, `phone`, `skills`, `matched skills`, `missing skills`,`education`, `experience`, `projects`)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',(
            data["name"],
            data["email"],
            data["phone"],
            ', '.join(data["skills"]),
            ', '.join(data["matched skills"]),
            ', '.join(data["missing skills"]),
            data["education"],
            ', '.join(data["experience"]),
            ', '.join(data["projects"])
        ))

            conn.commit()
            conn.close()
            return "✅ Successfully saved in SQLite DB"
        
        except Exception as e:
            print("⚠️ An error has occured while storing in SQLite DB!\nError: ",e)
    
    else:
        print("❌ Parsed data is None! Skipping DB insert.")