from characters import characters
from houses import houses

# Create a histogram of the houses (it's the "allegiances" key)
def histogram_maker(character_list):

# a dictionary to hold our results
    result_dict = {}
    keys = range(1,445)

    # Create a key for each house. Using the number representing each house.
    for i in keys:
        result_dict[str(i)] = 0

    # for each dictionary in characters.
    for ea_dict in character_list:

        # Sort through all the characters with valid allegiances (some have no allegiances)
        if len(ea_dict["allegiances"]) > 0: 
            
            # We will now sort through each allegiance http link(string).
            for each_str in ea_dict["allegiances"]:

                # each time we sort through a new http link(string), 
                # we reset our new_var
                new_var = ''

                # each character starting from the end of the string (http link) 
                # working backwards.
                for each_char in each_str[len(each_str) - 1:len(each_str) - 5: -1]:
                    
                    # if each character is a number
                    if each_char in "1234567890":
                        
                        # add it to the beginning of our new_var.
                        new_var = each_char + new_var
                    else:
                        
                        # if a character is not a number, 
                        # add 1 to the key representing the allegiance of new_var
                        result_dict[new_var] += 1
                # loop through the next string(http link)
    # create a dictionary for our final results
    final_dict = {}
    link = 'https://www.anapioficeandfire.com/api/houses/'
    # for each number that represents each house
    for i in keys:
        # add the name of that house to the key in our final dictionary
        #  and the value of how many people are in that house
        final_dict[houses[link + "%s" % i]] = result_dict[str(i)]
    return(final_dict)

# a small function - to print our results on seperate lines.
def pretty_print_histogram(histogram):
    for house in histogram:
        print("%s has %d members" % (house, histogram[house]))

print(pretty_print_histogram(histogram_maker(characters)))