from cld_utils import *
from plant import *
import matplotlib.pyplot as plt

sets, names = get_sets()

vert = [0,0,1,1,0,0]
plt.figure(figsize=(10,3))
plt.title("Fuzzy Sets")
for fset, fname in zip(sets, names):
  if fset[0]==fset[1]==-1.0: plt.plot([*fset[1:],1.0],vert[2:],label=fname)
  elif fset[2]==fset[3]==1.0: plt.plot([-1.0,*fset[:3]],vert[:4],label=fname)
  else: plt.plot([-1.0,*fset,1.0],vert,label=fname)
plt.legend()