## Time Series Forecasting for Tech Mahindra Stock Prices

### Overview
- This is my project on time series forecasting, where I predict stock prices for **Tech Mahindra (BSE: TECHM)** using historical data from 2020-08-23 to 2025-08-23. 
- I built this Jupyter notebook to demonstrate how to fetch, preprocess, visualize, and forecast stock prices using two popular models: **ARIMA** and **Prophet**. 
- My goal was to compare these models and explore their strengths for financial time series analysis.

### Project Structure
The notebook (`Time_series_prediction.ipynb`) is organized as follows:
- **Data Collection**: I used the `yfinance` library to download daily stock data (Open, High, Low, Close, Volume) for Tech Mahindra (`TECHM.BO`) and saved it as `TECHM.csv`.
- **Data Preprocessing**: I converted the `Date` column to datetime, set it as the index, and inspected the dataset for completeness.
- **Exploratory Data Analysis (EDA)**: I plotted the closing price trend to identify patterns like trends or volatility.
- **Modeling**:
  - **ARIMA**: I applied the ARIMA model to capture linear trends and autocorrelations (assuming stationarity after differencing).
  - **Prophet**: I used Prophet to model trends and seasonality, leveraging its ability to handle complex patterns.
- **Forecasting and Evaluation**: I generated forecasts for both models, visualized the Prophet predictions, and saved them to `Prophet_forecast.csv`. I also compared the models based on their strengths and use cases.

### Summary 
- I concluded with a comparison of ARIMA (better for short-term, linear trends) and Prophet (great for seasonality and longer-term forecasts).