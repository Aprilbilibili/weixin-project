# coding:utf8
import urllib
class UrlCreator:
    #通过提供工作(必要)，工作性质，工作经验，要求学历，融资阶段，行业领域，工作地点，地点行政区，商区 来创造一个url
    def Create_url(self,querylist):
        url = 'http://www.lagou.com/jobs/'
        if querylist["job"] != '':
            url += 'list_'+ querylist["job"] +'?px=defalut'
        else:
            url += 'list_?px=defalut'
        if querylist["job_nature"] != '':
            url += '&gx=' + querylist["job_nature"]
        if querylist["job_exp"] != '':
            url += '&gj=' + querylist["job_exp"]
        if querylist["edu"] != '':
            url += '&xl=' + querylist["edu"]
        if querylist["FinancingStage"] != '':
            url += '&jd=' + querylist["FinancingStage"]
        if querylist["IndustrySectors"] != '':
            url += '&hy=' + querylist["IndustrySectors"]
        if querylist["location"] != '':
            url += '&city=' + querylist["location"]
        if querylist["loc_adminarea"] != '':
            url += '&district=' + querylist["loc_adminarea"]
        if querylist["loc_busarea"] != '':
            url += '&bizArea=' + querylist["loc_busarea"]
        if querylist["salary"] != '':
            url += 'yx=' + querylist["salary"]

        return url


    #创建ajax的url
    def Create_url2(self,qs):
        url = "http://www.lagou.com/jobs/positionAjax.json?px=default"
        url += qs
        return url

    #创建内容页的url
    def Create_url3(self,id):
        url = "http://www.lagou.com/jobs/"
        if id == None:
            return
        else:
            url += id+".html"

        return url


    #创建一个可供urllencode使用的字典
    def Create_para(self,querydist):
        para ={ }
        if querydist['job_exp'] != '':
            para['gj'] = querydist['job_exp']
        if querydist['edu'] != '':
            para['xl'] = querydist['edu']
        if querydist['FinancingStage'] != '':
            para['jd'] = querydist['FinancingStage']
        if querydist['IndustrySectors'] != '':
            para['hy'] = querydist['IndustrySectors']
        if querydist['job_nature'] != '':
            para['gx'] = querydist['job_nature']
        if querydist['location'] != '':
            para['city'] = querydist['location']
        if querydist['loc_adminarea'] != '':
            para['district'] = querydist['loc_adminarea']
        if querydist['loc_busarea'] != '':
            para['bizArea'] = querydist['loc_busarea']
        para['needAddtionalResult'] = 'false'

        return para

    #url编码
    def Url_lencode(self,para):
        return urllib.urlencode(para)

    #form data
    def FormData(self,pn,kd):
        fd = {
            'first' : 'true',
            'pn' : pn ,
            'kd' : kd
        }
        return  urllib.urlencode(fd)