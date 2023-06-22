import yfinance as yf
import mplfinance as mpf
import tkinter as tk

# Create a tkinter window
root = tk.Tk()

# Add a label widget
label1 = tk.Label(root, text="Enter the stock symbol:")
label1.grid(row=0, column=0)

# Add an entry widget
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

# Add a label widget
label2 = tk.Label(root, text="Choose a timespan:")
label2.grid(row=1, column=0)

# Add an option menu widget
timespan_var = tk.StringVar(root)
timespan_var.set('1mo')
timespan_option = tk.OptionMenu(root, timespan_var, '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
timespan_option.grid(row=1, column=1)

# Define a function to submit the form
def submit():
    symbol = entry1.get()
    timespan = timespan_var.get()
    data = yf.download(symbol, period=timespan, interval='1d')
    mc = mpf.make_marketcolors(up='g',down='r',edge='inherit',wick='inherit',volume='in')
    s = mpf.make_mpf_style(marketcolors=mc, gridcolor='lightgrey')
    mpf.plot(data, type='candle', style=s, volume=True, ylabel=symbol)
    
# Add a button widget
button1 = tk.Button(root, text="Submit", command=submit)
button1.grid(row=2, column=1)

# Run the tkinter event loop
root.mainloop()
