import re, urllib

#print re.split(r'\s*', 'here are some words')
#print re.split(r'(\s*)', 'here are some words')
#print re.split(r'(s*)', 'here are some words')

s = """Aausu3BCuab6SudfgJ
FJKhkdkutkABRju5f"""
# print re.split(r'[a-fA-F]',s)
# print re.split(r'[a-f0-9]',s)

# ## re.I = Ignorecase
# ## re.M = Multiline
# print re.split(r'[a-f]',s)
# print re.split(r'[a-f]',s, flags = re.I|re.M)
# print re.split(r'[a-f][a-f]',s, flags = re.I|re.M)

# ## \d = digit
# ## \D = non-digit
# ## find the longest possible from the fisrt letter
# print re.findall(r'\d', 'finqwekr123 main st.iasmdk1fl') # a digit
# print re.findall(r'\D', 'finqwekr123 main st.iasmdk1fl') # non digit
# print re.findall(r'\d*', 'finqwekr123 main st.iasmdk1fl') # 0 or more digit
# print re.findall(r'\d+', 'finqwekr123 main st.iasmdk1fl') # 1 or more digit
# print re.findall(r'\d?', 'finqwekr123 main st.iasmdk1fl') # 0 or 1 digit
# print re.findall(r'\d{2}', 'finqwekr123 main st.iasmdk1fl') # 2 digit
# print re.findall(r'\d{1,2}', 'finqwekr123 main st.iasmdk1fl') # 1-2 digit

# ## \. = "."
# ## . = anything but newline
# print re.findall(r'\d{1,5}\s\w*\s\w+\.ias', 'finqwekr123 main st.iasmdk1fl') # 1-2 digit

sites = 'facebook google cnn youtube'.split()
pat = re.compile(r'<title>.*</title>', flags = re.I|re.M) #pre compile the reg ex

for s in sites:
	print ('Searching: ' + s)
	u = urllib.urlopen('http://' + s + '.com')
	text = u.read()
	title = re.findall(pat, str(text))
	try: 
		print title[0].replace("<title>", "").replace("</title>", "")
	except:
		pass




