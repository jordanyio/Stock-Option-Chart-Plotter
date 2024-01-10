import yfinance as yf
import mplfinance as mpf
import tkinter as tk

# Create a tkinter window
root = tk.Tk()

# Add a label and entry widget for stock symbol
label1 = tk.Label(root, text="Enter the stock symbol:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

# Add a label and entry widgets for start and end dates
label2 = tk.Label(root, text="Enter start date (YYYY-MM-DD):")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Enter end date (YYYY-MM-DD):")
label3.grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

# Define a function to submit the form
def submit():
    symbol = entry1.get()
    start_date = entry2.get()
    end_date = entry3.get()
    data = yf.download(symbol, start=start_date, end=end_date, interval='1d')
    mc = mpf.make_marketcolors(up='g', down='r', edge='inherit', wick='inherit', volume='in')
    s = mpf.make_mpf_style(marketcolors=mc, gridcolor='lightgrey')
    mpf.plot(data, type='candle', style=s, volume=True, ylabel=symbol)

# Add a submit button
button1 = tk.Button(root, text="Submit", command=submit)
button1.grid(row=3, column=1)

# Run the tkinter event loop
root.mainloop()
