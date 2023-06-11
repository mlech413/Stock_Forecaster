# Stock Market Predictor

The website for this information can be found at [stock-forecaster.herokuapp.com](https://stock-forecaster.herokuapp.com/).

## Summary

The Vix is the popular name for the Chicago Board Options Exchange's Volatility Index, a measure of the stock market's expected volatility based on S&P 500 index options. It is often referred to as the fear index or fear gauge. The Vix signals the level of fear or stress in the stock market. The higher the VIX, the greater the level of fear and uncertainty in the market, with levels above 30 indicating high levels of uncertainty.

The S&P 500 is the Standard and Poor's 500 index - a stock market index tracking the stock performance of 500 of the largest companies listed on stock exchanges in the United States. It is one of the most commonly followed equity indices, and is the index frequently referred to as "the market".

Machine learning models here demonstrate how elevated levels of the Vix can help predict a positive gain for the S&P 500 index one year into the future. When the Vix rises above 35, and especially above 50, this chart illustrates the historical return on the S&P 500 over the following year.

![alt text](./static/images/vix_sp500_regressions.jpg)
The performance of the S&P 500 is charted here from 2000-2023.

For each day, the one-year future return of the S&P 500 is plotted, with the percentage return on left (y-axis). The bottom (x-axis) shows the corresponding Vix value one-year prior. When the Vix is above 35, the S&P 500 has yielded positive returns 92.5% of the time over the following year. When the Vix exceeds 50, 98.6% of the returns were positive.


