import streamlit as st
import sqlite3
import os

st.title("🌌 KRISHNA - Browser Artifact Collector")

if st.button("Load Chrome History"):
    path = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\History"
    if os.path.exists(path):
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, visit_count FROM urls LIMIT 10")
        rows = cursor.fetchall()
        for row in rows:
            st.write(row)
    else:
        st.error("History DB not found.")