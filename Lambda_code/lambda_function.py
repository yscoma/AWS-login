#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8

import urllib3
import json
http = urllib3.PoolManager()

def lambda_handler(event, context):
    url = "https://hooks.slack.com/services/<< 당신의 Webhook 주소>>"

    username = '[SYSTEM-lambda]' 
    pretext  = '[Event]' + event['detail-type']
    account = event['account']
    time = event['time']
    region = event['region']
    detail = event['detail']
    SourceIP = event['detail']['sourceIPAddress']
    userAgent = event['detail']['userAgent']
    eventName = event['detail']['eventName']
    
    userIdentity =''
    try :
        userIdentity = event['detail']['userIdentity']['userName']
    except  Exception as e :
        userIdentity =''
    
    senText = 'Account "{}/{}" {} 으로 다음과 같이 이벤트가 발생 하였습니다.  \n시간 : {} \n소스 IP : {}  \n접속 방법 : {}'.format(account,userIdentity, eventName, time , SourceIP , userAgent )
    msg = {
        "username": '[SYSTEM-lambda]' ,
        "pretext": pretext,
        "text": senText,
        "icon_emoji": ""
    }
    
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',url, body=encoded_msg)

    print({
        "status_code": resp.status, 
        "response": resp.data
    })
    return {
        'statusCode': resp.status,
        'body': resp.data
    }