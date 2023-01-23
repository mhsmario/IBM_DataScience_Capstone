Author: Mario Saraiva
Date: Jan, 2023

# IBM_DataScience_Capstone
  IBM data science capstone as part of the last module of the  IBM Data Science PROFESSIONAL CERTIFICATE.
  Learn more about the IBM professional certification [here](https://www.coursera.org/professional-certificates/ibm-data-science).


## Executive Summary
  The goal of this project is to predict if the first stage of the SpaceX Falcon 9 rocket will
  land successfully.

  • The process behind the prediction models used follow the Data Science methodology
  including data collection (API and Web Scrapping), data wrangling (Pandas and Numpy
  Libraries), exploratory data analysis (EDA with SQL), data visualization (Seaborn,
  Plotly/Dash, and Folium), model development (GridSearch) and evaluation (Accuracy
  scores and Confusion Matrix).

  • The main findings are the following:
    1. Payload mass and launch site are key predictors. These two variables are extensively explored
    throughout this report.
    2. The best performing model was the Decision Tree Classifier;
    3. All machine learning models appear to be overfitting the testing data due to a small sample size.
    
 ##Introduction
    • SpaceX (advertises) Falcon 9 rocket launches costs approximately 62 million dollars;
    other providers cost upward of 165 million dollars each, much of the savings is
    because SpaceX can reuse the first stage.
    • Therefore if we can predict if the first stage will land, we can determine the cost
    of a launch. This information may be important to investors and competitors
    considering the cost and future of rocket launches.
  
  ##Methodology
      (*) Data collection methodology: SpaceX API GET Request and Web Scrapping (bs4) Wikipedia
      (*) Perform data wrangling: The data wrangling consisted of two sections: (1) Exploratory Data Analysis; (2) Deciding on Training Labels
      (*) Perform exploratory data analysis (EDA) using visualization and SQL: Pandas and Numpy Libraries + SQL queries. Seaborn and Ploty data visualizations.
      (*) Perform interactive visual analytics using Folium and Plotly Dash
      (*) Perform predictive analysis using classification models: Models used are: 
        (1) Logistic Regression, 
        (2) Sector Vector Machine, 
        (3) Decision Tree Classifier, and 
        (4) K-nearest neighbors.

  ## Data Collection
  
    • Data was collected from SpaceX's API and scrapped from the Wikipedia (Falcon 9 and Falcon
  Heavy launches [page]((https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches))).
  
    • From the API, our request focused on getting the following data regarding: rockets,
    launchpad, payload, the outcome of the landing, the type of the landing, number of flights with
    that core, whether gridfins were used, whether the core is reused, whether legs were used, the
    landing pad used, the block of the core which is a number used to separate version of cores, the
    number of times this specific core has been reused, and the serial of the core. We limited the
    data to Falcon 9 launches.

    • From Wikipedia, we scrapped Falcon 9 historical launch records from a (9th June 2021
    page titled 'List of Falcon 9 and Falcon Heavy launches' . A GET Request with BeaufitulSoup (bs4)
    were used to extract the data.
  
  ## Data Wrangling (summary)
  
    • Only the Pandas and Numpy libraries were used in the data wrangling script.
    • Exploratory Data Analysis
      • Calculate the number of launches on each site;
      • Calculate the number and occurrence of each orbit;
      • Calculate the number and occurrence of mission outcome per orbit type.
    • Deciding on Training Labels
      • Create a landing outcome label;
      • Success = 1 and Failure = 0.
   
   ##E DA with Data Visualization
   
     (*) Plot Summary: We used plots to understand the relationship between the variables and the success rate. This understanding is key to predicting the outcome.
        • Plot 1: The Flight Number and Pay load Mass and overlay the outcome of the launch.
        • Plot 2: Flight Number and Launch Site. • Plot 3: Payload and Launch Site.
        • Plot 4: Success rate per Orbit.
        • Plot 5: Flight Number and Orbit.
        • Plot 6: Launch success yearly trend.¶
      
   ## EDA with SQL
    • In total 10 queries were performed as part of the EDA seeking to understand:
    • The Context: The first four queries were to understand the distinct launch sites, maximum and average
    payload mass used.
    • The Timeline: A query was used to get the date of the first successful landing.
    • The Payload mass: A query was used to explore the relationship between successful drone ship landings with payload mass between 4.000 – 6.000 Kg. A query investigated the relationship between booster version and max payload mass.
    • The Success rate: A query was used to summarize total success and failure outcomes. Lastly, we ranked the count of landing outcomes (such as Failure or Success) between 2010-06-04 and 2017-03-20.
    
   ## Interactive Map with Folium
     • In our Folium map we:
        • Marked all launch sites on a map;
        • Marked the success/failed launches for each site on the map;
        • Calculated the distances between a launch site and the coastline
    • The map is an important visualization to help assess geographical patterns between sites that affect the outcome of landings.
    
    ## Dashboard with Plotly Dash
    
      • The Dashboard comprises of two visualizations – (1) a Pie Chart with the success ratio according to the site and (2) a scatter plot   displaying the relationship between Payload mass, landing outcome and Booster version used.
      • The goal was to identify which sites had the most (and least) successful landings and to further explore and quantify the ideal payload mass associated with successful outcomes.
    
    ## Predictive Analysis (Classification)
    
      • Summarize how you built, evaluated, improved, and found the best performing classification model
      • You need present your model development process using key phrases and flowchart
      • Add the GitHub URL of your completed predictive analysis lab, as an external reference and peer-review purpose
      
   ## CONCLUSION
   
    • The purpose of this project is to determine the cost of a launch by predicting if the Falcon 9 first stage will land successfully.
    • As seen throughout this report, payload mass and launch site are very important factors associated with the landing outcome. Other variables such as booster version and orbit show mixed results in regards to its impact on the outcome.
    • The position of the launching site relative to the coastline and the Tropic of Cancer are important variables that must be further explored.
    • All our classification models performed well. Our best model was the Decision Tree Classifier. However, our testing sample was very small (n = 18) and the results are likely to be a classical example of model overfitting.
    • The next step in this work is to test our models with out-of-sample data and to validate the relationship between proximity to coastline and the Tropic of Cancer.
