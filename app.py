import streamlit as st

st.set_page_config(page_title="うさぎのごはん達成率", layout="centered")

st.title("🐇 うさぎのごはん達成率チェッカー")
st.markdown("各食材の**基準量**と**実際に食べた量**を入力してください。")

with st.form("intake_form"):
    st.subheader("📅 1日のごはん記録")

    def number_input_with_unit(label, key, default, unit="g"):
        col1, col2 = st.columns([4, 1])
        with col1:
            val = st.number_input(label, min_value=0.0, max_value=100.0, step=0.5, value=default, format="%.1f", key=key)
        with col2:
            st.markdown(unit)
        return val

    # ペレット
    st.markdown("### • ペレット")
    pellet_goal = number_input_with_unit("基準量（合計/1日あたり）", "pellet_goal", 30.0)
    pellet_morning = number_input_with_unit("朝 食べた量", "pellet_morning", 0.0)
    pellet_evening = number_input_with_unit("晩 食べた量", "pellet_evening", 0.0)

    # 牧草
    st.markdown("### • 牧草")
    hay_goal = number_input_with_unit("基準量（合計/1日あたり）", "hay_goal", 0.0)
    hay_morning = number_input_with_unit("朝 食べた量", "hay_morning", 0.0)
    hay_evening = number_input_with_unit("晩 食べた量", "hay_evening", 0.0)

    # 水分摂取量（単位は ml）
    st.markdown("### • 水分摂取量（飲水）")
    water_goal = number_input_with_unit("基準量（合計/1日あたり）", "water_goal", 0.0, unit="ml")
    water_morning = number_input_with_unit("朝 飲んだ量", "water_morning", 0.0, unit="ml")
    water_evening = number_input_with_unit("晩 飲んだ量", "water_evening", 0.0, unit="ml")

    submitted = st.form_submit_button("摂取率を計算")

if submitted:
    def calc_rate(goal, morning, evening):
        return round(((morning + evening) / goal) * 100, 1) if goal > 0 else 0.0

    pellet_rate = calc_rate(pellet_goal, pellet_morning, pellet_evening)
    hay_rate = calc_rate(hay_goal, hay_morning, hay_evening)
    water_rate = calc_rate(water_goal, water_morning, water_evening)

    total_goal = pellet_goal + hay_goal + water_goal
    total_intake = (
        pellet_morning + pellet_evening +
        hay_morning + hay_evening +
        water_morning + water_evening
    )
    total_rate = round((total_intake / total_goal) * 100, 1) if total_goal > 0 else 0.0

    st.success("✅ 今日の摂取率結果")
    st.markdown(f"""
    **ペレット：** {pellet_rate:.1f}%  
    **牧草：** {hay_rate:.1f}%  
    **水分摂取：** {water_rate:.1f}%  
    ---
    **💪 総合達成率：{total_rate:.1f}%**
    """)
