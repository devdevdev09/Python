from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ','').replace('이모티콘\n', '').replace('사진\n', '').replace('삭제된 메시지입니다.\n', '')

# print(text)

wc = WordCloud(font_path='C:/Windows/Fonts/malgunsl.ttf', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

# mask = np.array(Image.open('cloud.png'))
# wc = WordCloud(font_path='C:/Windows/Fonts/malgunsl.ttf', background_color="white", mask=mask)
# wc.generate(text)
# wc.to_file("result_masked.png")