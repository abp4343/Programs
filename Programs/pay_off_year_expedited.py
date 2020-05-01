# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:02:35 2018

@author: apark
"""

def payoffyearexpedited(balance, annualInterestRate):
    
    '''
    input: beginning debt balance, annual interest rate
    output: none.  Prints minimum monthly payment needed to pay off debt in a year.
    finds minumum monthly payment by bisection search
    '''
    
    #upper bound must be compound interest formula broken into months with annual interest rate given
    upper = (balance*((1+(annualInterestRate/12))**12))/12
    #lower bound must be balance broken into twelve months if interest rate is zero
    lower = balance/12

    #assign variable to balance in order to revert back to original after each payment check
    samebalance = balance
    while balance > 0.01 or balance < -0.01:
        balance = samebalance
            #first bisection: lower boud + upper bound / 2
        payment = 0.5*(lower + upper)
        #go through twelve months of payment to see if balance is paid off
        for i in range(12):
                #no interest at month 0, so the balance after first month is just the initial balance minus the payment
                balance = balance - payment
            #declining balance is balance plus month interest accrued minus payment
                balance = (balance + (balance*(annualInterestRate/12)))
            #if the balance is not paid off, revert balance back to original amount
        if balance > 0:
            #since balance is not paid, payment must be greater, so average of initial paymment and upper bound
            lower = 0.5*(payment + upper)
            #if too much has been paid off, revert balance back to original
        elif balance < 0:
            #since balance has been overpaid, monthly payment must be smaller, so average of initial payment and lower bound
            upper = 0.5*(payment + lower)
            #if balance has been paid off after a year, exit loop and print lowest payment
        
        #round lowest payment to two decimals to give a dollar and cents amount
    print("Lowest Payment: " + str(round(payment, 2)))