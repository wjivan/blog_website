title: R functions
date: 2021-10-15
description: R functions that are worth remembering
image: /static/pictures/Gender/gender-equality.png
readtime: 2 MINS
time: TUESDAY, NOVEMBER, 2021
tags: ["R"]

# Some R functions that blew my mind recently

I use R at work and Python for my personal projects. I find that R's efficiency in data wrangling and visualisation is still really hard to beat. I stumbled across [David Robinson's Tidytuesday screencast](https://www.youtube.com/watch?v=5ub92c-5xFQ&t=119s) recently and it really blew my mind on the kind of efficiency you can obtain just sticking with the tidyverse packages. Here are some of the functions I have come to adopt from his videos. 

## 1. Using count() to understand categorical variables
There are many times where I find myself trying to understand what are the unique factors of the categorical variables and what are their counts. My usual approach to doing this is through `table$variable` or `unique(df$variable)` using base R functions or `df %>% distinct(variable)` using dplyr package. 

I now realise I could achieve so much more using `df %>% count(variable, sort = T)` which basically gives you a sorted unique table. There is also an option to sum up weights by a second variable like this `df %>% count(variable, sort = T, wt = weights)`

BONUS: There is also a function called `add_count(variable)` that adds a a counts column to the dataframe without the need to do `group_by(variable) %>% mutate(count = n())`. 

## 2. Using fct_lump_n() to group categorical variables
When we have a lot of levels in the categorical variables, sometimes what we are interested is in the top few categories and group the rest as "others". This function does that for you and it comes in a few flavours in the forcats package:

- `fct_lump_n()`: lumps all levels except for top `n` most frequent
- `fct_lump_min()`: allows you specify a minimum frequency
- `fct_lump_lowfreq()`: lumps all the low frequencies automatically such that the "others" category is still the lowest frequency

## 3. Using fct_reorder() + geom_col() + coord_flip
In [Story Telling with Data](https://www.amazon.co.uk/Storytelling-Data-Cole-Nussbaumer-Knaflic/dp/1119621496), Knaflic talked about using a **sorted horizontal barchart** for plotting. I really like this kind of bar charts for its easy readability and clear messages. In R, it is really easy to do this plot using the fct_reorder() + geom_col() + coord_flip() functions. The trick here is to do a `mutate(fct_reorder(plot_variable, val))` to sort the factor level in ascending order 

## 4. Using clean_names() to get nice column names
By default, this produces clean names in the snake format like `snake_format`. We can use this with `select(columnName1, columnName2) %>% clean_name()` to produce `column_name1, column_name2`. Super neat!

## 5. Using map_dfr() to join up all dataframes while using map function
Usually when I use map function, I would give it a list of dataframes and then apply the function of interest to get a list of dataframes. I will then use `reduce` and `bind_rows` to join up everything together. However, this can now be achieved in one step in `map_dfr()`. 



