import numpy as np 
import math; sqrt = math.sqrt

class LinearRegression(object):
    
    def __init__(self):
        pass

    ##taking a data_sframe, pick the features as new column and output matrix X and Y.

    @staticmethod
    def get_numpy_data(data_sframe, features, output):

        if type(features) != list:
            features = [features]

        if type(output) != list:
            output = [output]
        
        # add a constant column to an SFrame
        data_sframe['constant'] = 1 
        features = ['constant'] + features
        
        # select the columns of features list
        features_sframe = data_sframe.select_columns(features)
        output_sarray   = data_sframe.select_columns(output)
        
        # this will convert the SArray into a numpy array:
        features_matrix = features_sframe.to_numpy()            
        output_array    =   output_sarray.to_numpy()
        
        #return a 10000 * 3 vector and another 10000 * 1 vector
        return(features_matrix, output_array)    
    
    ##calculate inner product of Xw.    
    @staticmethod    
    def dotProduct(feature_matrix, weights):
        predictions = np.dot(feature_matrix, weights)
        return(predictions)        
        
    ##calculate derivative of multiple Gradient.    
    @staticmethod    
    def derivative(errors, Xmatrix):
        derivative = 2 * np.dot( errors.T, Xmatrix )
        return (derivative)  

    #remember the arguments that this function takes in
    @staticmethod
    def regression_gradient_descent(Xmatrix, Ymatrix, initial_weights, step_size, tolerance):

        converged = False 

        weights = initial_weights # make sure it's a numpy array
        count   = 0        
        
        while not converged:
            # compute the predictions based on feature_matrix and weights using your predict_output() function
            # compute the errors as predictions - output
            predictions = LinearRegression.dotProduct(Xmatrix, weights)
            errors      = predictions - Ymatrix
            derivative  = LinearRegression.derivative(errors, Xmatrix)
            
            weights     = weights- step_size * derivative.T

            gradient_sum_squares = (errors * errors).sum()
            
            gradient_magnitude = sqrt(gradient_sum_squares)
            
            if gradient_magnitude < tolerance:
                converged = True
                
            if count%10000 == 0:
                print 'count is ', count
                print 'gradient is ', gradient_sum_squares
                print 'weights are ', weights
            count  += 1
        print 'final count is ', count
        print 'final weights is', weights
        return(weights)
    @staticmethod
    def cost(Xmatrix, Ymatrix, weights):
        errors = np.dot(Xmatrix, weights) - Ymatrix
        cost   = (errors *  errors).sum()
        return(cost) 
