import streamlit as st

def P(M,D,L):
    X=(1/31/D)+M
    if 4<=M<=12:
        Y=12-X+4#残り
    else:
        Y=4-X#残り
    if L==2:
        return round(X/12*100,3)
    else:
        return round(X/(Y+(L-2)*12)*100,3)
st.title("１年４組　劣化版MOODLE")
#C:\Users\kinas\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\streamlit.cmd run main.py
st.info("""
**このアプリについて**
---
昼休みに作ったwEBアプリです。ゴミです。打倒MOODLE！

**できること**
---
・次の学年まであと何％かを確認できる

・課題を確認する

・１年４組だけの予定を確認する

・その他ゴミ機能
""")
Mli=list(range(1,13))
st.error("""
**初めに入力してくれ**
-
""")
M=st.selectbox("今日の日付（月）は？",Mli)
D=st.slider(label="今日は何日？",min_value=1,max_value=31,value=1)
W=st.selectbox("今日は何曜日？",["月","火","水","木","金","土","日"])
#時間割
T=["データ未準備","データ未準備","データ未準備","データ未準備",]
st.error("""
**１－４今日の予定**
-
""")
st.markdown("""
>**（１）{}**

>**（２）{}**

>**（３）{}**

>**（４）{}**
""".format(*T))
st.error("""
**卒業まであと何％？**
-
""")
st.write("いろいろ日付を変えて試してみてるのだ")
if M and D:
    st.success(f"""
    **２年生まであと（約）
    {P(M,D,2)}％です…**
    """)
    st.success(f"""
    **３年生まであと（約）
    {P(M,D,3)}％です…**
    """)
    st.success(f"""
    **４年生まであと（約）
    {P(M,D,4)}％です…**
    """)
    st.success(f"""
    **５年生まであと（約）
    {P(M,D,5)}％です…**
    """)
    st.success(f"""
    **卒業まであと（約）
    {P(M,D,6)}％です…**
    """)
st.error("""
**夏休みまであと何日？**
-
""")
if M and D:
    if M>8:
        st.success("""
        **夏休みは終わってんだよ！**
        -
        """)
    if D>5:
        st.success(f"""
        **約{31-D+(8-M-1)*31}日や！**
        -
        """)
    else:
        st.success(f"""
        **約{5-D+(8-M)*31}日や！**
        -
        """)
