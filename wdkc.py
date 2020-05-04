from PIL import Image, ImageDraw, ImageFont
import random
import sys

FONT_PATH = "./.fonts/NotoSansMonoCJKjp-Regular.otf"


def load_dic():
    dic = {
        "曜": ["土曜", "月曜", "金曜", "日曜", "曜日"],
        "場": ["場合", "市場", "出場", "球場", "馬場", "登場", "場所", "広場", "会場", "劇場", "工場"],
        "転": ["移転", "運転", "回転", "自転"],
        "政": ["政治", "政府", "政策", "行政", "政党", "政権"],
        "年": ["同年", "元年", "年間", "少年", "年代", "青年", "年表", "毎年", "年度", "生年", "近年"],
        "高": ["高校", "高松", "高知", "最高", "高原", "高山", "高速"],
        "備": ["整備", "警備", "装備", "設備"],
        "海": ["海道", "海洋", "海上", "北海", "海外", "東海", "海岸"],
        "線": ["無線", "幹線", "本線", "路線"],
        "品": ["商品", "製品", "食品", "作品", "薬品"],
        "動": ["動画", "動産", "自動", "移動", "動作", "行動", "動物", "不動", "運動", "活動"],
        "国": ["国際", "王国", "国王", "四国", "国連", "全国", "国有", "国語", "本国", "国家", "戦国", "国民", "中国", "米国", "国鉄", "各国", "国会", "公国", "諸国", "国境", "国土", "三国", "国立", "国内", "外国", "英国", "国外", "国道"],
        "数": ["代数", "複数", "関数", "数学", "整数", "多数"],
        "劇": ["演劇", "劇団", "歌劇", "劇場"],
        "活": ["活用", "生活", "復活", "活動"],
        "日": ["人日", "西日", "日記", "朝日", "全日", "今日", "平日", "日産", "毎日", "日曜", "春日", "曜日", "日本"],
        "参": ["参議", "参照", "参考", "参加"],
        "民": ["市民", "人民", "民間", "国民", "民地", "民主", "民族", "住民"],
        "員": ["教員", "議員", "会員", "委員", "職員"],
        "出": ["出演", "出家", "出場", "出来", "演出", "出版", "選出", "出入", "出身"],
        "当": ["担当", "当初", "当主", "相当", "当時"],
        "域": ["区域", "広域", "地域", "流域", "領域"],
        "県": ["県北", "県西", "県内", "県警", "県立", "県東", "県南", "県道", "府県"],
        "伝": ["伝統", "遺伝", "伝承", "伝説"],
        "衛": ["衛生", "衛星", "防衛", "自衛"],
        "産": ["動産", "日産", "生産", "産業", "水産", "共産", "遺産"],
        "士": ["博士", "戦士", "力士", "富士", "武士"],
        "院": ["議院", "病院", "寺院", "院議", "学院"],
        "中": ["中川", "山中", "中村", "中間", "中野", "中学", "中等", "市中", "中世", "戦中", "中国", "中央", "中島", "中山", "中期", "中心", "中部"],
        "期": ["長期", "定期", "短期", "後期", "前期", "初期", "末期", "期間", "中期"],
        "部": ["学部", "一部", "部長", "支部", "南部", "外部", "部分", "東部", "西部", "北部", "本部", "部隊", "部屋", "部門", "中部", "内部"],
        "府": ["政府", "幕府", "都府", "府県"],
        "南": ["南部", "南東", "県南", "南西", "南北"],
        "歌": ["歌人", "歌手", "歌劇", "和歌"],
        "学": ["光学", "学部", "小学", "中学", "学問", "学的", "学校", "力学", "大学", "史学", "化学", "理学", "学術", "修学", "学習", "学会", "数学", "語学", "医学", "学科", "学館", "学長", "工学", "法学", "文学", "学者", "科学", "神学", "学院", "学名", "学生", "学園"],
        "第": ["第二", "第三", "第四", "第一"],
        "現": ["現象", "現在", "現行", "現存", "表現", "現代"],
        "義": ["義人", "主義", "広義", "名義", "義務", "定義"],
        "工": ["人工", "工事", "加工", "工業", "工学", "工場"],
        "史": ["史上", "史学", "歴史", "史的", "史家"],
        "式": ["株式", "方式", "公式", "正式", "形式", "様式"],
        "全": ["全国", "完全", "全日", "全体", "安全"],
        "明": ["発明", "説明", "証明", "不明"],
        "連": ["連続", "国連", "連合", "連盟", "関連"],
        "著": ["著名", "著書", "著作", "著者"],
        "規": ["規格", "規定", "規則", "規模", "規制"],
        "治": ["政治", "自治", "治世", "統治"],
        "族": ["一族", "家族", "貴族", "皇族", "氏族", "民族"],
        "広": ["広域", "広告", "広義", "広場", "広島"],
        "用": ["専用", "用語", "使用", "応用", "活用", "信用", "運用", "適用", "採用", "作用", "利用"],
        "料": ["料金", "資料", "材料", "料理", "燃料"],
        "地": ["地下", "土地", "地理", "民地", "地上", "山地", "地方", "地域", "基地", "地形", "在地", "地球", "団地", "各地", "要地", "地図", "地名", "地区"],
        "空": ["航空", "空港", "空軍", "空間"],
        "同": ["合同", "同様", "同年", "同人", "協同", "同盟", "同時", "共同", "同名", "同一"],
        "大": ["大島", "大正", "大野", "大橋", "大和", "拡大", "市大", "大学", "大型", "大賞", "大名", "大田", "大使", "大陸", "大谷", "大臣", "東大", "大字", "大戦", "最大", "大分", "大統", "大会", "立大"],
        "社": ["社団", "神社", "社長", "社会", "会社", "公社", "本社"],
        "島": ["大島", "児島", "半島", "諸島", "徳島", "中島", "広島", "福島"],
        "能": ["能力", "機能", "芸能", "可能"],
        "経": ["経験", "経歴", "神経", "経済", "経営"],
        "議": ["議会", "議員", "会議", "協議", "議院", "参議", "議論", "院議", "衆議"],
        "子": ["分子", "子供", "王子", "原子", "男子", "量子", "女子", "息子", "電子"],
        "団": ["社団", "集団", "楽団", "教団", "劇団", "財団", "団体", "団地"],
        "術": ["技術", "術者", "学術", "美術", "芸術"],
        "西": ["県西", "西日", "北西", "西部", "関西", "南西", "西洋"],
        "代": ["代数", "初代", "代表", "近代", "時代", "古代", "年代", "千代", "歴代", "代田", "現代", "世代", "代理"],
        "北": ["県北", "北西", "北海", "北条", "北部", "東北", "南北", "北東"],
        "法": ["司法", "方法", "憲法", "法人", "手法", "法令", "法則", "法律", "法学"],
        "事": ["事典", "事故", "事務", "事例", "事実", "軍事", "行事", "仕事", "記事", "工事", "理事", "知事", "人事"],
        "手": ["歌手", "選手", "手法", "岩手"],
        "理": ["処理", "理由", "定理", "地理", "理学", "論理", "理事", "原理", "心理", "推理", "料理", "管理", "理論", "代理"],
        "関": ["関東", "関数", "機関", "関係", "関西", "関連"],
        "行": ["行列", "単行", "発行", "運行", "行事", "行政", "現行", "急行", "刊行", "銀行", "旅行", "実行", "移行", "行動", "飛行"],
        "小": ["小学", "小倉", "小説", "小松", "小山", "小林", "小型", "小川"],
        "放": ["放射", "解放", "放送", "放映"],
        "類": ["種類", "分類", "人類", "類似"],
        "表": ["表記", "表面", "代表", "発表", "表現", "年表", "表示"],
        "内": ["県内", "市内", "内閣", "河内", "国内", "内部", "内容"],
        "業": ["作業", "開業", "職業", "実業", "商業", "農業", "業務", "業者", "卒業", "創業", "産業", "工業", "営業", "業界"],
        "競": ["競輪", "競馬", "競技", "競走"],
        "最": ["最後", "最初", "最終", "最高", "最大"],
        "楽": ["楽団", "楽曲", "音楽", "楽器"],
        "言": ["言語", "方言", "宣言", "言葉"],
        "近": ["近世", "近代", "付近", "近年"],
        "作": ["作戦", "作業", "作成", "制作", "作者", "作画", "著作", "作品", "作詞", "動作", "操作", "製作", "作家", "原作", "作曲", "作用"],
        "人": ["人日", "人工", "義人", "歌人", "人民", "新人", "個人", "同人", "法人", "人気", "詩人", "人物", "名人", "人類", "人形", "人口", "本人", "人名", "主人", "一人", "人事", "人間", "殺人", "軍人"],
        "松": ["高松", "小松", "松山", "松本"],
        "原": ["原則", "原因", "原題", "原子", "原理", "高原", "原作", "原町", "田原"],
        "区": ["区域", "区画", "区分", "区別", "区間", "管区", "地区"],
        "家": ["家庭", "出家", "国家", "家族", "家臣", "画家", "本家", "作家", "史家"],
        "様": ["同様", "仕様", "多様", "様式"],
        "保": ["保護", "保安", "保存", "保険", "保健", "保有", "保障"],
        "加": ["加盟", "追加", "加工", "参加"],
        "天": ["天使", "天然", "天文", "天体"],
        "市": ["市民", "市場", "市街", "市大", "市中", "市内", "市長", "城市", "都市", "市立"],
        "土": ["土地", "土曜", "郷土", "国土", "安土"],
        "町": ["室町", "町村", "町名", "原町", "町立"],
        "会": ["協会", "議会", "会議", "教会", "学会", "国会", "社会", "会主", "会社", "会長", "会員", "会計", "会館", "会場", "大会"],
        "主": ["主義", "君主", "当主", "主張", "民主", "会主", "主要", "主人", "主題"],
        "協": ["協力", "協会", "協議", "協同", "協定"],
        "初": ["初代", "最初", "当初", "初期"],
        "要": ["要素", "主要", "必要", "重要", "要地"],
        "時": ["時点", "時代", "同時", "臨時", "時間", "戦時", "当時"],
        "設": ["設定", "創設", "設置", "建設", "設計", "設立", "設備"],
        "公": ["公立", "公演", "公開", "公共", "公益", "公式", "公国", "公園", "公社"],
        "発": ["発電", "発行", "発明", "発生", "開発", "発表", "発足", "発展", "発見", "発音", "発売"],
        "車": ["戦車", "乗車", "車道", "車両", "停車", "電車", "列車"],
        "以": ["以上", "以前", "以降", "以外", "以後", "以下"],
        "自": ["自然", "自治", "自動", "自衛", "独自", "自転"],
        "実": ["実際", "事実", "実業", "実験", "実行", "実績"],
        "野": ["中野", "大野", "野川", "長野", "高野", "分野", "上野", "平野", "野球", "野田"],
        "置": ["配置", "位置", "装置", "設置"],
        "元": ["紀元", "元年", "次元", "元号"],
        "在": ["存在", "現在", "在位", "所在", "在地", "在住"],
        "東": ["関東", "東洋", "県東", "南東", "東部", "東海", "東京", "東北", "東大", "北東"],
        "編": ["編曲", "長編", "短編", "編集", "編成"],
        "安": ["保安", "平安", "安全", "安土", "安定"],
        "電": ["発電", "電力", "帯電", "電鉄", "電子", "電話", "電気", "電車"],
        "号": ["山号", "記号", "信号", "番号", "元号"],
        "合": ["合同", "場合", "統合", "複合", "試合", "総合", "合唱", "組合", "結合", "集合", "合成", "合体", "合戦", "化合", "連合"],
        "建": ["建築", "建物", "建造", "建設"],
        "古": ["古典", "古代", "考古", "古川"],
        "本": ["本文", "山本", "本名", "本国", "基本", "絵本", "本家", "本部", "本人", "本線", "松本", "資本", "本社", "日本", "本来", "旗本"],
        "語": ["言語", "用語", "国語", "物語", "語学", "英語", "落語"],
        "気": ["人気", "蒸気", "電気", "気象"],
        "護": ["守護", "保護", "看護", "弁護"],
        "道": ["街道", "海道", "車道", "報道", "水道", "県道", "道路", "鉄道", "修道", "国道", "都道"],
        "間": ["中間", "民間", "年間", "空間", "期間", "時間", "人間", "区間"],
        "演": ["出演", "演劇", "公演", "演出", "演者", "演奏"],
        "対": ["対象", "対応", "対立", "反対", "対戦", "対策"],
        "位": ["単位", "位置", "在位", "官位"],
        "外": ["外部", "外交", "以外", "海外", "外国", "国外"],
        "資": ["投資", "資源", "資料", "資格", "資本"],
        "方": ["方法", "方向", "方言", "方式", "地方", "方面"],
        "世": ["近世", "治世", "中世", "世界", "世紀", "世代"],
        "力": ["協力", "能力", "勢力", "力学", "電力", "力士", "暴力"],
        "文": ["本文", "論文", "文庫", "英文", "国文", "文台", "文化", "文芸", "天文", "文学", "文書", "文字"],
        "長": ["長期", "部長", "長野", "長編", "社長", "局長", "市長", "成長", "会長", "学長", "長官", "長男"],
        "記": ["表記", "記録", "日記", "記述", "記号", "記者", "記事", "記念"],
        "成": ["作成", "育成", "養成", "成立", "完成", "成長", "成分", "形成", "結成", "合成", "生成", "成功", "編成", "構成", "成績"],
        "集": ["集団", "集合", "編集", "集英"],
        "所": ["所属", "場所", "役所", "所在", "所管", "所有"],
        "化": ["進化", "化学", "酸化", "文化", "化合", "変化"],
        "体": ["体育", "全体", "合体", "体系", "体制", "天体", "団体"],
        "歴": ["歴任", "経歴", "歴史", "歴代"],
        "正": ["改正", "大正", "正教", "正式"],
        "通": ["交通", "通常", "通算", "共通", "流通", "通信"],
        "都": ["首都", "都府", "都市", "京都", "都道"],
        "村": ["田村", "中村", "村立", "村上", "山村", "町村"],
        "知": ["知識", "高知", "知事", "愛知"],
        "制": ["制作", "制定", "強制", "制度", "体制", "制限", "規制"],
        "定": ["認定", "測定", "定期", "規定", "設定", "検定", "定理", "予定", "指定", "制定", "一定", "限定", "特定", "決定", "定義", "安定", "協定"],
        "画": ["区画", "動画", "作画", "映画", "計画", "画家", "絵画", "画像"],
        "説": ["説明", "小説", "解説", "伝説"],
        "者": ["作者", "術者", "奏者", "導者", "害者", "記者", "演者", "業者", "著者", "学者"],
        "形": ["形態", "山形", "形状", "人形", "地形", "形成", "形式"],
        "師": ["絵師", "教師", "講師", "医師"],
        "開": ["開業", "展開", "開発", "開始", "公開", "再開"],
        "前": ["以前", "戦前", "前身", "前期", "名前"],
        "川": ["中川", "田川", "野川", "河川", "古川", "小川"],
        "面": ["表面", "仮面", "面積", "方面"],
        "軍": ["陸軍", "軍事", "空軍", "将軍", "軍人"],
        "交": ["交通", "交流", "外交", "交差"],
        "戦": ["作戦", "戦車", "戦後", "戦士", "戦中", "戦争", "戦国", "戦前", "合戦", "大戦", "戦時", "対戦", "戦略"],
        "一": ["一族", "一部", "一帯", "一種", "一次", "一丁", "一定", "統一", "一覧", "一人", "第一", "同一"],
        "題": ["問題", "原題", "主題", "題材"],
        "田": ["田村", "上田", "田川", "山田", "新田", "大田", "太田", "豊田", "代田", "野田", "田原"],
        "新": ["新聞", "新人", "新宿", "新田", "日新"],
        "造": ["構造", "製造", "改造", "建造", "造物"],
        "王": ["王国", "国王", "王朝", "王子", "親王"],
        "論": ["論文", "論争", "論理", "議論", "評論", "理論"],
        "物": ["生物", "植物", "物語", "人物", "建物", "貨物", "物質", "博物", "造物", "動物"],
        "名": ["本名", "命名", "名義", "著名", "大名", "名人", "有名", "人名", "町名", "名前", "同名", "地名", "別名", "学名"],
        "機": ["機能", "機動", "機器", "機関", "機構", "有機", "危機", "機械"],
        "後": ["後半", "最後", "戦後", "後期", "以後"],
        "生": ["厚生", "衛生", "生物", "発生", "再生", "派生", "生産", "生成", "生活", "生徒", "誕生", "生年", "生命", "学生"],
        "共": ["公共", "共通", "共産", "共同"],
        "流": ["交流", "流域", "流通", "支流"],
        "統": ["系統", "統合", "伝統", "統計", "統一", "大統", "統治"],
        "水": ["水道", "清水", "水戸", "水系", "水素", "水産"],
        "英": ["英文", "英語", "集英", "英国"],
        "山": ["山中", "郡山", "山形", "山本", "山号", "山城", "山田", "山口", "山脈", "山地", "松山", "小山", "富山", "山村", "中山", "高山", "青山"],
        "書": ["著書", "図書", "聖書", "文書", "書店"],
        "上": ["以上", "上田", "史上", "向上", "地上", "海上", "村上", "陸上", "上野"],
        "優": ["声優", "優勝", "女優", "俳優"],
        "運": ["運行", "運営", "運転", "運用", "運輸", "運動"],
        "系": ["系統", "体系", "水系", "系列"],
        "科": ["歯科", "学科", "百科", "科学"],
        "信": ["信号", "信用", "配信", "送信", "通信"],
        "分": ["分布", "分子", "区分", "分類", "分野", "部分", "分割", "成分", "大分", "分解", "分校"],
        "教": ["教員", "教授", "教会", "教師", "教団", "正教", "宗教", "教育"],
        "平": ["平日", "平和", "平安", "平野", "太平"],
        "音": ["音声", "音楽", "発音", "福音"],
        "立": ["成立", "公立", "県立", "独立", "村立", "私立", "対立", "創立", "国立", "市立", "町立", "設立", "立大"],
        "来": ["出来", "未来", "由来", "本来"],
        "構": ["構造", "機構", "構想", "構成"],
        "女": ["女性", "女子", "女優", "少女"],
        "有": ["国有", "有名", "有機", "有限", "所有", "保有"],
        "解": ["解散", "解放", "解説", "分解"],
        "神": ["神社", "神戸", "神経", "神宮", "精神", "神学", "神話"],
        "計": ["統計", "計算", "計画", "設計", "会計"]}
    return dic


def create_text(ans, four):
    # fourの4要素を順番に上右下左の順で割当
    for i in range(len(four)):
        if i == 0:
            upper_char = four[i][0] if four[i][1] == ans else four[i][1]
            upper_arrow = "↓" if four[i][1] == ans else "↑"
        elif i == 1:
            right_char = four[i][0] if four[i][1] == ans else four[i][1]
            right_arrow = "←" if four[i][1] == ans else "→"
        elif i == 2:
            lower_char = four[i][0] if four[i][1] == ans else four[i][1]
            lower_arrow = "↑" if four[i][1] == ans else "↓"
        elif i == 3:
            left_char = four[i][0] if four[i][1] == ans else four[i][1]
            left_arrow = "→" if four[i][1] == ans else "←"
        else:
            print("fourに要素が4個以上あります")
            sys.exit(four)
    up = "　　" + upper_char + "　　" + "\n"
    um = "　　" + upper_arrow + "　　" + "\n"
    mid = left_char + left_arrow + "□" + right_arrow + right_char + "\n"
    ml = "　　" + lower_arrow + "　　" + "\n"
    low = "　　" + lower_char + "　　"
    text = up + um + mid + ml + low
    return text


def create_img(ans, four):
    text = create_text(ans, four)
    img = Image.new("RGB", (450, 500), "white")
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype(FONT_PATH, 72)
    draw.text((40, 0), text, font=fnt, fill=(0, 0, 0, 255))
    return img


def main():
    args = sys.argv
    if len(args) != 2:
        if len(args) == 1:
            print("引数を指定してください")
            sys.exit(1)
        elif 2 < len(args):
            print("引数は一つだけ指定してください")
            sys.exit(1)
    elif not args[1].isdigit():
        print("引数は数値を指定してください")
        sys.exit(1)
    elif 200 < int(args[1]):
        print("引数は200以下にしてください")
        sys.exit(1)

    dic = load_dic()

    selected = []
    counter = 0
    while counter < int(args[1]):
        # 和同開珎の答えと、問題4単語を取り出す
        ans = random.choice(list(dic.keys()))
        four = random.sample(dic[ans], 4)

        if ans in selected and len(dic[ans]) == 4:
            continue

        selected.append(ans)
        counter += 1

        img = create_img(ans, four)
        img_path = "./result/" + str(counter) + ".jpg"
        img.save(img_path)

    print("generated.")

if __name__ == '__main__':
    main()