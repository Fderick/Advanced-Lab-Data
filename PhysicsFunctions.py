import numpy as np 
import lmfit

    #fits a linear function to an x,y dataset
def fitLinear(iX,iY, iSlope = 1, iB = 0):
    #Define a linear function
    def linearFunc(x,slope,b):
        result = slope*x+b
        return result
    #Create fit
    model = lmfit.Model(linearFunc) 
    p = model.make_params(slope=iSlope,b=iB) 
    result = model.fit(data=iY,params=p,x=iX) 
    output = model.eval(params=result.params,x=iX)  # If you want more points to be produced based on the fit, you can change iX here.
    
    lmfit.report_fit(result) #Necessary to show results.
    return output,result
    
    #Fits a quadratic function to an x,y dataset
def fitQuadratic(iX,iY,iA = 1 ,iB = 0,iC = 0):
    #Define a quadratic function
    def quadFunc(x,a,b,c):
        result = a*x**2+b*x+c
        return result
    
    #Create fit
    model = lmfit.Model(quadFunc) 
    p = model.make_params(a=iA,b=iB,c=iC) 
    result = model.fit(data=iY,params=p,x=iX) 
    output = model.eval(params=result.params,x=iX) 
    
    lmfit.report_fit(result) #Necessary to show results.
    return output,result


def fitGauss(iX,iY,iMu=0,iSigma=1):#What is this?!?! This is a function to define the model fit. 
                                          #The iX and iY values are the ones from your data, iFunc is your previously defined linear or quadratic function, 
                                          #mu is the mean of the gaussian, sigma is the standard deviation.
    def gauss(x, amp, mu, sigma):
        result = np.abs(amp)*np.exp(-(x-mu)**2/sigma**2)  #This is just the mathematical definition of a gaussian.
        return result #after running the function we return the result.
   

    model  = lmfit.Model(gauss) #This line is always included
    p = model.make_params(amp=0,mu=iMu,sigma=iSigma) #This line will include the parameters of your function, for a gaussian the parameters that change are amp, mu, and sigma. 
                                                     #For y = mx + b, the changing parameters will be m and b. 
    result = model.fit(data=iY,params=p,x=iX) #This is the line where we actually run a fit! Be sure to follow the syntax in this example.
    output = model.eval(params=result.params,x=iX) #Now that we have the results lets evaluate how good the fit did, this is the output line 
                                                   #This will tell you what values your fit got.
    lmfit.report_fit(result) #Necessary to show results.
    return output,result #you can return multiple values with a function.

#Fit for a reciprocal function y = a/x + b
def fitReciprocal(iX,iY,iA = 0, iB = 0):
                  
    #Define a reciprocal function
    def recipFunc(x,a,b):
        result = a/x + b
        return result
    
    #Create fit
    model = lmfit.Model(recipFunc) 
    p = model.make_params(a=iA,b=iB) 
    result = model.fit(data=iY,params=p,x=iX) 
    output = model.eval(params=result.params,x=iX) 
    
    lmfit.report_fit(result) #Necessary to show results.
    return output,result

#Reads and extracts data points from a csv file. Assumes that x is in the first column and that y is in the second. Returns np arrays.
def readCSV(filename):
    data = open(filename,"r")
    
    x = []
    y = []
    for row in data: #For every line in the file.
        row = row.strip()
        values = row.split(',') #This separates the values in the each row. It creates a list 'values' with each row value. 
        try:
            x.append(float(values[0]))  
            y.append(float(values[1]))
            
        except: 
            print("______________________________________")
            print('Invalid value:', values)
            print('Found text, or invalid numerical value')
            print("______________________________________")

    x_arr = np.array(x)
    y_arr = np.array(y)
    data.close()
    return x_arr,y_arr