import pycurl
import thread
from StringIO import StringIO

def request_url(thread_name, start, end):
    buffer = StringIO()

    for x in range(start, end):
        c = pycurl.Curl()
        print(str(thread_name)+"Processando --> "+str(x))
        c.setopt(c.URL, 'http://www.site.com.br/?id='+str(x))
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        f = open('pagina-'+str(x)+'.html','w')
        f.write(body)
        f.close()



try:
    thread.start_new_thread( request_url, ("Thread(1)", 19,8998) )
    thread.start_new_thread( request_url, ("Thread(2)", 8998,17999) )

except:
    print "Error: unable to start thread"

while 1:
    pass

#print(body)
