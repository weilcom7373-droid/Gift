import streamlit as st

# 1. 設定網頁標題
st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

# 2. 圖片 ID 處理 (已經幫你轉好 Google Drive 直接連結格式)
GIFT_IMAGE_URL = "https://drive.google.com/uc?export=view&id=1F9lAIRkmhpqwZesoZoT2Gq4j8fs1Z0W2"
FINAL_IMAGE_URL = "https://drive.google.com/uc?export=view&id=18w-ZSzSB2UtnhgYWZah48iROFPGJZd3M"

# 3. 初始化狀態
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# 4. 自定義 CSS：這段是用來把你的 Google Drive 圖片變成「超大按鈕」
st.markdown(f"""
    <style>
    .stButton > button {{
        width: 300px;
        height: 300px;
        background-image: url('{GIFT_IMAGE_URL}');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-color: transparent;
        border: none;
        color: transparent !important;
        display: block;
        margin: 0 auto;
        cursor: pointer;
        transition: transform 0.2s;
    }}
    .stButton > button:active {{
        transform: scale(0.95);
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

# 5. 遊戲邏輯判斷
if st.session_state.clicks < 10:
    # 第一關：點擊圖片 10 次
    st.markdown(f"<h3 class='text-center'>請點點圖片拆開它<br>({st.session_state.clicks} / 10)</h3>", unsafe_allow_html=True)
    
    # 這裡的按鈕標籤寫 "Click" 但會被上面的 CSS 隱藏，顯示出來的是你的圖片
    if st.button("Click"):
        st.session_state.clicks += 1
        st.rerun()

elif not st.session_state.unlocked:
    # 第二關：輸入密碼
    st.balloons()
    st.markdown("<h3 class='text-center'>🔒 盒子被鎖住了！</h3>", unsafe_allow_html=True)
    
    st.write("<p style='text-align:center;'>請輸入日期與英文(小寫且不含空格)</p>", unsafe_allow_html=True)
    
    # 密碼就是你設定的：20260510happymother'sday
    password = st.text_input("輸入密碼：", type="password")
    
    if password == "20260510happymother'sday":
        st.success("密碼正確！")
        if st.button("點擊查看驚喜 ✨", key="final_btn"):
            st.session_state.unlocked = True
            st.rerun()
    elif password != "":
        st.error("密碼不對喔，再試一次！")

else:
    # 第三關：顯示最終圖片
    st.markdown("<h2 class='text-center'>🎉 驚喜揭曉！ 🎉</h2>", unsafe_allow_html=True)
    
    # 顯示你放在 Google Drive 的第二張圖
    st.image(FINAL_IMAGE_URL, caption="這是我準備的禮物", use_container_width=True)
    
    st.balloons()
    st.snow()
    
    if st.button("重新開始"):
        st.session_state.clicks = 0
        st.session_state.unlocked = False
        st.rerun()
