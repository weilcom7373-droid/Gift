import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

# 初始化狀態
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# 自定義 CSS：讓按鈕變超級大，並置中
st.markdown("""
    <style>
    /* 讓按鈕容器寬度 100% 並居中 */
    .stButton > button {
        width: 250px;
        height: 250px;
        font-size: 120px !important;
        background-color: #ffffff;
        border: 4px dashed #ff4b4b;
        border-radius: 30px;
        display: block;
        margin: 0 auto;
        transition: transform 0.2s;
    }
    .stButton > button:active {
        transform: scale(0.9);
    }
    .text-center {
        text-align: center;
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='text-center'>🎁 送你的禮物 </h1>", unsafe_allow_html=True)

# 邏輯判斷
if st.session_state.clicks < 10:
    # 階段 1：點擊禮物盒
    st.markdown(f"<h3 class='text-center'>請點擊禮物盒拆開它<br>({st.session_state.clicks} / 10)</h3>", unsafe_allow_html=True)
    
    # 建立一個置中的按鈕
    if st.button("🎁"):
        st.session_state.clicks += 1
        st.rerun()

elif not st.session_state.unlocked:
    # 階段 2：輸入密碼
    st.balloons() # 點完 10 次噴氣球
    st.markdown("<h3 class='text-center'>🔒 盒子被鎖住了！</h3>", unsafe_allow_html=True)
    
    password = st.text_input("請輸入今天的日期 (YYYYMMDD)：", type="password")
    
    if password == "20260510":
        st.success("密碼正確！")
        if st.button("點擊查看驚喜 ✨"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("日期不對喔，再試一次！")

else:
    # 階段 3：顯示圖片
    st.markdown("<h2 class='text-center'>🎉 驚喜揭曉！ 🎉</h2>", unsafe_allow_html=True)
    
    # --- 在這裡替換你的圖片網址 ---
    st.image("https://placekitten.com/800/600", caption="這是我準備的驚喜圖片", use_container_width=True)
    
    st.balloons()
    st.snow()
    
    if st.button("重新開始"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()
