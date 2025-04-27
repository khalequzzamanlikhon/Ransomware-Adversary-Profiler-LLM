import logging
import sqlite3
import requests
from pathlib import Path
from typing import List, Dict
import time
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('D:\CyberSecurity_Projects\Ransomware_Adversary_Profiler_Using_LLMs\Ransomware_data\_api.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def create_database(db_path: str) -> sqlite3.Connection:
    """Create SQLite database and reports table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                title TEXT,
                content TEXT,
                url TEXT UNIQUE,
                scrape_date TEXT
            )
        ''')
        conn.commit()
        logger.info(f"Database created at {db_path}")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise

def fetch_recent_victims(base_url: str = "https://api.ransomware.live/v2") -> List[Dict]:
    """Fetch recent victims from Ransomware.live API."""
    endpoint = f"{base_url}/recentvictims"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
    reports = []
    
    try:
        response = requests.get(endpoint, headers=headers, timeout=10)
        response.raise_for_status()
        victims = response.json()
        
        for victim in victims:
            # Combine description and press summary (if available) for SKRAM-rich content
            content = victim.get('description', '')
            if victim.get('press') and victim['press'].get('summary'):
                content += f"\nPress Summary: {victim['press']['summary']}"
            
            report = {
                'title': f"{victim.get('victim', 'Unknown')} - {victim.get('group', 'Unknown')}",
                'content': content,
                'url': victim.get('url', victim.get('claim_url', '')),
                'source': 'Ransomware.live API',
                'scrape_date': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            reports.append(report)
            logger.info(f"Fetched victim: {victim.get('victim', 'Unknown')}")
        
        return reports
    except requests.RequestException as e:
        logger.error(f"API fetch error: {e}")
        return []

def save_reports(conn: sqlite3.Connection, reports: List[Dict]) -> None:
    """Save API-fetched reports to SQLite database."""
    try:
        cursor = conn.cursor()
        for report in reports:
            cursor.execute('''
                INSERT OR IGNORE INTO reports (source, title, content, url, scrape_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                report['source'],
                report['title'],
                report['content'],
                report['url'],
                report['scrape_date']
            ))
        conn.commit()
        logger.info(f"Saved {len(reports)} reports to database")
    except sqlite3.Error as e:
        logger.error(f"Database save error: {e}")
        raise

def main():
    db_path = 'D:\CyberSecurity_Projects\Ransomware_Adversary_Profiler_Using_LLMs\Ransomware_data\_reports.db'
    Path(db_path).parent.mkdir(exist_ok=True)
    
    conn = create_database(db_path)
    reports = fetch_recent_victims()
    save_reports(conn, reports)
    
    conn.close()
    logger.info("API data retrieval completed")

if __name__ == "__main__":
    main()