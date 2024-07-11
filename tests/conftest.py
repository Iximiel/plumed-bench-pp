import pytest


@pytest.fixture
def full_benchmark_output():
    return (
        r"""PLUMED: PLUMED is starting
PLUMED: Version: 2.10.0-dev (git: b52ce2675-dirty) compiled on Jul 10 2024 at 11:30:47
PLUMED: Please cite these papers when using PLUMED [1][2]
PLUMED: For further information see the PLUMED web page at http://www.plumed.org
PLUMED: Root: /plumed2-dev/
PLUMED: LibraryPath: /plumed2-dev/src/lib/libplumedKernel.so
PLUMED: For installed feature, see /src/config/config.txt
PLUMED: Molecular dynamics engine: benchmarks
PLUMED: Precision of reals: 8
PLUMED: Running over 1 node
PLUMED: Number of threads: 1
PLUMED: Cache line size: 512
PLUMED: Number of atoms: 500
PLUMED: File suffix: 
PLUMED: FILE: plumed.dat
PLUMED: Action DEBUG
PLUMED:   with label @0
PLUMED:   with stride 1
PLUMED:   Detailed timing on
PLUMED:   on plumed log file
PLUMED: Action COORDINATION
PLUMED:   with label cpu
PLUMED:   between two groups of 500 and 0 atoms
PLUMED:   first group:
PLUMED:   1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  
PLUMED:   25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  
PLUMED:   50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  
PLUMED:   75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  
PLUMED:   100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123  124  
PLUMED:   125  126  127  128  129  130  131  132  133  134  135  136  137  138  139  140  141  142  143  144  145  146  147  148  149  
PLUMED:   150  151  152  153  154  155  156  157  158  159  160  161  162  163  164  165  166  167  168  169  170  171  172  173  174  
PLUMED:   175  176  177  178  179  180  181  182  183  184  185  186  187  188  189  190  191  192  193  194  195  196  197  198  199  
PLUMED:   200  201  202  203  204  205  206  207  208  209  210  211  212  213  214  215  216  217  218  219  220  221  222  223  224  
PLUMED:   225  226  227  228  229  230  231  232  233  234  235  236  237  238  239  240  241  242  243  244  245  246  247  248  249  
PLUMED:   250  251  252  253  254  255  256  257  258  259  260  261  262  263  264  265  266  267  268  269  270  271  272  273  274  
PLUMED:   275  276  277  278  279  280  281  282  283  284  285  286  287  288  289  290  291  292  293  294  295  296  297  298  299  
PLUMED:   300  301  302  303  304  305  306  307  308  309  310  311  312  313  314  315  316  317  318  319  320  321  322  323  324  
PLUMED:   325  326  327  328  329  330  331  332  333  334  335  336  337  338  339  340  341  342  343  344  345  346  347  348  349  
PLUMED:   350  351  352  353  354  355  356  357  358  359  360  361  362  363  364  365  366  367  368  369  370  371  372  373  374  
PLUMED:   375  376  377  378  379  380  381  382  383  384  385  386  387  388  389  390  391  392  393  394  395  396  397  398  399  
PLUMED:   400  401  402  403  404  405  406  407  408  409  410  411  412  413  414  415  416  417  418  419  420  421  422  423  424  
PLUMED:   425  426  427  428  429  430  431  432  433  434  435  436  437  438  439  440  441  442  443  444  445  446  447  448  449  
PLUMED:   450  451  452  453  454  455  456  457  458  459  460  461  462  463  464  465  466  467  468  469  470  471  472  473  474  
PLUMED:   475  476  477  478  479  480  481  482  483  484  485  486  487  488  489  490  491  492  493  494  495  496  497  498  499  
PLUMED:   500  
PLUMED:   second group:
PLUMED:   
PLUMED:   without periodic boundary conditions
PLUMED:   contacts are counted with cutoff 1.  Using rational switching function with parameters d0=0 nn=6 mm=12
PLUMED: Action PRINT
PLUMED:   with label @2
PLUMED:   with stride 1
PLUMED:   with arguments : 
PLUMED:    scalar with label cpu 
PLUMED:   on file Colvar
PLUMED:   with format  %8.4f
PLUMED: Action FLUSH
PLUMED:   with label @3
PLUMED:   with stride 1
PLUMED: END FILE: plumed.dat
PLUMED: Timestep: 1.000000
PLUMED: KbT has not been set by the MD engine
PLUMED: It should be set by hand where needed
PLUMED: Relevant bibliography:
PLUMED:   [1] The PLUMED consortium, Nat. Methods 16, 670 (2019)
PLUMED:   [2] Tribello, Bonomi, Branduardi, Camilloni, and Bussi, Comput. Phys. Commun. 185, 604 (2014)
PLUMED: Please read and cite where appropriate!
PLUMED: Finished setup
BENCH:  Starting MD loop
BENCH:  Use CTRL+C to stop at any time and collect timers (not working in MPI runs)
BENCH:  Warm-up completed
BENCH:  60% completed
BENCH:  Single run, skipping comparative analysis
BENCH:  
BENCH:  Kernel:      this
BENCH:  Input:       plumed.dat
BENCH:                                                Cycles        Total      Average      Minimum      Maximum
BENCH:  A Initialization                                   1     0.001654     0.001654     0.001654     0.001654
BENCH:  B0 First step                                      1     0.001588     0.001588     0.001588     0.001588
BENCH:  B1 Warm-up                                       999     1.630039     0.001632     0.001513     0.002375
BENCH:  B2 Calculation part 1                           2000     3.219555     0.001610     0.001502     0.002428
BENCH:  B3 Calculation part 2                           2000     3.110648     0.001555     0.001491     0.002460
PLUMED:                                               Cycles        Total      Average      Minimum      Maximum
PLUMED:                                                    1     7.959897     7.959897     7.959897     7.959897
PLUMED: 1 Prepare dependencies                          5000     0.002370     0.000000     0.000000     0.000009
PLUMED: 2 Sharing data                                  5000     0.010464     0.000002     0.000001     0.000024
PLUMED: 3 Waiting for data                              5000     0.003127     0.000001     0.000000     0.000008
PLUMED: 4 Calculating (forward loop)                    5000     7.868715     0.001574     0.001479     0.002362
PLUMED: 4A  1 posx                                      5000     0.000612     0.000000     0.000000     0.000004
PLUMED: 4A  2 posy                                      5000     0.000279     0.000000     0.000000     0.000006
PLUMED: 4A  3 posz                                      5000     0.000265     0.000000     0.000000     0.000004
PLUMED: 4A  4 Masses                                    5000     0.000288     0.000000     0.000000     0.000005
PLUMED: 4A  5 Charges                                   5000     0.000294     0.000000     0.000000     0.000007
PLUMED: 4A  6 Box                                       5000     0.000342     0.000000     0.000000     0.000008
PLUMED: 4A  7 benchmarks                                5000     0.000406     0.000000     0.000000     0.000001
PLUMED: 4A  8 @0                                        5000     0.000226     0.000000     0.000000     0.000001
PLUMED: 4A  9 cpu                                       5000     7.849295     0.001570     0.001476     0.002354
PLUMED: 4A 10 @2                                        5000     0.000440     0.000000     0.000000     0.000004
PLUMED: 4A 11 @3                                        5000     0.000314     0.000000     0.000000     0.000007
PLUMED: 5 Applying (backward loop)                      5000     0.017107     0.000003     0.000003     0.000053
PLUMED: 5A  0 @3                                        5000     0.000255     0.000000     0.000000     0.000006
PLUMED: 5A  1 @2                                        5000     0.000123     0.000000     0.000000     0.000003
PLUMED: 5A  2 cpu                                       5000     0.000516     0.000000     0.000000     0.000006
PLUMED: 5A  3 @0                                        5000     0.000331     0.000000     0.000000     0.000006
PLUMED: 5A  4 benchmarks                                5000     0.002406     0.000000     0.000000     0.000007
PLUMED: 5A  5 Box                                       5000     0.000468     0.000000     0.000000     0.000006
PLUMED: 5A  6 Charges                                   5000     0.000212     0.000000     0.000000     0.000001
PLUMED: 5A  7 Masses                                    5000     0.000161     0.000000     0.000000     0.000006
PLUMED: 5A  8 posz                                      5000     0.000119     0.000000     0.000000     0.000005
PLUMED: 5A  9 posy                                      5000     0.000127     0.000000     0.000000     0.000000
PLUMED: 5A 10 posx                                      5000     0.000130     0.000000     0.000000     0.000000
PLUMED: 5B Update forces                                5000     0.000119     0.000000     0.000000     0.000002
PLUMED: 6 Update                                        5000     0.041863     0.000008     0.000005     0.000098
""",
        {
            "this": {
                "kernel": "this",
                "input": "plumed.dat",
                "A Initialization": {
                    "Average": 0.001654,
                    "Cycles": 1,
                    "Maximum": 0.001654,
                    "Minimum": 0.001654,
                    "Total": 0.001654,
                },
                "B0 First step": {
                    "Average": 0.001588,
                    "Cycles": 1,
                    "Maximum": 0.001588,
                    "Minimum": 0.001588,
                    "Total": 0.001588,
                },
                "B1 Warm-up": {
                    "Average": 0.001632,
                    "Cycles": 999,
                    "Maximum": 0.002375,
                    "Minimum": 0.001513,
                    "Total": 1.630039,
                },
                "B2 Calculation part 1": {
                    "Average": 0.00161,
                    "Cycles": 2000,
                    "Maximum": 0.002428,
                    "Minimum": 0.001502,
                    "Total": 3.219555,
                },
                "B3 Calculation part 2": {
                    "Average": 0.001555,
                    "Cycles": 2000,
                    "Maximum": 0.00246,
                    "Minimum": 0.001491,
                    "Total": 3.110648,
                },
                "Plumed": {
                    "Cycles": 1,
                    "Total": 7.959897,
                    "Average": 7.959897,
                    "Minimum": 7.959897,
                    "Maximum": 7.959897,
                },
                "1 Prepare dependencies": {
                    "Cycles": 5000,
                    "Total": 0.00237,
                    "Average": 0.0,
                    "Minimum": 0.0,
                    "Maximum": 9e-06,
                },
                "2 Sharing data": {
                    "Cycles": 5000,
                    "Total": 0.010464,
                    "Average": 2e-06,
                    "Minimum": 1e-06,
                    "Maximum": 2.4e-05,
                },
                "3 Waiting for data": {
                    "Cycles": 5000,
                    "Total": 0.003127,
                    "Average": 1e-06,
                    "Minimum": 0.0,
                    "Maximum": 8e-06,
                },
                "4 Calculating (forward loop)": {
                    "Cycles": 5000,
                    "Total": 7.868715,
                    "Average": 0.001574,
                    "Minimum": 0.001479,
                    "Maximum": 0.002362,
                },
                "4A  1 posx": {"Cycles": 5000, "Total": 0.000612, "Average": 0.0, "Minimum": 0.0, "Maximum": 4e-06},
                "4A  2 posy": {"Cycles": 5000, "Total": 0.000279, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
                "4A  3 posz": {"Cycles": 5000, "Total": 0.000265, "Average": 0.0, "Minimum": 0.0, "Maximum": 4e-06},
                "4A  4 Masses": {"Cycles": 5000, "Total": 0.000288, "Average": 0.0, "Minimum": 0.0, "Maximum": 5e-06},
                "4A  5 Charges": {"Cycles": 5000, "Total": 0.000294, "Average": 0.0, "Minimum": 0.0, "Maximum": 7e-06},
                "4A  6 Box": {"Cycles": 5000, "Total": 0.000342, "Average": 0.0, "Minimum": 0.0, "Maximum": 8e-06},
                "4A  7 benchmarks": {
                    "Cycles": 5000,
                    "Total": 0.000406,
                    "Average": 0.0,
                    "Minimum": 0.0,
                    "Maximum": 1e-06,
                },
                "4A  8 @0": {"Cycles": 5000, "Total": 0.000226, "Average": 0.0, "Minimum": 0.0, "Maximum": 1e-06},
                "4A  9 cpu": {
                    "Cycles": 5000,
                    "Total": 7.849295,
                    "Average": 0.00157,
                    "Minimum": 0.001476,
                    "Maximum": 0.002354,
                },
                "4A 10 @2": {"Cycles": 5000, "Total": 0.00044, "Average": 0.0, "Minimum": 0.0, "Maximum": 4e-06},
                "4A 11 @3": {"Cycles": 5000, "Total": 0.000314, "Average": 0.0, "Minimum": 0.0, "Maximum": 7e-06},
                "5 Applying (backward loop)": {
                    "Cycles": 5000,
                    "Total": 0.017107,
                    "Average": 3e-06,
                    "Minimum": 3e-06,
                    "Maximum": 5.3e-05,
                },
                "5A  0 @3": {"Cycles": 5000, "Total": 0.000255, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
                "5A  1 @2": {"Cycles": 5000, "Total": 0.000123, "Average": 0.0, "Minimum": 0.0, "Maximum": 3e-06},
                "5A  2 cpu": {"Cycles": 5000, "Total": 0.000516, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
                "5A  3 @0": {"Cycles": 5000, "Total": 0.000331, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
                "5A  4 benchmarks": {
                    "Cycles": 5000,
                    "Total": 0.002406,
                    "Average": 0.0,
                    "Minimum": 0.0,
                    "Maximum": 7e-06,
                },
                "5A  5 Box": {"Cycles": 5000, "Total": 0.000468, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
                "5A  6 Charges": {"Cycles": 5000, "Total": 0.000212, "Average": 0.0, "Minimum": 0.0, "Maximum": 1e-06},
                "5A  7 Masses": {"Cycles": 5000, "Total": 0.000161, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
                "5A  8 posz": {"Cycles": 5000, "Total": 0.000119, "Average": 0.0, "Minimum": 0.0, "Maximum": 5e-06},
                "5A  9 posy": {"Cycles": 5000, "Total": 0.000127, "Average": 0.0, "Minimum": 0.0, "Maximum": 0.0},
                "5A 10 posx": {"Cycles": 5000, "Total": 0.00013, "Average": 0.0, "Minimum": 0.0, "Maximum": 0.0},
                "5B Update forces": {
                    "Cycles": 5000,
                    "Total": 0.000119,
                    "Average": 0.0,
                    "Minimum": 0.0,
                    "Maximum": 2e-06,
                },
                "6 Update": {"Cycles": 5000, "Total": 0.041863, "Average": 8e-06, "Minimum": 5e-06, "Maximum": 9.8e-05},
            }
        },
    )


@pytest.fixture
def readme_example_benchmark_output():
    return (
        r"""BENCH:  Kernel:      this
BENCH:  Input:       plumed.dat
BENCH:  Comparative: 1.000 +- 0.000
BENCH:                                                Cycles        Total      Average      Minimum      Maximum
BENCH:  A Initialization                                   1     0.214297     0.214297     0.214297     0.214297
BENCH:  B0 First step                                      1     0.062736     0.062736     0.062736     0.062736
BENCH:  B1 Warm-up                                       199    12.618833     0.063411     0.055884     0.076860
BENCH:  B2 Calculation part 1                            400    25.567659     0.063919     0.054110     0.113234
BENCH:  B3 Calculation part 2                            400    25.594014     0.063985     0.059516     0.102646
PLUMED:                                               Cycles        Total      Average      Minimum      Maximum
PLUMED:                                                    1    64.054325    64.054325    64.054325    64.054325
PLUMED: 1 Prepare dependencies                          1000     0.003443     0.000003     0.000001     0.000013
PLUMED: 2 Sharing data                                  1000     0.305915     0.000306     0.000015     0.037867
PLUMED: 3 Waiting for data                              1000     0.003051     0.000003     0.000002     0.000013
PLUMED: 4 Calculating (forward loop)                    1000    63.459357     0.063459     0.054012     0.091577
PLUMED: 5 Applying (backward loop)                      1000     0.008520     0.000009     0.000005     0.000044
PLUMED: 6 Update                                        1000     0.043188     0.000043     0.000031     0.000080
BENCH:  
BENCH:  Kernel:      ../../src/lib/install/libplumedKernel.so
BENCH:  Input:       plumed.dat
BENCH:  Comparative: 0.941 +- 0.002
BENCH:                                                Cycles        Total      Average      Minimum      Maximum
BENCH:  A Initialization                                   1     0.216190     0.216190     0.216190     0.216190
BENCH:  B0 First step                                      1     0.058967     0.058967     0.058967     0.058967
BENCH:  B1 Warm-up                                       199    11.983512     0.060219     0.056412     0.102643
BENCH:  B2 Calculation part 1                            400    24.035510     0.060089     0.056539     0.113900
BENCH:  B3 Calculation part 2                            400    24.084369     0.060211     0.056866     0.097184
PLUMED:                                               Cycles        Total      Average      Minimum      Maximum
PLUMED:                                                    1    60.373083    60.373083    60.373083    60.373083
PLUMED: 1 Prepare dependencies                          1000     0.003351     0.000003     0.000001     0.000014
PLUMED: 2 Sharing data                                  1000     0.329323     0.000329     0.000015     0.032672
PLUMED: 3 Waiting for data                              1000     0.003078     0.000003     0.000001     0.000013
PLUMED: 4 Calculating (forward loop)                    1000    59.752459     0.059752     0.056310     0.083841
PLUMED: 5 Applying (backward loop)                      1000     0.008900     0.000009     0.000006     0.000034
PLUMED: 6 Update                                        1000     0.043015     0.000043     0.000032     0.000239
    """,
        {
            "this": {
                "kernel": "this",
                "input": "plumed.dat",
                "compare": {"fraction": 1.0, "error": 0.0},
                "A Initialization": {
                    "Cycles": 1,
                    "Total": 0.214297,
                    "Average": 0.214297,
                    "Minimum": 0.214297,
                    "Maximum": 0.214297,
                },
                "B0 First step": {
                    "Cycles": 1,
                    "Total": 0.062736,
                    "Average": 0.062736,
                    "Minimum": 0.062736,
                    "Maximum": 0.062736,
                },
                "B1 Warm-up": {
                    "Cycles": 199,
                    "Total": 12.618833,
                    "Average": 0.063411,
                    "Minimum": 0.055884,
                    "Maximum": 0.07686,
                },
                "B2 Calculation part 1": {
                    "Cycles": 400,
                    "Total": 25.567659,
                    "Average": 0.063919,
                    "Minimum": 0.05411,
                    "Maximum": 0.113234,
                },
                "B3 Calculation part 2": {
                    "Cycles": 400,
                    "Total": 25.594014,
                    "Average": 0.063985,
                    "Minimum": 0.059516,
                    "Maximum": 0.102646,
                },
                "Plumed": {
                    "Cycles": 1,
                    "Total": 64.054325,
                    "Average": 64.054325,
                    "Minimum": 64.054325,
                    "Maximum": 64.054325,
                },
                "1 Prepare dependencies": {
                    "Cycles": 1000,
                    "Total": 0.003443,
                    "Average": 3e-06,
                    "Minimum": 1e-06,
                    "Maximum": 1.3e-05,
                },
                "2 Sharing data": {
                    "Cycles": 1000,
                    "Total": 0.305915,
                    "Average": 0.000306,
                    "Minimum": 1.5e-05,
                    "Maximum": 0.037867,
                },
                "3 Waiting for data": {
                    "Cycles": 1000,
                    "Total": 0.003051,
                    "Average": 3e-06,
                    "Minimum": 2e-06,
                    "Maximum": 1.3e-05,
                },
                "4 Calculating (forward loop)": {
                    "Cycles": 1000,
                    "Total": 63.459357,
                    "Average": 0.063459,
                    "Minimum": 0.054012,
                    "Maximum": 0.091577,
                },
                "5 Applying (backward loop)": {
                    "Cycles": 1000,
                    "Total": 0.00852,
                    "Average": 9e-06,
                    "Minimum": 5e-06,
                    "Maximum": 4.4e-05,
                },
                "6 Update": {
                    "Cycles": 1000,
                    "Total": 0.043188,
                    "Average": 4.3e-05,
                    "Minimum": 3.1e-05,
                    "Maximum": 8e-05,
                },
            },
            "../../src/lib/install/libplumedKernel.so": {
                "kernel": "../../src/lib/install/libplumedKernel.so",
                "input": "plumed.dat",
                "compare": {"fraction": 0.941, "error": 0.002},
                "A Initialization": {
                    "Cycles": 1,
                    "Total": 0.21619,
                    "Average": 0.21619,
                    "Minimum": 0.21619,
                    "Maximum": 0.21619,
                },
                "B0 First step": {
                    "Cycles": 1,
                    "Total": 0.058967,
                    "Average": 0.058967,
                    "Minimum": 0.058967,
                    "Maximum": 0.058967,
                },
                "B1 Warm-up": {
                    "Cycles": 199,
                    "Total": 11.983512,
                    "Average": 0.060219,
                    "Minimum": 0.056412,
                    "Maximum": 0.102643,
                },
                "B2 Calculation part 1": {
                    "Cycles": 400,
                    "Total": 24.03551,
                    "Average": 0.060089,
                    "Minimum": 0.056539,
                    "Maximum": 0.1139,
                },
                "B3 Calculation part 2": {
                    "Cycles": 400,
                    "Total": 24.084369,
                    "Average": 0.060211,
                    "Minimum": 0.056866,
                    "Maximum": 0.097184,
                },
                "Plumed": {
                    "Cycles": 1,
                    "Total": 60.373083,
                    "Average": 60.373083,
                    "Minimum": 60.373083,
                    "Maximum": 60.373083,
                },
                "1 Prepare dependencies": {
                    "Cycles": 1000,
                    "Total": 0.003351,
                    "Average": 3e-06,
                    "Minimum": 1e-06,
                    "Maximum": 1.4e-05,
                },
                "2 Sharing data": {
                    "Cycles": 1000,
                    "Total": 0.329323,
                    "Average": 0.000329,
                    "Minimum": 1.5e-05,
                    "Maximum": 0.032672,
                },
                "3 Waiting for data": {
                    "Cycles": 1000,
                    "Total": 0.003078,
                    "Average": 3e-06,
                    "Minimum": 1e-06,
                    "Maximum": 1.3e-05,
                },
                "4 Calculating (forward loop)": {
                    "Cycles": 1000,
                    "Total": 59.752459,
                    "Average": 0.059752,
                    "Minimum": 0.05631,
                    "Maximum": 0.083841,
                },
                "5 Applying (backward loop)": {
                    "Cycles": 1000,
                    "Total": 0.0089,
                    "Average": 9e-06,
                    "Minimum": 6e-06,
                    "Maximum": 3.4e-05,
                },
                "6 Update": {
                    "Cycles": 1000,
                    "Total": 0.043015,
                    "Average": 4.3e-05,
                    "Minimum": 3.2e-05,
                    "Maximum": 0.000239,
                },
            },
        },
    )


@pytest.fixture
def plumed_time_report():
    return (
        r"""PLUMED:                                               Cycles        Total      Average      Minimum      Maximum
PLUMED:                                                    1     7.959897     7.959897     7.959897     7.959897
PLUMED: 1 Prepare dependencies                          5000     0.002370     0.000000     0.000000     0.000009
PLUMED: 2 Sharing data                                  5000     0.010464     0.000002     0.000001     0.000024
PLUMED: 3 Waiting for data                              5000     0.003127     0.000001     0.000000     0.000008
PLUMED: 4 Calculating (forward loop)                    5000     7.868715     0.001574     0.001479     0.002362
PLUMED: 4A  1 posx                                      5000     0.000612     0.000000     0.000000     0.000004
PLUMED: 4A  2 posy                                      5000     0.000279     0.000000     0.000000     0.000006
PLUMED: 4A  3 posz                                      5000     0.000265     0.000000     0.000000     0.000004
PLUMED: 4A  4 Masses                                    5000     0.000288     0.000000     0.000000     0.000005
PLUMED: 4A  5 Charges                                   5000     0.000294     0.000000     0.000000     0.000007
PLUMED: 4A  6 Box                                       5000     0.000342     0.000000     0.000000     0.000008
PLUMED: 4A  7 benchmarks                                5000     0.000406     0.000000     0.000000     0.000001
PLUMED: 4A  8 @0                                        5000     0.000226     0.000000     0.000000     0.000001
PLUMED: 4A  9 cpu                                       5000     7.849295     0.001570     0.001476     0.002354
PLUMED: 4A 10 @2                                        5000     0.000440     0.000000     0.000000     0.000004
PLUMED: 4A 11 @3                                        5000     0.000314     0.000000     0.000000     0.000007
PLUMED: 5 Applying (backward loop)                      5000     0.017107     0.000003     0.000003     0.000053
PLUMED: 5A  0 @3                                        5000     0.000255     0.000000     0.000000     0.000006
PLUMED: 5A  1 @2                                        5000     0.000123     0.000000     0.000000     0.000003
PLUMED: 5A  2 cpu                                       5000     0.000516     0.000000     0.000000     0.000006
PLUMED: 5A  3 @0                                        5000     0.000331     0.000000     0.000000     0.000006
PLUMED: 5A  4 benchmarks                                5000     0.002406     0.000000     0.000000     0.000007
PLUMED: 5A  5 Box                                       5000     0.000468     0.000000     0.000000     0.000006
PLUMED: 5A  6 Charges                                   5000     0.000212     0.000000     0.000000     0.000001
PLUMED: 5A  7 Masses                                    5000     0.000161     0.000000     0.000000     0.000006
PLUMED: 5A  8 posz                                      5000     0.000119     0.000000     0.000000     0.000005
PLUMED: 5A  9 posy                                      5000     0.000127     0.000000     0.000000     0.000000
PLUMED: 5A 10 posx                                      5000     0.000130     0.000000     0.000000     0.000000
PLUMED: 5B Update forces                                5000     0.000119     0.000000     0.000000     0.000002
PLUMED: 6 Update                                        5000     0.041863     0.000008     0.000005     0.000098
    """,
        {
            "Plumed": {"Cycles": 1, "Total": 7.959897, "Average": 7.959897, "Minimum": 7.959897, "Maximum": 7.959897},
            "1 Prepare dependencies": {
                "Cycles": 5000,
                "Total": 0.00237,
                "Average": 0.0,
                "Minimum": 0.0,
                "Maximum": 9e-06,
            },
            "2 Sharing data": {
                "Cycles": 5000,
                "Total": 0.010464,
                "Average": 2e-06,
                "Minimum": 1e-06,
                "Maximum": 2.4e-05,
            },
            "3 Waiting for data": {
                "Cycles": 5000,
                "Total": 0.003127,
                "Average": 1e-06,
                "Minimum": 0.0,
                "Maximum": 8e-06,
            },
            "4 Calculating (forward loop)": {
                "Cycles": 5000,
                "Total": 7.868715,
                "Average": 0.001574,
                "Minimum": 0.001479,
                "Maximum": 0.002362,
            },
            "4A  1 posx": {"Cycles": 5000, "Total": 0.000612, "Average": 0.0, "Minimum": 0.0, "Maximum": 4e-06},
            "4A  2 posy": {"Cycles": 5000, "Total": 0.000279, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
            "4A  3 posz": {"Cycles": 5000, "Total": 0.000265, "Average": 0.0, "Minimum": 0.0, "Maximum": 4e-06},
            "4A  4 Masses": {"Cycles": 5000, "Total": 0.000288, "Average": 0.0, "Minimum": 0.0, "Maximum": 5e-06},
            "4A  5 Charges": {"Cycles": 5000, "Total": 0.000294, "Average": 0.0, "Minimum": 0.0, "Maximum": 7e-06},
            "4A  6 Box": {"Cycles": 5000, "Total": 0.000342, "Average": 0.0, "Minimum": 0.0, "Maximum": 8e-06},
            "4A  7 benchmarks": {"Cycles": 5000, "Total": 0.000406, "Average": 0.0, "Minimum": 0.0, "Maximum": 1e-06},
            "4A  8 @0": {"Cycles": 5000, "Total": 0.000226, "Average": 0.0, "Minimum": 0.0, "Maximum": 1e-06},
            "4A  9 cpu": {
                "Cycles": 5000,
                "Total": 7.849295,
                "Average": 0.00157,
                "Minimum": 0.001476,
                "Maximum": 0.002354,
            },
            "4A 10 @2": {"Cycles": 5000, "Total": 0.00044, "Average": 0.0, "Minimum": 0.0, "Maximum": 4e-06},
            "4A 11 @3": {"Cycles": 5000, "Total": 0.000314, "Average": 0.0, "Minimum": 0.0, "Maximum": 7e-06},
            "5 Applying (backward loop)": {
                "Cycles": 5000,
                "Total": 0.017107,
                "Average": 3e-06,
                "Minimum": 3e-06,
                "Maximum": 5.3e-05,
            },
            "5A  0 @3": {"Cycles": 5000, "Total": 0.000255, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
            "5A  1 @2": {"Cycles": 5000, "Total": 0.000123, "Average": 0.0, "Minimum": 0.0, "Maximum": 3e-06},
            "5A  2 cpu": {"Cycles": 5000, "Total": 0.000516, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
            "5A  3 @0": {"Cycles": 5000, "Total": 0.000331, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
            "5A  4 benchmarks": {"Cycles": 5000, "Total": 0.002406, "Average": 0.0, "Minimum": 0.0, "Maximum": 7e-06},
            "5A  5 Box": {"Cycles": 5000, "Total": 0.000468, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
            "5A  6 Charges": {"Cycles": 5000, "Total": 0.000212, "Average": 0.0, "Minimum": 0.0, "Maximum": 1e-06},
            "5A  7 Masses": {"Cycles": 5000, "Total": 0.000161, "Average": 0.0, "Minimum": 0.0, "Maximum": 6e-06},
            "5A  8 posz": {"Cycles": 5000, "Total": 0.000119, "Average": 0.0, "Minimum": 0.0, "Maximum": 5e-06},
            "5A  9 posy": {"Cycles": 5000, "Total": 0.000127, "Average": 0.0, "Minimum": 0.0, "Maximum": 0.0},
            "5A 10 posx": {"Cycles": 5000, "Total": 0.00013, "Average": 0.0, "Minimum": 0.0, "Maximum": 0.0},
            "5B Update forces": {"Cycles": 5000, "Total": 0.000119, "Average": 0.0, "Minimum": 0.0, "Maximum": 2e-06},
            "6 Update": {"Cycles": 5000, "Total": 0.041863, "Average": 8e-06, "Minimum": 5e-06, "Maximum": 9.8e-05},
        },
    )
