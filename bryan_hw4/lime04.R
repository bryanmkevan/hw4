#install.packages("magick")
#install.packages("lime")

suppressMessages(suppressWarnings(library(keras)))
suppressMessages(suppressWarnings(library(lime)))
suppressMessages(suppressWarnings(library(magick)))
suppressMessages(suppressWarnings(library(dplyr)))
suppressMessages(suppressWarnings(library("rvest")))
suppressMessages(suppressWarnings(library(tensorflow)))

args <- commandArgs(TRUE)

## Search term
term = as.character(args[1])

# Create temp folder
system("mkdir /home/bryanmkevan/hw4/bryan_hw4/images")

## Testing image accuracy
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
    download.file(imageurl[i],
                  destfile = paste0(outPath, "/", i, ".jpg"),
                  mode = 'wb',
                  quiet = TRUE)
  }
}

get_stats <- function(term, outPath) {
  
  url <- paste0("https://www.google.com/search?q=", term,
                "&source=lnms&tbm=isch&sa=X&tbs=isz:m")
  download_images(term, url, outPath)
  
  ## Create bin for output stats
  stats_out <- matrix(nrow = 0, ncol = 3)
  for (i in c(1:length(list.files(outPath)))) {
    img <- image_read(paste0(outPath, "/",i,".jpg"))
    img_path <- file.path(tempdir(), 'image.jpg')
    image_write(img, img_path)
    
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

stats_out <- get_stats(term, outPath = "/home/bryanmkevan/hw4/bryan_hw4/images")

### percent of first page of google results recognized as containing 'term'
stats_out2 <- stats_out %>%
  group_by(n) %>%
  filter(score == max(score)) %>%
  ungroup() %>%
  select(class_description, score) %>%
  mutate(item = ifelse(grepl(term, class_description), 1, 0)) %>%
  summarize(mean(item))

cat("The neural net recognized", as.character(100*stats_out2),"%",
    "of the pictures of", term, "on the first page of Google results \n\n")

### top frequency item recognized of 'term'

cat("Here are the top items that were identified as", term, 
    " in the first page of images:\n")

stats_out3 <- stats_out %>%
  select(-class_name, -score, -n) %>%
  group_by(class_description) %>%
  summarize(n = n()) %>%
  arrange(desc(n)) %>%
  head(15)

as.data.frame(stats_out3)

# remove temp files

system("rm -r /home/bryanmkevan/hw4/bryan_hw4/images")












