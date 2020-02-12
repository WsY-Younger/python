f = open('计算器自做哦eval.html','rb')
jsj = f.read()
f.close()




def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    
    return [jsj]




