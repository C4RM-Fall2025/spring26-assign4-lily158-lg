

def getBondPrice_Z(face, couponRate, times, yc):
    #change yield and time
    pvcfsum=0
    cf=couponRate*face
    for timeZ, ycZ in zip(times, yc): # times and yc are in next cell. link each time with corropoding yield #changed 
        pv =(1+ycZ)**-timeZ  # changed 
        pvcf = pv*cf
        pvcfsum+=pvcf 
    bondprice = pvcfsum +pv*face
    return(bondprice)