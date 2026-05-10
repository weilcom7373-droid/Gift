import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

# --- 這裡使用更穩定的 Google 直連格式 ---
# 如果圖片還是不出來，請檢查 Google Drive 分享設定是否為「知道連結的任何人」
GIFT_URL = "https://lh3.googleusercontent.com/d/1F9lAIRkmhpqwZesoZoT2Gq4j8fs1Z0W2"
FINAL_URL = "https://lh3.googleusercontent.com/d/18w-ZSzSB2UtnhgYWZah48iROFPGJZd3M"

# 初始化狀態
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# 自定義 CSS
st.markdown("""
    <style>
    .center-text { text-align: center; color: #ff4b4b; }
    .hint-text { text-align: center; color: #555555; font-size: 18px; font-weight: bold; background-color: #ffebeb; padding: 10px; border-radius: 10px; }
    .stButton > button { display: block; margin: 0 auto; width: 80%; height: 60px; font-size: 20px; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='center-text'>🎁 給你的驚喜</h1>", unsafe_allow_html=True)

# 遊戲邏輯
if st.session_state.clicks < 10:
    st.markdown(f"<h3 class='center-text'>請點擊下方按鈕拆開禮物<br>({st.session_state.clicks} / 10)</h3>", unsafe_allow_html=True)
    
    # 顯示圖片，如果連結失效會顯示說明文字
    st.image(GIFT_URL, use_container_width=True)
    
    if st.button("按我拆禮物 👆"):
        st.session_state.clicks += 1
        st.rerun()

elif not st.session_state.unlocked:
    st.balloons()
    st.markdown("<h2 class='center-text'>🔒 盒子被鎖住了！</h2>", unsafe_allow_html=True)
    
    # --- 密碼提示語 ---
    st.markdown("<p class='hint-text'>提示：今天的日期與母親節快樂英文<br>(共24個字，小寫且不含空格)</p>", unsafe_allow_html=True)
    
    password = st.text_input("在下方輸入密碼：", type="password")
    
    if password == "20260510happymother'sday":
        st.success("密碼正確！")
        if st.button("點擊查看最終驚喜 ✨"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("密碼不對喔，再檢查一下大小寫、有沒有包含 ' 符號或日期是否正確！")

else:
    st.markdown("<h2 class='center-text'>🎉 母親節快樂！ 🎉</h2>", unsafe_allow_html=True)
    st.image(FINAL_URL, use_container_width=True)
    st.balloons()
    st.snow()
    
    if st.button("重新開始"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()
