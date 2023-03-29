#Lior Vanounou
#313333106

def my_func(x1,x2,x3):
        my_list=[x1,x2,x3]
        for i in my_list:
            if type(i) == str :
                return("None")

            elif type(i) == int:
                return("Error: parameters shoul be float")
        if x1+x2+x3 == 0 :
            return("Not a number - denominator equals zero")
        else:
            my_calc= ((x1+x2+x3) * (x2+x3) * x3) / (x1+x2+x3)
            return(my_calc)
