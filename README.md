## Final Project ST0270-1587
### Made by: Pablo Moreno Quintero
---
## Development Environment
- Operating System: Windows 10 Home v22H2
- Programming language: Python 3.10.6
- Tools used: No external libraries where used

---
## Use instructions
---
#### 1. Preliminary configurations
Make sure you have Python latest version (check in your command prompt)
```bash
python 
```
This command should return something like this:
```
Python 3.10.6 (<tags>, <installation date>) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
Make sure you have git installed
```bash
git --version
```
This command should return something like this:
```
git version 2.35.1.windows.2
```
---
#### 2. To download the code to your machine
Select the route where you want the repository to be downloaded
```bash
cd <Route to your especified file>
```
Then download the repository
```bash
git clone https://github.com/PabloMorenoEAFIT/Final_compi_PMQ/blob/main/README.md
```
Acces the route where the file was downloaded
```bash
cd <Final_compi_PMQ>
```
---
#### 3. To run the program
As the programm doesn't require any external libraries you can run the program with  the following command in your command prompt
```bash
py final-project-PMQ.py
```
---
#### 4. To use the program
When you run the program, it will wait for input from the user. The program processes context-free grammar (CFG) and computes the First and Follow sets for all nonterminal symbols in the grammar.
Sample Input:
```
1
2
S AS A
A a
```

Sample Output:
```
First(A) = { a }
First(S) = { a }
Follow(A) = { $ , a }
Follow(S) = { $ }
```

---
## Program Functionality
This Python program is designed to compute the First and Follow sets of all nonterminal symbols for a given context-free grammar (CFG). These sets are crucial for constructing parsers in compiler design, particularly for LL(1) parsers.

## Key Functions
*parse_input():*
- Purpose: Reads the grammar input from the user.
- How it works: The function parses the input grammar, processes the number of test cases, and extracts the nonterminals and their corresponding derivations.

*compute_first():*
- Purpose: Computes the First sets for each nonterminal.
- How it works: For each nonterminal, the function looks at its production rules. It adds the first terminal symbol from each production to the First set of the nonterminal. If a production can derive the empty string (e), then the First set of the nonterminal includes the symbols of any other nonterminal that it can derive.

*compute_follow():*
- Purpose: Computes the Follow sets for each nonterminal.
- How it works: The Follow set of a nonterminal includes the terminal symbols that can appear immediately to the right of the nonterminal in any sentential form derivable from the start symbol. If a nonterminal can derive the empty string (e), the Follow set includes the Follow set of the nonterminal on the left-hand side of its production.

*print_sets():*
- Purpose: Displays the First and Follow sets for each nonterminal.
- How it works: This function formats and prints the computed sets in a readable form for the user.
