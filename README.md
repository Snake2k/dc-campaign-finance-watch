

# DC Campaign Finance Watch

DC Campaign Finance Watch uses open source tools and publicly available data to show the public where the money in politics is coming from and going to.

## Components

The project comprises several components.  

### DC Campaign Finance Scraper

This will go away soon, as DC will provide data via a nice API. Thanks Tim! 

The DC Campaign Finance Scraper pulls campaign contribution and expenditure data from the District's Office of Campaign Finance Website and converts it into a CSV file for further analysis. You can obtain it here: [https://github.com/codefordc/dc-campaign-finance-scraper](https://github.com/codefordc/dc-campaign-finance-scraper).  It is currently fully functional and should work.  If you have any problems with it, please let us know.

### DC Public Contracts and Procurement Scraper

The DC Public Contracts Scraper pulls data from the District's [Office of Campaign Finance Website] (http://app.ocp.dc.gov/RUI/information/award/search.asp) and converts it into a CSV file for further analysis. It is a python script that is located in the 'wrangler' directory of the 'watch' repo. 


#### DC Campaign Finance Wrangler

These are python scripts that we use to analyze the data.  They are broken into two functions, each of which is intended to be run every night.  (1) download (downloads campaign finance and public contract data); (2) wrangler (turns that data into graphable json files for the website).  They are scripts located in the 'wrangler' directory of the 'watch' repo. 

#### DC Campaign Finance Data

This is the source data we scrape OCF and OCP. They are csv files located in the 'csv' directory of the 'watch' repo. 

### DC Campaign Finance Watch

Where you are now.  This is the front end that display the analyses we develop.


# Roadmap

The following describes a provisional path for the development of the website that will track campaign finance data, and help citizens, news media, and candidates make sense of that data with those tools.

Our roadmap recognizes that all data analysis is normative; every display tells a story and helps people draw conclusions. As such, we pay close attention to the kinds of stories our analyses underwrite. It also acknowledges that some projects are more ambitious than others, and will require more data than we have at present.

Just as importantly, the roadmap avoids analyses that are already available or that support the misdirection of political representation by turning campaigns into fundraising contests.  The “warchest competition narrative” that supports stories about which candidate is likely to succeed based on the amount of cash they have raised is both lazy and corrupting, and we will avoid producing materials that support it.  It is lazy because it takes the easiest data to access -- topline fundraising numbers -- and says nothing about how they relate to candidates’ connections to the public interest, to corporate interests, or to pay-to-play norms that are all-too-prevalent in District politics.

##Candidates

We'd like to have a page showing all elected officials with summary data. The data will show: (1) money quality (grassroots v corporate cash); and (2) data quality (percentage of filing data that is complete / missing). 

####Organization

The page will list the races in the following order:

```
All Offices
++++
Mayor
++++
Council Chair
Council at Large
Council Ward 1
…
Council Ward 8
++++
School Board at Large
School Board Ward 1
…
School Board Ward 8
++++
US Representative
US Senator
```
[Quick mockup](https://docs.google.com/presentation/d/1WvTNgmqvy31nZ-25LUniX8EGbF74IiSDPwPWQs6W9BI)

When any candidate is selected, a Summary page will show the  most important summary for the official, and invite a click-through to more detailed data. 

##Elected Officials 

Do the same thing for elected officials.   Of course, once they start voting, there are some other analyses we can do. 

##Pay-to-Play

Link campaign contributions to District contracts [like this](http://wamu.org/projects/paytoplay/#/officials), but open source and programatic.  The cash paid to office holders’ campaigns will be linked to past, existing, and pending contracts with the city. 

Expose [OCP Contract and Procurement Data](http://app.ocp.dc.gov/RUI/information/award/search.asp) via API?

Use [dedupe](https://github.com/datamade/dedupe-examples) to wrangle names and addresses of contractors and donors? 

##Industry Influence

Using NIGP codes and all available online data, we will link donors with specific industries. We can then sort each candidate and political office-holder by level of industry influence and relate them to upcoming bills.

In DC -  Solicitations and local registered CBE’s use something called [NIGP codes](https://en.wikipedia.org/wiki/NIGP_Code).  Lookups are available [here](http://app.ocp.dc.gov/RUI/information/nigplist.asp) and [here](http://vendornet.state.wi.us/vendornet/asp/CC13_Process.asp).

One can find local businesses [here](https://lsdbe.dslbd.dc.gov/public/certification/search.aspx) and if one click on a business the NIGP codes for which it is certified are revealed.  One caveat, this is only DC CBE’s – so will not capture any information about the Large Businesses (Deloitte, CACI, etc.) that do business in the District and CBE’s can win solicitations in other than their NIGP codes.

##Basic contributor search

Organize the data by contributor, to generate a table of top contributors, and power a search wherein a citizen can enter the name of a individual or organization to see a basic table of contribution history -- how much have they given, to whome, when. Ideally this eventually covers both current cycle and historical races. 

##Twitter Servo
Like this: [https://github.com/vzvenyach/scotus-servo](https://github.com/vzvenyach/scotus-servo), but for data from the DC OCF

###Future Goals:

Location based information for relevant races.

[Greenhouse](http://allaregreen.us/) for dc.

A moving average of corporate capture & grass roots support for each current officeholder. Will span available data.

Add blog. Maybe using Poole? Include in angular gh-pages or vice-versa? Custom domain?

Add party affiliations. Would be a new code related to candidate & election cycle (some candidates change affiliation).

contribution timing / filters. Post-election & pre-legislation contributions to catch "pay-to-play" post-win contributions.

Big v Small donors: Count of small donors; Count of large donors; Sum of small donors; Sum of large donors; Percent of “max-ers”

Burn rate. Show area chart of cash on hand (contributions & expenditures).

non-local influence. Show contributions from DC v outside DC.

Show percentage of each candidates donors from each ward/zip/etc. (heat map?)

2 Lederboards for each race, each of which will show each candidate relative to historical mean & sd for their office. 

  GRASSROOTS LEADERBOARD: 
   - percentage of grassroots donors
   - number of grassroots donors
   - percentage of small donors
   - number of small donors
   - and the average (of standard deviations reative to the means) 
   
  CORPORATE TOOL LEADERBOARD: 
   - percentage of corporate-style donors
   - number of corporate-style donors
   - percentage of corporate-style dollars
   - number of small corporate-style dollars
   - and the average (of standard deviations reative to the means) 

Breakout contributions by year, office and candidate into seperate json files.  This will allow us to track changes as they update. 

[Quick mockup](https://docs.google.com/presentation/d/1WvTNgmqvy31nZ-25LUniX8EGbF74IiSDPwPWQs6W9BI)
