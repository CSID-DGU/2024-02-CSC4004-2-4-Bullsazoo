from openai import OpenAI

#https://platform.openai.com/api-keys Create API Key
#setx OPENAI_API_KEY "my_key" --> Windows PowerShell
#https://mz-moonzoo.tistory.com/49 -- How to Discipline this model

def gpt_response(question):
    client = OpenAI(
        project='proj_vNFRktfgC1qSLMvWrFHCnp2u',
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 이제부터 최고의 '시각 장애인 쇼핑 도우미'야"},
            {"role": "system", "content": "또한 나는 '전맹이 아닌 시각장애인'이야"},
            {"role": "system","content": "상품 정보, 안내, 재안내, 가격, 최다 구매, 금일 쇼핑 리스트, 영수증 스캔"},
            {"role": "system","content": "상품 정보나 영수증 스캔을 할때는, 물건의 종류를 카메라로 인식해서 품목, 가격,"
                                         " 제조사, 할인율 사용자에게 출력하고 이를 테이블화 해서 DB에 저장할거야"},
            {"role": "system", "content": "재안내 스크립트의 종류 1. 회원 가입 후 전반적인 기능 설명, 2. 사용자의 재안내 요청이 왔을 때, 이전 스크립트를 기억해서 다시 안내"},
            {"role": "system", "content": "최대 구매 상품이랑 금일 쇼핑 리스트는 각각 DB에 저장된 정보를 따올꺼야"},
            {"role": "system", "content": "let's think step by step"},
            {"role": "system", "content": "너는 무슨 질문이 들어와도 잘 답변할 수 있을거야!!"},
            {"role": "user", "content": question},
        ]
    )

    answer = completion.choices[0].message.content
    output_text = ''
    # text 에서 *, ~ 등의 문자 제거
    for i in range (len(answer)):
        if answer[i] == '*' or answer[i] == '~':
            continue
        output_text += answer[i]

    return output_text
