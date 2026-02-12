import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap

df = pd.read_excel('near_star_list.xlsx', sheet_name='Near Star Cat.')
df = df[df["–log10(T)"] != 0]
print(df.shape)
print(df.columns)

print("Displaying graph:")

# Declare graph
plt.scatter(df["Effective Temperature"],df["log10(L)"], s=1,alpha=0.7)


# Invert the X axis
plt.gca().invert_xaxis()

# Scale and values
plt.xscale("log")
plt.xticks([2000, 4000, 6000, 8000, 10000])
plt.gca().set_xticklabels(['1E2','1E4','1E6', '1E8', '1E10'])

# Axis labels
plt.xlabel("T/K")
plt.ylabel("log10(L/L⊙)")
plt.title("Hertzsprung–Russell Diagram")
plt.axvline(x=6000, color='gray', linestyle='--', alpha=0.5, linewidth=1)

plt.show()

print(df[["Effective Temperature", "ColorIndex B-V"]].head(10))