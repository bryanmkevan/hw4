README.Rmd
================

HW4: Group Project
------------------

Biostat 280M - Bryan Kevan, Kristen McGreevy, Suneeta Godbole, Stephen Kwok

Readme

Lime v.04: Bryan Kevan
----------------------

For my blog post replication, I implemented the code on the tensorflow blog for image recognition on a selection of google search results to test its accuracy. The first part of the app pulls the top images on google for a given search term, and determines the percentage of them the lime algorithm can identify correctly.

The second part of kittens.R determines the top 15 items that the algorithm identified in its results for the set of pictures.

``` bash
  Rscript bryan_hw4/lime04.R pizza
```

    ## Using TensorFlow backend.
    ## WARNING:tensorflow:From /home/bryanmkevan/.virtualenvs/r-tensorflow/lib/python2.7/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
    ## Instructions for updating:
    ## Colocations handled automatically by placer.
    ## 2019-03-19 01:36:51.777767: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
    ## 2019-03-19 01:36:51.784749: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2000165000 Hz
    ## 2019-03-19 01:36:51.785905: I tensorflow/compiler/xla/service/service.cc:150] XLA service 0xf406c00 executing computations on platform Host. Devices:
    ## 2019-03-19 01:36:51.785955: I tensorflow/compiler/xla/service/service.cc:158]   StreamExecutor device (0): <undefined>, <undefined>
    ## 2019-03-19 01:36:51.902418: W tensorflow/core/framework/allocator.cc:124] Allocation of 411041792 exceeds 10% of system memory.
    ## 2019-03-19 01:36:52.177153: W tensorflow/core/framework/allocator.cc:124] Allocation of 411041792 exceeds 10% of system memory.
    ## 2019-03-19 01:36:52.767366: W tensorflow/core/framework/allocator.cc:124] Allocation of 411041792 exceeds 10% of system memory.
    ## The neural net recognized 75 % of the pictures of pizza on the first page of Google results 
    ## 
    ## Here are the top items that were identified as pizza  in the first page of images:
    ##    class_description  n
    ## 1              pizza 17
    ## 2             potpie 11
    ## 3        French_loaf  8
    ## 4              plate  8
    ## 5             bakery  7
    ## 6             trifle  5
    ## 7        waffle_iron  5
    ## 8          meat_loaf  4
    ## 9        toilet_seat  3
    ## 10           ocarina  2
    ## 11           spatula  2
    ## 12      butcher_shop  1
    ## 13            candle  1
    ## 14         carbonara  1
    ## 15          carousel  1

The algorithm works pretty well for pizzas (75% accuracy), and less well for bagels (45%).
