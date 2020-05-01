# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 08:59:38 2018

@author: apark
"""

def debtpayments(balance, annualInterestRate, monthlyPaymentRate):
    
    '''
    input (beginning balance, annual interest rate, minimum monthly payment rate)
    prints remaining balance after 1 year
    
    '''
        #loop for twelve months
    for i in range(12):
            
        if balance == 0:
                #no need to pay if there is no debt to pay
            break
            #monthly payment is the balance including interest accrued throughout month times minimum monthly payment rate
            #balance after 1 month is the balance including interest accrued throughout month minus payment
        payment = monthlyPaymentRate*(balance + (balance*(annualInterestRate/12)))
        balance = (balance + (balance*(annualInterestRate/12))) - payment
            
    print("Remaining balance: " + str(round(balance, 2)))