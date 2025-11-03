import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("PYTHON PROGRAMMING PUZZLES")
print("=" * 60)

# =============================================================================
# PUZZLE 1: SUPPLY & DEMAND EQUILIBRIUM
# =============================================================================

def find_equilibrium(supply_intercept, supply_slope, demand_intercept, demand_slope):
    if supply_slope == demand_slope:
        return None
    price = (demand_intercept - supply_intercept) / (supply_slope - demand_slope)
    quantity = supply_intercept + supply_slope * price
    return {'price': round(price,2), 'quantity': round(quantity,2)}

def plot_supply_demand(supply_intercept, supply_slope, demand_intercept, demand_slope, equilibrium):
    prices = np.linspace(0, 100, 200)
    supply = supply_intercept + supply_slope*prices
    demand = demand_intercept + demand_slope*prices

    plt.figure(figsize=(7,5))
    plt.plot(prices, supply, label="Supply")
    plt.plot(prices, demand, label="Demand")
    if equilibrium:
        plt.scatter(equilibrium['price'], equilibrium['quantity'], c='red', s=80, label="Equilibrium")
    plt.title("Supply & Demand")
    plt.xlabel("Price"); plt.ylabel("Quantity")
    plt.grid(); plt.legend(); plt.show()

# =============================================================================
# PUZZLE 2: ELASTICITY
# =============================================================================

def calculate_elasticity(p1, q1, p2, q2):
    pct_q = (q2-q1) / ((q2+q1)/2)
    pct_p = (p2-p1) / ((p2+p1)/2)
    if pct_p == 0:
        return None
    e = pct_q/pct_p
    classification = "Elastic" if abs(e)>1 else ("Inelastic" if abs(e)<1 else "Unit Elastic")
    return {"elasticity": round(e,3), "classification": classification}

def analyze_demand_curve(df):
    results=[]
    for i in range(len(df)-1):
        p1,q1=df.iloc[i]
        p2,q2=df.iloc[i+1]
        e=calculate_elasticity(p1,q1,p2,q2)
        results.append([p1,p2,q1,q2,e['elasticity'],e['classification']])
    
    out=pd.DataFrame(results,columns=["P1","P2","Q1","Q2","Elasticity","Classification"])

    plt.plot(df['price'],df['quantity_demanded'],marker='o')
    plt.title("Demand Curve"); plt.xlabel("Price"); plt.ylabel("Quantity"); plt.grid(); plt.show()
    return out

# =============================================================================
# PUZZLE 3: SURPLUS
# =============================================================================

def calculate_surplus(d_int,d_slp,s_int,s_slp,price=None,quantity=None):
    eq=find_equilibrium(s_int,s_slp,d_int,d_slp)
    if price is None:
        price=eq['price']; quantity=eq['quantity']

    choke = d_int/-d_slp
    min_supply = s_int/-s_slp

    CS=0.5*(choke-price)*quantity
    PS=0.5*(price-min_supply)*quantity
    return {
        "price":price,"quantity":quantity,
        "consumer_surplus":round(CS,2),
        "producer_surplus":round(PS,2),
        "total_surplus":round(CS+PS,2)
    }

def deadweight_loss_analysis(d_int,d_slp,s_int,s_slp,regulated_price):
    eq=find_equilibrium(s_int,s_slp,d_int,d_slp)
    
    qd=d_int + d_slp*regulated_price
    qs=s_int + s_slp*regulated_price
    q=min(qd,qs)

    eq_sur=calculate_surplus(d_int,d_slp,s_int,s_slp)
    regulated_sur=calculate_surplus(d_int,d_slp,s_int,s_slp,regulated_price,q)

    dwl = eq_sur['total_surplus'] - regulated_sur['total_surplus']
    return {"regulated_price":regulated_price,"Qd":qd,"Qs":qs,"shortage/surplus":qd-qs,"deadweight_loss":round(dwl,2)}

# =============================================================================
# PUZZLE 4: CONSUMER CHOICE
# =============================================================================

def budget_constraint(income,px,py):
    x=np.linspace(0,income/px,100)
    y=(income-px*x)/py
    return {"x_values":x,"y_values":y}

def cobb_douglas_utility(x,y,alpha=0.5):
    return (x**alpha)*(y**(1-alpha))

def find_optimal_consumption(income,px,py,alpha=0.5):
    x_star=(alpha*income)/px
    y_star=((1-alpha)*income)/py
    util=cobb_douglas_utility(x_star,y_star,alpha)

    bc=budget_constraint(income,px,py)
    plt.plot(bc['x_values'],bc['y_values'],label="Budget Line")
    plt.scatter(x_star,y_star,c='red',label="Optimal")
    plt.title("Consumer Choice"); plt.xlabel("X"); plt.ylabel("Y")
    plt.legend(); plt.grid(); plt.show()

    return {"x*":x_star,"y*":y_star,"utility":round(util,2)}

# =============================================================================
# PUZZLE 5: GDP + GROWTH (✅ FIXED!)
# =============================================================================

def calculate_gdp_expenditure(C,I,G,X,M):
    return np.array(C)+np.array(I)+np.array(G)+(np.array(X)-np.array(M))

def calculate_growth_rates(gdp):
    growth=[np.nan]   # np.nan instead of None (fix)
    for i in range(1,len(gdp)):
        rate=((gdp[i]-gdp[i-1])/gdp[i-1])*100
        growth.append(rate)

    avg=np.nanmean(growth)
    recession=[i for i,g in enumerate(growth) if not np.isnan(g) and g<0]

    return {"growth_rates":growth,"average_growth":round(avg,2),"recession_years":recession}

def gdp_analysis_dashboard(df):
    gdp = calculate_gdp_expenditure(df['consumption'],df['investment'],df['government_spending'],df['exports'],df['imports'])
    growth=calculate_growth_rates(gdp)

    plt.plot(df['year'],gdp,marker='o'); plt.title("GDP Trend"); plt.grid(); plt.show()
    plt.bar(df['year'][1:],growth['growth_rates'][1:]); plt.title("GDP Growth"); plt.grid(); plt.show()

    return {"gdp":gdp,"growth":growth}

# =============================================================================
# PUZZLE 6: CPI + INFLATION
# =============================================================================

def calculate_cpi(df,base_year=2020):
    base=df[df['year']==base_year]
    base_cost=(base['bread_price']*base['bread_quantity']+
               base['milk_price']*base['milk_quantity']+
               base['gas_price']*base['gas_quantity']).values[0]
    
    CPI=[]
    for i in range(len(df)):
        cost=(df['bread_price'][i]*df['bread_quantity'][i] +
              df['milk_price'][i]*df['milk_quantity'][i] +
              df['gas_price'][i]*df['gas_quantity'][i])
        CPI.append((cost/base_cost)*100)
    return pd.Series(CPI,index=df['year'])

def calculate_inflation_rate(cpi):
    inflation = [np.nan]  # first year has no previous year

    for i in range(1, len(cpi)):
        rate = ((cpi.iloc[i] - cpi.iloc[i-1]) / cpi.iloc[i-1]) * 100
        inflation.append(rate)

    return {
        "inflation_rates": inflation,
        "average_inflation": round(np.nanmean(inflation), 2)
    }

def nominal_to_real(nom,cpi,base=100):
    return (np.array(nom)/np.array(cpi))*base

# =============================================================================
# RUN ALL PUZZLES
# =============================================================================

if __name__ == "__main__":
    print("\n✅ Running All Puzzle Outputs...\n")

    # Puzzle 1
    eq=find_equilibrium(-10,2,100,-3)
    print("Puzzle 1:",eq)
    plot_supply_demand(-10,2,100,-3,eq)

    # Puzzle 2
    df_price=pd.DataFrame({"price":[10,9,8,7,6,5,4,3,2,1],
                           "quantity_demanded":[5,8,12,17,23,30,38,47,57,68]})
    print("\nPuzzle 2 Example:",calculate_elasticity(10,5,9,8))
    print(analyze_demand_curve(df_price))

    # Puzzle 3
    print("\nPuzzle 3 Surplus:",calculate_surplus(100,-3,-10,2))
    print("Puzzle 3 DWL:",deadweight_loss_analysis(100,-3,-10,2,15))

    # Puzzle 4
    print("\nPuzzle 4:",find_optimal_consumption(100,5,2,alpha=0.6))

    # Puzzle 5
    df_gdp=pd.DataFrame({
        'consumption':[800,820,850,880,900],
        'investment':[200,180,220,240,260],
        'government_spending':[300,310,305,320,330],
        'exports':[150,160,170,180,185],
        'imports':[120,130,145,150,155],
        'year':[2019,2020,2021,2022,2023]
    })
    print("\nPuzzle 5:",gdp_analysis_dashboard(df_gdp))

    # Puzzle 6
    price_data=pd.DataFrame({
        'year':[2020,2021,2022,2023],
        'bread_price':[2.5,2.65,2.8,3.0],
        'milk_price':[3.2,3.35,3.6,3.75],
        'gas_price':[2.85,3.1,4.2,3.8],
        'bread_quantity':[100]*4,
        'milk_quantity':[50]*4,
        'gas_quantity':[200]*4
    })

    cpi=calculate_cpi(price_data)
    print("\nPuzzle 6 CPI:\n",cpi)
    print("Inflation:",calculate_inflation_rate(cpi))
    print("Real values:",nominal_to_real([1000,1100,1200,1300],cpi))