# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:02:35 2018

@author: apark
"""

def payoffyear(balance, annualInterestRate):
    
    '''
    input: beginning debt balance, annual interest rate
    output: none.  Prints minimum monthly payment needed to pay off debt in a year.
    '''
    payment = 0
    #assign variable to balance in order to revert back to original after each payment check
    samebalance = balance
    while balance > 0:
        #go through twelve months of payment to see if balance is paid off
        for i in range(12):
            if balance <= 0:
                #no need to pay if there is no debt to pay
                break
            else:
                #no interest at month 0, so the balance after first month is just the initial balance minus the payment
                if i == 0:
                    balance = balance - payment
                else:
            #declining balance is balance plus month interest accrued minus payment
                    balance = (balance + (balance*(annualInterestRate/12))) - payment
            #if the balance is not paid off, revert balance back to original amount
        if balance > 0:
            balance = samebalance
            #if balance has been paid off after a year, exit loop and print lowest payment
        else:
            break
        #add 10 to payment and loop again with new payment
        payment += 10
        
        
    print("Lowest Payment: " + str(payment))