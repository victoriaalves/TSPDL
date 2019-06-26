Problem:    TSPDL
Rows:       20
Columns:    18 (9 integer, 9 binary)
Non-zeros:  56
Status:     INTEGER OPTIMAL
Objective:  total = 24 (MINimum)

   No.   Row name        Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 total                      24                             
     2 c1[1]                       1             1             = 
     3 c1[B]                       1             1             = 
     4 c1[C]                       1             1             = 
     5 c2[1]                       1             1             = 
     6 c2[B]                       1             1             = 
     7 c2[C]                       1             1             = 
     8 c3[B]                       1             1             = 
     9 c3[C]                       2             2             = 
    10 c4                          3             3             = 
    11 c5                          0            -0             = 
    12 c6[1,1]                     0                          -0 
    13 c6[1,B]                     0                          -0 
    14 c6[1,C]                     0                          -0 
    15 c6[B,1]                  -100                          -0 
    16 c6[B,B]                     0                          -0 
    17 c6[B,C]                     0                          -0 
    18 c6[C,1]                     0                          -0 
    19 c6[C,B]                    -1                          -0 
    20 c6[C,C]                     0                          -0 

   No. Column name       Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 x[1,1]       *              0             0             1 
     2 x[1,B]       *              0             0             1 
     3 x[1,C]       *              1             0             1 
     4 x[B,1]       *              1             0             1 
     5 x[B,B]       *              0             0             1 
     6 x[B,C]       *              0             0             1 
     7 x[C,1]       *              0             0             1 
     8 x[C,B]       *              1             0             1 
     9 x[C,C]       *              0             0             1 
    10 y[1,B]                      0             0               
    11 y[B,B]                      0             0               
    12 y[C,B]                      1             0               
    13 y[B,1]                      0             0               
    14 y[B,C]                      0             0               
    15 y[1,C]                      3             0               
    16 y[C,C]                      0             0               
    17 y[C,1]                      0             0               
    18 y[1,1]                      0             0               

Integer feasibility conditions:

KKT.PE: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
