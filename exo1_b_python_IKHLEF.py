# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TQOJ48EL23NkGrfMcg5xxowf-9F7SFtg

1.b Factorielle :
"""

def factorielle(x):
  x = int(input())
  if x == 0:
    return 1
  else : 
    f = 1
    for n in range(2,x+1):
      f = f*n
    return f;

factorielle(x)