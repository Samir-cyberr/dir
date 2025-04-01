import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

db_name = "jobs.db"
url = "https://realpython.github.io/fake-jobs"

def create_table():
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                location TEXT,
                description TEXT,
                application_link TEXT,
                UNIQUE(title, company, location)
            )
        ''')
        conn.commit()

def scrape_jobs():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []
    
    for job_card in soup.find_all("div", class_="card-content"):
        title = job_card.find("h2", class_="title").text.strip()
        company = job_card.find("h3", class_="company").text.strip()
        location = job_card.find("p", class_="location").text.strip()
        description = job_card.find("div", class_="content").text.strip()
        application_link = job_card.find("a", text="Apply")['href']
        jobs.append((title, company, location, description, application_link))
    
    return jobs

def insert_jobs(jobs):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        for job in jobs:
            cursor.execute('''
                INSERT INTO jobs (title, company, location, description, application_link)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(title, company, location) DO UPDATE SET
                description=excluded.description,
                application_link=excluded.application_link
            ''', job)
        conn.commit()

def filter_jobs(company=None, location=None):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM jobs WHERE 1=1"
        params = []
        if company:
            query += " AND company = ?"
            params.append(company)
        if location:
            query += " AND location = ?"
            params.append(location)
        cursor.execute(query, params)
        return cursor.fetchall()

def export_to_csv(filtered_jobs, filename="filtered_jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(filtered_jobs)
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    create_table()
    jobs = scrape_jobs()
    insert_jobs(jobs)
    print("Job scraping and insertion completed.")