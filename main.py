from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ask = input('What item?\n')

path = './chromedriver'
driver = webdriver.Chrome(path)
driver.get(f'https://www.amazon.com/s?k={ask}&ref=nb_sb_noss_2')
assert 'Amazon' in driver.title

boxes = driver.find_element_by_class_name('s-main-slot')

f = open('amazontranscript.txt','w+')
# f.write(boxes.text)

costs = []

textlines = boxes.text.split('\n')
for ind, i in enumerate(textlines):
    if ind == len(textlines) -2:
        break
    else:
        if i[0] == '$' and textlines[ind+1].isnumeric():
            costs.append(i[1:] + textlines[ind+1])

for i in costs:
    print(f'${i[:-2]}.{i[-2:]}')

driver.close()
