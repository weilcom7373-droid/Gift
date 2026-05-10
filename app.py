import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

# --- 這裡更換圖片 ID (如果圖片反了，請把這兩個 ID 對調即可) ---
# 目前設定：1F9... 是禮物盒，18w... 是最後驚喜
GIFT_ID = "1F9lAIRkmhpqwZesoZoT2Gq4j8fs1Z0W2" 
FINAL_ID = "18w-ZSzSB2UtnhgYWZah48iROFPGJZd3M"

GIFT_URL = f"https://lh3.googleusercontent.com/d/{GIFT_ID}"
FINAL_URL = f"https://lh3.googleusercontent.com/d/{FINAL_ID}"

# 初始化狀態
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# 2. 自定義 CSS：強化點擊感
st.markdown(f"""
    <style>
    /* 禮物圖片按鈕樣式 */
    .stButton > button {{
        width: 320px;
        height: 320px;
        background-image: url('{GIFT_URL}');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-color: #ffffff;
        border: 5px solid #ffebeb;
        border-radius: 40px;
        color: transparent !important;
        display: block;
        margin: 0 auto;
        cursor: pointer;
        box-shadow: 0 8px 15px rgba(0,0,0,0.1); /* 加入陰影 */
        transition: all 0.1s ease; /* 讓動畫平滑 */
    }}

    /* 按下去時的效果：縮小、變暗、陰影消失 */
    .stButton > button:active {{
        transform: scale(0.85) !important; 
        filter: brightness(0.7); 
        box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
        background-color: #f0f0f0;
    }}

    /* 防止滑鼠經過變色 */
    .stButton > button:hover {{
        border: 5px solid #ff4b4b;
        color: transparent !important;
    }}

    .center-text {{ text-align: center; color: #ff4b4b; }}
    .hint-box {{
        text-align: center; 
        background-color: #fff0f0; 
        padding: 15px; 
        border-radius: 15px; 
        border: 2px dashed #ffcccc;
        margin: 10px auto;
        width: 90%;
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='center-text'>🎁 點點禮物拆開它</h1>", unsafe_allow_html=True)

# 3. 遊戲邏輯
if st.session_state.clicks < 10:
    # 第一階段：點擊圖片計數
    st.markdown(f"<h3 class='center-text'>拆解進度：{st.session_state.clicks} / 10</h3>", unsafe_allow_html=True)
    
    if st.button("Click"):
        st.session_state.clicks += 1
        st.rerun()
        
    st.markdown("<p style='text-align:center; color:#888;'>👆 請直接點擊上面的禮物圖案</p>", unsafe_allow_html=True)

elif not st.session_state.unlocked:
    # 第二階段：輸入密碼
    st.balloons()
    st.markdown("<h2 class='center-text'>🔒 這個盒子被鎖住了！</h2>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='hint-box'>
            <strong>🔑 密碼提示：</strong><br>
            今天的日期與母親節快樂英文<br>
            (共24個字，小寫且不含空格)
        </div>
    """, unsafe_allow_html=True)
    
    password = st.text_input("請輸入密碼：", type="password")
    
    # 驗證密碼：20260510happymother'sday
    if password == "20260510happymother'sday":
        st.success("密碼正確！")
        if st.button("點擊查看最後驚喜 ✨", key="final_check"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("密碼不太對喔，再試一次！")

else:
    # 第三階段：揭曉真正的驚喜圖片
    st.markdown("<h2 class='center-text'>🎉 祝你母親節快樂！ 🎉</h2>", unsafe_allow_html=True)
    
    # 顯示最終驚喜圖片
    st.image(FINAL_URL, use_container_width=True)
    
    st.balloons()
    st.snow()
    
    if st.button("重啟驚喜"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()
