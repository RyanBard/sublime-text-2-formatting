# Backup of my Sublime Text 2 scripts

This is heavily inspired from:

* https://twigstechtips.blogspot.com/2014/06/sublime-text-automatically-pretty.html
* https://github.com/twig/twigstechtips-snippets

Paraphrased steps from the blog:

* In ST, go to Preferences -> Browse Packages
* Navigate into the User directory (on my Linux box it is `~/.config/sublime-text-2/Packages/User`)
* Drop the [format_json.py](format_json.py) and [format_xml.py](format_xml.py) files into that directory
* Create/modify [Main.sublime-menu](Main.sublime-menu) file to have the Format option under Selection
* Create/modify the [Default (YourOs).sublime-keymap](Default (Linux).sublime-keymap) file(s) to have the `format_json` and `format_xml` commands
* Double check that the pyc file was created and is a later timestamp than your source files
* Test formating with both the menu under Selection -> Format and the keymap you chose (ctrl+shift+j / ctrl+shift+x in my files)
* Profit
