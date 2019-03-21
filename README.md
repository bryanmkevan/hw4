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

Suneeta Godbole's Contributions
===============================

1.  For my blog post: I replicated the physical activity recognition post from: <https://blogs.rstudio.com/tensorflow/posts/2018-07-17-activity-detection/>. All under suni\_hw4 in the PAblog.Rmd file I attempted to improve the performance by changing the number of filters and adding a convolution layer and playing with the spatial dropout layer. None of these modification improved the performance of the app.

2.  For the Android App called CloudVision. I adapted an app created by Fung Lam (seventhmoon) from: <https://github.com/GoogleCloudPlatform/cloud-vision/tree/master/android>. I set up a project on the Google Cloud Platform called "M280 Food Recog Project". To this project I added the Cloud Vision service and set up an Cloud Vision API. Then I just added the API key to the app under the build.gradle. I had to add escape characters to the API keep to get the app to work. Finally I added the same background that Kristen used in her app to the this one and changed the color of the header and image selection button.

Stephen Kwok's Contributions
============================

1.  I replicated a RStudio blog post on variational autoencoders (VAE):

<https://blogs.rstudio.com/tensorflow/posts/2018-10-22-mmd-vae/>

These used two kinds of VAE to model the domain space of a set of images (of clothing), and generated a large number of images of the latent space of the test images. These can be found in the

stephen\_hw4

folder of the GitHub repository.

1.  I added a simple credits button to the Google Cloud Vision Android app (discussed under Suneeta Godbole's contributions), that, when clicked, displays a message containing the purpose of the project and the names of the team members who worked on it.

2.  I put together a second Android food image classification app, adapting a project from:

<https://riggaroo.co.za/building-a-custom-machine-learning-model-on-android-with-tensorflow-lite/>

Using this project as a template, I retrained a pretrained neural net using TensorFlow on a dataset of images of 100 types of Japanese food obtained from:

<http://foodcam.mobi/dataset100.html>

optimized the net for TensorFlow Lite, and installed it in a prebuilt Android image classification app. I tested the app in the Android Studio emulator, using my laptop camera.

The app lists the three most likely predicted classes of food present in the camera's field of vision, in real time. The app can take a picture of the current image and the predicted classes for that image.

The image dataset is not included in the GitHub repository for reasons of space; however, the final training summaries, retrained labels, and retrained net itself can be found in the

stephen\_hw4/tf\_files

folder of the GitHub repository.

To run this app in Android Studio: go to the

"stephen\_hw4/android/tflite"

folder on the GitHub repository. Inside, locate a folder titled "app". Build this "app" folder in Android Studio. Then you can either run the app on an emulator, or download it to your phone.
