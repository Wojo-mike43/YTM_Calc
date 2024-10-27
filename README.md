# YTM_Calc
This simple project calculates the yield-to-maturity of a bond based on provided inputs. The project requires no dependencies and solves a bond's YTM using a binary search algorithm.

**How it works:**
Users start by inputting simple variables such as:
- bond's current price
- par value
- coupon
- maturity (in years)

The script then starts by calculating the bond price with a guess YTM (consisting of a high and a low guess). The process is then repeated with the high and low guesses adjusted based on the difference between the bond's input price and the calculated price. Once the prices are within a tolerance of each other of 0.0001, the script returns the calculated YTM.
