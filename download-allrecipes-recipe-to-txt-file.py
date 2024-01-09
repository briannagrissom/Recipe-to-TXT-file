
import requests
from scrapy import Selector

link= input('Allrecipes Link:' )
name= input('Item you are making: ')

# Get the HTML
html= requests.get(f'{link}').text

# Initiate selector
selector= Selector(text=html)

# Extract the heading
heading= selector.xpath('//h2[@id="mntl-structured-ingredients__heading_1-0"]//text()').extract_first()

# Extract the ingredients
ingredients= selector.xpath('//p/span//text()').extract()

# Extract the second heading
heading2= selector.xpath('//h2[@class="comp recipe__steps-heading mntl-text-block"]/text()').extract_first() # directions

# Append the steps of the recipe to a list
n= 1
steps= []
for i in range(20):
    directions= selector.xpath(f'//p[@id="mntl-sc-block_2-0-{n}"]//text()').extract()
    if directions != []:
        steps.append(directions[0])
    n= n + 1

# Initiate new txt file and write the headings, ingredients, and the steps to it
with open(f'{name} Recipe','w') as file:
    file.write(f'{heading}\n')
    file.write('\n')
    
    for each in ingredients:
        file.write(f'{each}\n')
    
    file.write(f'{heading2}')
    file.write('\n')
    file.write('\n')
    for step in steps:
        file.write(f'{step}\n')
        
        
        
