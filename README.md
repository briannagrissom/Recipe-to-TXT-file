# Recipe-to-TXT-file
`download-allrecipes-recipe-to-txt-file.py` downloads an Allrecipes recipe to a TXT file.

Includes:

1) User input to specify the Allrecipes URL of choice and the name of the dish.
2) Assigning the HTML for the URL to a Python variable.
3) Using XPATH through a scrapy Selector to extract the recipe's heading and ingredients.
4) Using a for loop to obtain each step of the directions one at a time.
5) Writing the heading, ingredients, and directions to a new TXT file.
