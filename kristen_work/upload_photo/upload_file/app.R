library(shiny)

# Define UI for data upload app ----
shinyUI(fluidPage(
  
  # App title ----
  titlePanel("Uploading Files"),
  
  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    
    # Sidebar panel for inputs ----
    sidebarPanel(
      
      # Input: Select a file ----
            fileInput(inputId = 'files', 
                      label = 'Select an Image',
                      multiple = TRUE,
                      accept=c('image/png', 'image/jpeg'))),

      # Horizontal line ----
      tags$hr()
    ),
    
    # Main panel for displaying outputs ----
    mainPanel(
      tableOutput('files'),
      uiOutput('images')
    )
    
  )
)



# Define server logic to read selected file ----
  server <- function(input, output) {
# 
#   output$file2 <- renderImage({
#     
#     # Generate the image file
#     png(file1, width = 100, height = 100,
#         res = 72)
     imageOutput("file1")
#     })
#   
#   output$preImage <- renderImage({
#     # When input$n is 3, filename is ./images/image3.jpeg
#     filename <- normalizePath(file.path('/home/kristenmae/biostat-m280-2019-winter/hw4/kristen_work/cookies/images',
#                                         paste('10', '.jpeg', sep='')))
#     
#   }, deleteFile = FALSE)
#   
#   
#   
#   
}
# Run the app ----
shinyApp(ui, server)