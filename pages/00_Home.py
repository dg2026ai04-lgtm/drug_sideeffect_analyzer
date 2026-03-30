import streamlit as st

st.set_page_config(page_title="의약품 부작용 분석", layout="wide")

st.title("💊 의약품 부작용 분석 서비스")

st.markdown("""
## 👋 프로젝트 소개

이 서비스는 의약품 부작용 데이터를 분석하여  
연령과 성별에 따른 패턴을 시각화하는 웹앱입니다.
""")

st.markdown("---")

st.subheader("📌 데이터 출처")
st.markdown("""
- 식품의약품안전처(MFDS) 데이터 기반  
- 학습용 재구성 데이터
""")

st.info("👉 왼쪽 메뉴에서 Analysis 페이지로 이동하세요!")
