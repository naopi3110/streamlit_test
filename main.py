from operator import truediv
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門') #タイトルの追加




#st.write('Dataframe')#テキストの追加

df = pd.DataFrame({
    '１列目': [1,2,3,4],
    '２列目': [10,20,30,40]
})
#dfの表示方法
if st.checkbox('show df'):
    st.table(df.style.highlight_max(axis=0))
#st.write(df)でも可、ただし引数(width,height)の使用不可
#static（静的な）表の作成→ st.table(df)
#st.dataframe(df)も可



df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
#折れ線グラフの表示
if st.checkbox('show chart'):
    st.line_chart(df)
#area_chart, bar_chartなどなど


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
#マップへのプロット
if st.checkbox('show map'):
    st.map(df)

#画像の読み込み
img = Image.open('sample.JPG')


#インタラクティブなウィジェット
if st.checkbox('show image'):
    st.image(img, caption='my desk', use_column_width=True)

#セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

#テキスト入力
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味は', text, 'です。'

#スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション', condition

#レイアウトを整える
#サイドバー st.sidebarでサイドバーへ
#2カラムレイアウト
#expander
left_column, right_column = st.columns(2)
botton = left_column.button('右カラムに表示')
if botton:
    right_column.write('ここは右カラム')
#プログレスバー
latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


