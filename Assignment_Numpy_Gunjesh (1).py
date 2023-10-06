#!/usr/bin/env python
# coding: utf-8

# In[59]:


import numpy as np

def product_except_self(nums):
    nums = np.array(nums)
    total_product = np.prod(nums)
    answer = total_product / nums # this line works because of Ufunc (vectorization)
    return answer

# Example usage
nums = [4,2,5,1]
print(product_except_self(nums)) 


# In[61]:


import numpy as np
from scipy.interpolate import CubicSpline

shocks = {
    506: 0.486,
    258: 0.661,
    358: 0.371,
    735: 0.293,
    166: 0.203,
    781: 0.633,
    789: 0.529,
    822: 0.86,
    728: 0.038,
    725: 0.886
}

pnl_grid = {
    506: ([0.465,0.05,0.345,0.629,0.289,0.05,0.243,0.822,0.665,0.856], [-220.983,-217.841,-220.074,-222.224,-219.65,-217.841,np.nan,-223.685,np.nan,-223.942]),
    258: ([0.473,0.232,0.649,0.19,0.962,0.93,0.639,0.059,0.831,0.837], [-653.225,-654.91,-651.994,-655.203,-649.806,-650.03,-652.064,np.nan,-650.722,-650.68]),
    358: ([0.97,0.836,0.031,0.831,0.634,0.56,0.046,0.094,0.202,0.198], [687.434,686.908,683.749,686.888,686.115,685.825,683.808,683.997,684.42,684.405]),
    735: ([0.949,0.326,0.205,0.952,0.543,0.032,0.926,0.826,0.875,0.846], [-426.147,-428.488,-428.943,-426.136,-427.673,-429.593,-426.234,-426.609,np.nan,-426.534]),
    166: ([0.041,0.48,0.575,0.09,0.412,0.12,0.584,0.306,0.981,0.649], [769.374,762.653,761.199,768.624,763.694,np.nan,761.061,np.nan,754.983,760.066]),
    781: ([0.569,0.334,0.102,0.744,0.685,0.546,0.85,0.097,0.791,0.249], [-449.069,-448.246,np.nan,-449.682,np.nan,-448.989,-450.054,-447.416,-449.847,-447.948]),
    789: ([0.864,0.536,0.223,0.578,0.646,0.147,0.401,0.535,0.51,0.69], [477.718,472.913,468.328,473.528,474.525,467.215,470.936,472.899,472.532,475.169]),
    822: ([0.051,0.068,0.386,0.224,0.618,0.969,0.581,0.616,0.405,0.573], [-999.429,-999.695,-1004.679,-1002.14,-1008.315,-1013.816,-1007.735,-1008.284,-1004.977,-1007.61]),
    728: ([0.605,0.18,0.575,0.316,0.723,0.911,0.98,0.291,0.823,0.63], [336.468,332.996,336.223,334.107,np.nan,338.968,339.531,333.903,338.249,336.672]),
    725: ([0.76,0.703,0.223,0.785,0.211,0.48,0.644,0.551,0.871,0.275], [-204.815,-205.658,-212.755,np.nan,-212.933,-208.955,-206.53,-207.905,-203.174,-211.986]),
}

# Function to calculate interpolated pnl
def calculate_interpolated_pnl(sorted_shock_list, sorted_pnl_list, shock_value):
    
    spline= CubicSpline(sorted_shock_list, sorted_pnl_list, bc_type='natural')(shock_value)
    return spline

# Calculate pnl for each issuer using shocks
pnl_results = {}

for issuer_id, (shock_list, pnl_list) in pnl_grid.items():
    non_nan_indices = np.where(np.isfinite(pnl_list))
    shock_list = np.array(shock_list)[non_nan_indices]
    pnl_list = np.array(pnl_list)[non_nan_indices]
    sorted_indices = np.argsort(shock_list)
   
    sorted_shock_list = shock_list[sorted_indices]
   
    sorted_pnl_list = pnl_list[sorted_indices]
    x_cummax = np.maximum.accumulate(sorted_shock_list)

    sorted_shock_list, idx = np.unique(x_cummax, return_index=True)
    sorted_pnl_list=sorted_pnl_list[idx]
    
    
    shock_value = shocks.get(issuer_id)
    
    
    
    if shock_value is None:
        pnl_results[issuer_id] = None
    else:
        
        interpolated_pnl = calculate_interpolated_pnl(sorted_shock_list, sorted_pnl_list,shock_value)
        pnl_results[issuer_id] = interpolated_pnl 

print(pnl_results)


# In[58]:


import numpy as np
from scipy.interpolate import CubicSpline



cutoffs = {
    506: 0.4,
    258: 0.6,
    358: 0.3,
    735: 0.3,
    166: 0.2,
    781: 0.6,
    789: 0.5,
    822: 0.8,
    728: 0.4,
    725: 0.4
}
pnl_grid = {
    506: ([0.465,0.05,0.345,0.629,0.289,0.05,0.243,0.822,0.665,0.856], [-220.983,-217.841,-220.074,-222.224,-219.65,-217.841,np.nan,-223.685,np.nan,-223.942]),
    258: ([0.473,0.232,0.649,0.19,0.962,0.93,0.639,0.059,0.831,0.837], [-653.225,-654.91,-651.994,-655.203,-649.806,-650.03,-652.064,np.nan,-650.722,-650.68]),
    358: ([0.97,0.836,0.031,0.831,0.634,0.56,0.046,0.094,0.202,0.198], [687.434,686.908,683.749,686.888,686.115,685.825,683.808,683.997,684.42,684.405]),
    735: ([0.949,0.326,0.205,0.952,0.543,0.032,0.926,0.826,0.875,0.846], [-426.147,-428.488,-428.943,-426.136,-427.673,-429.593,-426.234,-426.609,np.nan,-426.534]),
    166: ([0.041,0.48,0.575,0.09,0.412,0.12,0.584,0.306,0.981,0.649], [769.374,762.653,761.199,768.624,763.694,np.nan,761.061,np.nan,754.983,760.066]),
    781: ([0.569,0.334,0.102,0.744,0.685,0.546,0.85,0.097,0.791,0.249], [-449.069,-448.246,np.nan,-449.682,np.nan,-448.989,-450.054,-447.416,-449.847,-447.948]),
    789: ([0.864,0.536,0.223,0.578,0.646,0.147,0.401,0.535,0.51,0.69], [477.718,472.913,468.328,473.528,474.525,467.215,470.936,472.899,472.532,475.169]),
    822: ([0.051,0.068,0.386,0.224,0.618,0.969,0.581,0.616,0.405,0.573], [-999.429,-999.695,-1004.679,-1002.14,-1008.315,-1013.816,-1007.735,-1008.284,-1004.977,-1007.61]),
    728: ([0.605,0.18,0.575,0.316,0.723,0.911,0.98,0.291,0.823,0.63], [336.468,332.996,336.223,334.107,np.nan,338.968,339.531,333.903,338.249,336.672]),
    725: ([0.76,0.703,0.223,0.785,0.211,0.48,0.644,0.551,0.871,0.275], [-204.815,-205.658,-212.755,np.nan,-212.933,-208.955,-206.53,-207.905,-203.174,-211.986]),
}



expected_pnl = {}

for issuer_id, (shock_list, pnl_list) in pnl_grid.items():
    non_nan_indices = np.where(np.isfinite(pnl_list))
    shock_list = np.array(shock_list)[non_nan_indices]
    pnl_list = np.array(pnl_list)[non_nan_indices]
    sorted_indices = np.argsort(shock_list)
   
    sorted_shock_list = shock_list[sorted_indices]
   
    sorted_pnl_list = pnl_list[sorted_indices]
    x_cummax = np.maximum.accumulate(sorted_shock_list)

    sorted_shock_list, idx = np.unique(x_cummax, return_index=True)
    sorted_pnl_list=sorted_pnl_list[idx]
   
    
   

for issuer_id, cutoff in cutoffs.items():
    np.random.seed(issuer_id)
    random_no = np.random.random(size=(1000, 4))
    default_flags = np.where( random_no > cutoff, 1, 0)

    # Initializing result array to capture default flag for each simulation

    result = np.zeros(default_flags.shape)
    idx =  np.arange(result.shape[0])
    #calculating index of time stamp where issuer defaults in each simulation
    args = default_flags.astype(bool).argmax(1)
    # after default, subsequent time stamps are marked as default as well
    result[idx, args] = default_flags[idx, args]

    # calculate pnl using interpolation of shocks 

    shocks = (random_no * res).sum(axis=1)
    pnls = calculate_interpolated_pnl(sorted_shock_list, sorted_pnl_list, shocks)
    expected_pnl[issuer_id]=np.mean(pnls)

print(expected_pnl)
    
    
    
    


# In[ ]:




