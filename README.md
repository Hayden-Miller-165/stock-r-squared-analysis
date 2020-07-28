# Stocks-and-Indices-R-Squared-Analysis
Finds the highest R-squared of any two variables. Variables can be either a stock or index found on Yahoo Finance or an economic data table found on the St. Louis Federal Reserve Economic Data site.

Packages needed for program: pandas, pandas_datareader, scipy

1. Specify desired stock or index ticker(s) if applicable
2. Pulls adjusted close info for each stock or index in from Yahoo Finance
3. Specify Federal Reserve Economic Data ticker(s) if applicable
4. Pulls FRED ticker data from FRED site
5. Loops through data and finds total number of Nan values in each column to remove
6. Creates % Change columns based on prior period
7. Calculates the R-squared for each possible combination and prints the two variables with the highest R-squared value
