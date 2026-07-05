# doc-decoder
<i>Take a specifically-formatted Google Doc of x,y coordinates tied to an ASCII character and prints the ASCII characters on a grid, ideally making art.</i>

This project was created for a specific context. A user would have a Google Doc that contained one table with a header.
This table has an x-coordinate as a positive integer, a single ASCII character like ▓ or █, and a y-coordinate as a positive integer.
The program is designed to take a shared link to the Google Doc, scrape the document for its table, turn the table into a dict of coords:chars, and then print a grid of the characters (or a space when none is provided).
With ideal input, this program can print ASCII art that's stored in a table. The specific use for this project was to display the block characters of a hidden message.

<u>What could be done better?</u>
First off, there is zero work in catching errors.
<ul>
  <li>The code will break if it receives a doc with a table in any format other than [int], [char], [int].</li>
  <li>I have no idea what'll happen if the table contains extra columns. It may still work, it may break.</li>
  <li>What happens if there are multiple tables in the doc?</li>
  <li>Proper error handling can easily be put in place to catch errors in the link.</li>
  <li>What happens if there are multiple characters in one coord? If both are printed, this won't be an error but it'll misalign the print.</li>
</ul>
Now, some features that'll make the program "feel" more complete.
<ul>
  <li>An input loop for users to provide a link. Loop back to input when one of the above errors kicks back.</li>
  <li>Some better handling of the loop - it's supposed to handle arbitrarily-large grids, but eventually the program will be unweildy or impossible to execute if (1000001, 2^128+1) is assigned.</li>
</ul>

## table_maker
<i>Take the document and make it useable.</i>

This function takes input in the form of the link to the Google Doc.
It looks in the document for a table, and assigns that table to a placeholder to be worked.
The table placeholder is parsed such that each row is turned into an array, and then each row array is put into the return's array.
After this function, the table is broken down like [[1, █, 1], [2, █, 1],...]


## crypto_sorter
<i>Sort the array.</i>

This function takes an array as input and returns the array sorted in ascending order.
Note: This function is never called in the final main() call - it's entirely redundant and doesn't appear useful in execution or efficiency.

## message_printer
<i>Print the final art/message.</i>

This function first removes the header from the table and then determines the max-size of the grid.
The function then creates the dict of (x,y):char to be printed.
The function then goes through each row to be printed and prints the specified character per row. If the printhead is on a coordinate with no assigned char in the dict, it will print a space.
