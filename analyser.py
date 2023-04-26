import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#print(*os.listdir("./opinons")) #wyświetlanie plików w folderze
print(*[filename.split(".")[0] for filename in os.listdir("./opinons")],sep="\n")


product_code = "62290435" #input("Podaj kod produktu: ") # 96693065 " 62290434

opinions = pd.read_json(f"./opinons/{product_code}.json")
opinions.rating = opinions.rating.map(lambda x: float(x.split("/")[0].replace(",",".")))
#print(opinions)
#print(type(opinions))

#podstawowe statystyki
opinions_count =  opinions.opinion_id.count() #len(opinions) | opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
avg_rating = opinions.rating.mean().round(2)
print(f"""Dla produktu o kodzie {product_code} pobrano {opinions_count} opinii. Dla {pros_count} dostępna jest lista zalet, a dla {cons_count} opinii dostępna jest lista wad. 
Średnia ocen produktu wynosi {avg_rating}.""")

# histogram częstości ocen produktu
rating = opinions.rating.value_counts().reindex(list(np.arange(0,5.5,0.5)),fill_value = 0)
#print(rating)
rating.plot.bar(color="hotpink")
#plt.show()
plt.savefig(f"./plots/{product_code}_rating.png")
plt.close()

#udzial rekomomendacji w opiniach
recommendations = opinions.recommendation.value_counts(dropna=False)
recommendations.plot.pie(label="", autopct ="%1.1f%%")
plt.savefig(f"./plots/{product_code}_recomm.png")
plt.close()