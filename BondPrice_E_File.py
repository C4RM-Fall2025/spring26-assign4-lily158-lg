def getBondPrice_E(face, couponRate, yc):
    pvcfsum=0
    cf=couponRate*face
    for t, y in enumerate(yc, start=1):
        pv =(1+y)**(-t)
        pvcf = pv*cf
        pvcfsum+=pvcf 
    bondprice = pvcfsum +pv*face
    return(bondprice)