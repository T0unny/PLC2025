import re

def list1(text):
  a=re.findall(r'(?:(\d+)\. (.*?)\n?)',text)
  for i in range(1,len(a)+1):
    if i == 1:
      text =re.sub(r'(?:1\. (.*))',r'<ol>\n<li>\1</li>', text, count=1)
    elif i == len(a):
      text =re.sub(rf'(?:{len(a)}\. (.*))',r'<li>\1</li>\n</ol>', text, count=1)
    else:
      text = re.sub(rf'(?:{i}\. (.*))',r'<li>\1</li>', text,count=1)
  return text
  
def list2(text):
    result = ""
    i = 0
    for m in re.finditer(r'((?:\d+\. .+(?:\n|$))+)', text):
        result += text[i:m.start()]
        result += list1(m.group(1))
        i = m.end()
    result += text[i:]
    return result

def conv(text):
   er11=re.compile(r'^### (.+)$',re.MULTILINE) 
   text=er11.sub(r'<h3>\1</h3>',text)
   
   er12=re.compile(r'^## (.+)$',re.MULTILINE) 
   text=er12.sub(r'<h2>\1</h2>',text)
   
   er13=re.compile(r'^# (.+)$',re.MULTILINE) 
   text=er13.sub(r'<h1>\1</h1>',text)
   
   er2=re.compile(r'\*\*(.+?)\*\*') 
   text=er2.sub(r'<b>\1</b>',text)
   
   er3=re.compile(r'\*(.+?)\*') 
   text=er3.sub(r'<i>\1</i>',text)
   
   text=list2(text) 
   
   er4=re.compile(r'\!\[(.*?)\]\((.*?)\)') 
   text=er4.sub(r'<img src="\2" alt="\1"/>',text)
   
   er5=re.compile(r'\[(.*?)\]\((.*?)\)') 
   text=er5.sub(r'<a href="\2">\1</a>',text)
  
   return(text)