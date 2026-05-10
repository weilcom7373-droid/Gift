import streamlit as st

st.set_page_config(page_title="給你的驚喜", page_icon="🎁")

if 'clicks' not in st.session_state: st.session_state.clicks = 0
if 'stage' not in st.session_state: st.session_state.stage = 1

st.markdown("<h2 style='text-align: center;'>🎁 一份神祕禮物 🎁</h2>", unsafe_allow_html=True)

if st.session_state.stage <= 5:
    if st.session_state.stage < 5:
        st.write(f"<p style='text-align: center;'>這是第 {st.session_state.stage} 層包裝 (點擊 10 次)</p>", unsafe_allow_html=True)
    else:
        st.write("<p style='text-align: center;'>最後一層了！加油！</p>", unsafe_allow_html=True)
    
    # 這裡顯示禮物盒按鈕
    # 隨階段變換大小（100px 遞減到 60px）
    size = 110 - (st.session_state.stage * 10)
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🎁", key=f"btn_{st.session_state.stage}_{st.session_state.clicks}"):
            st.session_state.clicks += 1
            if st.session_state.clicks >= 10:
                st.session_state.stage += 1
                st.session_state.clicks = 0
                st.balloons()
                st.rerun()
    
    st.progress(st.session_state.clicks / 10)

elif st.session_state.stage == 6:
    st.write("<h3 style='text-align: center;'>🔑 盒子被鎖住了！</h3>", unsafe_allow_html=True)
    password = st.text_input("請輸入今天的日期 (YYYYMMDD)：", type="password")
    
    if password == "20260510":
        st.success("密碼正確！正在打開最後的驚喜...")
        if st.button("點擊看驚喜內容"):
            st.session_state.stage = 7
            st.rerun()
    elif password != "":
        st.error("日期不對喔，再想想？")

else:
    st.balloons()
    st.snow()
    st.markdown("<h2 style='text-align: center;'>✨ 祝你快樂 ✨</h2>", unsafe_allow_html=True)
    # 這裡請換成你真正想展示的圖片網址
    st.image("https://placekitten.com/500/500", caption="這是給你的最終驚喜！", use_container_width=True)
    if st.button("再玩一次"):
        st.session_state.stage = 1
        st.rerun()
