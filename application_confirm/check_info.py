def check(phone_num):
  check_form = "<p>신청내역</p><br><br>"
  info = [["01059327308", "최서영", "롱돕바-흰색", "S", "영", "O"],
["01051584690", "김채은", "롱돕바-흰색", "L", "성씨 김 金/ 캘 채 采/ 온화할 은誾", "O"],
["01037636164", "이건명", "롱돕바-검정", "XL", "", "O"],
["01031239516", "안준서", "롱돕바-흰색", "XL", "11-Jun", "O"],
["01057659832", "손온혜", "롱돕바-검정", "XXL", "ssunonhye", "O"],
["01032375975", "한승민", "롱돕바-흰색", "XL", "", "O"],
["01077359157", "고한아", "롱돕바-검정", "XL", "HanA", "O"],
["01065415604", "김민서", "롱돕바-흰색", "L", "金 珉 瑞 (성씨 김, 옥돌 민, 상서 서)", "O"],
["01020543884", "이지윤", "롱돕바-흰색", "M", "李知潤(오얏 리, 알 지, 윤택할 윤)", "O"],
["01026071910", "이성빈", "숏돕바-검정", "XL", "李(오얏 리), 誠(정성 성), 彬(빛날 빈)", "O"],
["01048087015", "오채원", "롱돕바-흰색", "M", "jia", "O"],
["01052277585", "양윤아", "롱돕바-흰색", "M", "梁允娥 (들보 량, 진실로 윤, 예쁠 아)", "O"],
["01033091887", "김채원", "롱돕바-흰색", "L", "金(쇠 금)彩(채색 채)媛(계집 원)", ""],
["01021569011", "최은희", "롱돕바-흰색", "L", "CHOI E H", ""],
["01028033316", "박하연", "롱돕바-흰색", "L", "PARK H Y", "O"],
["01035953751", "윤나영", "롱돕바-검정", "S", "尹(성씨 윤) 那 (어찌 나) 瑛(옥빛 영)", "O"],
["01056683816", "박동희", "숏돕바-검정", "XL", "성씨 박/ 동녘 동/ 빛날 희", "O"],
["01056683816", "박동희", "숏돕바-흰색", "XL", "성씨 박/ 동녘 동/ 빛날 희", "O"],
["01040718424", "박소원", "롱돕바-흰색", "M", "Park Sowon", "O"],
["01090672501", "정지우", "롱돕바-흰색", "M", "丁(고무래 정)志(뜻 지)宇(집 우)", "O"],
["01088376048", "엄태용", "롱돕바-검정", "XL", "UMTAEYONG", "O"],
["01065885246", "김윤서", "롱돕바-흰색", "M", "金潤序", "O"],
["01028864801", "김도희", "롱돕바-흰색", "S", "度希", "O"],
["01033689363", "전은서", "롱돕바-흰색", "S", "eun", "O"],
["01034231810", "조하진", "롱돕바-흰색", "S", "趙(나라 조) 夏(여름 하) 眞(참 진)", "O"],
["01087534988", "류건영", "롱돕바-흰색", "XL", "C’est La Vie", "O"],
["01075634524", "박예균", "롱돕바-흰색", "L", "", "O"],
["01034108220", "박수영", "롱돕바-흰색", "XXL", "", "O"],
["01072663561", "이준수", "롱돕바-흰색", "XL", "Lee", ""],
["01052648637", "김규리", "롱돕바-검정", "S", "gyuri", ""],
["01073457450", "정우진", "롱돕바-흰색", "XL", "Jeong.W.J.", "O"],
["010-4004-2078", "신동녘", "롱돕바-검정", "XXL", "申( 납 신)동녘(성은 한자로 이름은 한글로 부탁드립니다)", "O"],
["01024649255", "이현서", "롱돕바-흰색", "L", "李炫抒 (오얏 리, 밝을 현, 풀 서)", "O"],
["01029757330", "박민서", "롱돕바-검정", "S", "朴民恕 (성씨 박/백성 민/용서할 서)", "O"],
["01036073051", "이현서", "롱돕바-흰색", "L", "", "O"],
["01076126890", "장유경", "롱돕바-흰색", "L", "yugyeong", "O"],
["01050686392", "피지윤", "롱돕바-검정", "S", "PJY", "O"],
["01044048403", "변채은", "롱돕바-흰색", "XS", "Jelly Byeon", "O"],
["01086618541", "남수빈", "롱돕바-검정", "M", "", "O"],
["01091317905", "정서윤", "롱돕바-흰색", "XS", "鄭棲尹 (나라 정 깃들일 서 다스릴 윤)", "O"],
["01086618541", "남수빈", "롱돕바-흰색", "M", "Subin", ""],
["01029008277", "박성빈", "롱돕바-흰색", "XXL", "psb", "O"],
["01034526390", "박서현", "롱돕바-흰색", "L", "", "O"],
["01039348530", "한예리", "롱돕바-흰색", "M", "韓 (나라 한) 䜭 (밝을 예, 준설할 준) 利 (이로울 리)", "O"],
["01099235640", "원영중", "숏돕바-흰색", "XL", "Wayne", "O"],
["01091942628", "신지원", "롱돕바-검정", "S", "S.Jiwon", "O"],
["01062518034", "이지민", "롱돕바-검정", "XS", "李知珉", ""],
["01090829007", "엄상진", "롱돕바-흰색", "L", "eom_sj", ""],
["01092267595", "김휘성", "롱돕바-흰색", "L", "H.S.Kim", ""],
["01029918623", "고종훈", "롱돕바-검정", "XL", "", ""],
["01073410641", "손성경", "롱돕바-검정", "M", "Sonny", ""],
["01025310037", "임나영", "숏돕바-흰색", "L", "N Y", ""],
["01025310037", "임나영", "숏돕바-검정", "M", "", ""],
["01094281685", "정지원", "롱돕바-흰색", "S", "N Y", ""],
["01094281685", "정지원", "롱돕바-검정", "XL", "", ""],
["01054022584", "이석원", "롱돕바-검정", "XL", "LEE.S.W", ""],
["01067741539", "박윤호", "롱돕바-흰색", "XXL", "", ""],
["01084105028", "백승준", "롱돕바-검정", "XL", "白承准", ""]]
  for i in range(len(info)):
    if phone_num == info[i][0]:
      check_form += "이름:"+info[i][1]+" / 종류-색상:"+info[i][2]+" / 사이즈:"+info[i][3]+" / 이니셜자수:"+info[i][4]
      if info[i][4] == "":
        check_form += "(미기입)"
      check_form += " / 입금여부:"+info[i][5]
      if info[i][5] == "":
        check_form += "X"
      check_form += "<br>"
  check_form += "<br><br>// 최근 입금 여부 갱신 : 2023.10.16 17:00<br>"
  check_form += "<a href='/application_confirm/'>Go back</a><br>"
  return check_form