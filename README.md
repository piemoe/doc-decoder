# doc-decoder
<i>Take a specifically-formatted Google Doc of x,y coordinates tied to an ASCII character and prints the ASCII characters on a grid, ideally making art.</i>

This project was created for a specific context. A user would have a Google Doc that contained one table with a header.
This table has an x-coordinate as a positive integer, a single ASCII character like ▓ or █, and a y-coordinate as a positive integer.
The program is designed to take a shared link to the Google Doc, scrape the document for its table, turn the table into a dict of coords:chars, and then print a grid of the characters (or a space when none is provided).
With ideal input, this program can print ASCII art that's stored in a table. The specific use for this project was to display the block characters of a hidden message.
