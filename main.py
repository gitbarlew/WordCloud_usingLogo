import pandas as pd
import prepare
import openpyxl
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def load_excel(file_path):
    return pd.read_excel(file_path)

file_path = 'Results_data_SmartWifiPods_deepdive_Okt23_translated - Copy.xlsx'
column_name = 'Q1.3'


df = load_excel(file_path)
responses = df[column_name]

type(responses)

ds_text = prepare.clean(str(responses))
print(ds_text)
ds_mask = np.array(Image.open('logo.png'))

# Plot the wordcloud with the mask applied
wc = WordCloud(background_color='white', mask= ds_mask, contour_width=1, contour_color='white', colormap = 'Reds', stopwords = ['nan'], width=800, height = 600).generate(ds_text)
plt.figure(figsize=[16,16])
plt.tight_layout()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig('wordcloud.png')
plt.show()
