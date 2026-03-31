import streamlit as st

st.set_page_config(page_title="의약품 부작용 분석", layout="wide")

# 🎨 CSS 디자인
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e0f7fa, #fce4ec);
}

.block-container {
    background-color: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.title("💊 의약품 부작용 분석 서비스")

st.markdown("""
## 👋 프로젝트 소개
의약품 부작용 데이터를 분석하여  
연령과 성별에 따른 패턴을 시각화하는 서비스입니다.
""")

st.markdown("---")

st.subheader("📌 데이터 출처")
st.markdown("""
- 식품의약품안전처(MFDS) 데이터 기반  
- 학습용 재구성 데이터
""")

st.info("👉 왼쪽 메뉴에서 페이지를 선택하세요!")
