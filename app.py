import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

# 2. 圖片網址 (使用剛才測試成功的連結)
GIFT_URL = "https://lh3.googleusercontent.com/d/1F9lAIRkmhpqwZesoZoT2Gq4j8fs1Z0W2"
FINAL_URL = "https://lh3.googleusercontent.com/d/18w-ZSzSB2UtnhgYWZah48iROFPGJZd3M"

# 初始化狀態
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# 3. 自定義 CSS：把按鈕變成你的禮物圖片
st.markdown(f"""
    <style>
    /* 讓按鈕背景變成禮物圖 */
    .stButton > button {{
        width: 300px;
        height: 300px;
        background-image: url('{GIFT_URL}');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-color: transparent;
        border: none;
        color: transparent !important; /* 隱藏按鈕文字 */
        display: block;
        margin: 0 auto;
        cursor: pointer;
        transition: transform 0.1s;
    }}
    /* 點擊時縮小的視覺效果 */
    .stButton > button:active {{
        transform: scale(0.9);
        background-color: transparent;
    }}
    /* 防止滑鼠移上去變色 */
    .stButton > button:hover {{
        background-color: transparent;
        color: transparent !important;
        border: none;
    }}
    .center-text {{ text-align: center; color: #ff4b4b; }}
    .hint-box {{
        text-align: center; 
        background-color: #fff0f0; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #ffcccc;
        margin: 10px 0;
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='center-text'>🎁 點點禮物拆開它</h1>", unsafe_allow_html=True)

# 4. 遊戲邏輯
if st.session_state.clicks < 10:
    # 第一階段：點擊圖片計數
    st.markdown(f"<h3 class='center-text'>進度：{st.session_state.clicks} / 10</h3>", unsafe_allow_html=True)
    
    # 這個按鈕現在看起來就是那張禮物圖
    if st.button("點擊禮物"):
        st.session_state.clicks += 1
        st.rerun()
        
    st.markdown("<p style='text-align:center; color:gray;'>直接點擊上方的禮物圖片</p>", unsafe_allow_html=True)

elif not st.session_state.unlocked:
    # 第二階段：輸入密碼
    st.balloons()
    st.markdown("<h2 class='center-text'>🔒 盒子被鎖住了！</h2>", unsafe_allow_html=True)
    
    # 顯示你要求的提示語
    st.markdown(f"""
        <div class='hint-box'>
            <strong>密碼提示：</strong><br>
            今天的日期與母親節快樂英文<br>
            (共24個字，小寫且不含空格)
        </div>
    """, unsafe_allow_html=True)
    
    password = st.text_input("請輸入密碼：", type="password")
    
    # 驗證密碼
    if password == "20260510happymother'sday":
        st.success("密碼正確！")
        if st.button("點擊查看最終驚喜 ✨", key="unlock_btn"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("密碼不對喔，請檢查日期與拼字（記得包含 ' 喔）")

else:
    # 第三階段：揭曉驚喜
    st.markdown("<h2 class='center-text'>🎉 母親節快樂！ 🎉</h2>", unsafe_allow_html=True)
    
    # 顯示最終驚喜圖片
    st.image(FINAL_URL, use_container_width=True)
    
    st.balloons()
    st.snow()
    
    if st.button("重新開始"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()
