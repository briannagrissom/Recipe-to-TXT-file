# Recipe-to-TXT-file
Download an Allrecipes recipe to a TXT file.

This involved:

1) Including an input to insert the Allrecipes link of choice and the name of the dish.
2) Assigning the HTML for the link to a Python variable.
3) Using XPATH through a scrapy Selector to extract the recipe's heading and ingredients.
4) Using a for loop to obtain each step of the directions one at a time.
5) Writing the heading, ingredients, and directions to a new TXT file.
