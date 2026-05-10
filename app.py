import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

# 2. 圖片網址處理 (Google Drive 直接連結)
GIFT_URL = "https://drive.google.com/uc?export=view&id=1F9lAIRkmhpqwZesoZoT2Gq4j8fs1Z0W2"
FINAL_URL = "https://drive.google.com/uc?export=view&id=18w-ZSzSB2UtnhgYWZah48iROFPGJZd3M"

# 初始化狀態
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# 自定義 CSS 讓文字居中
st.markdown("""
    <style>
    .center-text { text-align: center; color: #ff4b4b; }
    .hint-text { text-align: center; color: #555555; font-size: 18px; font-weight: bold; }
    .stButton > button { display: block; margin: 0 auto; width: 100%; height: 60px; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='center-text'>🎁 給你的驚喜</h1>", unsafe_allow_html=True)

# 3. 遊戲邏輯
if st.session_state.clicks < 10:
    # 第一階段：點擊
    st.markdown(f"<h3 class='center-text'>請點擊下方按鈕拆開禮物<br>({st.session_state.clicks} / 10)</h3>", unsafe_allow_html=True)
    
    # 這裡直接用 st.image 顯示圖片，確保它能跑出來
    st.image(GIFT_URL, caption="我的禮物盒", use_container_width=True)
    
    if st.button("按我拆禮物 👆"):
        st.session_state.clicks += 1
        st.rerun()

elif not st.session_state.unlocked:
    # 第二階段：輸入密碼
    st.balloons()
    st.markdown("<h2 class='center-text'>🔒 盒子被鎖住了！</h2>", unsafe_allow_html=True)
    
    # --- 這裡是你要求的密碼提示語 ---
    st.markdown("<p class='hint-text'>今天的日期與母親節快樂英文<br>(共24個字，小寫且不含空格)</p>", unsafe_allow_html=True)
    
    password = st.text_input("在下方輸入密碼：", type="password")
    
    # 判斷密碼
    if password == "20260510happymother'sday":
        st.success("密碼正確！")
        if st.button("點擊查看最終驚喜 ✨"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("密碼不對喔，再檢查一下大小寫或符號！")

else:
    # 第三階段：顯示最後驚喜
    st.markdown("<h2 class='center-text'>🎉 母親節快樂！ 🎉</h2>", unsafe_allow_html=True)
    
    # 顯示驚喜圖片
    st.image(FINAL_URL, caption="這是我準備的驚喜圖片", use_container_width=True)
    
    st.balloons()
    st.snow()
    
    if st.button("重新開始"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()
