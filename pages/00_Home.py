import streamlit as st

st.set_page_config(page_title="의약품 부작용 분석", layout="wide")

st.title("💊 의약품 부작용 분석 서비스")

st.markdown("""
## 👋 프로젝트 소개

이 서비스는 의약품 복용 시 발생할 수 있는 부작용을  
연령과 성별에 따라 분석하는 데이터 시각화 웹 애플리케이션입니다.

사용자는 약물을 선택하고 조건을 설정하여  
부작용 발생 패턴을 직관적으로 확인할 수 있습니다.
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
1. 왼쪽 사이드바에서 📊 Analysis 페이지 선택  
2. 약, 연령, 성별 조건 설정  
3. 그래프를 통해 부작용 확인  
""")

st.info("👉 왼쪽 메뉴에서 페이지를 이동하세요!")
