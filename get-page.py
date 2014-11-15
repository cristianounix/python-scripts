import pycurl
import thread
from StringIO import StringIO

def request_url(thread_name, start, end):
    buffer = StringIO()

    for x in range(start, end):
        c = pycurl.Curl()
        print(str(thread_name)+"Processando --> "+str(x))
        c.setopt(c.URL, 'http://www.tudogostoso.com.br/receita/print_recipe.php?recipe_id='+str(x))
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        f = open('receita-'+str(x)+'.html','w')
        f.write(body)
        f.close()



try:
    thread.start_new_thread( request_url, ("Thread(19-8998)", 19,8998) )
    thread.start_new_thread( request_url, ("Thread(8998-17999)", 8998,17999) )

except:
    print "Error: unable to start thread"

while 1:
    pass

#print(body)
