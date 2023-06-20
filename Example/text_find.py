"""
    returns substring between two given markers
"""


i = text.find(begin) + 1
j = text.find(end, i)
return text[i:j]


return text[text.index(start)+1:text.index(end)]

between_markers = lambda t, b, e, f=lambda x,y: x.find(y): t[f(t,b)+1:f(t,e)]
