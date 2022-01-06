title: Is Modern House able to sell houses at a premium?
date: 2020-01-15
description: Modern House is a prime real estate broker but can it actually outperform on its listings compared to other agencies?
image: /static/pictures/modernhouse/pictures/modernhouse/output.png
time: TUESDAY, DECEMBER 15, 2020
tags: ["Web scraping", "API", "Applied Data Science", "Project"]

# The Modern House Premium

[The Modern House](https://www.themodernhouse.com) is a niche real estate agent that lists only architecturally unique homes for sale. The listings are tastefully presented with professional photos and introduction into the architecture history of the building. As such, the website claims that they are able to achieve a 12% premium in selling prices compared with other real estate agencies. 

<img class="responsive-img" src="static/pictures/modernhouse/dataloft.png">

I attempt to verify this claim through a webscraping exercise. To do this, I scrape Modern House's current listing prices, address and number of bedrooms from their website. I then use the Zoopla API to download price information of other house for sale around 0.5 mile radius of the Modern House listings to get a sense of average selling price of the neighbourhood. I then compare to see if the Modern House listings do actually have a premium price listing compared to its neighbours. 

## 1. Data collection

### Webscraping The Modern House website using Selenium & Beautiful Soup

The modern house url ends with all the houses on sale for a specific number of bedrooms. Ideally, I would need the per square meter prices of a property. However, this information is only available in the form of floor plan which is in a PDF image. The closest approximation to the size would be number of bedrooms. My strategy is to create functions to scroll through the website and collect data. This is then repeated for all the pages for different number of bedrooms. 

<img class="responsive-img" src='static/pictures/modernhouse/dataframe.jpg'>

### Download neighbourhood price data from Zoopla API
The Zoopla API breaks easily but I was able to extract some data to compare with some of the listing data found on Modern House

<img class="responsive-img" src='static/pictures/modernhouse/datazoopla.jpg'>


## 2. Data cleaning

### Cleaning the scraping data from Modern House
The main problems are:
1. Changing price data to numeric
2. Parts of the address data is within the postcode column: Need to split out the address into building, block, street, postcode and area

After cleaning the data, I visualise the data in a regression to check if the data fits common sense. I would think that there would be a positive correlation between house prices and the number of bedrooms. 

<img class="responsive-img" src='static/pictures/modernhouse/modernhousereg.png'>

### Cleaning the API data from Zoopla
The data from the API is relatively clean. I just need to match it to the Modern House data so that I have neighbourhood data merged into one. I visualise this using Folium to add some interactivity to make sure that visually I'm getting the right neighbourhoods. Icons in red are ModernHouse and green are the neighbourhood. 

<img class="responsive-img" src='static/pictures/modernhouse/folium.jpg'>
The map shows that there are certain outliers that I would need to remove because they are miles away from the Modern House buildings. 

## 3. Analysis
In order to have a fair comparison, ideally we would really need size data from Modern House. This is because prices are very sensitive to sizes especially in London. In fact there are many other variables to adjust for in order to compare houses like-for-like. As such, the claims that Modern House can bring in more premium is really difficult to justify with my limited dataset. However it was still a lot of fun trying. The output I could get to is below:

<img class="responsive-img" src='static/pictures/modernhouse/output.png'>

For code and further analysis, see [Github repo](https://github.com/wjivan/modernhousescraper)

