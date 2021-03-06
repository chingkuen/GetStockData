#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import time, datetime

def GetData(date, stock_no):
    '''
    get stock data from the link http://www.twse.com.tw/exchangeReport/
    It will return the data with list type
    date format is YYYYMMDD
    '''
    time.sleep(3)
    #if sleep time is less than 3 second, TWSE will block the request from the same host
    
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s' % ( date, stock_no)
    print ('url:', url)
    r = requests.get(url)
    d = r.json()
    return d.get('data')

def MergeData(StartDate, EndDate, StockNumber):
    '''
    Get the data from StartDate to EndDate for StockNumber and merge them into one list
    '''
    WholeData = []

    S_Year, S_Month, S_Day = StartDate.split('/')
    start_year = int(S_Year)
    start_month = int(S_Month)
    E_Year, E_Month, E_Day = EndDate.split('/')
    end_year = int(E_Year)
    end_month = int(E_Month)
    while start_year < end_year:
        while start_month < 13:
            if start_month < 10:
                WholeData.extend(GetData(str(start_year)+'0'+str(start_month)+'01', StockNumber))
            else:
                WholeData.extend(GetData(str(start_year)+str(start_month)+'01', StockNumber))
            start_month += 1
        start_year += 1
        start_month = 1
    if start_year == end_year:
        while start_month <= end_month:
            if start_month < 10:
                WholeData.extend(GetData(str(start_year)+'0'+str(start_month)+'01', StockNumber))
            else:
                WholeData.extend(GetData(str(start_year)+str(start_month)+'01', StockNumber))
            start_month += 1
    return WholeData

def main():
    StartDate = input('Please input start date (format pattern is YYYY/MM/DD):')
    EndDate = input ('Please input end date (format pattern is YYYY/MM/DD):')
    StockNumber = input ('Please input stock number:')
    Whole_Data = MergeData(StartDate, EndDate, StockNumber)
    print (Whole_Data)