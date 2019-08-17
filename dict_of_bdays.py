#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime

def dict_of_bdays():
    today = date.today()
    d1 = today.strftime("%d/%m")
    dict = {
        '17/07': 'Eshwar',
        '01/03': 'Devi',
        '04/11': 'Nana',
        '02/06': 'Amma',
        '04/09': 'Krishna',
        '31/10': 'Isha',
        '17/09': 'susan',
        '03/10': 'Rajeshwari',
        '06/08': 'anurag agarwal',
        '28/05': 'deepali',
		'02/02': 'sudeep',
		'10/04': 'sai chand',
		d1: 'no one'
        }
    print ('searched for birthdays')
    print ('dict[d1]',dict[d1])
    print ('d1',d1)
    msg = 'There are no birthdays today BOSS'
    if(d1 in dict):
        msg = 'Let me check once Boss, Today  '+ dict[d1] + 's birthday'
    return msg
