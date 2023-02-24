from django.shortcuts import render

def indexPage(request):
   context={"breadcrumb":{"parent":"Dashboard","child":"Stater-kit"}}
   return render(request,'general/index.html',context)

def index2(request):
   context={"breadcrumb":{"parent":"Dashboard","child":"Dashboard"}}
   return render(request,'default/index2.html',context)


