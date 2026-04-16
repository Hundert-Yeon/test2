#0416
import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="AI 지역분석시스템 | 영업기획팀",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap');
html,body,[class*="css"]{font-family:'Noto Sans KR',sans-serif}
[data-testid="stSidebar"]{background:#0f2d52!important}
[data-testid="stSidebar"] *{color:rgba(255,255,255,.85)!important}
[data-testid="stSidebarContent"] hr{border-color:rgba(255,255,255,.1)!important}
[data-testid="metric-container"]{background:#f0f6ff;border:1px solid #dde5f0;border-radius:10px;padding:14px 16px}
[data-testid="metric-container"] [data-testid="stMetricLabel"]{font-size:12px;color:#64748b}
[data-testid="metric-container"] [data-testid="stMetricValue"]{font-size:22px;font-weight:700;color:#0f2d52}
.cover{background:linear-gradient(135deg,#0f2d52,#1a4a8a);border-radius:14px;padding:36px 40px;margin-bottom:24px}
.cover h1{font-size:30px;font-weight:700;color:#fff;margin:0 0 8px}
.cover p{font-size:14px;color:rgba(255,255,255,.6);margin:0 0 20px}
.cover-meta{display:flex;gap:28px;flex-wrap:wrap}
.cm-lbl{font-size:10px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:.08em}
.cm-val{font-size:13px;color:rgba(255,255,255,.9);font-weight:500;margin-top:2px}
.sec-num{font-size:11px;font-weight:700;color:#2e7dd4;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px}
.sec-title{font-size:22px;font-weight:700;color:#0f2d52;margin:0 0 4px}
.sec-line{width:36px;height:3px;background:#2e7dd4;border-radius:2px;margin-bottom:20px}
.card{background:#fff;border:1px solid #dde5f0;border-radius:12px;padding:18px;margin-bottom:10px}
.card-blue{border-left:4px solid #2e7dd4;background:#f4f8fe}
.card-green{border-left:4px solid #1b6e3a;background:#f0faf5}
.card-amber{border-left:4px solid #c47a00;background:#fffbf0}
.card-red{border-left:4px solid #9b1c1c;background:#fff5f5}
.tag{display:inline-block;font-size:11px;font-weight:500;padding:3px 9px;border-radius:20px;margin:2px}
.t-blue{background:#e8f2fd;color:#1a56a0}
.t-green{background:#e6f4ec;color:#1b6e3a}
.t-amber{background:#fff4e0;color:#7c4a00}
.t-red{background:#fdecea;color:#9b1c1c}
.rank-row{display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0f4f8}
.rank-row:last-child{border:none}
.rk{font-size:11px;font-weight:700;color:#cbd5e1;width:16px;text-align:center}
.rn{font-size:13px;color:#1a2332;flex:1}
.rb{font-size:10px;padding:2px 6px;border-radius:20px;font-weight:600}
.rb-hot{background:#fff4e0;color:#c45900}
.rb-new{background:#fdecea;color:#9b1c1c}
.rb-up{background:#e6f4ec;color:#1b6e3a}
.rb-ss{background:#e8f2fd;color:#1a56a0}
.hl{background:#e8f2fd;border-left:4px solid #2e7dd4;border-radius:0 8px 8px 0;padding:12px 16px;font-size:13px;color:#1a56a0;margin:16px 0;font-style:italic}
.flow{display:flex;margin:16px 0}
.fs{flex:1;padding:16px 12px;border:1px solid #dde5f0}
.fs:first-child{border-radius:10px 0 0 10px;background:#f0f7ff}
.fs:nth-child(3){background:#f0faf5;border-left:none}
.fs:nth-child(5){background:#fffbf0;border-left:none}
.fs:last-child{border-radius:0 10px 10px 0;background:#f5f0ff;border-left:none}
.fs-tag{font-size:10px;font-weight:700;color:#2e7dd4;letter-spacing:.08em;text-transform:uppercase;margin-bottom:5px}
.fs-title{font-size:14px;font-weight:700;color:#0f2d52;margin-bottom:4px}
.fs-desc{font-size:11px;color:#64748b;line-height:1.5}
.fa{display:flex;align-items:center;padding:0 2px;font-size:16px;color:#2e7dd4}
.kpi-tbl{width:100%;border-collapse:collapse;border:1px solid #dde5f0;border-radius:10px;overflow:hidden}
.kpi-tbl th{background:#0f2d52;color:#fff;font-size:12px;font-weight:600;padding:11px 13px;text-align:left}
.kpi-tbl td{padding:10px 13px;font-size:13px;border-bottom:1px solid #f0f4f8}
.kpi-tbl tr:nth-child(even) td{background:#f7f9fc}
.kpi-tbl tr:last-child td{border-bottom:none}
.kpi-num{font-weight:700;color:#1b6e3a}
.kpi-lbl{font-weight:600;color:#0f2d52}
.risk-num{font-size:36px;font-weight:700;color:#e2e8f0;line-height:1;margin-bottom:8px}
.risk-title{font-size:14px;font-weight:700;color:#0f2d52;margin-bottom:6px}
.risk-tag{font-size:11px;padding:3px 8px;border-radius:4px;background:#fdecea;color:#9b1c1c;display:inline-block;margin-bottom:8px}
.risk-desc{font-size:12px;color:#64748b;line-height:1.6}
.db-bar{background:#0f2d52;border-radius:10px 10px 0 0;padding:11px 18px;display:flex;justify-content:space-between;align-items:center}
.db-bar-title{font-size:14px;font-weight:600;color:#fff}
.db-bar-upd{font-size:11px;color:rgba(255,255,255,.4);background:rgba(255,255,255,.07);padding:3px 10px;border-radius:20px}
.bc{font-size:12px;color:#94a3b8;margin-bottom:8px}
.bc-link{color:#2e7dd4;font-weight:500}
.bc-cur{color:#0f2d52;font-weight:600}
.bc-sep{color:#dde5f0;margin:0 3px}
.lv-bar{display:flex;gap:6px;align-items:center;margin-bottom:12px;flex-wrap:wrap}
.lv{font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px}
.lv-active{background:#e8f2fd;color:#1a56a0}
.lv-done{background:#e6f4ec;color:#1b6e3a}
.lv-next{background:#f0f0f4;color:#aaa}
.lv-sep{color:#dde5f0;font-size:12px}
.insight-row{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px solid #f0f4f8}
.insight-row:last-child{border:none}
.i-icon{width:26px;height:26px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;flex-shrink:0}
.ic-blue{background:#e8f2fd;color:#1a56a0}
.ic-green{background:#e6f4ec;color:#1b6e3a}
.ic-amber{background:#fff4e0;color:#c45900}
.ic-red{background:#fdecea;color:#9b1c1c}
.i-head{font-size:13px;font-weight:600;color:#0f2d52;margin-bottom:2px}
.i-desc{font-size:12px;color:#64748b;line-height:1.5}
</style>
""", unsafe_allow_html=True)


# ── 데이터 ────────────────────────────────────────────────────────────────────
@st.cache_data
def get_db():
    return {
        "인천": {
            "pop":"299만","grdp":"89.2조","retail":112.4,"spend":"198만원","popT":"+0.8%","retailT":"+2.1%",
            "tags":[("크루즈 관광객","t-blue"),("인천공항 면세","t-blue"),("송도 팝업","t-green"),("외국인 소비↑","t-amber"),("청라 개발호재","t-amber")],
            "food":[("송도 오마카세 급부상","rb-hot"),("차이나타운 재방문↑","rb-up"),("부평 로컬카페 확산","rb-up"),("연수구 브런치 맛집↑","rb-ss")],
            "trend":[("인천 크루즈 일정","rb-hot"),("송도 신규 맛집","rb-up"),("인천 팝업스토어","rb-new")],
            "districts":{
                "연수구":{
                    "pop":"36.2만","popT":"+1.4%","retail":118.0,"spend":"212만원","retailT":"+2.8%","grdp":"18.4%",
                    "tags":[("송도 팝업","t-blue"),("국제도시 개발","t-green"),("글로벌캠퍼스","t-blue"),("고급주거 수요","t-amber")],
                    "food":[("오마카세 급부상","rb-hot"),("센트럴파크 카페↑","rb-up"),("글로벌 브런치","rb-new"),("CGV 주변 맛집","rb-ss")],
                    "trend":[("송도동 맛집","rb-hot"),("연수구 아파트","rb-up"),("국제병원","rb-ss")],
                    "dongs":[
                        {"n":"송도1동","pop":"2.8만","hot":True,"rise":False,"badge":"검색 1위"},
                        {"n":"송도2동","pop":"2.6만","hot":True,"rise":False,"badge":"소비 급등"},
                        {"n":"송도3동","pop":"2.1만","hot":False,"rise":True,"badge":"개발 활성"},
                        {"n":"연수1동","pop":"2.4만","hot":False,"rise":False,"badge":None},
                        {"n":"연수2동","pop":"2.2만","hot":False,"rise":False,"badge":None},
                        {"n":"연수3동","pop":"1.9만","hot":False,"rise":False,"badge":None},
                        {"n":"청학동","pop":"1.8만","hot":False,"rise":True,"badge":"재개발↑"},
                        {"n":"선학동","pop":"1.7만","hot":False,"rise":False,"badge":None},
                        {"n":"옥련1동","pop":"2.0만","hot":False,"rise":False,"badge":None},
                        {"n":"옥련2동","pop":"1.6만","hot":False,"rise":False,"badge":None},
                        {"n":"동춘1동","pop":"2.3만","hot":False,"rise":True,"badge":"소비↑"},
                        {"n":"동춘2동","pop":"2.1만","hot":False,"rise":False,"badge":None},
                        {"n":"동춘3동","pop":"1.9만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail":{
                        "송도1동":{
                            "pop":"2.8만","popT":"+2.3%","spend":"241만원","retail":124.8,"foreign":"6.4%",
                            "age":[18,14,34,22,12],"ageLbl":["10대이하","20대","30대","40대","50대+"],
                            "tags":[("국제업무지구","t-blue"),("외국인 거주↑","t-blue"),("오마카세 급부상","t-green"),("센트럴파크 인근","t-green"),("프리미엄 소비","t-amber")],
                            "trend":[("송도1동 오마카세","rb-hot"),("센트럴파크 카페","rb-up"),("송도 파인다이닝","rb-new"),("외국인 맛집","rb-up"),("루프탑 레스토랑","rb-new")],
                            "food":[("오마카세·파인다이닝","rb-hot"),("스페셜티 커피 카페","rb-up"),("글로벌 브런치","rb-new"),("와인바·비스트로","rb-up"),("프리미엄 베이커리","rb-ss")],
                            "insights":[
                                ("ic-blue","↑","프리미엄 F&B 수요 급증","외국인 거주자 증가(+0.9%p)와 국제업무지구 직장인 유입으로 오마카세·파인다이닝 검색 전월 대비 38% 급등."),
                                ("ic-green","+","30대 핵심 소비층 집중","평균 연령 36.2세로 연수구 내 최연소 동. 30대 비중 34%로 트렌디한 라이프스타일 MD 구성 우위."),
                                ("ic-amber","!","센트럴파크 집객 효과 활용","센트럴파크 주변 카페·브런치 검색 지속 상위권. 주말 10~14시 팝업 이벤트 연계 권장."),
                                ("ic-red","↓","가성비보다 프리미엄 적합","20대 비중 14%로 낮음. 품질·경험 중심 프리미엄 포지셔닝이 이 상권에 더 적합."),
                            ],
                        },
                        "송도2동":{
                            "pop":"2.6만","popT":"+1.9%","spend":"228만원","retail":121.3,"foreign":"4.8%",
                            "age":[16,15,30,26,13],"ageLbl":["10대이하","20대","30대","40대","50대+"],
                            "tags":[("주거 밀집","t-blue"),("소비 급증","t-amber"),("신규 상권 형성","t-green")],
                            "trend":[("송도2동 카페","rb-hot"),("송도2동 맛집","rb-up"),("신규 상가","rb-up")],
                            "food":[("카페형 베이커리↑","rb-hot"),("가족 레스토랑","rb-up"),("편의식 전문점","rb-ss")],
                            "insights":[
                                ("ic-blue","↑","소비 급증 중인 신흥 상권","신규 입주세대 증가로 소비지출 전년 대비 5.2% 급증. 생활밀착형 상권 육성 시점."),
                                ("ic-green","+","40대 가족 소비층 강세","40대 비중 26%로 가족 외식·교육 관련 소비 강세. 키즈 친화 MD 검토 가능."),
                            ],
                        },
                    },
                },
                "남동구":{
                    "pop":"52.1만","popT":"+0.3%","retail":110.0,"spend":"185만원","retailT":"+0.8%","grdp":"12.1%",
                    "tags":[("구월상권","t-blue"),("소래포구 관광","t-green"),("남동공단","t-amber")],
                    "food":[("소래포구 해산물↑","rb-hot"),("구월동 음식거리","rb-up"),("간석오거리 카페","rb-ss")],
                    "trend":[("구월동 쇼핑","rb-hot"),("남동공단 채용","rb-ss"),("소래포구 주차","rb-up")],
                    "dongs":[
                        {"n":"구월1동","pop":"4.1만","hot":True,"rise":False,"badge":"검색 1위"},
                        {"n":"구월2동","pop":"3.8만","hot":False,"rise":True,"badge":"소비↑"},
                        {"n":"구월3동","pop":"3.2만","hot":False,"rise":False,"badge":None},
                        {"n":"간석1동","pop":"2.9만","hot":False,"rise":False,"badge":None},
                        {"n":"만수1동","pop":"2.4만","hot":False,"rise":True,"badge":"재개발"},
                        {"n":"서창동","pop":"3.1만","hot":False,"rise":False,"badge":None},
                    ], "dong_detail":{},
                },
                "부평구":{
                    "pop":"50.8만","popT":"-0.5%","retail":106.0,"spend":"176만원","retailT":"-0.3%","grdp":"10.8%",
                    "tags":[("부평역 상권","t-blue"),("문화특구","t-green"),("재개발 이슈","t-amber")],
                    "food":[("부평 먹자골목↑","rb-hot"),("삼산동 카페거리","rb-up"),("갈산동 브런치","rb-ss")],
                    "trend":[("부평역 맛집","rb-hot"),("부평 재개발","rb-up"),("문화특구 행사","rb-ss")],
                    "dongs":[
                        {"n":"부평1동","pop":"4.2만","hot":True,"rise":False,"badge":"검색 상위"},
                        {"n":"부평2동","pop":"3.9만","hot":False,"rise":False,"badge":None},
                        {"n":"부평3동","pop":"3.4만","hot":False,"rise":True,"badge":"소비↑"},
                        {"n":"십정1동","pop":"2.8만","hot":False,"rise":False,"badge":None},
                        {"n":"갈산1동","pop":"2.4만","hot":False,"rise":True,"badge":"카페↑"},
                    ], "dong_detail":{},
                },
            },
        },
        "서울":{
            "pop":"941만","grdp":"480조","retail":118.7,"spend":"234만원","popT":"-0.4%","retailT":"+1.5%",
            "tags":[("성수 팝업 열풍","t-blue"),("강남 명품↑","t-amber"),("2030 소비회복","t-green"),("외국인 관광객","t-blue")],
            "food":[("성수 빈티지샵 핫플","rb-hot"),("한남동 카페거리↑","rb-up"),("강남 오마카세 대기↑","rb-hot")],
            "trend":[("성수동 팝업스토어","rb-hot"),("강남 명품 세일","rb-up"),("한남동 맛집","rb-up")],
            "districts":{
                "강남구":{
                    "pop":"55.3만","popT":"+0.2%","retail":132.0,"spend":"312만원","retailT":"+2.1%","grdp":"9.8%",
                    "tags":[("명품 소비↑","t-amber"),("청담 플래그십","t-blue"),("압구정 재개발","t-amber")],
                    "food":[("오마카세 대기↑","rb-hot"),("청담 파인다이닝","rb-up"),("압구정 카페거리","rb-ss")],
                    "trend":[("강남 명품 세일","rb-hot"),("압구정 재개발","rb-up"),("청담 레스토랑","rb-ss")],
                    "dongs":[
                        {"n":"압구정동","pop":"2.1만","hot":True,"rise":False,"badge":"명품 1위"},
                        {"n":"신사동","pop":"2.8만","hot":True,"rise":False,"badge":"팝업↑"},
                        {"n":"청담동","pop":"1.9만","hot":False,"rise":True,"badge":"플래그십"},
                        {"n":"역삼1동","pop":"4.2만","hot":False,"rise":False,"badge":None},
                        {"n":"삼성1동","pop":"3.1만","hot":False,"rise":True,"badge":"소비↑"},
                    ], "dong_detail":{},
                },
                "성동구":{
                    "pop":"30.1만","popT":"+1.2%","retail":124.0,"spend":"245만원","retailT":"+3.4%","grdp":"4.2%",
                    "tags":[("성수 팝업 성지","t-blue"),("MZ 핫플","t-green"),("젠트리피케이션","t-amber")],
                    "food":[("성수 팝업 줄서기","rb-hot"),("뚝도시장 카페↑","rb-up"),("왕십리 먹자골목","rb-ss")],
                    "trend":[("성수동 팝업","rb-hot"),("성수 카페","rb-up"),("뚝섬역 맛집","rb-up")],
                    "dongs":[
                        {"n":"성수1가1동","pop":"1.8만","hot":True,"rise":False,"badge":"팝업 1위"},
                        {"n":"성수1가2동","pop":"1.6만","hot":True,"rise":False,"badge":"급등"},
                        {"n":"성수2가1동","pop":"2.1만","hot":False,"rise":True,"badge":"상권↑"},
                        {"n":"왕십리2동","pop":"2.8만","hot":False,"rise":False,"badge":None},
                    ], "dong_detail":{},
                },
                "마포구":{
                    "pop":"37.8만","popT":"-0.2%","retail":119.0,"spend":"228만원","retailT":"+1.2%","grdp":"5.1%",
                    "tags":[("홍대 상권","t-blue"),("망원 로컬","t-green"),("연남 카페거리","t-green")],
                    "food":[("망원동 브런치↑","rb-hot"),("연남동 카페거리","rb-up"),("홍대 클럽거리","rb-ss")],
                    "trend":[("홍대 맛집","rb-hot"),("망원동 카페","rb-up"),("연남동 팝업","rb-new")],
                    "dongs":[
                        {"n":"서교동","pop":"2.6만","hot":True,"rise":False,"badge":"홍대 핫플"},
                        {"n":"연남동","pop":"2.2만","hot":True,"rise":False,"badge":"급상승"},
                        {"n":"망원1동","pop":"2.4만","hot":False,"rise":True,"badge":"브런치↑"},
                        {"n":"합정동","pop":"2.1만","hot":False,"rise":False,"badge":None},
                    ], "dong_detail":{},
                },
            },
        },
        "부산":{
            "pop":"332만","grdp":"98.5조","retail":108.3,"spend":"186만원","popT":"-0.6%","retailT":"-0.8%",
            "tags":[("해운대 관광시즌","t-blue"),("북항 재개발","t-amber"),("서면 상권 회복","t-green")],
            "food":[("해운대 씨푸드↑","rb-hot"),("서면 로컬카페↑","rb-up"),("광안리 루프탑 바","rb-new")],
            "trend":[("부산 해수욕장","rb-hot"),("해운대 맛집","rb-up"),("북항 개발","rb-ss")],
            "districts":{
                "해운대구":{
                    "pop":"41.8만","popT":"-0.3%","retail":114.0,"spend":"198만원","retailT":"+0.8%","grdp":"8.4%",
                    "tags":[("해변 관광","t-blue"),("마린시티 부촌","t-amber"),("센텀 쇼핑","t-blue")],
                    "food":[("해수욕장 씨푸드↑","rb-hot"),("센텀 레스토랑","rb-up"),("마린시티 와인바","rb-new")],
                    "trend":[("해운대 해수욕장","rb-hot"),("센텀시티 쇼핑","rb-up"),("마린시티 맛집","rb-ss")],
                    "dongs":[
                        {"n":"우1동","pop":"3.8만","hot":True,"rise":False,"badge":"관광 1위"},
                        {"n":"중1동","pop":"3.2만","hot":True,"rise":False,"badge":"소비↑"},
                        {"n":"재송1동","pop":"4.1만","hot":False,"rise":True,"badge":"개발↑"},
                        {"n":"반여1동","pop":"2.9만","hot":False,"rise":False,"badge":None},
                        {"n":"송정동","pop":"1.8만","hot":False,"rise":True,"badge":"서핑↑"},
                    ], "dong_detail":{},
                },
                "부산진구":{
                    "pop":"37.1만","popT":"-0.7%","retail":109.0,"spend":"182만원","retailT":"-0.2%","grdp":"6.2%",
                    "tags":[("서면 중심상권","t-blue"),("전포카페거리","t-green"),("부전시장","t-amber")],
                    "food":[("서면 먹자골목↑","rb-hot"),("전포카페거리 MZ↑","rb-hot"),("부전시장 먹거리","rb-ss")],
                    "trend":[("서면 맛집","rb-hot"),("전포 카페","rb-up"),("부산진 쇼핑","rb-ss")],
                    "dongs":[
                        {"n":"부전1동","pop":"3.6만","hot":True,"rise":False,"badge":"검색 1위"},
                        {"n":"전포1동","pop":"2.4만","hot":True,"rise":False,"badge":"MZ 급등"},
                        {"n":"전포2동","pop":"2.2만","hot":False,"rise":True,"badge":"카페↑"},
                        {"n":"당감1동","pop":"2.8만","hot":False,"rise":False,"badge":None},
                    ], "dong_detail":{},
                },
            },
        },
        "대구":{
            "pop":"236만","grdp":"56.2조","retail":104.1,"spend":"172만원","popT":"-0.9%","retailT":"+0.5%",
            "tags":[("동성로 상권 부활","t-blue"),("섬유산업 침체","t-red"),("청년 창업↑","t-green")],
            "food":[("동성로 MZ 맛집↑","rb-hot"),("수성못 카페투어↑","rb-up"),("서문시장 먹거리","rb-ss")],
            "trend":[("동성로 팝업","rb-hot"),("수성못 카페","rb-up"),("청년 창업","rb-new")],
            "districts":{
                "수성구":{
                    "pop":"43.2만","popT":"-0.4%","retail":112.0,"spend":"224만원","retailT":"+1.4%","grdp":"7.8%",
                    "tags":[("수성못 관광","t-green"),("학군 수요↑","t-blue"),("범어 부촌","t-amber")],
                    "food":[("수성못 카페투어↑","rb-hot"),("범어동 파인다이닝","rb-up"),("황금동 음식거리","rb-ss")],
                    "trend":[("수성못 카페","rb-hot"),("범어동 맛집","rb-up"),("수성구 학원","rb-ss")],
                    "dongs":[
                        {"n":"수성1가동","pop":"2.4만","hot":True,"rise":False,"badge":"카페 1위"},
                        {"n":"황금1동","pop":"3.8만","hot":False,"rise":True,"badge":"소비↑"},
                        {"n":"범어1동","pop":"3.2만","hot":True,"rise":False,"badge":"파인다이닝"},
                        {"n":"만촌1동","pop":"3.6만","hot":False,"rise":False,"badge":None},
                    ], "dong_detail":{},
                },
                "중구":{
                    "pop":"7.8만","popT":"-1.2%","retail":116.0,"spend":"208만원","retailT":"+0.9%","grdp":"3.1%",
                    "tags":[("동성로 핵심","t-blue"),("근대골목 관광","t-green"),("이월드 인근","t-blue")],
                    "food":[("동성로 팝업↑","rb-hot"),("서문시장 야시장","rb-up"),("근대골목 카페","rb-ss")],
                    "trend":[("동성로 맛집","rb-hot"),("서문시장 야시장","rb-up"),("근대골목 투어","rb-ss")],
                    "dongs":[
                        {"n":"성내1동","pop":"1.2만","hot":True,"rise":False,"badge":"팝업 1위"},
                        {"n":"남산1동","pop":"1.4만","hot":False,"rise":True,"badge":"트렌드↑"},
                        {"n":"대봉1동","pop":"1.6만","hot":False,"rise":False,"badge":None},
                    ], "dong_detail":{},
                },
            },
        },
        "광주":{
            "pop":"143만","grdp":"38.7조","retail":106.8,"spend":"168만원","popT":"-0.3%","retailT":"+1.2%",
            "tags":[("비엔날레 시즌","t-blue"),("친환경 소비↑","t-green"),("문화예술 행사","t-amber")],
            "food":[("양림동 역사카페↑","rb-hot"),("충장로 로컬맛집","rb-up"),("상무지구 브런치↑","rb-up")],
            "trend":[("광주 비엔날레","rb-hot"),("양림동 카페거리","rb-up"),("상무지구 맛집","rb-up")],
            "districts":{
                "서구":{
                    "pop":"28.4만","popT":"-0.5%","retail":108.0,"spend":"172만원","retailT":"+0.6%","grdp":"6.2%",
                    "tags":[("상무지구 중심","t-blue"),("치평동 상권","t-green"),("금호지구","t-blue")],
                    "food":[("상무지구 브런치↑","rb-hot"),("치평동 카페거리","rb-up"),("금호동 맛집","rb-ss")],
                    "trend":[("상무지구 맛집","rb-hot"),("치평 카페","rb-up"),("서구 아파트","rb-ss")],
                    "dongs":[
                        {"n":"치평동","pop":"4.2만","hot":True,"rise":False,"badge":"브런치 1위"},
                        {"n":"상무1동","pop":"3.8만","hot":False,"rise":True,"badge":"소비↑"},
                        {"n":"화정1동","pop":"3.4만","hot":False,"rise":False,"badge":None},
                        {"n":"풍암동","pop":"3.6만","hot":False,"rise":False,"badge":None},
                    ], "dong_detail":{},
                },
                "동구":{
                    "pop":"9.5만","popT":"-1.1%","retail":112.0,"spend":"188만원","retailT":"+1.8%","grdp":"2.8%",
                    "tags":[("충장로 문화거리","t-blue"),("양림동 역사마을","t-green"),("5·18 성지","t-blue")],
                    "food":[("양림동 카페↑","rb-hot"),("충장로 맛집","rb-up"),("동명동 감성카페","rb-new")],
                    "trend":[("양림동 카페","rb-hot"),("충장로 쇼핑","rb-up"),("동구 문화행사","rb-ss")],
                    "dongs":[
                        {"n":"양림동","pop":"0.9만","hot":True,"rise":False,"badge":"역사카페 1위"},
                        {"n":"충장1동","pop":"1.8만","hot":True,"rise":False,"badge":"검색↑"},
                        {"n":"계림1동","pop":"1.4만","hot":False,"rise":True,"badge":"상권↑"},
                    ], "dong_detail":{},
                },
            },
        },
    }

DB = get_db()


# ── 헬퍼 ──────────────────────────────────────────────────────────────────────
def tags_html(lst):
    h = '<div style="display:flex;flex-wrap:wrap;gap:4px;margin:8px 0">'
    for t, c in lst:
        h += f'<span class="tag {c}">{t}</span>'
    h += '</div>'
    st.markdown(h, unsafe_allow_html=True)

def rank_list(items, title):
    lbl_map = {"rb-hot":"급등","rb-new":"신규","rb-up":"상승","rb-ss":"유지"}
    rows = "".join(
        f'<div class="rank-row"><span class="rk">·</span><span class="rn">{t}</span>'
        f'<span class="rb {c}">{lbl_map.get(c,"")}</span></div>'
        for t, c in items
    )
    st.markdown(
        f'<div class="card" style="padding:12px 14px">'
        f'<div style="font-size:11px;font-weight:600;color:#64748b;margin-bottom:6px">{title}</div>'
        f'{rows}</div>',
        unsafe_allow_html=True
    )

def metrics4(d):
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("인구수", d["pop"], d["popT"])
    with c2: st.metric("소매판매지수", str(d["retail"]), d.get("retailT","—"))
    with c3: st.metric("1인당 소비지출", d["spend"])
    with c4: st.metric("GRDP / 기여도", d.get("grdp","—"))

def retail_chart(base, key):
    rng = random.Random(int(base * 100))
    months = ["10월","11월","12월","1월","2월","3월","4월"]
    vals = [round(base - 4 + i * 0.9 + (rng.random() - 0.5) * 0.8, 1) for i in range(7)]
    df = pd.DataFrame({"월": months, "소매판매지수": vals})
    st.line_chart(df.set_index("월"), height=160, use_container_width=True)

def age_chart(vals, lbls):
    df = pd.DataFrame({"연령대": lbls, "비율(%)": vals})
    st.bar_chart(df.set_index("연령대"), height=150, use_container_width=True)

def gu_retail_chart(sido_name):
    gd = DB[sido_name]["districts"]
    names = list(gd.keys())
    vals = [gd[g]["retail"] for g in names]
    df = pd.DataFrame({"구": names, "소매판매지수": vals})
    st.bar_chart(df.set_index("구"), height=180, use_container_width=True)

def sec_header(num, title):
    st.markdown(
        f'<div class="sec-num">{num}</div>'
        f'<div class="sec-title">{title}</div>'
        f'<div class="sec-line"></div>',
        unsafe_allow_html=True
    )


# ── 사이드바 ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        '<div style="padding:14px 0 10px">'
        '<div style="font-size:17px;font-weight:700;color:#fff">📊 AI 지역분석</div>'
        '<div style="font-size:11px;color:rgba(255,255,255,.4);margin-top:3px">영업기획팀 · 2026.04</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown("---")
    page = st.radio("메뉴", [
        "📋 기획서 전문",
        "01 요약",
        "02 현황 및 문제 정의",
        "03 AI 솔루션 설계",
        "04 기대 효과 / KPI",
        "05 리스크 및 대응",
        "06 실행 계획",
        "🗺 대시보드 라이브 데모",
    ], label_visibility="collapsed")
    st.markdown("---")
    st.markdown(
        '<div style="font-size:11px;color:rgba(255,255,255,.3)">수치는 추정치이며<br>도입 전 검증이 필요합니다</div>',
        unsafe_allow_html=True
    )


# ════════════════════════════════════════════════════════════════════════════
# 기획서 전문
# ════════════════════════════════════════════════════════════════════════════
if "기획서 전문" in page:
    st.markdown("""
    <div class="cover">
      <h1>AI 지역 거시환경 자동 분석 시스템 구축</h1>
      <p>Regional Intelligence Dashboard — 영업기획팀 효율화 프로젝트</p>
      <div class="cover-meta">
        <div><div class="cm-lbl">제안팀</div><div class="cm-val">영업기획팀</div></div>
        <div><div class="cm-lbl">대상</div><div class="cm-val">9명 전체 구성원</div></div>
        <div><div class="cm-lbl">기간</div><div class="cm-val">총 8주 (4단계)</div></div>
        <div><div class="cm-lbl">작성일</div><div class="cm-val">2026. 04</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.info("좌측 사이드바에서 각 섹션(01~06) 또는 대시보드를 선택하세요.")
    c1, c2, c3 = st.columns(3)
    items = [
        ("card-blue","01 요약","문제 / 솔루션 / 기대효과"),
        ("card-red","04 KPI","5가지 정량 목표"),
        ("card-blue","02 현황","문제 정의 및 수치 근거"),
        ("card-red","05 리스크","3가지 리스크 및 대응"),
        ("card-green","03 솔루션","AI 설계 및 역할 분담"),
        ("card-amber","06 실행계획","8주 마일스톤"),
    ]
    for col, (cls, title, sub) in zip([c1,c2,c3,c1,c2,c3], items):
        with col:
            st.markdown(f'<div class="card {cls}"><b>{title}</b><br><small style="color:#64748b">{sub}</small></div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# 01 요약
# ════════════════════════════════════════════════════════════════════════════
if "01" in page:
    sec_header("01", "요약")
    c1, c2, c3 = st.columns(3)
    cards = [
        ("card-red","문제","36h","지역별 거시경제·트렌드 데이터를 <b>1인당 주 4시간 이상</b> 수작업 수집·분석. 팀 전체 주 36시간 낭비로 전략 기획 본연의 업무 투입 구조적 제한.","#9b1c1c"),
        ("card-blue","솔루션","3단계","AI가 통계청·검색트렌드·뉴스를 실시간 수집·분석. <b>시·도→행정구→행정동</b> 3단계 드릴다운 대시보드로 클릭 한 번에 인사이트 제공.","#1a56a0"),
        ("card-green","기대효과","↓90%","분석 소요시간 <b>90% 단축</b> (4시간→24분), 데이터 정확도 향상, MD 의사결정 속도 2배 이상 향상.","#1b6e3a"),
    ]
    for col, (cls, lbl, num, txt, color) in zip([c1,c2,c3], cards):
        with col:
            st.markdown(
                f'<div class="card {cls}">'
                f'<div style="font-size:10px;font-weight:700;color:{color};text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px">{lbl}</div>'
                f'<div style="font-size:36px;font-weight:700;color:{color};line-height:1;margin-bottom:10px">{num}</div>'
                f'<div style="font-size:13px;color:#1a2332;line-height:1.7">{txt}</div>'
                f'</div>',
                unsafe_allow_html=True
            )


# ════════════════════════════════════════════════════════════════════════════
# 02 현황
# ════════════════════════════════════════════════════════════════════════════
if "02" in page:
    sec_header("02", "현황 및 문제 정의")
    st.markdown("""
현재 영업기획팀 9명은 매주 지역별 거시경제 분석 자료를 통계청 KOSIS, 네이버·구글 트렌드, 뉴스 검색 등 다수의 사이트에 개별 접속하여 데이터를 직접 수집하고 있다.
이 과정에서 1인당 최소 4시간, 팀 전체로는 **주 36시간 이상**의 시간이 단순 수집 작업에 소비되어 전략 기획 본연의 업무 투입이 구조적으로 제한된다.

데이터 수집 방식의 파편화로 인해 담당자별 분석 기준과 수집 범위가 달라 동일 지역에 대한 해석이 팀원 간 불일치하는 사례가 발생한다.
또한 트렌드·이슈 데이터는 실시간성이 중요함에도 수작업 특성상 **주 1~2회 업데이트**가 한계로, 시의성 있는 의사결정에 걸림돌이 된다.

MD 전략 수립에 필요한 정보는 거시지표를 넘어 지역별 실시간 소비 이슈, 검색 트렌드 키워드, 맛집·라이프스타일 변화까지 포함한다.
이를 개인이 모두 탐색하는 현재 구조는 인력 효율 측면의 명백한 비효율이며 AI 자동화가 시급하다.
    """)
    st.markdown('<div class="hl">※ 수치 근거: 팀원 인터뷰 기반 평균 소요시간 추정 (1인 4시간 × 9명). 도입 전 2주간 실제 측정으로 검증 권장.</div>', unsafe_allow_html=True)
    st.markdown("#### 주간 소요시간 비교 (수작업 vs AI 도입 후)")
    df_time = pd.DataFrame({
        "항목": ["데이터 수집","분석·정리","보고서 작성"],
        "수작업(현재)": [18, 12, 6],
        "AI 도입 후":   [0.5, 1.5, 1.6],
    }).set_index("항목")
    st.bar_chart(df_time, height=260, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# 03 솔루션
# ════════════════════════════════════════════════════════════════════════════
if "03" in page:
    sec_header("03", "AI 솔루션 설계")
    st.markdown("""
    <div class="flow">
      <div class="fs"><div class="fs-tag">Problem</div><div class="fs-title">분산 데이터</div><div class="fs-desc">통계청, 검색포털, 뉴스 등 소스별 수작업 수집</div></div>
      <div class="fa">→</div>
      <div class="fs"><div class="fs-tag">Data</div><div class="fs-title">자동 수집</div><div class="fs-desc">API·크롤링으로 지역별 데이터 실시간 통합</div></div>
      <div class="fa">→</div>
      <div class="fs"><div class="fs-tag">Insight</div><div class="fs-title">AI 분석</div><div class="fs-desc">LLM이 트렌드 요약·이슈 추출·소비지표 해석</div></div>
      <div class="fa">→</div>
      <div class="fs"><div class="fs-tag">Action</div><div class="fs-title">MD 의사결정</div><div class="fs-desc">대시보드 클릭 → 인사이트 즉시 활용</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### AI 활용 방식 — 3개 레이어")
    a1, a2, a3 = st.columns(3)
    layers = [
        ("card-blue","🔗 데이터 수집 레이어","통계청 KOSIS Open API, 네이버·구글 트렌드 API, 뉴스 RSS 자동 호출. 매일 새벽 스케줄러로 전국 지역별 갱신."),
        ("card-green","🤖 AI 분석 레이어","LLM(Claude/GPT)이 핵심 이슈 키워드·소비 트렌드·맛집 버즈 순위를 자동 추출·요약."),
        ("card-amber","📊 시각화 레이어","시·도→행정구→행정동 3단계 드릴다운. 클릭 시 인구·소비 지표 차트와 이슈 태그 즉시 렌더링."),
    ]
    for col, (cls, title, desc) in zip([a1,a2,a3], layers):
        with col:
            st.markdown(f'<div class="card {cls}"><b>{title}</b><br><br><span style="font-size:13px;color:#4a5568;line-height:1.7">{desc}</span></div>', unsafe_allow_html=True)

    st.markdown("#### 사람 vs AI 역할 분담")
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("""
        <div class="card card-green">
        <b style="color:#1b6e3a">🤖 AI 담당 역할</b>
        <ul style="font-size:13px;color:#4a5568;line-height:2.1;margin-top:10px;padding-left:16px">
          <li>공공 API·뉴스 데이터 자동 수집 및 정제</li>
          <li>지역별 이슈 키워드 추출 및 요약</li>
          <li>소비 트렌드 변화 감지 및 알림</li>
          <li>지표 간 상관관계 1차 해석</li>
          <li>차트·표·태그 자동 생성</li>
        </ul></div>""", unsafe_allow_html=True)
    with r2:
        st.markdown("""
        <div class="card card-amber">
        <b style="color:#7c4a00">👤 사람 담당 역할</b>
        <ul style="font-size:13px;color:#4a5568;line-height:2.1;margin-top:10px;padding-left:16px">
          <li>MD 전략 방향성 및 기획 판단</li>
          <li>AI 분석 결과의 맥락적 해석</li>
          <li>이상 데이터 검증 및 보정</li>
          <li>임원 보고 자료 편집·커뮤니케이션</li>
          <li>신규 분석 어젠다 설정</li>
        </ul></div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# 04 기대효과
# ════════════════════════════════════════════════════════════════════════════
if "04" in page:
    sec_header("04", "기대 효과 — KPI 5가지")
    kpi_rows = [
        ("분석 소요시간 절감","1인 주 4시간","1인 주 24분 (↓90%)","팀원 작업일지 월 측정"),
        ("팀 전체 절감 시간","주 36시간","주 3.6시간 (32.4h 절감)","시스템 접속 로그"),
        ("데이터 업데이트 주기","주 1~2회 수작업","매일 자동 갱신","스케줄러 실행 로그"),
        ("분석 커버 지역 수","2~3개 지역/담당","전국 17개 광역시도 100%","대시보드 지역 탭 수"),
        ("MD 보고서 작성 시간","보고서당 평균 3시간","보고서당 1시간 이내 (↓67%)","착수~완료 시간 측정"),
    ]
    rows_html = "".join(
        f"<tr><td class='kpi-lbl'>{r[0]}</td><td>{r[1]}</td><td class='kpi-num'>{r[2]}</td>"
        f"<td style='font-size:12px;color:#64748b'>{r[3]}</td></tr>"
        for r in kpi_rows
    )
    st.markdown(
        f"<table class='kpi-tbl'><thead><tr><th>KPI</th><th>현재 (Before)</th><th>목표 (After)</th><th>측정 방식</th></tr></thead>"
        f"<tbody>{rows_html}</tbody></table>",
        unsafe_allow_html=True
    )
    st.markdown('<div class="hl">※ 목표 수치는 유사 사례(유통사 데이터팀 AI 도입) 기반 추정치. 도입 후 4주 시점 중간 측정으로 재조정 권장.</div>', unsafe_allow_html=True)
    st.markdown("#### KPI 목표 달성률 시각화 (현재=100 기준)")
    df_kpi = pd.DataFrame({
        "KPI": ["분석시간","팀절감시간","업데이트주기","커버지역수","보고서작성"],
        "현재": [100,100,100,100,100],
        "목표": [10,10,14,100,33],
    }).set_index("KPI")
    st.bar_chart(df_kpi, height=240, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# 05 리스크
# ════════════════════════════════════════════════════════════════════════════
if "05" in page:
    sec_header("05", "리스크 및 대응 방안")
    risks = [
        ("01","데이터 정확도·신뢰성","공공 API 오류·결측, AI 요약 오류 가능성","원본 소스 링크 동시 노출, 월 1회 샘플 검증 프로세스 수립, AI 요약에 검토 필요 플래그 기능 추가."),
        ("02","초기 구축 비용·일정","개발 인력 부재, 일정 지연, 예산 초과","무료 공공 API로 MVP 먼저 구축, 단계별 검수 계약, 8주 타임박스 내 최소 기능 우선 완성."),
        ("03","구성원 활용도 저하","새 시스템 학습 저항, 기존 습관 유지","파일럿 2명 설계 참여, 1페이지 가이드 제작, 4주 기존 방식 병행 후 전환."),
    ]
    for col, (num, title, tag, desc) in zip(st.columns(3), risks):
        with col:
            st.markdown(
                f'<div class="card"><div class="risk-num">{num}</div>'
                f'<div class="risk-title">{title}</div>'
                f'<div class="risk-tag">{tag}</div>'
                f'<div class="risk-desc">{desc}</div></div>',
                unsafe_allow_html=True
            )


# ════════════════════════════════════════════════════════════════════════════
# 06 실행계획
# ════════════════════════════════════════════════════════════════════════════
if "06" in page:
    sec_header("06", "실행 계획 — 8주 마일스톤")
    st.markdown("전체 프로젝트는 4단계 8주로 운영된다. 1~2주차 기반 설계→3~4주차 MVP 개발→5~6주차 고도화·검증→7~8주차 운영 전환 순으로 진행한다.")
    milestones = [
        ("1–2주차","기반 설계","#2e7dd4",["요구사항 정의 (팀 인터뷰)","활용 데이터 소스 확정","API 연결 가능 여부 검증","화면 와이어프레임 작성"]),
        ("3–4주차","MVP 개발","#1b6e3a",["통계청 API 자동 수집 구축","AI 키워드 추출 연동","지역 클릭 대시보드 프로토타입","2개 지역 파일럿 테스트"]),
        ("5–6주차","고도화·검증","#c47a00",["전국 17개 지역 확대","맛집·트렌드 데이터 연동","행정동 드릴다운 완성","데이터 정확도 1차 검증"]),
        ("7–8주차","운영 전환","#7c3aed",["팀 전체 사용법 교육","기존 방식 병행 후 전환","KPI 초기값 측정","개선사항 수집·반영"]),
    ]
    for col, (week, title, color, items) in zip(st.columns(4), milestones):
        with col:
            li = "".join(f"<li style='padding:4px 0;border-bottom:1px solid #f0f4f8;font-size:12px;color:#64748b'>{it}</li>" for it in items)
            st.markdown(
                f'<div class="card" style="border-top:3px solid {color}">'
                f'<div style="font-size:11px;font-weight:700;color:{color};text-transform:uppercase;letter-spacing:.06em;margin-bottom:5px">{week}</div>'
                f'<div style="font-size:14px;font-weight:700;color:#0f2d52;margin-bottom:8px">{title}</div>'
                f'<ul style="list-style:none;padding:0;margin:0">{li}</ul></div>',
                unsafe_allow_html=True
            )
    st.markdown("#### 8주 타임라인")
    df_gantt = pd.DataFrame({
        "단계": ["기반 설계","MVP 개발","고도화·검증","운영 전환"],
        "시작(주)": [1, 3, 5, 7],
        "종료(주)": [2, 4, 6, 8],
    })
    timeline_data = pd.DataFrame(
        {"주차": list(range(1, 9)),
         "기반 설계":   [1,1,0,0,0,0,0,0],
         "MVP 개발":    [0,0,1,1,0,0,0,0],
         "고도화·검증": [0,0,0,0,1,1,0,0],
         "운영 전환":   [0,0,0,0,0,0,1,1],
        }
    ).set_index("주차")
    st.bar_chart(timeline_data, height=200, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# 대시보드 라이브 데모
# ════════════════════════════════════════════════════════════════════════════
if "대시보드" in page:
    sec_header("부록", "대시보드 — 라이브 데모")

    for key in ("sido","gu","dong"):
        if key not in st.session_state:
            st.session_state[key] = None

    def set_sido(n):
        st.session_state.sido = n
        st.session_state.gu   = None
        st.session_state.dong = None

    def set_gu(n):
        st.session_state.gu   = n
        st.session_state.dong = None

    def set_dong(n):
        st.session_state.dong = n

    sido = st.session_state.sido
    gu   = st.session_state.gu
    dong = st.session_state.dong

    # 대시보드 상단바
    st.markdown(
        '<div class="db-bar">'
        '<span class="db-bar-title">🟢 지역 거시환경 AI 분석 대시보드</span>'
        '<span class="db-bar-upd">기준 2026.04 · 자동 갱신</span>'
        '</div>',
        unsafe_allow_html=True
    )

    # 브레드크럼
    bc = '<div class="bc"><span class="bc-link">전국</span>'
    if sido: bc += f'<span class="bc-sep"> › </span><span class="{"bc-cur" if not gu else "bc-link"}">{sido}</span>'
    if gu:   bc += f'<span class="bc-sep"> › </span><span class="{"bc-cur" if not dong else "bc-link"}">{gu}</span>'
    if dong: bc += f'<span class="bc-sep"> › </span><span class="bc-cur">{dong}</span>'
    bc += '</div>'
    st.markdown(bc, unsafe_allow_html=True)

    # 레벨 바
    lv1 = "lv-done" if sido else "lv-active"
    lv2 = "lv-done" if gu else ("lv-active" if sido else "lv-next")
    lv3 = "lv-active" if dong else ("lv-active" if gu else "lv-next")
    st.markdown(
        f'<div class="lv-bar">'
        f'<span class="lv {lv1}">시·도{"  ✓" if sido else ""}</span>'
        f'<span class="lv-sep">›</span>'
        f'<span class="lv {lv2}">행정구{"  ✓" if gu else ""}</span>'
        f'<span class="lv-sep">›</span>'
        f'<span class="lv {lv3}">행정동 상세</span>'
        f'</div>',
        unsafe_allow_html=True
    )

    # 검색
    sq = st.text_input("🔍 지역 검색", placeholder="연수구, 송도1동, 강남구...", label_visibility="collapsed")
    if sq:
        results = []
        for sn, sd in DB.items():
            if sq in sn: results.append(("시·도", sn, None, None))
            for gn, gd in sd["districts"].items():
                if sq in gn: results.append(("행정구", sn, gn, None))
                for dk in gd["dongs"]:
                    if sq in dk["n"]: results.append(("행정동", sn, gn, dk["n"]))
        if results:
            st.caption(f"검색 결과 {len(results)}건")
            rcols = st.columns(min(len(results), 4))
            for i, (typ, sn, gn, dn) in enumerate(results[:4]):
                with rcols[i]:
                    lbl = sn + (f" {gn}" if gn else "") + (f" {dn}" if dn else "")
                    if st.button(f"📍 {lbl}\n({typ})", key=f"sr_{i}", use_container_width=True):
                        st.session_state.sido = sn
                        if gn: st.session_state.gu = gn
                        if dn: st.session_state.dong = dn
                        st.rerun()
        else:
            st.caption("검색 결과 없음")
        st.divider()
        sido = st.session_state.sido
        gu   = st.session_state.gu
        dong = st.session_state.dong

    # ── LEVEL 1: 시·도 ──
    st.markdown('<div style="font-size:12px;font-weight:700;color:#64748b;margin-bottom:8px">시·도를 선택하세요</div>', unsafe_allow_html=True)
    sido_cols = st.columns(len(DB))
    for col, (sn, sd) in zip(sido_cols, DB.items()):
        with col:
            is_sel = sido == sn
            bg  = "#0f2d52" if is_sel else "#fff"
            bdr = "1.5px solid #1a56a0" if is_sel else "1px solid #dde5f0"
            tc  = "#fff" if is_sel else "#0f2d52"
            sub_c = "rgba(255,255,255,.6)" if is_sel else "#94a3b8"
            tr_c  = "#a5f3c0" if is_sel else ("#2E7D32" if sd["popT"].startswith("+") else "#C62828")
            st.markdown(
                f'<div style="background:{bg};border:{bdr};border-radius:8px;padding:11px 8px;text-align:center;margin-bottom:4px">'
                f'<div style="font-size:14px;font-weight:700;color:{tc}">{sn}</div>'
                f'<div style="font-size:11px;color:{sub_c};margin-top:2px">인구 {sd["pop"]}</div>'
                f'<div style="font-size:11px;color:{tr_c};margin-top:3px">{sd["popT"]}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
            btn_type = "primary" if is_sel else "secondary"
            if st.button("✓" if is_sel else "선택", key=f"sido_{sn}", use_container_width=True, type=btn_type):
                set_sido(sn); st.rerun()

    if sido:
        st.divider()
        sd = DB[sido]
        metrics4({"pop":sd["pop"],"popT":sd["popT"],"retail":sd["retail"],"retailT":sd["retailT"],"spend":sd["spend"],"grdp":sd.get("grdp","—")})
        tags_html(sd["tags"])
        fc1, fc2 = st.columns(2)
        with fc1: rank_list(sd["food"], "인기 맛집·소비 트렌드")
        with fc2: rank_list(sd["trend"], "급상승 검색어")
        st.markdown("**행정구별 소매판매지수**")
        gu_retail_chart(sido)
        st.divider()

        # ── LEVEL 2: 행정구 ──
        st.markdown('<div style="font-size:12px;font-weight:700;color:#64748b;margin-bottom:8px">행정구·군을 선택하세요</div>', unsafe_allow_html=True)
        gu_list = list(sd["districts"].keys())
        gu_cols = st.columns(len(gu_list))
        for col, gn in zip(gu_cols, gu_list):
            with col:
                gd = sd["districts"][gn]
                is_sel = gu == gn
                bg  = "#1a4a8a" if is_sel else "#f7f9fc"
                bdr = "1.5px solid #2e7dd4" if is_sel else "1px solid #dde5f0"
                tc  = "#fff" if is_sel else "#0f2d52"
                sc  = "rgba(255,255,255,.6)" if is_sel else "#94a3b8"
                trc = "#a5f3c0" if is_sel else ("#2E7D32" if gd["popT"].startswith("+") else "#C62828")
                st.markdown(
                    f'<div style="background:{bg};border:{bdr};border-radius:8px;padding:10px 8px;text-align:center;margin-bottom:4px">'
                    f'<div style="font-size:13px;font-weight:700;color:{tc}">{gn}</div>'
                    f'<div style="font-size:11px;color:{sc}">인구 {gd["pop"]}</div>'
                    f'<div style="font-size:11px;color:{trc};margin-top:2px">{gd["popT"]}</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )
                if st.button("✓" if is_sel else "선택", key=f"gu_{gn}", use_container_width=True,
                             type="primary" if is_sel else "secondary"):
                    set_gu(gn); st.rerun()

        if gu:
            st.divider()
            gd = sd["districts"][gu]
            hc1, hc2 = st.columns([8, 1])
            with hc1: st.markdown(f"#### {gu} 상세 현황")
            with hc2:
                if st.button("← 뒤로", key="bk_gu"):
                    st.session_state.gu = None; st.session_state.dong = None; st.rerun()
            metrics4({"pop":gd["pop"],"popT":gd["popT"],"retail":gd["retail"],"retailT":gd["retailT"],"spend":gd["spend"],"grdp":gd.get("grdp","—")})
            tags_html(gd["tags"])
            fc1, fc2 = st.columns(2)
            with fc1: rank_list(gd["food"], "인기 맛집·소비 트렌드")
            with fc2: rank_list(gd["trend"], "급상승 검색어")
            st.markdown("**소매판매지수 추이**")
            retail_chart(gd["retail"], gu)
            st.divider()

            # ── LEVEL 3: 행정동 ──
            dl = gd["dongs"]
            st.markdown(f'<div style="font-size:12px;font-weight:700;color:#64748b;margin-bottom:8px">행정동 목록 — {gu} ({len(dl)}개동) · ▶ 클릭하여 상세 분석</div>', unsafe_allow_html=True)
            n = 5
            for row in [dl[i:i+n] for i in range(0, len(dl), n)]:
                dcols = st.columns(n)
                for col, dk in zip(dcols, row):
                    with col:
                        is_sel = dong == dk["n"]
                        bg  = "#e8f2fd" if is_sel else ("#fff8ed" if dk["hot"] else ("#e6f4ec" if dk["rise"] else "#f7f9fc"))
                        bdr = "#1a56a0" if is_sel else ("#e08020" if dk["hot"] else ("#1b6e3a" if dk["rise"] else "#dde5f0"))
                        badge = f'<br><span style="font-size:10px;padding:1px 6px;border-radius:20px;background:{"#fff4e0" if dk["hot"] else "#e6f4ec"};color:{"#c45900" if dk["hot"] else "#1b6e3a"};font-weight:600">{dk["badge"]}</span>' if dk.get("badge") else ""
                        st.markdown(
                            f'<div style="background:{bg};border:1.5px solid {bdr};border-radius:8px;padding:9px 6px;text-align:center;margin-bottom:4px">'
                            f'<div style="font-size:12px;font-weight:{"700" if is_sel else "600"};color:#0f2d52">{dk["n"]}</div>'
                            f'<div style="font-size:10px;color:#94a3b8;margin-top:2px">{dk["pop"]}</div>'
                            f'{badge}</div>',
                            unsafe_allow_html=True
                        )
                        if st.button("▶", key=f"dk_{dk['n']}", use_container_width=True,
                                     type="primary" if is_sel else "secondary"):
                            set_dong(dk["n"]); st.rerun()

            if dong:
                st.divider()
                dd = gd.get("dong_detail", {}).get(dong)
                dh1, dh2 = st.columns([8,1])
                with dh1: st.markdown(f"#### {dong} 상세 분석")
                with dh2:
                    if st.button("← 뒤로", key="bk_dong"):
                        st.session_state.dong = None; st.rerun()

                if dd:
                    c1,c2,c3,c4 = st.columns(4)
                    with c1: st.metric("총 인구", dd["pop"], dd["popT"])
                    with c2: st.metric("1인당 월 소비지출", dd["spend"])
                    with c3: st.metric("외국인 비율", dd["foreign"])
                    with c4: st.metric("소매판매지수", str(dd["retail"]))
                    tags_html(dd["tags"])
                    ac1, ac2 = st.columns(2)
                    with ac1:
                        st.markdown("**연령대별 인구 분포**")
                        age_chart(dd["age"], dd["ageLbl"])
                    with ac2:
                        st.markdown("**소매판매지수 추이**")
                        retail_chart(dd["retail"], dong)
                    fc1, fc2 = st.columns(2)
                    with fc1: rank_list(dd["trend"], "급상승 검색 키워드")
                    with fc2: rank_list(dd["food"], "인기 맛집·소비 업종")
                    st.markdown("**AI 종합 인사이트**")
                    for ic, icon, head, desc in dd["insights"]:
                        card_cls = {"ic-blue":"card-blue","ic-green":"card-green","ic-amber":"card-amber","ic-red":"card-red"}.get(ic,"card")
                        st.markdown(
                            f'<div class="card {card_cls}" style="padding:14px;margin-bottom:8px">'
                            f'<div class="insight-row">'
                            f'<div class="i-icon {ic}">{icon}</div>'
                            f'<div><div class="i-head">{head}</div><div class="i-desc">{desc}</div></div>'
                            f'</div></div>',
                            unsafe_allow_html=True
                        )
                else:
                    dk_info = next((d for d in dl if d["n"] == dong), {})
                    st.metric("추정 인구", dk_info.get("pop","—"))
                    st.info("이 행정동의 상세 데이터는 실제 시스템 구축 후 통계청 KOSIS API와 연동하여 자동 수집됩니다.")
