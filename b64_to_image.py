#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-15 09:10:15
# @Author  : xuetu


import base64

data = '''
	"R0lGODdhkAFYAIcAAPn5+VVVVejo6NbW1nR0dJeXl4aGhmNjY8XFxaioqLm5uWtra8vLy7Ozs3x8\nfOLi4qKiooyMjNzc3J2dnZCQkNDQ0K6urnx8fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAkAFYAEAI/wABCBxI\nsKDBgwgTKlzIsKHDhxAjSpxIsaLFixgzatzIsaPHjyBDihxJsqTJkyhTqlzJ8mQDAgUGAJhJs6bN\nmzhz6tzJs6fPn0CDCh1KtKhRnQIaFAgQgICDAAUQAJhKtarVq1izat3KtavXr2DDai0QoGyABg8G\n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\nXNnyZcyZNW/m3NnzZ9CPAwIAOw==\n
'''
image = base64.b64decode(data)
fi = open("/home/hacker/pythonts/im.gif","wb")
fi.write(image)
fi.close()

