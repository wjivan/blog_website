title: Network analysis of power and influence in foreign aid
date: 2020-01-15
description: Hypothesize that foreign aid is used as a political tool to gain influence in developing countries
image: /static/pictures/foreignaid/thumb.jpg
tags: ["Network analysis, R, Visualisation"]

###### Dataset and descriptive statistics
The OECD dataset contains information on donor commitments for ten years spanning 2009-2018 (inclusive). This allows us to understand how donor behaviour changes over time. 

<figure> 
    <img class="responsive-img" src="/static/pictures/foreignaid/donor_table.png">
    <figcaption>Table 1: Summary of donor counts and top 5 donor countries 2009-2018</figcaption>
</figure>

Table 1 shows that on average, the number of donors has increased slightly over the years from 21 in 2009 to 30 in 2018. Total amount of aid for renewable energy has increased from USD $1.1bn in 2009 to USD $3.5bn in 2018. Germany, Japan and France are consistently among the top five donor countries in the past ten years by total amount of aid committed. In fact, the top five donor countries represent about 87%-94% of total aid over the decade. The average aid committed is around USD $10m while the median is around USD $1m,  showing a huge skew on some of the bigger aid commitments. 

These aid flow into recipient countries to support local efforts for renewable energy projects. Table 2 shows that aid is distributed to around 96-115 countries over the decade. Unlike the donor countries which are rather stable, the top five recipients change considerably from year to year. 

<figure> 
    <img class="responsive-img" src="/static/pictures/foreignaid/recipient_table.png">
    <figcaption>Table 2: Summary of recipient counts and top 5 recipient countries 2009-2018</figcaption>
</figure>

###### Network analysis
One of the hypotheses of this paper is that aid flows can be politically motivated. Network analysis of aid flows can be used to quantify the proportionate size of impact a donor can have on recipients in the aid flow network. 

We represent each country (donor or recipient) as a node in the network. The aid flow from the donor to recipient represent edges in the network, creating links from one node to the other. To illustrate this, we take the top 5 donors in 2018 and their aid flows to form the aid flow network shown in Figure 1.

<figure> 
    <img class="responsive-img" src="/static/pictures/foreignaid/top5_network.png">
    <figcaption>Figure 1: Illustrative network for top 5 donors in 2018</figcaption>
</figure>

We can see from the aid flow network that there are some recipients who are solely dependent on one donor whereas others are dependent on several donors. The colours of the network show the principal donor for each recipient – i.e. the donor providing the highest share of aid for that recipient. 

One way of measuring the power dynamics between donor and recipients is through the share of donation a donor country provides to the recipient. Visually, if we isolate the top recipients of aid in 2018, we could see that each of these recipients receives aid from a diverse set of donors. 

<figure> 
    <img class="responsive-img" src="/static/pictures/foreignaid/significant_recipients.png">
    <figcaption>Figure 2 Top 5 recipient's aid network in 2018</figcaption>
</figure>

Figure 2 shows that, for example, Morocco receives aid from France, Spain and Germany. To proxy the power relationship between the donors to the recipient, we calculate which donor country provides the highest share of aid to Morocco. 

More formally, for each triadic donor-recipient-year pair, we calculate the weighted share in-degree centrality in the network, given by the formula below. 
