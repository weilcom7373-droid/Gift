import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

# --- Google Drive 圖片連結處理 ---
# 我已經幫你把連結轉換成程式可以讀取的格式
GIFT_URL = "https://drive.google.com/uc?export=view&id=1F9lAIRkmhpqwZesoZoT2Gq4j8fs1Z0W2"
FINAL_URL = "https://drive.google.com/uc?export=view&id=18w-ZSzSB2UtnhgYWZah48iROFPGJZd3M"

# 初始化狀態 (記錄點擊與是否解鎖)
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# 自定義 CSS：讓禮物圖片變大、置中，並變成可點擊的按鈕
st.markdown(f"""
    <style>
    .stButton > button {{
        width: 300px;
        height: 300px;
        background-image: url('{GIFT_URL}');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-color: transparent;
        border: none;
        color: transparent !important;
        display: block;
        margin: 0 auto;
        cursor: pointer;
        transition: transform 0.1s;
    }}
    .stButton > button:active {{
        transform: scale(0.9);
    }}
    .stButton > button:hover {{
        border: none;
        color: transparent !important;
    }}
    .text-center {{
        text-align: center;
        color: #ff4b4b;
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='text-center'>🎁 送你的禮物 </h1>", unsafe_allow_html=True)

# 遊戲邏輯
if st.session_state.clicks < 10:
    # 第一階段：點擊圖片 10 次
    st.markdown(f"<h3 class='text-center'>點點圖片拆開它！<br>({st.session_state.clicks} / 10)</h3>", unsafe_allow_html=True)
    
    if st.button("點擊"):
        st.session_state.clicks += 1
        st.rerun()

elif not st.session_state.unlocked:
    # 第二階段：輸入密碼
    st.balloons()
    st.markdown("<h3 class='text-center'>🔒 盒子被鎖住了！</h3>", unsafe_allow_html=True)
    
    st.write("<p style='text-align:center;'>請輸入今天的日期與母親節快樂英文<br>(共24個字，小寫且不含空格)</p>", unsafe_allow_html=True)
    
    # 這裡的密碼設定為你指定的：20260510happymother'sday
    password = st.text_input("請輸入密碼：", type="password")
    
    if password == "20260510happymother'sday":
        st.success("密碼正確！")
        if st.button("點擊查看驚喜 ✨"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("密碼不對喔，再試一次！")

else:
    # 第三階段：展示最終驚喜圖片
    st.markdown("<h2 class='text-center'>🎉 母親節快樂！ 🎉</h2>", unsafe_allow_html=True)
    
    # 顯示你準備的最終禮物圖
    st.image(FINAL_URL, use_container_width=True)
    
    st.balloons()
    st.snow()
    
    if st.button("重新開始"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()st.markdown("<h1 class='text-center'>🎁 送你的禮物 </h1>", unsafe_allow_html=True)

# 邏輯判斷
if st.session_state.clicks < 10:
    # 階段 1：點擊禮物盒
    st.markdown(f"<h3 class='text-center'>請點擊禮物盒拆開它<br>({st.session_state.clicks} / 10)</h3>", unsafe_allow_html=True)
    
    # 建立一個置中的按鈕
    if st.button(https://drive.google.com/file/d/1F9lAIRkmhpqwZesoZoT2Gq4j8fs1Z0W2/view?usp=drivesdk):
        st.session_state.clicks += 1
        st.rerun()

elif not st.session_state.unlocked:
    # 階段 2：輸入密碼
    st.balloons() # 點完 10 次噴氣球
    st.markdown("<h3 class='text-center'>🔒 盒子被鎖住了！</h3>", unsafe_allow_html=True)
    
    password = st.text_input("請輸入今天的日期 (YYYYMMDD)，並在後方拼出母親節快樂的英文（不用空格與大寫）：", type="password")
    
    if password == "20260510happymother'sday":
        st.success("密碼正確！")
        if st.button("點擊查看驚喜 ✨"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("密碼不對喔，再試一次！")

else:
    # 階段 3：顯示圖片
    st.markdown("<h2 class='text-center'>🎉 驚喜揭曉！ 🎉</h2>", unsafe_allow_html=True)
    
    # --- 在這裡替換你的圖片網址 ---
    st.image("https://drive.google.com/file/d/18w-ZSzSB2UtnhgYWZah48iROFPGJZd3M/view?usp=drivesdk", caption="這是我準備的禮物", use_container_width=True)
    
    st.balloons()
    st.snow()
    
    if st.button("重新開始"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()
