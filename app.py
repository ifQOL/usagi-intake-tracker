import streamlit as st

st.set_page_config(page_title="うさぎのごはん達成率", layout="centered")

st.title("🐇 うさぎのごはん達成率チェッカー")
st.markdown("各食材の**基準量**と**実際に食べた量**を入力してください（g 単位）。")

with st.form("intake_form"):
    st.subheader("📅 1日のごはん記録")

    # ペレット
    st.markdown("### • ペレット")
    pellet_goal = st.number_input("基準量（合計/1日あたり）", min_value=0.0, max_value=100.0, step=0.5, value=30.0, format="%.1f")
    pellet_morning = st.number_input("朝 食べた量", min_value=0.0, max_value=100.0, step=0.5, value=0.0, format="%.1f")
    pellet_evening = st.number_input("晩 食べた量", min_value=0.0, max_value=100.0, step=0.5, value=0.0, format="%.1f")

    # 牧草
    st.markdown("### • 牧草")
    hay_goal = st.number_input("基準量（合計/1日あたり） ", min_value=0.0, max_value=100.0, step=0.5, value=60.0, format="%.1f")
    hay_morning = st.number_input("朝 食べた量 ", min_value=0.0, max_value=100.0, step=0.5, value=0.0, format="%.1f")
    hay_evening = st.number_input("晩 食べた量 ", min_value=0.0, max_value=100.0, step=0.5, value=0.0, format="%.1f")

    # 野菜
    st.markdown("### • 野菜")
    veggie_goal = st.number_input("基準量（合計/1日あたり）  ", min_value=0.0, max_value=100.0, step=0.5, value=60.0, format="%.1f")
    veggie_morning = st.number_input("朝 食べた量  ", min_value=0.0, max_value=100.0, step=0.5, value=0.0, format="%.1f")
    veggie_evening = st.number_input("晩 食べた量  ", min_value=0.0, max_value=100.0, step=0.5, value=0.0, format="%.1f")

    submitted = st.form_submit_button("摂取率を計算")

if submitted:
    def calc_rate(goal, morning, evening):
        return round(((morning + evening) / goal) * 100, 1) if goal > 0 else 0

    pellet_rate = calc_rate(pellet_goal, pellet_morning, pellet_evening)
    hay_rate = calc_rate(hay_goal, hay_morning, hay_evening)
    veggie_rate = calc_rate(veggie_goal, veggie_morning, veggie_evening)

    total_goal = pellet_goal + hay_goal + veggie_goal
    total_intake = (
        pellet_morning + pellet_evening +
        hay_morning + hay_evening +
        veggie_morning + veggie_evening
    )
    total_rate = round((total_intake / total_goal) * 100, 1) if total_goal > 0 else 0

    # 出力をゼロ埋め（00.0%）に整形
    st.success("✅ 今日の摂取率結果")
    st.markdown(f"""
    **ペレット：** {pellet_rate:05.1f}%  
    **牧草：** {hay_rate:05.1f}%  
    **野菜：** {veggie_rate:05.1f}%  
    ---
    **💪 総合達成率：{total_rate:05.1f}%**
    """)
