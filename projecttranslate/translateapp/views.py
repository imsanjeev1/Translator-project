from django.shortcuts import render
from googletrans import Translator
# Create your views here.

def translator(request):

    return render(request,'page.html')

def translated(request):
    # import pdb
    # pdb.set_trace()
    # import sys
    # sys.path.append("C:\Program Files\JetBrains\PyCharm 2017.2.3\debug-eggs")
    # import pydevd
    # pydevd.settrace('localhost', port=6089, stdoutToServer=True, stderrToServer=True)
    text = request.GET.get("text")
    lang = request.GET.get("lang")
    print("TEXT>>", text, "Language>>>>>>>>", lang)
    translator = Translator()
    dt=translator.detect(text)
    dt2=dt.language
    trans = translator.translate(text,lang)
    tr=trans.text
    return render(request,'translate.html',{'trans':tr,'u_lang':dt2,'t_lang':lang})