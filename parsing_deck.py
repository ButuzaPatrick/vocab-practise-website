import sqlite3
import csv

conn = sqlite3.connect("deck_folder/collection.anki2")
cur = conn.cursor()

# The main table for cards/notes is 'notes'
cur.execute("SELECT flds FROM notes")
rows = cur.fetchall()

parsed_rows = []
parsed_row = []

for row in rows:
    parsed_row = list(row[0].split("\x1f"))
    parsed_row.pop()
    parsed_rows.append(parsed_row)

print(parsed_rows)

with open("deck_folder/anki_deck.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["GERMAN_NOUN", "ENGLISH_TRANSLATION", "PLURAL", "EXAMPLE"])
    writer.writerows(parsed_rows)
