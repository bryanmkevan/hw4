#install.packages("magick")
#install.packages("lime")

library(keras)
library(lime)
library(magick)


model <- application_vgg16(
  weights = "imagenet",
  include_top = TRUE
)
model

img <- image_read('en.wikipedia.org/wiki/Hot_dog_bun#/media/File:Hotdog_-_Evan_Swigart.jpg')
img_path <- file.path(tempdir(), 'kitten.jpg')
image_write(img, img_path)
plot(as.raster(img))

image_prep <- function(x) {
  arrays <- lapply(x, function(path) {
    img <- image_load(path, target_size = c(224,224))
    x <- image_to_array(img)
    x <- array_reshape(x, c(1, dim(x)))
    x <- imagenet_preprocess_input(x)
  })
  do.call(abind::abind, c(arrays, list(along = 1)))
}
explainer <- lime(img_path, model, image_prep)

res <- predict(model, image_prep(img_path))
imagenet_decode_predictions(res)

plot_superpixels(img_path, n_superpixels = 200, weight = 40)
packageVersion("magick")



