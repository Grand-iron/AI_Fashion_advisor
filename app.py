import streamlit as st
from utils.color_analyzer import get_main_colors
from utils.gpt_feedback import generate_feedback
from utils.clothing_detector import detect_clothing
from PIL import Image
from io import BytesIO


st.set_page_config(page_title="AI 패션 피드백 도우미", layout="centered")

# 전체 배경 흰색으로 설정
st.markdown("""
<style>
            
/* 전체 배경*/
.stApp {
    background-color: #ffffff;
}
            
/* 사이드바 스타일 */
[data-testid="stSidebar"] {
    background-color: #f5f7fa;
    padding: 20px;
    border-right: 1px solid #d0d3d8;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #2c3e50;
}
.css-1c7y2kd, .css-1inwz65 {
    font-size: 16px !important;
    color: #333 !important;
    padding: 8px 12px !important;
    border-radius: 8px;
    transition: 0.2s;
}
.css-1inwz65:has(input:checked) {
    background-color: #d0ebff;
    font-weight: bold;
    color: #007BFF !important;
}

            
/* 말풍선 및 카드 스타일 */
.hero-bubble {
    position: relative;
    background-color: #ffe5e5;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
    margin-left: 16px;
}
.hero-bubble::before {
    content: "";
    position: absolute;
    left: -16px;
    top: 30px;
    width: 0;
    height: 0;
    border-top: 12px solid transparent;
    border-bottom: 12px solid transparent;
    border-right: 16px solid #ffe5e5;
}
.hero-title {
    font-size: 24px;
    font-weight: 800;
    color: #d10000;
    margin-bottom: 10px;
}
.hero-sub {
    font-size: 16px;
    color: #660000;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# 사이드바 메뉴
with st.sidebar:
    st.image("images/logo_image.png", width=120)  # 로고 이미지 파일 경로는 프로젝트에 맞게 조정하세요
    st.markdown("<h2 style='color:#2c3e50; font-weight:700; margin-top:10px;'>👗 AI 스타일 도우미</h2>", unsafe_allow_html=True)
    st.subheader("")
    menu = st.selectbox("📂 메뉴를 선택하세요", ["🏠 홈", "👕 패션 피드백"])

# 홈 화면
if menu == "🏠 홈":
    st.title("👗 AI 패션 스타일 피드백 도우미")

    st.subheader("")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("images/home_image.png", use_container_width=True)
    with col2:
        st.markdown("""
        <div class="hero-bubble">
            <div class="hero-title">😳 당신의 패션, 괜찮은가요?</div>
            <div class="hero-sub">
                지금 AI 스타일리스트가 평가해드립니다.<br>
                업로드하고, 피드백 받고, 자신감을 가져보세요!
            </div>
        </div>
        
        <br>

        <style>
        .card-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-top: 20px;
        }

        .card-item {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            padding: 18px;
            border-radius: 14px;
            font-size: 16px;
            line-height: 1.6;
            color: #1a1a1a;
            transition: 0.3s;
        }
        .card-item:hover {
            background-color: #f5f5f5;
        }

        .card-icon {
            font-size: 20px;
            margin-right: 18px;
            color: #007BFF;
            font-weight: bold;
        }
        </style>

        <h3 style='color:#f9a825; font-weight:700;'>✨ 무엇을 할 수 있나요?</h3>

        <div class='card-list'>
            <div class='card-item'><span class='card-icon'>📸</span><b>전신 사진</b>을 업로드하면 GPT가 스타일 분석</div>
            <div class='card-item'><span class='card-icon'>🎨</span>쿨/웜톤, 채도, 색상 대비 분석</div>
            <div class='card-item'><span class='card-icon'>📅</span>데이트, 면접, 하객 등 <b>TPO 상황별 피드백</b> 제공</div>
            <div class='card-item'><span class='card-icon'>🛍️</span>추후 <i>연예인 스타일 매칭</i>, 쇼핑 추천 기능 추가 예정</div>
        </div>
                    
        <br>

    
        """, unsafe_allow_html=True)
    
elif menu == "👕 패션 피드백":
    st.title("👕 패션 피드백 받기")

    uploaded = st.file_uploader("전신 패션 사진을 업로드해주세요", type=["jpg", "png"])
    tpo = st.selectbox("TPO (상황)를 선택하세요", ["일상", "데이트", "면접", "하객"])

    if uploaded:
        # 이미지 열기 및 표시 (저장 없이)
        image = Image.open(uploaded)
        st.image(image, use_container_width=True)

        # 색상 분석
        with st.spinner("색상 분석 중..."):
            colors = get_main_colors(image)
        st.markdown("### 🎨 주요 색상")
        for color in colors:
            rgb = color.replace("RGB(", "").replace(")", "")
            st.markdown(
                f"<div style='width: 100%%; height: 50px; background-color: rgb({rgb}); border-radius: 8px; margin-bottom: 8px'></div>",
                unsafe_allow_html=True
            )

        # 의류 분석 (이미지 메모리로 전송)
        with st.spinner("의류 분석 중..."):
            image_buffer = BytesIO()
            image.save(image_buffer, format="JPEG")
            image_buffer.seek(0)
            clothing_items = detect_clothing(image_buffer)

        st.markdown("### 👕 감지된 옷 종류")
        st.write(", ".join(clothing_items))
        

        # GPT 피드백 생성
        with st.spinner("AI 피드백 생성 중..."):
            prompt = f"""
            당신은 다정하고 센스 있는 패션 스타일리스트입니다.
            다음은 사용자 착장 정보입니다:

            - 감지된 옷: {', '.join(clothing_items)}
            - 주요 색상: {', '.join(colors)}
            - 착용 상황(TPO): {tpo}

            친근하고 따뜻한 말투로, 마치 친구에게 이야기하듯 패션 피드백을 주세요.
            칭찬도 아끼지 말고, 개선할 부분이 있다면 숨기지 말고 부드럽게 말해주세요 😊
            너무 길지 않게 4~5줄 정도로 간결하게 작성해주세요.
            """
            feedback = generate_feedback(prompt)

        # GPT 결과 출력
        st.markdown("### 📢 스타일 피드백")
        st.markdown(f"""
        <div style="background-color:#f0f2f6; padding:15px; border-radius:10px; font-size:16px;">
        🧠 <b>AI 피드백:</b><br>
        {feedback}
        </div>
        """, unsafe_allow_html=True)
