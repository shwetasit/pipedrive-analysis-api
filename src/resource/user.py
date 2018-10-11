from flask import jsonify,request
import requests
import json
from pipedrive.client import Client
from flask_restful import Resource
from model.abc import db
from model import User
#from client import superhero
from util import parse_params
#import mysql.connector
#conn = mysql.connector.connect(host='localhost', database='mysql', user='root', password='12121212')
from .test import Analysis 

api_token="137f09ef7c288dedc165c51bce0a0cffe571e1d5"
domain_url="https://api.pipedrive.com/"
client = Client(api_base_url=domain_url)
client.set_token(api_token)

#mine
class UserListAPI(Resource):
    def get(self):

        # status = ""
        # url = domain_url+"/deals"
        # querystring = {"status":status,"api_token":api_token}
        # response = requests.request("GET", url, params=querystring)

        get_deals = client.get_deals()
        #return Analysis.callingDeals(get_deals)
        #Analysis.topTenDeals(get_deals)
        #print(get_deals)
        # json_data = json.loads(response.text)
        #return Analysis.openDeal(get_deals)
        #return Analysis.closeDeal(get_deals)
        #return Analysis.wonDeal(get_deals)
        return Analysis.pandasdemo(get_deals)

       # return Analysis.openDeal(get_deals)

        # cursor = conn.cursor()
        # cursor.execute("SELECT * FROM newdb.employee")
        # rows = cursor.fetchall()
        # print('Total Row(s):', cursor.rowcount)
        # # for row in rows:
        # #     print(row)
        # row_headers=[x[0] for x in cursor.description] #this will extract row headers
        # json_data=[]
        # for result in rows:
        #     json_data.append(dict(zip(row_headers,result)))

      
        # return jsonify(data=json_data)

    @parse_params(
        {'name': 'email', 'type': str, 'required': True},
        {'name': 'password', 'type': str, 'required': True},
        {'name': 'empid', 'type': int, 'required': True}
    )


    def post(self, params):
        empId=params.empid
        email=params.email
        password=params.password
        
        cursor = conn.cursor()
        print(empId)
        cursor.execute("SELECT * FROM newdb.employee where idEMPLOYEE = %s",(empId,)) 
        #rows = cursor.fetchall()
        #print('Total Row(s):', cursor.rowcount)
        if cursor.rowcount > 0:
            print('No matched employee')

        # else:
        #     cursor.execute("INSERT INTO newdb.employee values(empId, "Mahesh","Accountant", "M", 123 ")
        #     
        #     for row in rows:
        #         print(row)
        
        rows = cursor.fetchall()
        return jsonify(data=rows)
        
        #return param
