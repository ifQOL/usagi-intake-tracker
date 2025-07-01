import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="うさぎのごはん達成率", layout="centered")

st.title("\U0001F407 うさぎのごはん達成率チェッカー")
st.markdown("各食材の""\**基準量\**""と""\**実際に食べた量\**""を入力してください（g 単位）。")

# 各位のリスト（十の位・一の位・小数第一位）
tens_options = list(range(0, 10))      # 0〜9（十の位）
ones_options = list(range(0, 10))      # 0〜9（一の位）
decimal_options = [i / 10 for i in range(0, 10)]  # 0.0〜0.9（小数第一位）

def combine_weight(tens, ones, decimal):
    return round((tens * 10) + ones + decimal, 1)

with st.form("intake_form"):
    st.subheader("\U0001F4C5 1日のごはん記録")

    def intake_input(label_prefix, default=(3,0,0.0)):
        st.markdown(f"**{label_prefix}**")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            t = st.selectbox("十の位", tens_options, index=default[0], label_visibility="collapsed")
        with col2:
            o = st.selectbox("一の位", ones_options, index=default[1], label_visibility="collapsed")
        with col3:
            d = st.selectbox("小数位", decimal_options, index=int(default[2]*10), label_visibility="collapsed")
        return combine_weight(t, o, d)

    # ペレット
    pellet_goal = intake_input("ペレット 基準量（1日あたり）", (3, 0, 0.0))
    pellet_morning = intake_input("ペレット 朝 食べた量", (0, 0, 0.0))
    pellet_evening = intake_input("ペレット 晩 食べた量", (0, 0, 0.0))

    # 牧草
    hay_goal = intake_input("牧草 基準量（1日あたり）", (6, 0, 0.0))
    hay_morning = intake_input("牧草 朝 食べた量", (0, 0, 0.0))
    hay_evening = intake_input("牧草 晩 食べた量", (0, 0, 0.0))

    # 野菜
    veggie_goal = intake_input("野菜 基準量（1日あたり）", (2, 0, 0.0))
    veggie_morning = intake_input("野菜 朝 食べた量", (0, 0, 0.0))
    veggie_evening = intake_input("野菜 晩 食べた量", (0, 0, 0.0))

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

    st.success("\u2705 今日の摂取率結果")
    st.markdown(f"**ペレット：** {pellet_rate}%\n\n**牧草：** {hay_rate}%\n\n**野菜：** {veggie_rate}%\n\n---\n**\U0001f4aa 総合達成率：{total_rate}%**")
