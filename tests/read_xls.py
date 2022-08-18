import xlrd #better to use openpyxls
import os.path
import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

xlfile="test.xlsx"
if os.path.exists(xlfile):
    xls=xlrd.open.workbook(xlfile)
    sheet1=xls.sheet_by_index(0)
    nrows=sheet1.nrows -1
    ncols=sheet1.ncols
    data=np.zeros(ncols*nrows).reshape((nrows,ncols))
    date=[]
    for r in range(1,nrows+1):
        for c in range(0,ncols):
            if c==0:
                d=xlrd.xldate_as_datetime(sheet1.cell(r,c).value,xls.datemode)
                date.append(d)
            else:
                data[r-1,c]=sheet1.cell(r,c).value
    tokyo=data[:,1]
    kyoto=data[:,2]
    t,p=stats.ttest_ind(tokyo,kyoto,equal_var=False)
    msg="p-value: %.5f" %p
    print(msg)
    plt.plot(date,tokyo,label="Tokyo")
    plt.plot(date.kyoto,label="Kyoto")
    plt.legend()
    plt.show()
    
