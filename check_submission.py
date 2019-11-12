#!/usr/bin/python 

"""
Check a coursework submission for
1. correctly filled header
2. sympy syntax.

$Id: check_submission.py 881 2017-05-22 16:15:42Z ag0015
"""

from sympy import *
import operator

import sys
import re

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
import string


def get_form_data(filename):
    """ 
    extract form contents of PDF file as a dict of key-value pairs. Based
    on code by Steven from Belgium at 
    http://stackoverflow.com/questions/3984003/how-to-extract-pdf-fields-from-a-filled-out-form-in-python
    """

    fp = open(filename, "rb")
    parser = PDFParser(fp)
    doc = PDFDocument(parser)

    data = {}
    
    fields = resolve1(doc.catalog['AcroForm'])['Fields']
    for i in fields:
        field = resolve1(i)
        data[field.get('T')] = "".join(filter(lambda x: x in string.printable, str(field.get('V'))))
    return data

def check_header(form, fb):
   """ 
   check the form data extraced from the pdf for correctness. Put
   any textual feedback into stream fb and return URN, lastname and forename.
   Check in particular:
   1. has the most recently available version of the PDF form been
   used?
   2. Have firstname, lastname and URN been provided?
   3. Has the originality declariation been ticked?
   """

   if(1220 < 1220) :
      print >>fb, "Warning: Your coursework form is not the most recent. " \
      + "Visit SurreyLearn and download the most " \
      + "recent version of the coursework. Check for changes and " \
      + "updates to the questions which might have impact on your answers." 

   if(len(form["firstname"]) < 2) :
      print >> fb, "Warning: You did not enter your first name."
      #form["firstname"] = "???"

   if(len(form["lastname"]) < 2) :
      print >>fb,  "Warning: You did not enter your last name."
      #form["lastname"] = "???"
      
   if len(form["URN"]) != 7 or not form["URN"].isdigit() or int(form["URN"]) < 6000000 :
      print >>fb,  "Error: You did not provide a valid URN."
      # add a regular expression here.
      #form["URN"] = "xxxxxxx"

   print >>fb,  "Originality box shows: " + form["originality"]
   if form["originality"] not in ("'/Yes'", "/Yes", "/Oui", "/Ja", "/Ano", "/'Yes'") :
       print >>fb,  "Error: You did not confirm the originality declaration."
       print >>fb,  "Error: I cannot accept submissions without the confirmation."
       del form["originality"]

   if "dummy" in form.keys() :
       del form["dummy"] # ignore dummy

   return form["URN"], form["lastname"], form["firstname"]


def get_fieldnames(filename) :
    """ 
    get list of fieldnames produced by latex while compiling
    coursework.tex 
    """
    return [line.rstrip('\n') for line in open(filename)]

def check_completeness(form, fb) :
    """ 
    check whether fieldnames from the latex file have a nonnull answer. 
    @Todo: change so that it does not need to read textfields
    """
    
    fields = get_fieldnames("cw_textfields.txt")

    for field in fields :
        if field not in form or form[field] == None or form[field].strip() == "" :
            print >>fb, ("Warning: You did not submit an answer for {}.").format(field)

def eval_expressions(form, fb) :
    """evaluate all submitted expressions as python types"""

    def check_type(x, fb) :

        if type(x) is type(1) : return True
        if type(x) is type(0.1): return True

        print >> fb, "Error cannot evaluate {} to a number. I remove the whole answer.".format(x)
        return False

    xpr = [key for key in form.keys() if re.match("q", key)]
    for x in xpr :
        if form[x] == "" or form[x] == None:
            print >>fb,  "Info: No reply in field {}. This may or may not be a correct answer for this question.".format(x[1:])
            form[x] = ()
            continue
        elif "=" in form[x] :
            print >>fb,  "Error: Do not include assignments '=' in your expression {}.".format(form[x])
            del form[x]
            continue
        A = 0
        B = 1
        C = 2
        D = 3
        E = 4
        F = 5
        G = 6
        H = 7
        form[x] = eval(form[x])
        if type(form[x]) is type( () ) :
            flag = True
            for t in form[x] :
                flag &= check_type(t, fb)
            if not flag : del form[x]
        else :
            if not check_type(form[x], fb) : del form[x]
        
def check_submission(filename, fb=sys.stdout) :
    """
    execute all available checks and return URN, lastname, and
    forename along with a dict of syntactically valid answers.
    """

    form = get_form_data(filename)
    URN, name, forename = check_header(form, fb)
    # check_completeness(form, fb) # todo: why did I comment it out?
    # Because sympy does the same check implicitly?
    #check_mcq(form) # no mcq in cw COM1033 2018
    #sympify_expressions(form, fb)
    eval_expressions(form, fb)

    return URN, name, forename, form

def formatter(str) :
    """ 
    removes prefix "xpr" from as string
    """
    if str.startswith("xpr") :
       return str[3:]
    return str   

if __name__== "__main__" :

    if len(sys.argv) > 1 :
        filename = sys.argv[1]
    else :
        filename = "coursework_filled3.pdf"

    print "Submission Checker -- Version $Version${}".format("$Id: check_submission.py 1221 2018-11-02 17:49:34Z ag0015 $")
    print "Use as follows:"
    print "python check_submission <your_submission.pdf>\n\n"
        
    URN,name,forename,form = check_submission(filename)    

    print "\nFYI: Valid data extracted from your PDF:"

    print "Submitted by {} {}, {}.".format(forename, name, URN)

    for key in form.keys() :
        # print "Field {}:\nExpression: {}.\nType: {}\nLaTeX: {}\n".format(formatter(key), form[key], type(form[key]), latex(form[key]))
        print "Field {}:\nExpression: {}.\nType: {}\n".format(formatter(key), form[key], type(form[key]))
