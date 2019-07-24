import requests
import csv
from bs4 import BeautifulSoup

pno_list = {7811611,
			8012515,
			7976828,
			7867948,
			8202545,
			8202906,
			8329230,
			8618050,
			8513456,
			8802163}

def get_index(table):
	info_row = table.find('tr')
	try:
		check_box = info_row.find('th', attrs={"scope":"row", "valign":"top", 'align':"left", 'width':"10%"})
		if check_box.text.strip()=="Inventors:":
			return True
	except Exception:
		return False

def get_info(trow, info):
	check_box = trow.find('th', attrs={"scope":"row", "valign":"top", 'align':"left"})
	try:
		if check_box.text.strip()==info:
			i_name_box = trow.find('td')
			iname = i_name_box.text.strip()
			return iname
		else:
			return ''
	except Exception:
		return ''

patents = []
for pno in pno_list:
	url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=1&p=1&f=G&l=50&d=PTXT&S1={}.PN.&OS=PN/({})&RS=PN/{}'.format(pno, pno, pno)

	headers = {	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

	r = requests.get(url, headers=headers)
	soup = BeautifulSoup(r.text, 'lxml')

	#find title
	title_box = soup.find('font', attrs={'size':'+1'})
	title = title_box.text.strip()
	
	#find abstract
	abs_box = soup.find('p')
	abstract = abs_box.text.strip()

	#find date
	tables = soup.find_all('table', attrs={'width':'100%'})

	inventors = date = assignee = ''
	for i in range(len(tables)):
		check = get_index(tables[i])
		if(check==True):
			break
	
	info_row = tables[i].find_all('tr')

	for row in info_row:
		if inventors == '':
			inventors = get_info(row, 'Inventors:')
		if date == '':
			date = get_info(row, 'Filed:')
		if assignee == '':
			assignee = get_info(row, 'Assignee:')
	
	p = [str(pno), title, abstract, date, inventors, date, assignee]
	patents.append(p)
	
print (patents)
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(patents)
