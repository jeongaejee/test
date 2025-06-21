import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 🎯 스터디카페 샘플 데이터
data = {
    '이름': ['공부의신 카페', '스터디앤카페 홍대점', '룰루스터디카페', '에듀존 스터디카페'],
    '위도': [37.5665, 37.5550, 37.5400, 37.5800],
    '경도': [126.9780, 126.9234, 126.9700, 126.9900],
    '요금': ['1시간 2,000원', '3시간 5,000원', '무제한 10,000원', '1일권 9,000원'],
    '운영시간': ['24시간', '09:00~23:00', '07:00~01:00', '24시간'],
    '분위기': ['조용함', '오픈형', '프리미엄 조용형', '스터디룸 가능']
}

df = pd.DataFrame(data)

# 📍 지도 초기 위치 설정 (서울 중심)
center_lat, center_lon = 37.5665, 126.9780
m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

# 🗺️ 마커 추가
for index, row in df.iterrows():
    popup_text = f"""
    <b>{row['이름']}</b><br>
    🕒 운영시간: {row['운영시간']}<br>
    💸 요금: {row['요금']}<br>
    🌈 분위기: {row['분위기']}
    """
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=popup_text,
        tooltip=row['이름'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# 🌐 Streamlit 앱 구성
st.title("📚 스터디카페 지도 시각화")
st.markdown("서울시 주요 스터디카페의 위치, 운영시간, 요금, 분위기 등을 지도로 확인해보세요!")

# 지도 출력
st_data = st_folium(m, width=700, height=500)
