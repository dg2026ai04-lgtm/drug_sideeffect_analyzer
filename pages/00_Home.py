import streamlit as st

st.set_page_config(page_title="의약품 부작용 분석", layout="wide")

st.title("💊 의약품 부작용 분석 서비스")

st.markdown("""
## 👋 프로젝트 소개

이 서비스는 의약품 부작용 데이터를 분석하여  
연령과 성별에 따른 패턴을 시각화하는 웹 애플리케이션입니다.

사용자는 Analysis 페이지에서 약을 선택하고  
부작용 발생 경향을 확인할 수 있습니다.
""")

st.markdown("---")

st.subheader("📌 데이터 출처")

st.markdown("""
- 식품의약품안전처(MFDS) 의약품 이상사례 보고 데이터 기반  
- 학습용으로 재구성된 데이터  
- 실제 의료 판단을 위한 자료가 아닙니다.
""")

st.markdown("---")

st.subheader("🚀 사용 방법")

st.markdown("""
1. 왼쪽 메뉴에서 📊 Analysis 클릭  
2. 약, 연령, 성별 선택  
3. 그래프 확인  
""")

st.info("👉 왼쪽 사이드바에서 페이지를 이동하세요!")
