# ASCII-ART
This Python code implements a program that allows users to perform various operations related to ASCII art and Run-Length Encoding (RLE). Here's a description of what the code does:

Menu Display:

It presents a menu to the user with the following options:
Enter RLE: Allows the user to input RLE compressed data.
Display ASCII art: Displays ASCII art stored in a text file.
Convert to ASCII art: Converts RLE compressed data to ASCII art.
Convert to RLE: Converts ASCII art to RLE compressed data.
Quit: Exits the program.

Enter RLE:

Asks the user to input the number of lines of RLE compressed data they want to enter.
Validates that the number of lines is greater than 2.
Accepts compressed data input for each line.
Decompresses the RLE data (placeholder logic) and displays the decompressed ASCII art.

Display ASCII art:

Asks the user to enter the name of the text file containing ASCII art.
Attempts to read the ASCII art from the specified file.
If successful, prints the ASCII art to the console.
Convert to ASCII art:

Asks the user to enter the name of the text file containing RLE compressed data.
Attempts to read the RLE data from the specified file.
Decompresses the RLE data (placeholder logic) and displays the decompressed ASCII art.

Convert to RLE:

Asks the user to enter the name of the text file containing ASCII art.
Attempts to read the ASCII art from the specified file.
Compresses the ASCII art to RLE format (placeholder logic).
Calculates the difference in characters between the compressed and uncompressed versions of the ASCII art.
Writes the compressed data to a new file.

Main Function:

Provides a loop to continuously display the menu and handle user input until the user chooses to quit.

Replit: https://replit.com/@Hei-ChitChit/ASCII-Art#main.py
