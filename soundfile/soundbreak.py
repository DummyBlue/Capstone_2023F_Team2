Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('hello, python')
hello, python
>>> import librosa
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import librosa
ModuleNotFoundError: No module named 'librosa'
>>> import librosa
>>> import os
... 
... # 현재 스크립트의 전체 경로를 얻음
... script_path = os.path.realpath(__file__)
... print("스크립트의 전체 경로:", script_path)
... 
... # 현재 스크립트가 있는 디렉토리만 얻음
... directory = os.path.dirname(script_path)
... print("스크립트의 디렉토리:", directory)
SyntaxError: multiple statements found while compiling a single statement
>>> import os
... 
... # 현재 스크립트의 전체 경로를 얻음
... script_path = os.path.realpath(__file__)
... print("스크립트의 전체 경로:", script_path)
... 
SyntaxError: multiple statements found while compiling a single statement
