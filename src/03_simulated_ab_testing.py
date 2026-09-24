"""
03_simulated_ab_testing.py: Simulation of retention campaign and bootstrap CI.
"""
import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(42)
n = 2400
p_ctrl = 0.081
p_trt = 0.116

ctrl = np.random.binomial(1, p_ctrl, size=n//2)
trt = np.random.binomial(1, p_trt, size=n//2)

boot_lifts = [
    np.random.choice(trt, size=len(trt), replace=True).mean() -
    np.random.choice(ctrl, size=len(ctrl), replace=True).mean()
    for _ in range(5000)
]

ci_lower, ci_upper = np.percentile(boot_lifts, [2.5, 97.5])
print(f"Treatment Lift: {trt.mean() - ctrl.mean():.4f}")
print(f"95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]")
