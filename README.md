# AI_Fashion_advisor (패션 조언 AI)

#### 역할 배분

| 역할   | 인원                             |
| ------ | -------------------------------- |
| 기획   | 20230012 김지연, 20200811 곽상헌 |
| 프론트 | 20231385 박승찬                  |
| 백     | 20190685 권장혁, 20230643 권순도 |
| 총정리 | 20220832 김영조                  |

#### 기능

- 선택한 상황에 맞춘 피드백
- 의상 및 색상 분석
- 분석 결과에 따른 맞춤 피드백 생성
- 상세 내용 ppt 및 시연 연상 참조

#### HOW TO PLAY (API키는 별도 추가)

1.아나콘다 설치된 상태에서 아나콘다 프롬프트 또는 vscode 터미널 cmd창에서 아래 코드 실행

conda create -n fashion_ai python=3.10 가상환경 생성
conda activate fashion_ai 가상환경 실행

2.프로젝트 폴더로 이동. vscode 터미널 cmd창에서 입력
cd 압축 푼 경로
예: cd C:\Users\사용자이름\Downloads\fashion_ai_app

3.필요한 라이브러리 설치. vscode 터미널 cmd창에서 입력
pip install -r requirements.txt

4.Streamlit 앱 실행. vscode 터미널 cmd창에서 입력. 자동으로 창이 뜸.
streamlit run app.py
