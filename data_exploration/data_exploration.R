#Loading packages
library(tidyverse)

# Raw recipe and user data
RAWcipes <- read.csv("RAW_recipes.csv")
RAWteractions <- read.csv("RAW_interactions.csv")

# Count and average of each recipe reviews
interactions_avg_count <- RAWteractions |> group_by(recipe_id) |> 
  rename(id = `recipe_id`) |> summarize(Avg = mean(rating), Number_of_Reviews = n()) 

# DF to capture recipe info along with interaction average and count
recipe_and_reviews <- interactions_avg_count |> 
  inner_join(RAWcipes) |> select(id, name, Avg, Number_of_Reviews)

# Visualization of recipe review
ggplot(recipe_and_reviews, aes(x = Number_of_Reviews, fill = factor(Number_of_Reviews))) +
  geom_histogram(fill = "skyblue", color = "white") +
  scale_x_log10() +
  ggtitle("Distribution of Recepie Review Count (log scale)") +
  xlab("Number of Reviews for a Recipe") +
  ylab("Number of Recipes with that number of Reviews") 
  
# Count of each recipes reviews
recipe_and_reviews |> group_by(`Number_of_Reviews`) |> 
  summarize(count = n())

# Visualization of each recipes review
ggplot(recipe_and_reviews, aes(x = Avg, fill = factor(Avg))) +
  geom_histogram(fill = "orange", color = "white", bins = 50) +
  ggtitle("Recipe Review Distribution (sqrt scale)") +
  xlab("Avg. Review") +
  ylab("Avg. Review Count") +
  scale_y_sqrt()
  
# Percentage of recipes with description
percentage_w_description <- RAWcipes |> summarise(amount = sum(description != "")/n())

# Average number of tags per recipe
array_sizes <- map_int(RAWcipes$tags, ~ length(str_split(.x, ",")[[1]]))
mean(array_sizes)
min(array_sizes)
max(array_sizes)

# Average count of how many review each user left
Avg_user_reviews <- RAWteractions |> 
  group_by(`user_id`) |> summarize(count=n()) |> summarize(Avg=mean(count))

# Count of how many reviews each user left 
User_Review_Avg <- RAWteractions |> 
  group_by(`user_id`) |> summarize(count=n()) 

# Visualization of user review distribution
User_Review_Avg |> ggplot(aes(count)) + geom_histogram(fill = "purple", color = "white") + 
  scale_y_log10(labels = function(x) format(x, scientific = FALSE)) + scale_x_sqrt() + 
  ggtitle("Number of Review by User (log Scale)") +
  xlab("Amount of Reviews") + ylab("Users w/ given number of reviews")

mean_recipe_rating <- RAWteractions |> group_by(recipe_id) |> 
  summarize(Avg = mean(rating)) |> rename(id = recipe_id) |> 
  inner_join(RAWcipes) |>  select(id, contributor_id, Avg)

contribution_count <- RAWcipes |> group_by(contributor_id) |> 
  summarise(amount = n()) 

Avg_avg <- mean_recipe_rating |> group_by(contributor_id) |> 
  summarize(Avg.avg = mean(Avg))

Avg_avg |> inner_join(contribution_count) |>
  ggplot(aes(x = amount, y = Avg.avg, color = amount)) +
  geom_point(show.legend = FALSE) +
  scale_x_log10() +
  scale_color_gradient(low = "lightgreen", high = "black") +
  ylab("Average of the Average Rating") +
  xlab("Amount of Contributions") +
  ggtitle("Average of the Contributors Average Recipe Review (sqrt scale)")
            