import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 의약품 부작용 분석")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# 사이드바
st.sidebar.header("🔎 분석 조건")

drug = st.sidebar.selectbox("💊 약 선택", sorted(df["drug"].unique()))
ages = st.sidebar.multiselect("연령대", df["age_group"].unique(), default=df["age_group"].unique())
genders = st.sidebar.multiselect("성별", df["gender"].unique(), default=df["gender"].unique())

# 필터링
filtered = df[
    (df["drug"] == drug) &
    (df["age_group"].isin(ages)) &
    (df["gender"].isin(genders))
]

if filtered.empty:
    st.warning("조건에 맞는 데이터가 없습니다.")
else:
    st.subheader(f"💊 {drug} 부작용 분석 결과")

    col1, col2 = st.columns(2)

    # 1. 부작용 순위
    top_effects = filtered.groupby("side_effect")["count"].sum().reset_index()
    top_effects = top_effects.sort_values(by="count", ascending=False)

    with col1:
        fig1 = px.bar(
            top_effects,
            x="count",
            y="side_effect",
            orientation="h",
            title="🔝 주요 부작용 순위",
            color="side_effect"
        )
        st.plotly_chart(fig1, use_container_width=True)

    # 2. 연령별 비교
    with col2:
        fig2 = px.bar(
            filtered,
            x="age_group",
            y="count",
            color="side_effect",
            barmode="group",
            title="📊 연령별 부작용 비교"
        )
        st.plotly_chart(fig2, use_container_width=True)

    # 3. 성별 분석
    st.subheader("👥 성별 부작용 비율")

    gender_data = filtered.groupby("gender")["count"].sum().reset_index()

    fig3 = px.pie(
        gender_data,
        names="gender",
        values="count",
        title="성별 비율"
    )

    st.plotly_chart(fig3, use_container_width=True)
