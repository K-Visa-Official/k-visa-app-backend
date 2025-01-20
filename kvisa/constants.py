from enum import Enum


class VisaEnum(str, Enum):
    B1_C4 = "B1_C4"
    D2_D4 = "D2_D4"
    D7_D9 = "D7_D9"
    D10 = "D10"
    E1_E7 = "E1_E7"
    E8_E9 = "E8_E9"
    F1_F3 = "F1_F3"
    F2 = "F2"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    H2 = "H2"
    G1 = "G1"
    ETC = "ETC"


class LanguageEnum(str, Enum):
    KR = "KR"
    EN = "EN"
    CN = "CN"
    VN = "VN"


class PostTypeEnum(str, Enum):
    ROADMAP = "ROADMAP"
    BENEFIT = "BENEFIT"
    ADMIN = "ADMIN"
    CHATBOT = "CHATBOT"
    AD = "AD"
    NEWS = "NEWS"


VISA_CHOICES = [
    (VisaEnum.B1_C4.value, "여행비자 (B-1 ~ C-4)"),
    (VisaEnum.D2_D4.value, "유학생 (D-2 ~ D-4)"),
    (VisaEnum.D7_D9.value, "사업비자 (D-7 ~ D-9)"),
    (VisaEnum.D10.value, "회사구인 (D-10)"),
    (VisaEnum.E1_E7.value, "취업비자 (E-1 ~ E-7)"),
    (VisaEnum.E8_E9.value, "비전문취업 (E-8 ~ E-9)"),
    (VisaEnum.F1_F3.value, "동반가족 (F-1, F-3)"),
    (VisaEnum.F2.value, "거주 (F-2)"),
    (VisaEnum.F4.value, "재외동포 (F-4)"),
    (VisaEnum.F5.value, "영주자격 (F-5)"),
    (VisaEnum.F6.value, "국제결혼 (F-6)"),
    (VisaEnum.H2.value, "방문취업 (H-2)"),
    (VisaEnum.G1.value, "기타 (G-1)"),
    (VisaEnum.ETC.value, "그 밖에"),
]

LANGUAGE_CHOICES = [
    (LanguageEnum.KR.value, "한국어"),
    (LanguageEnum.EN.value, "영어"),
    (LanguageEnum.CN.value, "중국어"),
    (LanguageEnum.VN.value, "베트남어"),
]

POST_TYPE_CHOICES = [
    (PostTypeEnum.ROADMAP.value, "비자 로드맵"),
    (PostTypeEnum.BENEFIT.value, "혜택정보"),
    (PostTypeEnum.ADMIN.value, "비자/행정업무"),
    (PostTypeEnum.CHATBOT.value, "비자상담 챗봇"),
    (PostTypeEnum.AD.value, "광고"),
    (PostTypeEnum.NEWS.value, "한국소식"),
]
