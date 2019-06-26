Problem:    TSPDL
Rows:       20
Columns:    18 (9 integer, 9 binary)
Non-zeros:  59
Status:     INTEGER OPTIMAL
Objective:  total = 3 (MINimum)

   No.   Row name        Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 total                       3                             
     2 c1[1]                       1             1             = 
     3 c1[2]                       1             1             = 
     4 c1[3]                       1             1             = 
     5 c2[1]                       1             1             = 
     6 c2[2]                       1             1             = 
     7 c2[3]                       1             1             = 
     8 c3[2]                       1             1             = 
     9 c3[3]                       1             1             = 
    10 c4                          2             2             = 
    11 c5                          0            -0             = 
    12 c6[1,1]                     0                          -0 
    13 c6[1,2]                     0                          -0 
    14 c6[1,3]                     0                          -0 
    15 c6[2,1]                    -3                          -0 
    16 c6[2,2]                     0                          -0 
    17 c6[2,3]                     0                          -0 
    18 c6[3,1]                     0                          -0 
    19 c6[3,2]                     0                          -0 
    20 c6[3,3]                     0                          -0 

   No. Column name       Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 x[1,1]       *              0             0             1 
     2 x[1,2]       *              0             0             1 
     3 x[1,3]       *              1             0             1 
     4 x[2,1]       *              1             0             1 
     5 x[2,2]       *              0             0             1 
     6 x[2,3]       *              0             0             1 
     7 x[3,1]       *              0             0             1 
     8 x[3,2]       *              1             0             1 
     9 x[3,3]       *              0             0             1 
    10 y[1,2]                      0             0               
    11 y[2,2]                      0             0               
    12 y[3,2]                      1             0               
    13 y[2,1]                      0             0               
    14 y[2,3]                      0             0               
    15 y[1,3]                      2             0               
    16 y[3,3]                      0             0               
    17 y[3,1]                      0             0               
    18 y[1,1]                      0             0               

Integer feasibility conditions:

KKT.PE: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
