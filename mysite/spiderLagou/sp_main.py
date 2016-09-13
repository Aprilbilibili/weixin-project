# coding:utf8
import url_downloader,url_creator
import json
import string
import sys

class SpiderMain(object):
    def __init__(self):
        self.urlCreator = url_creator.UrlCreator()
        self.downloader = url_downloader.urlDownloader()

    def craw(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        qs = {
            'job': 'Java',
            'job_nature': '',
            'job_exp' : '',
            'edu' : '',
            'FinancingStage' : '',
            'IndustrySectors' : '',
            'location' : '北京',
            'loc_adminarea' : '朝阳区',
            'loc_busarea' : '望京',
            'salary': ''
        }
        pn = '1'
        kd = 'Java'

        json_response = {
            'pn' : '',
            'result':[]
        }
        data = {
            "positionId": "",         
            "positionName":"",        
            "jobNature":"",           
            "workYear":"",            
            "education":"",           
            "financeStage":"",        
            "industryField":"",       
            "city":"",               
            "district":"",            
            "salary":"",              
            "formatCreateTime":"",    
            "createTime":"",          
            "companyShortName":"",    
            "companyFullName":"",     
            "positionAdvantage":"",   
            "companyLabelList":[],    
            "jobDescription":[]       
        }

        kd = qs['job']
        para = self.urlCreator.Create_para(qs)
        querystring = self.urlCreator.Url_lencode(para)
        ajax_url = self.urlCreator.Create_url2(querystring)
        query_data = self.urlCreator.FormData(pn, kd)
        json_content = self.downloader.dounload_ajax(ajax_url, query_data)
        content = json_content["content"]
        result = content["positionResult"]
        if result['result'] == []:
            return  json_response
        else:
            for rn in result['result']:
                data["positionId"] = str(rn["positionId"])
                data["positionName"] = rn["positionName"]
                data["jobNature"] = rn["jobNature"]
                data["workYear"] = rn["workYear"]
                data["education"] = rn["education"]
                data["financeStage"] = rn["financeStage"]
                data["industryField"] = rn["industryField"]
                data["city"] = rn["city"]
                data["district"] = rn["district"]
                data["businessZones"] = rn["businessZones"]
                data["salary"] = rn["salary"]
                data["formatCreateTime"] = rn["formatCreateTime"]
                data["createTime"] = rn["createTime"]
                data["companyShortName"] = rn["companyShortName"]
                data["companyFullName"] = rn["companyFullName"]
                data["positionAdvantage"] = rn["positionAdvantage"]
                data["companyLabelList"] = rn["companyLabelList"]
                json_response['result'].append(data)

            return json_response


