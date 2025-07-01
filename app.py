import streamlit as st

st.set_page_config(page_title="うさぎのごはん達成率", layout="centered")

st.title("\U0001F407 うさぎのごはん達成率チェッカー")
st.markdown("各食材の""\**基準量\**""と""\**実際に食べた量\**""を入力してください（g 単位）。")

# 数値選択肢（0.0〜100.0gまで0.5刻み）
def get_weight_options():
    return [round(i * 0.5, 1) for i in range(0, 201)]

weight_options = get_weight_options()

with st.form("intake_form"):
    st.subheader("\U0001F4C5 1日のごはん記録")

    st.markdown("### • ペレット")
    pellet_goal = st.selectbox("基準量（合計/1日あたり）", options=weight_options, index=60, key="pellet_goal")
    pellet_morning = st.selectbox("朝 食べた量", options=weight_options, index=0, key="pellet_morning")
    pellet_evening = st.selectbox("晩 食べた量", options=weight_options, index=0, key="pellet_evening")

    st.markdown("### • 牧草")
    hay_goal = st.selectbox("基準量（合計/1日あたり）", options=weight_options, index=120, key="hay_goal")
    hay_morning = st.selectbox("朝 食べた量", options=weight_options, index=0, key="hay_morning")
    hay_evening = st.selectbox("晩 食べた量", options=weight_options, index=0, key="hay_evening")

    st.markdown("### • 野菜")
    veggie_goal = st.selectbox("基準量（合計/1日あたり）", options=weight_options, index=40, key="veggie_goal")
    veggie_morning = st.selectbox("朝 食べた量", options=weight_options, index=0, key="veggie_morning")
    veggie_evening = st.selectbox("晩 食べた量", options=weight_options, index=0, key="veggie_evening")

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
