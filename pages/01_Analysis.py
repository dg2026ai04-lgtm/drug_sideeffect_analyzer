import streamlit as st
import pandas as pd
import plotly.express as px

# 🎨 CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f3e5f5, #e1f5fe);
}
.block-container {
    background-color: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.title("📊 의약품 부작용 분석")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# 사이드바
st.sidebar.header("🔎 분석 조건")
drug = st.sidebar.selectbox("약 선택", sorted(df["drug"].unique()))
ages = st.sidebar.multiselect("연령대", df["age_group"].unique(), default=df["age_group"].unique())
genders = st.sidebar.multiselect("성별", df["gender"].unique(), default=df["gender"].unique())

filtered = df[
    (df["drug"] == drug) &
    (df["age_group"].isin(ages)) &
    (df["gender"].isin(genders))
]

if filtered.empty:
    st.warning("데이터 없음")
else:
    st.subheader(f"💊 {drug} 분석 결과")

    # 🔥 위험도 계산
    total = filtered["count"].sum()
    risk_df = filtered.groupby("side_effect")["count"].sum().reset_index()
    risk_df["risk_score"] = (risk_df["count"] / total) * 100
    risk_df = risk_df.sort_values(by="risk_score", ascending=False)

    # 그래프
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(risk_df, x="risk_score", y="side_effect",
                      orientation="h", title="⚠️ 부작용 위험도 (%)",
                      color="risk_score", color_continuous_scale="Reds")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.bar(filtered, x="age_group", y="count",
                      color="side_effect", title="📊 연령별 비교")
        st.plotly_chart(fig2, use_container_width=True)

    # 성별
    st.subheader("👥 성별 비율")
    gender_data = filtered.groupby("gender")["count"].sum().reset_index()
    fig3 = px.pie(gender_data, names="gender", values="count")
    st.plotly_chart(fig3, use_container_width=True)

    # 🔥 TOP 부작용 강조
    top = risk_df.iloc[0]
    st.error(f"🚨 가장 위험: {top['side_effect']} ({top['risk_score']:.1f}%)")
