import pandas as pd
import unittest


class TestPantryPal(unittest.TestCase):
    """Unit tests for the functions defined in PantryPal.py."""

    def test_insertion(self):
        """test insertion of rb-bst"""
        rb_tree = RBTree()

        # Insert various ingredients
        rb_tree.insert("salt")
        rb_tree.insert("pepper")
        rb_tree.insert("sugar")
        rb_tree.insert("flour")

        # Perform assertions to check if the tree structure is correct
        assert rb_tree.root.val == "salt"
        assert rb_tree.root.right.val == "sugar"
        assert rb_tree.root.left.val == "pepper"
        assert rb_tree.root.left.left.val == "flour"

    def test_search_substring(self):
        """test search substring function"""
        rb_tree = RBTree()

        # Insert various ingredients
        rb_tree.insert("salt")
        rb_tree.insert("pepper")
        rb_tree.insert("sugar")
        rb_tree.insert("flour")

        # Search for a substring
        search_result = rb_tree.search_substring("pep")

        # Ensure the search result matches the expected ingredient(s)
        assert search_result == "pepper"


    def test_search_recipes(self):
        """test search recipes method"""
        # Define a sample ingredient dictionary
        ingredient_dict = {
            "Recipe 1": ["tomato", "onion", "garlic", "pasta"],
            "Recipe 2": ["chicken", "garlic", "ginger", "soy sauce"],
            "Recipe 3": ["potato", "garlic", "onion", "cream"],
            "Recipe 4": ["eggplant", "tomato", "onion", "garlic"],
            "Recipe 5": ["rice", "carrot", "peas", "leeks"], 
            "Recipe 6": ["blueberry", "sugar", "mango", "salt"],
            "Recipe 7": ["butter", "oil", "parsley", "pepper"],
            "Recipe 8": ["brown sugar", "wheat", "pumpkin", "cinnamon"],
            "Recipe 9": ["eggplant", "flour", "oil", "basil"],
            "Recipe 10": ["rice", "carrot", "peas", "onion"]
        }

        # Define different sets of user ingredients
        user_ingredients_1 = ["onion", "tomato", "garlic"]

        # Test for different sets of user ingredients
        result_1 = search_recipes(ingredient_dict, user_ingredients_1)
        assert result_1 == ['Recipe 1', 'Recipe 4', 'Recipe 3', 'Recipe 2', 'Recipe 10']  # Expected result for user_ingredients_1


class RBNode:
    """Initializes nodes of the red-black tree"""
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    """Initializes a red-black tree, including a depth-first search method to search the tree's data"""
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)
    
    #dfs implementation to search ingredients
    def search_substring(self, substring):
        return self._search_substring_helper(self.root, substring)

    def _search_substring_helper(self, node, substring):
        if node == self.nil:
            return None

        # Check if the substring is present in the current node's value
        if substring in node.val:
            return node.val

        # Recursively search in the left and right subtrees
        left_result = self._search_substring_helper(node.left, substring)
        right_result = self._search_substring_helper(node.right, substring)

        # Return the result if found in either subtree
        if left_result:
            return left_result
        elif right_result:
            return right_result
        else:
            return None
        

def print_tree(node, lines, level = 0):
    """Prints red-black tree visualization"""
    if node != None:
        print_tree(node.left, lines, level + 1)
        print(' ' * 4 * level + '->', node.val,
              ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)


def create_ingredient_bst():
    """Creates red-black bst using ingredients from the recipe dataset."""
    recipe_df = pd.read_csv('CHANGE THIS TEXT TO THE PATH TO YOUR DATASET/full_dataset.csv', nrows=10000)
    title_list = recipe_df['title'].tolist()
    draft_ingredient_list = recipe_df['ingredients'].tolist()
    ingredient_list = []
    for lst in draft_ingredient_list:
        ingredient_list.append(lst)
        words = lst.split(', ')
        for i in words:
            if i not in ingredient_list:
                ingredient_list.append(i)

    link_list = recipe_df['link'].tolist()
    filtered_ingredient_list = []
    
    #create red-black tree, inserting ingredients as nodes
    ingredient_tree = RBTree()

    for ingredient in ingredient_list:
        if '. ' in ingredient:
            ingredient = ingredient.split('. ', 1)[1]
        if ', ' in ingredient:
            ingredient = ingredient.split(', ', 1)[0]
        ingredient = ingredient.strip("\'()\"[].")
        filtered_ingredient_list.append(ingredient.strip())

    for ingredient in sorted(filtered_ingredient_list):
        ingredient_tree.insert(ingredient)

    #create ingredient dictionary using recipe titles as keys and ingredients lists as values
    ingredient_dict = {title_list[i]: draft_ingredient_list[i] for i in range(len(title_list))}
    #create dictionary using recipe title as key and recipe link as value
    link_dict = {title_list[i].strip(): link_list[i] for i in range(len(title_list))}

    return ingredient_tree, ingredient_dict, link_dict
    
def search_recipes(ingredient_dict, new_user_ingredients):
    """Return five recipes with the highest match level to the input ingredient list."""
    match_level = {}
    for recipe in ingredient_dict:
        count = 0
        #linear search algorithm that updates counter when the user ingredient is found in a recipe ingredient list
        for ingredient in new_user_ingredients:
            if ingredient in ingredient_dict[recipe]:
                count += 1
        #divide count of matched ingredients by the number of ingredients in each recipe to get match levels and add to dictionary.
        match_level[recipe.strip()] = count / len(ingredient_dict[recipe])
    #get top five matches from match_level dictionary
    result = sorted(match_level, key = match_level.get, reverse = True)[:5]
    return result


if __name__ == '__main__':

    #testing commented out
    #unittest.main()

    WELCOME_MESSAGE = "Hey there! Welcome to PantryPal, your kitchen companion! I'm super excited to assist you in discovering delicious recipes based on the foods hanging out in your pantry. We'll serve up a recipe that contains many of the ingredients you already have!"
    CONTINUING_MESSAGE = "Ready for some culinary adventures? Type 'Yes' to keep the tasty train rolling! If you've had your fill, just type 'No' to exit: "
    INSTRUCTIONS = "Let's whip up some kitchen magic! Drop in the ingredients you've got, using commas to separate each ingredient (ex: milk, sugar, egg). Tell me what's in your culinary treasure trove and let the deliciousness begin: "
    GOODBYE_MESSAGE = "You're all set! Thanks you for hanging out with PantryPal. Until next time, happy cooking!"

    #request user input
    print(WELCOME_MESSAGE)

    #initialize ingredient binary tree
    ingredient_tree, ingredient_dict, link_dict = create_ingredient_bst()

    #loop program until user replies "no"
    continuing_user = "yes"

    while continuing_user == "yes":
        print()
        ingredient_input = input(INSTRUCTIONS)
        while not ingredient_input:
            ingredient_input = input("No input. Please try again: ")

        lower_ingredients = ingredient_input.lower()
        ingredient_list = lower_ingredients.split(", ")
        user_ingredients = sorted(ingredient_list)
        result = search_recipes(ingredient_dict, user_ingredients)

        count = 1
        for recipe in result:
            print()
            link = link_dict[recipe]
            print(str(count) + '. ' + str(recipe) + ': ' + link)
            count += 1

        print()

        #ask if user would like to continue with the program
        continuing_user = input(CONTINUING_MESSAGE)
        continuing_user = continuing_user.lower().strip()

        while continuing_user != "yes" and continuing_user != "no":
            continuing_user = input("Invalid input. Please reply with 'Yes' or 'No': ")
            continuing_user = continuing_user.lower().strip()

    #print goodbye message, end program
    print()
    print(GOODBYE_MESSAGE)

