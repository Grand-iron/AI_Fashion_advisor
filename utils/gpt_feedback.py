import openai

# 🔑 본인의 OpenAI API 키를 여기에 입력
openai.api_key = "##"

def generate_feedback(prompt):
    """
    사용자 프롬프트를 받아 GPT 스타일 피드백을 생성

    Parameters:
        prompt (str): GPT에게 전달할 텍스트 입력

    Returns:
        str: GPT가 생성한 스타일 피드백
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "당신은 트렌디한 패션 스타일리스트입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300,
        )
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"❌ GPT 호출 중 오류 발생: {str(e)}"
