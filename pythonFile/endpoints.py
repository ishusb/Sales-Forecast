import logging
from unittest import result
import pickle
from flask_pymongo import pymongo
from flask import jsonify, request, render_template
import pandas as pd
from algo import code
from error import errorC
import numpy as np

con_string = "mongodb+srv://ishwarya:ishu2817@cluster0.28rv67v.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_string)

db = client.get_database('demodb')

user_collection = pymongo.collection.Collection(db, 'demo')
print("MongoDB connected Successfully")

def project_api_routes(endpoints):
    # @endpoints.route('/login',method=['GET'])
    # def login():
    #     resp={}
    #     try:
    #         req=request.form
    #         email=request.email.get('email')
    #         password=request.password.get('password')
    #         print(email)
    #         print(password)
    #     except Exception as e:
    #         print(e)


    @endpoints.route('/file_upload',methods=['POST','GET'])
    def file_upload():
        
        resp = {}
        try:
            req = request.form
            value=request.form.get('time')
            #s = value.decode()
            file = request.files.get('file')  
            #value=int(value)
            #form = request.get_json()
            #name = form['name'] 
            #value=request.get_json().get('period')
            #value=form['time']
            # print(value)
            value=2

            newFile=code(file,value)
            with open('result','wb') as f:
                pickle.dump(newFile,f)
            with open('result','ab') as f:
                pickle.dump(newFile,f)
            with open('result','rb') as f:
                res=pickle.load(f)
            df = pd.DataFrame(res)
            df.to_csv(r'file.csv')


            # err=[]
            # err=errorC('file.csv')
            # print(err)
            # print(err)
            # print(err)
            # type code here
            
            #print(res)
            #df = pd.read_csv(file)
            # print(df.head)
            # print(df.columns)
            status = {
                "statusCode":"200",
                "statusMessage":"File uploaded Successfully."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp

    @endpoints.route('/predict',methods=['GET'])
    def predict():
        err=[]
        err=errorC('file.csv')
        return err


    return endpoints