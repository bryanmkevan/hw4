#install.packages("magick")
#install.packages("lime")

library(keras)
library(lime)
library(magick)
library(dplyr)
library("rvest")

## Testing Hotdog Accuracy
model <- application_vgg16(
  weights = "imagenet",
  include_top = TRUE
)

download_images <- function(term, url, outPath) {
  ## Initialize web session
  webpage <- read_html(url)
  imageurl <- webpage %>% 
    html_nodes("img") %>% 
    html_attr("src")
  
  for(i in 1:length(imageurl)){
    download.file(imageurl[i], destfile = paste0(outPath, "/", term, "_", i, ".jpg"), mode = 'wb')
  }
}

get_stats <- function(term, outPath) {
  
  url <- paste0("https://www.google.com/search?q=", term,
                "&source=lnms&tbm=isch&sa=X&tbs=isz:m")
  download_images(term, url, outPath)
  
  ## Create bin for output stats
  stats_out <- matrix(nrow = 0, ncol = 3)
  for (i in c(1:length(list.files(outPath)))) {
    img <- image_read(paste0(outPath, "/", term,"_",i,".jpg"))
    img_path <- file.path(tempdir(), 'image.jpg')
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
    stats <- as.data.frame(imagenet_decode_predictions(res))
    stats$n = i
    stats_out <- rbind(stats_out, stats)
  }
  return(stats_out)
}

term = "hotdog"
system(paste0("rm ~/hw4/kittens/images/*"))
stats_out <- get_stats(term, outPath = "~/hw4/kittens/images")

### percent of first page of google results recognized as hotdog
stats_out2 <- stats_out %>%
  group_by(n) %>%
  filter(score == max(score)) %>%
  ungroup() %>%
  select(class_description, score) %>%
  mutate(pizza = ifelse(grepl("hotdog|hot dog", class_description), 1, 0)) %>%
  summarize(mean(pizza))

cat("The neural net recognized", as.character(100*stats_out2),"%",
    "of the pictures of", term, "on the first page of Google results")

### top frequency item recognized of searchTerm
stats_out3 <- stats_out %>%
  select(-class_name, -score, -n) %>%
  group_by(class_description) %>%
  summarize(n = n()) %>%
  arrange(desc(n)) %>%
  head(15)















