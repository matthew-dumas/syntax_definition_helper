========================
Syntax Definition Helper
========================

This plug-in contains two tools to aid in the creation of basic syntax definition files.


The Problem
===========

Working with P-List and JSON files can be annoying when attempting to deal with syntax definitions. Furthermore, not looking directly at a file of the syntax definition type you're creating can cause you to miss tokens. Even further than that, people don't seem to understand regular expressions well enough to make basic regular expressions. 

For these reasons, and extreme laziness on my part, I made these tools. The Syntax Definition Helper creates a new syntax definition based on user input while the user is staring at a file that contains no syntax highlighting. It creates very basic regular expressions based off of the selected text, and allows the user to choose a scope and a comment, as well as edit the regular expression for that token. 

The syntax definition edit helper opens up the current syntax defintion, and allows the user to add basic patterns to the definition in exactly the same way as the Syntax Definition Helper. 


Getting Started
===============

- Install
	-> Install from the Package Manager
    -> Install by copying the package to your packages directory

	installation by hand: http://sublimetext.info/docs/extensibility/packages.html#installation-of-packages-with-sublime-package-archives

Once installed:
	
	Press ALT-CTRL-6 to start the Syntax Definition Helper Wizard
	Press ALT-CTRL-7 to start the Syntax Definition Edit Helper Wizard

Alternatively, you can define a new key binding for this command.

How to Use
==========

Create A Syntax Definition
--------------------------
	1. Open a file that doesn't contain a syntax definition
	2. Press ALT-CTRL-6
	3. Type "yes" and hit enter
	4. Type the file extensions this will apply to (Ex: .asm .txt .x86) and hit enter
	5. Give the language a name and hit enter.
	6. Press Enter or enter your own UUID
	7. Name the language root scope. This should be something followed by the file extension. (Ex: For XML I would enter Text.XML)
	8. Select a group of tokens (for example, command tokens -- if end last next continue for while loop do) then click into the dialog entry box and hit enter
	9. Edit the regex and hit enter.
	10. Add a comment to the group, describing it (ex: Control Tokens), and hit enter.
	11. Choose a named scope from the default color scheme list (ex: comment.py), and change the final extension to the extension you used for the root scope. (xml ex: comment.xml)
	12. Repeat 8-11 until you run out of groups or tokens to colorize. 
	13. Enter "no" at the token prompt and hit enter. 
	14. Wait for Sublime Text 2 to save and reload syntax definitions. 
	15. Set the syntax to your new syntax defintion and observer the colors.

Edit A Syntax Definition
------------------------
	1. Verify that the syntax in the file you're planning on editing is set to the correct syntax.
	2. Press ALT-CTRL-7
	3. Press Enter
	4. Perform the steps 8-15 from the above set of instructions.

Clicking into the text edit area in the dialog and pressing escape will cancel the entire process at any time. If you change your mind, and decide to not make the changes, then do this.
