import streamlit as st

# 🎨 CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e8f5e9, #fff3e0);
}
.block-container {
    background-color: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.title("📖 의약품 정보")

st.markdown("""
## 💊 주요 약물

### 아세트아미노펜
- 해열, 진통
- 간 손상 위험

### 이부프로펜
- 소염진통제
- 위장 장애

### 아스피린
- 혈액 응고 억제
- 출혈 위험
""")

st.markdown("---")

st.subheader("🧠 프로젝트 의의")
st.markdown("""
공공데이터를 활용하여  
의약품 부작용을 분석하고  
데이터 기반 의사결정의 중요성을 이해함
""")

st.warning("⚠️ 본 서비스는 학습용입니다.")
