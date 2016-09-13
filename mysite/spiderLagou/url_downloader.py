import  urllib2
import  json
class urlDownloader:

    def download(self, url):
        if url is None:
            return  None
        else:
            request = urllib2.Request(url)
            request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36')
            response = urllib2.urlopen(request)
            if response.getcode() != 200:
                return None
            else:
                return  response.read()

    def dounload_ajax(self,url,data={}):
        if url is None:
            return  None
        else:
            if data != {}:
                request = urllib2.Request(url=url,data=data)
            else:
                request = urllib2.Request(url=url)
            request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36')
            response = urllib2.urlopen(request)
            if response.getcode() != 200:
                return None
            else:
                return  json.loads(response.read())
                #return response.read()
