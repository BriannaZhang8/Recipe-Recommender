Pantry Pal

Purpose: Fresh produce often goes bad easily. Therefore, it is important for you to use your fresh ingredients in a timely manner. Pantry Pal makes searching for a recipe that uses a combination of those ingredients quick and easy.

Description: This program recommends recipes based on the ingredients that you currently have in you pantry. The program takes in user-input ingredients and outputs the top five recipes that best match the ingredient list.

Libraries:
The program uses the Pandas library to read the CSV dataset, create a data frame, and extract recipe information (titles, ingredients, links).
The unittest library is also used for testing.

Installation: 
- Download the RecipeRecommender.py file. 
- Download the dataset by visiting https://recipenlg.cs.put.poznan.pl/ and selecting "Download RecipeNLG dataset." The dataset used contains information on 2,231,142 different recipes.
    - Modify the text within the single quotes in line 232 of the project code to match the directory your recipe dataset is downloaded in
    - You may also change the number of recipes loaded in from the dataset. The default number of recipes is 10,000. Keep in mind that the runtime of the program will change depending on how much you increase or decrease the number.

Execution:
Run the program code. After the greeting message prints, there may be a few seconds of delay while the recommender loads in the data. Afterwards, it will prompt the user to input a list of ingredients. Follow the instructions in the printed messages. For example:

- User Input: powdered sugar, butter, peanut butter, paraffin, chocolate chip
- Output is: Buckeye Candy, …
- User Input: yes
- User Input: beef, tomato juice, oats, egg, onion, pepper, salt
- Output is: Bullets, Prize Winning Meat Loaf, …

Acknowledgements:
- RecipeNLG


