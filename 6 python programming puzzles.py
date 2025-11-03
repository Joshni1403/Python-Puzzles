# Python Programming Puzzles
# Instructions: Solve each puzzle and commit your solutions to GitHub

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("PYTHON PROGRAMMING PUZZLES")
print("=" * 60)
print("Instructions:")
print("1. Solve each puzzle in order")
print("2. Test your solutions with the provided sample data")
print("3. Commit your solutions to your GitHub repository (later)")
print("4. Include proper documentation and comments")
print("5. Add visualizations where appropriate")
print("=" * 60)

# =============================================================================
# PUZZLE 1: SUPPLY AND DEMAND EQUILIBRIUM
# Difficulty: Beginner
# =============================================================================

print("\n🧩 PUZZLE 1: Find Market Equilibrium")
print("─" * 35)
print("Given supply and demand functions, find the equilibrium price and quantity")
print("Supply: Qs = -10 + 2*P")
print("Demand: Qd = 100 - 3*P")

def find_equilibrium(supply_intercept, supply_slope, demand_intercept, demand_slope):
    """
    Find market equilibrium point where supply equals demand.

    Supply: Qs = supply_intercept + supply_slope * P
    Demand: Qd = demand_intercept + demand_slope * P

    Requirements:
    1. Calculate equilibrium price
    2. Calculate equilibrium quantity
    3. Return both as a dictionary
    4. Handle the case where lines are parallel (no equilibrium)

    Args:
        supply_intercept (float): Supply curve intercept
        supply_slope (float): Supply curve slope
        demand_intercept (float): Demand curve intercept
        demand_slope (float): Demand curve slope (should be negative)

    Returns:
        dict: {'price': float, 'quantity': float} or None if no equilibrium
    """
    # YOUR CODE HERE
    pass

def plot_supply_demand(supply_intercept, supply_slope, demand_intercept, demand_slope, equilibrium):
    """
    Plot supply and demand curves with equilibrium point marked.

    Requirements:
    1. Create price range from 0 to reasonable maximum
    2. Calculate quantity for each curve at each price
    3. Plot both curves on same graph
    4. Mark equilibrium point with a red dot
    5. Add labels, legend, and title
    """
    # YOUR CODE HERE
    pass

print("Test case: Supply: Qs = -10 + 2*P, Demand: Qd = 100 - 3*P")
print("Expected equilibrium: P = 22, Q = 34")

# =============================================================================
# PUZZLE 2: ELASTICITY CALCULATOR
# Difficulty: Beginner-Intermediate
# =============================================================================

print("\n🧩 PUZZLE 2: Calculate Price Elasticity of Demand")
print("─" * 48)
print("Calculate price elasticity using the midpoint method")

# Sample price and quantity data
price_quantity_data = pd.DataFrame({
    'price': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'quantity_demanded': [5, 8, 12, 17, 23, 30, 38, 47, 57, 68]
})

def calculate_elasticity(price1, quantity1, price2, quantity2):
    """
    Calculate price elasticity of demand using midpoint method.

    Formula: Elasticity = (% change in quantity) / (% change in price)
    Midpoint method: ((Q2-Q1)/((Q2+Q1)/2)) / ((P2-P1)/((P2+P1)/2))

    Requirements:
    1. Use midpoint method for accurate calculation
    2. Handle division by zero
    3. Return the elasticity value
    4. Classify as elastic, inelastic, or unit elastic

    Args:
        price1, price2 (float): Initial and final prices
        quantity1, quantity2 (float): Initial and final quantities

    Returns:
        dict: {'elasticity': float, 'classification': str}
    """
    # YOUR CODE HERE
    pass

def analyze_demand_curve(df):
    """
    Analyze entire demand curve and calculate elasticity at each point.

    Requirements:
    1. Calculate elasticity between each consecutive pair of points
    2. Classify each elasticity
    3. Create a summary DataFrame
    4. Plot demand curve with elasticity regions marked

    Args:
        df (pd.DataFrame): DataFrame with 'price' and 'quantity_demanded' columns

    Returns:
        pd.DataFrame: Summary with price ranges and elasticities
    """
    # YOUR CODE HERE
    pass

print("Test with the provided price_quantity_data")
print("Expected: Elasticity should vary along the demand curve")

# =============================================================================
# PUZZLE 3: CONSUMER AND PRODUCER SURPLUS
# Difficulty: Intermediate
# =============================================================================

print("\n🧩 PUZZLE 3: Calculate Economic Surplus")
print("─" * 38)
print("Calculate consumer surplus, producer surplus, and deadweight loss")

def calculate_surplus(demand_intercept, demand_slope, supply_intercept, supply_slope,
                     price=None, quantity=None):
    """
    Calculate consumer and producer surplus at market equilibrium or given price.

    Requirements:
    1. Find equilibrium if price/quantity not provided
    2. Calculate consumer surplus (area under demand curve above price)
    3. Calculate producer surplus (area above supply curve below price)
    4. Calculate total surplus
    5. Handle linear demand and supply curves

    Args:
        demand_intercept, demand_slope: Demand curve parameters
        supply_intercept, supply_slope: Supply curve parameters
        price, quantity: Optional specific price/quantity (default: equilibrium)

    Returns:
        dict: {'consumer_surplus': float, 'producer_surplus': float,
               'total_surplus': float, 'price': float, 'quantity': float}
    """
    # YOUR CODE HERE
    pass

def deadweight_loss_analysis(demand_intercept, demand_slope, supply_intercept, supply_slope,
                           regulated_price):
    """
    Calculate deadweight loss when price is regulated (price ceiling/floor).

    Requirements:
    1. Calculate equilibrium surplus
    2. Calculate surplus at regulated price
    3. Calculate deadweight loss
    4. Determine if regulation is price ceiling or floor
    5. Calculate shortage or surplus quantity

    Args:
        demand_intercept, demand_slope: Demand curve parameters
        supply_intercept, supply_slope: Supply curve parameters
        regulated_price: Government-imposed price

    Returns:
        dict: Analysis results including deadweight loss
    """
    # YOUR CODE HERE
    pass

print("Test case: Same supply/demand from Puzzle 1")
print("Try regulated price of 15 (price ceiling)")

# =============================================================================
# PUZZLE 4: BUDGET CONSTRAINT AND UTILITY MAXIMIZATION
# Difficulty: Intermediate
# =============================================================================

print("\n🧩 PUZZLE 4: Consumer Choice Theory")
print("─" * 37)
print("Find optimal consumption bundle given budget constraint and preferences")

def budget_constraint(income, price_x, price_y):
    """
    Generate budget constraint line: income = price_x * x + price_y * y

    Requirements:
    1. Create array of possible x values
    2. Calculate corresponding y values
    3. Handle boundary conditions
    4. Return feasible consumption combinations

    Args:
        income (float): Consumer's income
        price_x, price_y (float): Prices of goods X and Y

    Returns:
        dict: {'x_values': array, 'y_values': array, 'max_x': float, 'max_y': float}
    """
    # YOUR CODE HERE
    pass

def cobb_douglas_utility(x, y, alpha=0.5):
    """
    Calculate utility using Cobb-Douglas function: U = x^alpha * y^(1-alpha)

    Requirements:
    1. Handle arrays of x and y values
    2. Default alpha = 0.5 (equal preference)
    3. Handle edge cases (zero consumption)

    Args:
        x, y: Quantities of goods X and Y
        alpha: Preference parameter (0 < alpha < 1)

    Returns:
        Utility value(s)
    """
    # YOUR CODE HERE
    pass

def find_optimal_consumption(income, price_x, price_y, alpha=0.5):
    """
    Find utility-maximizing consumption bundle.

    For Cobb-Douglas utility with budget constraint:
    Optimal x* = (alpha * income) / price_x
    Optimal y* = ((1-alpha) * income) / price_y

    Requirements:
    1. Calculate optimal quantities analytically
    2. Verify budget constraint is satisfied
    3. Calculate maximum utility
    4. Plot indifference curves and budget line

    Args:
        income: Consumer's income
        price_x, price_y: Prices of goods
        alpha: Preference parameter

    Returns:
        dict: {'x_optimal': float, 'y_optimal': float, 'max_utility': float}
    """
    # YOUR CODE HERE
    pass

print("Test case: Income = 100, Price_x = 5, Price_y = 2, alpha = 0.6")
print("Expected: x* = 12, y* = 20, U* ≈ 16.87")

# =============================================================================
# PUZZLE 5: GDP CALCULATION AND GROWTH RATES
# Difficulty: Beginner-Intermediate
# =============================================================================

print("\n🧩 PUZZLE 5: GDP Analysis")
print("─" * 25)
print("Calculate GDP using different methods and analyze growth rates")

# Sample economic data
economic_data = {
    'consumption': [800, 820, 850, 880, 900],
    'investment': [200, 180, 220, 240, 260],
    'government_spending': [300, 310, 305, 320, 330],
    'exports': [150, 160, 170, 180, 185],
    'imports': [120, 130, 145, 150, 155],
    'year': [2019, 2020, 2021, 2022, 2023]
}

gdp_data = pd.DataFrame(economic_data)

def calculate_gdp_expenditure(consumption, investment, government, exports, imports):
    """
    Calculate GDP using expenditure approach: GDP = C + I + G + (X - M)

    Requirements:
    1. Handle both single values and arrays
    2. Calculate net exports correctly
    3. Return GDP value(s)

    Args:
        consumption, investment, government, exports, imports: Economic components

    Returns:
        GDP value or array of GDP values
    """
    # YOUR CODE HERE
    pass

def calculate_growth_rates(gdp_series):
    """
    Calculate year-over-year GDP growth rates.

    Requirements:
    1. Calculate percentage growth: ((GDP_t - GDP_{t-1}) / GDP_{t-1}) * 100
    2. Handle first year (no previous year)
    3. Calculate average growth rate
    4. Identify recession periods (negative growth)

    Args:
        gdp_series: Array or Series of GDP values

    Returns:
        dict: {'growth_rates': array, 'average_growth': float, 'recession_years': list}
    """
    # YOUR CODE HERE
    pass

def gdp_analysis_dashboard(df):
    """
    Create comprehensive GDP analysis with visualizations.

    Requirements:
    1. Calculate GDP for each year
    2. Calculate growth rates
    3. Create multiple plots: GDP level, growth rates, components
    4. Identify key economic trends
    5. Generate summary statistics

    Args:
        df: DataFrame with economic components and years

    Returns:
        dict: Complete analysis results
    """
    # YOUR CODE HERE
    pass

print("Test with provided economic_data")
print("Expected: GDP should show overall upward trend with growth rate variations")

# =============================================================================
# PUZZLE 6: INFLATION AND REAL VS NOMINAL VALUES
# Difficulty: Beginner-Intermediate
# =============================================================================

print("\n🧩 PUZZLE 6: Price Index and Inflation Analysis")
print("─" * 47)
print("Calculate CPI, inflation rates, and convert nominal to real values")

# Sample price data for market basket
price_data = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023],
    'bread_price': [2.50, 2.65, 2.80, 3.00],
    'milk_price': [3.20, 3.35, 3.60, 3.75],
    'gas_price': [2.85, 3.10, 4.20, 3.80],
    'bread_quantity': [100, 100, 100, 100],  # Base year quantities
    'milk_quantity': [50, 50, 50, 50],
    'gas_quantity': [200, 200, 200, 200]
})

def calculate_cpi(df, base_year=2020):
    """
    Calculate Consumer Price Index using Laspeyres method.

    CPI = (Cost of basket in current year / Cost of basket in base year) * 100

    Requirements:
    1. Calculate cost of market basket for each year
    2. Use base year quantities throughout
    3. Set base year CPI = 100
    4. Handle multiple goods

    Args:
        df: DataFrame with prices and quantities
        base_year: Base year for index (default 2020)

    Returns:
        pd.Series: CPI values for each year
    """
    # YOUR CODE HERE
    pass

def calculate_inflation_rate(cpi_series):
    """
    Calculate annual inflation rates from CPI data.

    Inflation rate = ((CPI_t - CPI_{t-1}) / CPI_{t-1}) * 100

    Requirements:
    1. Calculate year-over-year inflation
    2. Handle first year appropriately
    3. Identify periods of deflation
    4. Calculate average inflation rate

    Args:
        cpi_series: Series of CPI values

    Returns:
        dict: {'inflation_rates': Series, 'average_inflation': float}
    """
    # YOUR CODE HERE
    pass

def nominal_to_real(nominal_values, cpi_values, base_year_cpi=100):
    """
    Convert nominal values to real values using CPI.

    Real value = (Nominal value / CPI) * base_year_cpi

    Requirements:
    1. Handle arrays of values
    2. Use appropriate CPI deflator
    3. Maintain base year reference

    Args:
        nominal_values: Array of nominal values
        cpi_values: Corresponding CPI values
        base_year_cpi: CPI value for base year (default 100)

    Returns:
        Array of real values
    """
    # YOUR CODE HERE
    pass

print("Test with provided price_data")
print("Expected: CPI should generally increase, showing inflation")

# =============================================================================
# TESTING SECTION
# =============================================================================

print("\n" + "=" * 60)
print("TESTING YOUR SOLUTIONS")
print("=" * 60)
print("Run your functions with the test cases provided above.")
print("Make sure to:")
print("1. Handle edge cases appropriately")
print("2. Include proper error checking")
print("3. Add clear documentation")
print("4. Create meaningful visualizations")
print("5. Test with different parameter values")
print("\nGood luck! 🚀")

# Sample test runner (students can expand this)
def run_tests():
    """
    Run basic tests for all puzzle solutions.
    Students should expand this with their own test cases.
    """
    print("\n🧪 Running basic tests...")

    # Test Puzzle 1
    try:
        eq = find_equilibrium(-10, 2, 100, -3)
        print(f"✅ Puzzle 1 - Equilibrium: {eq}")
    except:
        print("❌ Puzzle 1 - Error in equilibrium calculation")

    # Test Puzzle 2
    try:
        elast = calculate_elasticity(10, 5, 9, 8)
        print(f"✅ Puzzle 2 - Elasticity: {elast}")
    except:
        print("❌ Puzzle 2 - Error in elasticity calculation")

    # Add more tests for other puzzles...

if __name__ == "__main__":
    run_tests()