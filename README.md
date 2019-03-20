README.Rmd
================

HW4: Group Project
------------------

Biostat 280M - Bryan Kevan, Kristen McGreevy, Suneeta Godbole, Stephen Kwok

Readme

Bryan Kevan's Contributions
---------------------------

For my blog post replication, I implemented the code on the tensorflow blog for image recognition on a selection of google search results to test its accuracy. The first part of the app pulls the top images on google for a given search term, and determines the percentage of them the lime algorithm can identify correctly.

The second part of lime04.R determines the top 15 items that the algorithm identified in its results for the set of pictures.

``` bash
  Rscript /hw4/bryan_hw4/lime04.R pizza
```

The algorithm works pretty well for pizzas (75% accuracy), and less well for bagels (45%).

Kristen McGreevy's Contributions
--------------------------------

1.  Blog Post on Bayesian approach to obtaining uncertainty estimates from neural networks: I replicated the blog code, graphs, and analytics which can be found in Blog\_Post\_bayes.R. I applied the code to an Italian air quality dataset from UCI to predict the level of CO in the air based on other air quality measures. I produce a plot showing the predicted and actual value of hourly CO concentration.
2.  Developed the iOS platform app: I adapted code from <https://www.appcoda.com/coreml-introduction/> and named the app CoreMLDemo. This Xcode can be found in the folder. I downloaded and used the Machine Learning Model Inception v3 for the image identification. I added photos to the simulated phone and tested the simulation on a variety of phones. Because this is a simulator, photos cannot actually be taken; if you have a photo of interest, drag it from your computer into the simulator and the image will be added to the photo library.
3.  Developed a Shiny App for uploading and displaying images: This is an alternative first step to developing a shiny app that can identify objects or food in images. This file is called app.R.
