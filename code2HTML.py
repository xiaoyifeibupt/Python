#! /usr/bin/env python

import os

from pygments import highlight
from pygments.lexers import CppLexer
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter

#create my own style
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

#Getting a list of available styles
from pygments.styles import get_all_styles
available_styles = list(get_all_styles())
print available_styles
class XStyle(Style):
    default_style = ""
    styles = {
        Comment:                'italic #888',
        Keyword:                'bold #005',
        Name:                   '#f00',
        Name.Function:          '#0f0',
        Name.Class:             'bold #0f0',
        String:                 'bg:#eee #111'
    }


def generate_html(co, sty, bo):
	return '''
	<html>
		<head>
			<META http-equiv=Content-Type content="text/html; charset=UTF-8">
			<title>%s</title>
			<style type="text/css">
			%s
			</style>
		</head>
		<body>
			<h2>%s</h2>
			%s
		</body>
	</html>	
	''' %(co, sty, co, bo)

FileExistNames = os.listdir('lintcode/')

for codeName in FileExistNames:
	code = open('lintcode/' + codeName, 'r').read()
	
	htmlFile = open('lintcodeHTML/' + codeName + '.html', 'w')

	formatter = HtmlFormatter(encoding='utf-8', style = available_styles[2], linenos = True)
	style = formatter.get_style_defs()
	body = highlight(code, CppLexer(), formatter)
	try:
		htmlFile.writelines(generate_html(codeName, style, body))
	finally:
		htmlFile.close()
