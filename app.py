import streamlit as st

st.set_page_config(page_title="うさぎのごはん達成率", layout="centered")

st.title("\U0001F407 うさぎのごはん達成率チェッカー")
st.markdown("各食材の**基準量**と**実際に食べた量**を入力してください（g 単位）。")

# CSSでselectboxの幅と間隔を整える
st.markdown("""
<style>
    div[data-baseweb="select"] {
        width: 80px !important;
        margin-right: -20px !important;
    }
</style>
""", unsafe_allow_html=True)

# 各位のリスト（十の位・一の位・小数第一位）
tens_options = list(range(0, 10))
ones_options = list(range(0, 10))
decimal_options = [(i / 10, f".{i}") for i in range(0, 10)]  # (0.0, ".0") 〜 (0.9, ".9")

def combine_weight(tens, ones, decimal):
    return round((tens * 10) + ones + decimal, 1)

with st.form("intake_form"):
    st.subheader("\U0001F4C5 1日のごはん記録")

    def intake_input(label_prefix, key_prefix, default=(0,0,0.0)):
        st.markdown(f"**{label_prefix}**")
        col1, col2, col3 = st.columns([1, 1, 1], gap="small")
        with col1:
            t = st.selectbox("", tens_options, index=default[0], key=f"{key_prefix}_tens")
        with col2:
            o = st.selectbox("", ones_options, index=default[1], key=f"{key_prefix}_ones")
        with col3:
            decimal_values = [d[0] for d in decimal_options]
            decimal_labels = [d[1] for d in decimal_options]
            d = st.selectbox("", options=decimal_values, format_func=lambda x: f".{int(x*10)}", index=int(default[2]*10), key=f"{key_prefix}_decimal")
        return combine_weight(t, o, d)

    # ペレット
    pellet_goal = intake_input("ペレット 基準量（1日あたり）", "pellet_goal", (3, 0, 0.0))
    pellet_morning = intake_input("ペレット 朝 食べた量", "pellet_morning", (0, 0, 0.0))
    pellet_evening = intake_input("ペレット 晩 食べた量", "pellet_evening", (0, 0, 0.0))

    # 牧草
    hay_goal = intake_input("牧草 基準量（1日あたり）", "hay_goal", (6, 0, 0.0))
    hay_morning = intake_input("牧草 朝 食べた量", "hay_morning", (0, 0, 0.0))
    hay_evening = intake_input("牧草 晩 食べた量", "hay_evening", (0, 0, 0.0))

    # 野菜
    veggie_goal = intake_input("野菜 基準量（1日あたり）", "veggie_goal", (2, 0, 0.0))
    veggie_morning = intake_input("野菜 朝 食べた量", "veggie_morning", (0, 0, 0.0))
    veggie_evening = intake_input("野菜 晩 食べた量", "veggie_evening", (0, 0, 0.0))

    submitted = st.form_submit_button("摂取率を計算")

if submitted:
    def calc_rate(goal, morning, evening):
        return round(((morning + evening) / goal) * 100, 1) if goal > 0 else 0

    pellet_rate = calc_rate(pellet_goal, pellet_morning, pellet_evening)
    hay_rate = calc_rate(hay_goal, hay_morning, hay_evening)
    veggie_rate = calc_rate(veggie_goal, veggie_morning, veggie_evening)

    total_goal = pellet_goal + hay_goal + veggie_goal
    total_intake = pellet_morning + pellet_evening + hay_morning + hay_evening + veggie_morning + veggie_evening
    total_rate = calc_rate(total_goal, total_intake, 0)

    st.success("✅ 今日の摂取率結果")
    st.markdown(f"""
    **ペレット：** {pellet_rate}%  
    **牧草：** {hay_rate}%  
    **野菜：** {veggie_rate}%  
    ---  
    **💪 総合達成率：{total_rate}%**
    """)
