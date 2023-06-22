# Stock-Option-Chart-Plotter
The code you sets up a tkinter window with a label, entry widget, option menu, and a submit button. 
When the user enters a stock symbol and selects a timespan from the dropdown menu, the submit() function is called. 
In the function, it uses the yfinance library to download stock price data for the specified symbol and timespan.

This works for any ticker, stock tickers and option tickers. 
I primarily use it for option tickers since those charts arent always readily avaliable. 

To use this code, you need to make sure you have yfinance and mplfinance libraries installed. 
You can install them using pip:     pip install yfinance mplfinance
tkinter should be included with python. 
