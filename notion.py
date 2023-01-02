from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3

def deploy_page(url):
	try:
		key_str = ".notion.site/"
		key_index = url.find(key_str)
		if key_index == -1:
			return { "status": "fail", "result": "wrong url input" }
		
		conn = sqlite3.connect("database.db")
		cur = conn.cursor()
		res = cur.execute(f"SELECT html FROM pages WHERE url='{url}'")
		fetch_list = res.fetchone()

		options = webdriver.ChromeOptions()
		options.add_argument("headless")
		browser = webdriver.Chrome("chromedriver", options=options)
		browser.get(url)
		wait = WebDriverWait(browser, 30)
		content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'notion-page-content')))
		html = content.get_attribute('innerHTML')
		browser.quit()

		main_url = url[:key_index + len(key_str) - 1]
		html = html.replace('src="/image', f'src="{main_url}/image')
		html = f'''
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>NOTION GOD</title>
			<link rel="preconnect" href="https://fonts.googleapis.com">
			<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
			<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
			<link rel="stylesheet" href="/static/css/style.css">
		</head>
		<body>
			<div id="god"></div>
			<div id="notion" style="display:none">
				{html}
			</div>
			<script defer src="/static/js/page.js"></script>
		</body>
		</html>
		'''

		if fetch_list is None:
			sql = '''INSERT INTO pages (url, html) VALUES (?,?)'''
			cur.execute(sql, (url, html))
			conn.commit()
			conn.close()
			return { "status": "success", "result": url }
		else:
			sql = '''UPDATE pages SET html = ? WHERE url = ?'''
			cur.execute(sql, (html, url))
			conn.commit()
			conn.close()
			return { "status": "success", "result": url }
	except Exception as e:
		print(e)
		return { "status": "fail", "result": "Error: " + e }

def get_page(url):
	conn = sqlite3.connect("database.db")
	cur = conn.cursor()
	res = cur.execute(f"SELECT html FROM pages WHERE url='{url}'")
	fetch_list = res.fetchone()
	if fetch_list is None:
		return { "status": "fail", "result": "no data" }
	return { "status": "success", "result": fetch_list[0] }


if __name__ == '__main__':
    deploy_page("https://cha3in.notion.site/12-30-d39c78695d6e4609931d7d2f5aa386dd")