# ---Breakdown Pseudo Code---
# Get User Input (String)
# Covert String Into Indexable List
# Determine length of list and find its nearest whole square root (this determines the dimensions of the caesar box)
# Add a filler character onto imperfectly square rootable messages until its length is perfectly squarable
# Split the now perfectly square rootable message into n groups (n is the message length square rooted)
# Take the first character from each group and add them to a string which is then placed in a list
# Repeat previous step with the second character in each group, then third, etc, till you have n number of box rows
# combine each of the box rows into one string, and print the final Encrypted Message to the user
# ---End Breakdown Pseudo Code---
import math


# Functions

def round_up(n, decimals=0):  # Rounds a float to the highest and nearest whole integer
    multiplier = 10 ** decimals  # Calculated amount to move decimal the right (default 0) Ex: 130.291 becomes 130291.0
    return math.ceil(n * multiplier) / multiplier  # moves decimal over, converts to whole int, then moves decimal back


# End Functions


original_message = list(str(input("Input Your Message: ")))  # Get String and convert to list

split_amount = int(round_up(math.sqrt(len(original_message))))  # Finds nearest (round up) perfect square for original_message

lines = []  # Stores each line of the caesar box
-
encrypted_message = ""  # final string of encrypted message to be returned to the user

for i in range(((split_amount * split_amount) - (len(original_message)))):
    #  Finds difference between closest perfect square and the current message length
    #  For every missing character, add a(n) | to the end of the final message until message length = perfect square
    original_message.append('|')

for i in range(split_amount):
    lines.append(''.join(original_message[(i * split_amount):(i * split_amount) + split_amount]))
    # Repeating for the dimensions of the box (n), split the message into n number of groups, then add them to a list

for j in range(split_amount):
    # repeating for the number of characters in a row
    for k in range(len(lines)):
        # repeating for the total amount of rows
        encrypted_message = encrypted_message + str(lines[k][j])
        # add the first character from each row, then the second character from each row, then third etc...

print(encrypted_message)

# Note: an issue with this cypher is that with a final message such as 'hoee|eurr|y  e| ot!|yvh||' an new line can be
# Created at every filler (in this case the | symbol) and the message will be revealed. Allowing the cracker to skip the
# Step of having to find the Square Root of the Message and the length. Not a massive flaw, but still a flaw nonetheless
# Ex. hoee|eurr|y  e| ot!|yvh|| turns into
# hoee|
# eurr|
# y  e|
#  ot!|
#  yvh|
#     |
# Notice how the right side is filled with fillers. Easy way to split it up if you know the trick. Feature or flaw?
