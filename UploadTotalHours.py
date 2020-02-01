#!/usr/bin/python3
import sqlite3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

dbfile = 'TimeTrack4237.db'
dbconn =  sqlite3.connect(dbfile)
student_hours = None

with dbconn:

    dbcursor = dbconn.cursor()
    dbcursor.execute("SELECT name, SUM( ROUND( CAST( (JULIANDAY(checkout) - JULIANDAY(checkin)) * 24 AS REAL), 2)) \
                    FROM activity, students \
                   WHERE activity.id = students.id \
                     AND checkin IS NOT NULL \
                     AND checkout IS NOT NULL \
                   GROUP BY name \
                   ORDER BY name")

    student_hours = dbcursor.fetchall()

if student_hours is not None:

    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials/timetrack4237-12f97a6ef02f.json', scope)

    gc = gspread.authorize(credentials)

    workbook = gc.open("TimeTrack4237")

    workbook.sheet1.clear()

    workbook.values_update(
        'Sheet1!A1', 
        params={'valueInputOption': 'RAW'}, 
        body={'values': student_hours}
    )