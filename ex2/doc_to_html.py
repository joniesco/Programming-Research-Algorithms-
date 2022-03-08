import sys
from io import StringIO
import os
""" this module gets a module as input and writing the module's description to a html file called mydoc.html """

if __name__ == '__main__':
    """To run an example run the command :python doc_to_html.py mymodule.py mydoc.html
and it will write the description of the module "mymodule.py"  which contains some simple math operations  into a html file called mydoc.html """


    # check number of args there should be exactly 3
    if (len(sys.argv) != 3):
        raise Exception("bad arguments")




    # import module
    mod = sys.argv[1].split('.')[0]   # we import module and not module.py
    eval("exec('import '+mod+' as mymod')")

    # open file for writing
    f = open(sys.argv[2], "w") # opening a file called mydoc.html
    # some html settings
    f.write("<html>\n")
    f.write("<body>\n")
    f.write("<h1>"+mod+"</h1>\n")
    # f.write("<h2>" + "Module homerworkmodule:" + "</h2>\n")

    for x in dir(mymod):
        if "__" not in x:  # we don't need the defaults in dir
            old_stdout = sys.stdout         # tooked from https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-into-some-sort-of-string-buffer
            sys.stdout = mystdout = StringIO()
            eval("exec('help(mymod.'+x+')')") # help will give us the required description
            sys.stdout = old_stdout
            message = mystdout.getvalue()

            f.write("<p>"+message+"</p>\n")

    # close file
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()