import enum
import random

class RSP(enum.Enum):
    가위 = 0
    바위 = 1
    보 = 2

    def game(user_choice: str = "가위") -> str:
        assert user_choice in [item.name for item in RSP], "잘못 입력했습니다."
        
        while True:
            computer_choice = random.choice(list(RSP.__members__))
            print(f"사용자입력: {user_choice} & 컴퓨터입력: {computer_choice}")
            
            결과 = (RSP[user_choice].value - RSP[computer_choice].value) % 3
            
            if 결과 == 1:
                return "승"
            elif 결과 == 2:
                return "패"
            else:
                continue

print("결과:", game("가위"))