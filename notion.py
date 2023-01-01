from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import multiprocessing as mp

def worker(url):
	conn = sqlite3.connect("database.db")
	cur = conn.cursor()

	key_str = ".notion.site/"
	key_index = url.find(key_str)
	if key_index == -1:
		return

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
	sql = '''UPDATE pages SET html = ? WHERE url = ?'''
	cur.execute(sql, (html, url))
	conn.commit()
	conn.close()
	print("child process end")

def get_page(url):
	key_str = ".notion.site/"
	key_index = url.find(key_str)
	if key_index == -1:
		return { "status": "fail", "result": "wrong url input" }
	
	conn = sqlite3.connect("database.db")
	cur = conn.cursor()
	res = cur.execute(f"SELECT html FROM pages WHERE url='{url}'")
	html = res.fetchone()

	if html is None:
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

		sql = '''INSERT INTO pages (url, html) VALUES (?,?)'''
		cur.execute(sql, (url, html))
		conn.commit()
		conn.close()
		
		data = {
			"result": "success",
			"html": html
			}
		return data
		
	else:
		p = mp.Process(name="SubProcess", target=worker, args=(url,), daemon=True)
		p.start()
		data = {
			"result": "success",
			"html": html[0]
			}
		return data

	# proc = mp.current_process()
	# print(proc.name)
	# print(proc.pid)

	# options = webdriver.ChromeOptions()
	# options.add_argument("headless")
	# browser = webdriver.Chrome("chromedriver", options=options)
	# browser.get(url)
	# wait = WebDriverWait(browser, 30)
	# content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'notion-page-content')))
	# html = content.get_attribute('innerHTML')
	# browser.quit()

	# f = open("./example", 'w')
	# f.write(html)
	# f.close()
	
	# # html = ""
	# # f = open("./example", 'r')
	# # while True:
	# # 	line = f.readline()
	# # 	if not line: break
	# # 	html += line
	# # f.close()
	
	# main_url = url[:key_index + len(key_str) - 1]
	# html = html.replace('src="/image', f'src="{main_url}/image')
	# html = f'''
	# <!DOCTYPE html>
	# <html lang="en">
	# <head>
	# 	<meta charset="UTF-8">
	# 	<title>NOTION GOD</title>
	# 	<link rel="preconnect" href="https://fonts.googleapis.com">
	# 	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	# 	<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
	# 	<link rel="stylesheet" href="/static/css/style.css">
	# </head>
	# <body>
	# 	<div id="god"></div>
	# 	<div id="notion" style="display:none">
	# 		{html}
	# 	</div>
	# 	<script defer src="/static/js/page.js"></script>
	# </body>
	# </html>
	# '''
	
	# ### gif 처리하는 방법 찾기 ###
	
	# data = {
	# 	"result": "success",
	# 	"html": html
	# 	}
	
	# return data

if __name__ == '__main__':
    get_page("https://cha3in.notion.site/12-30-d39c78695d6e4609931d7d2f5aa386dd")