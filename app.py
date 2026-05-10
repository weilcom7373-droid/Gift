import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

# --- 圖片連結設定 ---
# 禮物盒圖片 (1F9...)
GIFT_ID = "1F9lAIRkmhpqwZesoZoT2Gq4j8fs1Z0W2" 
# 最終驚喜圖片 (你剛才提供的 1OB...)
FINAL_ID = "1OBG3H77EBgEYRoUDcdAUY37AvGlUWjD4"

GIFT_URL = f"https://lh3.googleusercontent.com/d/{GIFT_ID}"
FINAL_URL = f"https://lh3.googleusercontent.com/d/{FINAL_ID}"

# 初始化狀態
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# 2. 自定義 CSS：強化點擊感與圖片顯示
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
        border: 4px dashed #ffcccc; /* 虛線邊框增加禮物感 */
        border-radius: 40px;
        color: transparent !important;
        display: block;
        margin: 0 auto;
        cursor: pointer;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transition: all 0.1s ease;
    }}

    /* 按下去時的超強回饋感 */
    .stButton > button:active {{
        transform: scale(0.85) !important; 
        filter: brightness(0.8); 
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
        background-color: #f8f8f8;
    }}

    /* 滑鼠經過時的邊框顏色變化 */
    .stButton > button:hover {{
        border: 4px solid #ff4b4b;
        color: transparent !important;
    }}

    .center-text {{ text-align: center; color: #ff4b4b; font-weight: bold; }}
    .hint-box {{
        text-align: center; 
        background-color: #fff5f5; 
        padding: 20px; 
        border-radius: 20px; 
        border: 2px solid #ffcccc;
        margin: 15px auto;
        width: 85%;
        font-size: 18px;
        line-height: 1.6;
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='center-text'>🎁 送你的驚喜禮物</h1>", unsafe_allow_html=True)

# 3. 遊戲邏輯
if st.session_state.clicks < 10:
    # 第一階段：點擊圖片計數
    st.markdown(f"<h3 class='center-text'>還要拆解 {10 - st.session_state.clicks} 次！</h3>", unsafe_allow_html=True)
    
    if st.button("ClickMe"):
        st.session_state.clicks += 1
        st.rerun()
        
    st.markdown("<p style='text-align:center; color:#999;'>👆 請直接點擊上面的禮物圖案</p>", unsafe_allow_html=True)

elif not st.session_state.unlocked:
    # 第二階段：輸入密碼
    st.balloons()
    st.markdown("<h2 class='center-text'>🔒 哎呀，盒子被鎖住了！</h2>", unsafe_allow_html=True)
    
    # 顯示密碼提示
    st.markdown(f"""
        <div class='hint-box'>
            <strong>🔑 密碼提示：</strong><br>
            今天的日期與母親節快樂英文<br>
            (共24個字，小寫且不含空格)
        </div>
    """, unsafe_allow_html=True)
    
    # 密碼：20260510happymother'sday
    password = st.text_input("請在此輸入密碼：", type="password")
    
    if password == "20260510happymother'sday":
        st.success("密碼正確！正在開啟驚喜...")
        if st.button("點擊打開盒子 ✨", key="open_action"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("密碼不太對喔，再檢查一下拼字 (包含 ') 或日期！")

else:
    # 第三階段：揭曉新的驚喜圖片
    st.markdown("<h2 class='center-text'>🎉 母親節快樂！ 🎉</h2>", unsafe_allow_html=True)
    
    # 顯示你剛提供的這張圖 (ID: 1OBG3H77EBgEYRoUDcdAUY37AvGlUWjD4)
    st.image(FINAL_URL, use_container_width=True)
    
    st.balloons()
    st.snow()
    
    if st.button("再玩一次"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()
