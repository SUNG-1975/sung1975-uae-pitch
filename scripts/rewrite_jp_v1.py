#!/usr/bin/env python3
"""Replace the JP map in V1 index.html with native Japanese copy."""
import re

NEW_JP = r"""    jp: {
      'cover.h1': '<em>湾岸へ、いま。</em>',
      'cover.intro': 'SUNG1975をアラブ首長国連邦・GCC市場へ展開するためのご提案。秋山様のブランドが、世界でこのブランドを最も必要としている都市へ。',
      'cover.prepared-for': 'ご献呈先',
      'cover.prepared-by': '提案者',
      'cover.prepared-by-val': 'Balraj Singh Kalra<br/>山田さん（Portgate）',
      'sec.08.akito.name': '山田さん',
      'cover.meeting': '会議',
      'cover.meeting-val': 'ビデオ会議（60分）· 2026年5月',
      'cover.status': 'ステータス',
      'cover.status-val': '機密 · v1',

      'sec.01-5.label': '全体像 — 1年目のかたち',
      'sec.01-5.h2': 'まず数字より先に、<em>私どもが実際に何をするのか</em>をご覧ください。',

      'sec.02.label': '02 — この提案の核心',
      'sec.02.h2': 'ブランドと都市、そしてタイミング。<br/>三つが重なる、<em>いまこの瞬間。</em>',

      'sec.03.label': '03 — なぜドバイなのか、なぜ今なのか',
      'sec.03.h2': 'ドバイはすでに、<br/>世界第二のアスレジャー都市になっています。',

      'sec.04.label': '04 — ドバイが扉を開く理由',
      'sec.04.h2': '一つの都市に、<em>200を超える国籍。</em><br/>世界の半分が、手の届く距離に。',

      'sec.04.5.label': '04.5 — UAEが今も育て続けている市場',
      'sec.04.5.h2': 'UAEのすべての学童は、柔術を学んでいます。<br/><em>国家の命令によって。毎年。18年間、途切れることなく。</em>',

      'sec.04.7.label': '04.7 — たった5%という景色',
      'sec.04.7.h2': 'SUNG1975が、すでにここにいる人々の<br/><em>たった5%を動かしたとしたら。</em>',

      'sec.05.label': '05 — 先行事例',
      'sec.05.h2': 'Giving Movementが証明しました。ドバイは<em>グローバルへの発射台</em>になれると。',

      'sec.06.label': '06 — すでにそこにいるオーディエンス',
      'sec.06.h2': 'ファンはすでにいます。<br/><em>ブランドに必要なのは、届けるチャネルだけ。</em>',

      'sec.06.5.label': '06.5 — 私どもが開けるポップアップ会場',
      'sec.06.5.h2': 'ドバイで最もデザインで語られるプレミアム・ジムチェーン。<br/><em>8拠点。温かいご紹介一本で、扉が開きます。</em>',

      'sec.06.6.label': '06.6 — ローンチの瞬間',
      'sec.06.6.h2': '秋山様 × Kris Fade。<br/><em>ドバイ到着を、バイラルな出来事に変えるドバイの声。</em>',

      'sec.07.label': '07 — 同じ棚、まったく違う物語',
      'sec.07.h2': '棚は同じ。<em>物語が、まるで違う。</em>',

      'sec.08.label': '08 — 私どもについて',
      'sec.08.h2': 'ドバイを拠点とする2人のオペレーター。<br/><em>東京に、運営を担う会社。</em>',

      'sec.9.label': '09 — なぜ私どもなのか',
      'sec.9.h2': 'この提案に必要な関係性を、<em>すでに持っている2人です。</em>',

      'sec.10.label': '10 — MMA × ドバイという交点',
      'sec.10.h2': '12ヶ月間、ドバイのすべての<br/>ファイトナイトに、<em>秋山様のお顔を。</em>',

      'sec.11.label': '11 — フェーズ別計画',
      'sec.11.h2': '4つのフェーズ。2年間。<em>ひとつの確信。</em>',

      'sec.12.label': '12 — 1年目のアクティベーション・カレンダー',
      'sec.12.h2': '12ヶ月で、<em>8つの現地の瞬間。</em><br/>秋山様のご来訪は、四半期に一度で足ります。',

      'sec.13.label': '13 — UAE限定カプセル',
      'sec.13.h2': 'アラビア書道と、<em>SUNG1975のミニマリズム。</em>',

      'sec.14.label': '14 — 価格はすでに市場が受け入れています',
      'sec.14.h2': '秋山様のブランドはすでに、<br/>この価格帯でUAEに届いています。',

      'sec.15.label': '15 — 契約の構造',
      'sec.15.h2': '秋山様がブランドを所有し続ける。<br/><em>Portgateが運営し、リスクを引き受ける。</em>',

      'sec.16.label': '16 — 並行展開 · スキンケア',
      'sec.16.h2': '第二のカテゴリー。<em>同じ進め方で、異なる棚へ。</em>',

      'sec.17.label': '17 — ご承諾後の最初の30日間',
      'sec.17.h2': 'ご承諾をいただいた翌日から、<em>私どもはこう動きます。</em>',

      // ── §01.5 walkthrough ──────────────────────────────────────────
      'sec.01-5.body.p1': '法人設立、ECサイト構築、マーケティング、フルフィルメント、リテール。秋山様のブランドがドバイ・UAEで出荷できる体制を、私どもがゼロから整えます。その全体像をご覧ください。',
      'sec.01-5.card1.title': '法人を立ち上げる',
      'sec.01-5.card1.body': 'Portgateがドバイのフリーゾーンに<strong>SUNG1975 Arabia</strong>を設立します。UAE・GCC商標を出願し、銀行口座を開設、貿易ライセンスを取得します。秋山様にご署名いただく書類はございません。<span style="color:var(--muted);">これは、Portgateが2022年以来40社超の日系企業に対して行ってきたことと同じです。</span>',
      'sec.01-5.card2.title': 'ECサイトを立ち上げる',
      'sec.01-5.card2.body': '日本ストアと同じカタログをベースに<strong>.aeストアフロント</strong>を構築します。英語・アラビア語のバイリンガル対応。内蔵の<strong>商品ファインダー</strong>が、体型・スポーツ・目的別にショッパーをご案内します。購買体験がブランドの水準に見合ったものになります。',
      'sec.01-5.card3.title': 'マーケティングを動かす',
      'sec.01-5.card3.body': '3つの施策を同時に展開します：<br/>· <strong>MMAイベント・ポップアップストア</strong>（Dubai Muscle Showを皮切りに、すでに名前の挙がっているイベントへ順次展開）。<br/>· <strong>ペイドソーシャル</strong>（IG・TikTok・YouTubeでUAE・GCC・在外日本人コミュニティをターゲット）。<br/>· <strong>Kris Fadeコラボ</strong>（ドバイ最大の英語ラジオ＋Netflixパーソナリティ）— 秋山様のドバイご訪問に合わせ、ポッドキャスト収録とバイラル動画を制作します。',
      'sec.01-5.card4.title': '翌日配送を実現する',
      'sec.01-5.card4.body': 'ドバイ自社倉庫でのピッキング＆パッキング。締め切り前の注文は<strong>ドバイ翌日着</strong>、UAE全土は1〜2日、GCC圏は3〜5日でお届けします。LululemonやALOと同水準のブランド体験を、このマーケットで実現します。リピート購買を阻む7日待ちは、最初から排除します。',
      'sec.01-5.card5.title': 'ジムにポップアップと棚を作る',
      'sec.01-5.card5.body': '私どものチームがすでにトレーニングし、関係を築いているジムにSUNG1975の棚またはポップアップを設けます。まずは<strong>Warehouse Gym</strong>（ドバイ最大のプレミアムチェーン、15拠点超）から。顧客がセットの合間に実際に素材を手に取り、ECサイトで翌日配送注文できる体験を届けます。',
      'sec.01-5.pull': '法人、チャネル、マーケティング、フルフィルメント、リテール — <em style="font-style:normal; color:var(--olive-deep);">これが全体像です。</em>このデッキ以降の内容は、それぞれの要素が機能する根拠です。',

      // ── §02 thesis ─────────────────────────────────────────────────
      'sec.02.body.p1': 'いま、ドバイは世界第二のアスレジャー都市です。ALO、Lululemon、Vuori、Gymshark、Giving Movementのすべてが、36ヶ月以内にフラッグシップを出店しました。UAE市場は<strong>$13.26B（2024年）</strong>、年率<strong>9.71%</strong>で成長を続けています。そしてこの都市にまだないのは、顔が見えるプレミアム・メンズブランドです。',
      'sec.02.body.p2': 'SUNG1975は、その棚にぴたりと収まります。デザイン言語も同じ。価格帯（$75〜$156）も同じ。ファウンダーのパーソナルチャンネルはInstagramとYouTube合わせて<strong>286万人</strong>にリーチしています。欠けているのは、韓国・日本の外への本格的な展開だけです。',
      'sec.02.body.p3': 'SUNG1975はまた、競合他社が踏み込めないレーンに位置しています。ALOとLululemonはスタジオヨガ。VuoriはカリフォルニアDTC。GymsharkはハードジムDTC。Giving Movementはモデストファッション・エコ。<strong>その棚でファウンダー主導かつMMAのクレディビリティを持つブランドは、SUNG1975だけです</strong> — そしてドバイは、価格ではなく「人物」に対価を支払う都市です。',
      'sec.02.body.p4': '私どもは、そのギャップを埋めることをご提案します。独占ライセンスのもと、SUNG1975のUAE・GCCアームを、私どもの資金と運営で立ち上げます。秋山様からの資金投資はゼロ。リスクは最初から非対称に設計されています。',
      'sec.02.body.p5': '運営のご負担もありません。<strong>Portgate</strong>（山田さんのドバイ運営会社）がすべてをエンドツーエンドで担います：UAE法人設立、銀行口座、商標、ビザ、マーケティング、物流、フルフィルメント。<strong>秋山様にご署名いただく書類はゼロです。</strong>',
      'sec.02.pull': 'ドバイは発射台です — <em>目的地ではありません。</em>',
      'sec.02.bsb.label': '同じ棚 · ドバイの日常Tシャツ価格帯',
      'sec.02.bsb.footnote': 'コアTシャツ価格帯 — ドバイ通年カテゴリー。フーディは12〜2月のみの販売のため、日常売上の軸はTシャツで構成されます。SUNG1975の既存$75 TシャツはAED 275として価格帯のど真ん中に着地します。データ取得：2026年5月18日。',

      // ── §03 why Dubai ──────────────────────────────────────────────
      'sec.03.gr.eyebrow': 'UAE アスレジャー市場 · 単位：10億ドル',
      'sec.03.gr.now': '2025年 現在',
      'sec.03.gr.then': '2033年 予測',
      'sec.03.gr.cagr': '年率9.71%の成長。ドバイで棚を持つことは、成長し続ける市場の中に存在し続けることを意味します。',
      'sec.03.gr.src': '◦ 出典：Grand View Research · UAE Athleisure Market Outlook 2026-2033 · Deep Market Insights 2026 · Statista。<span style="color:var(--olive-deep);">スナップショット · 2026-05-28。</span>',
      'sec.03.body.p1': '36ヶ月以内に、主要プレミアム・アスレジャーブランドのすべてがUAE出店を完了または確約しました。パートナー選定のパターンも変わっています。デジタルネイティブブランドは今やAlshaya（マスマーケット・フランチャイズ）を使わず、Al TayerまたはMAF（ラグジュアリー・キュレーション）を選びます。<strong>GymsharkもVuoriも、ともにAl Tayerを選んでいます。</strong>これがドバイに入るアスレジャーブランドの新しい進め方です。',
      'sec.03.body.p2': 'ドバイ発のベンチマーク、Giving Movementは、2020年の単独DTCサイトから<strong>5カ国13店舗</strong>（UAE 8店舗）、Series A $15Mへとスケールしました。ファウンダーは2025年5月に既存投資家に売却。新CEOは高コストに終わった米国展開の失敗を受け、明示的にMENA優先へ回帰しています。',
      'sec.03.body.p3': 'この都市は、強いパーソナリティとデザインを持つブランドを育てます。価格競争だけで戦おうとするブランドを、淘汰します。SUNG1975は、前者のレーンにいます。',
      'sec.03.chart1.title': 'UAEのプレミアム・アスレジャー — 検証済みパートナー事例',
      'sec.03.retailers.title': '各リテーラーについて',

      // ── §04 why Dubai opens doors ──────────────────────────────────
      'sec.04.stat1.body': '地球上で最も人口構成が多様な都市。SUNG1975が届けたいすべての顧客層が、すでにこの都市の中にいます。',
      'sec.04.stat2.body': 'エミレーツ便1本で世界の半分に到達できます。これほどの発信力を持つ都市は、他にありません。',
      'sec.04.stat3.body': '毎月100カ国以上の人々がこのブランドと出会います — ドバイの観光経済が、集客コストを代わりに支払ってくれます。',
      'sec.04.body.p1': 'ドバイはドバイ人だけに売る都市ではありません。ここを通過するすべての人に、売ります。<strong>200以上の国籍</strong>の人々がここに定住しています。<strong>35億人</strong>が4時間のフライト圏内にいます。<strong>1,872万人の国際旅行者</strong>が2024年に訪れ、その全員がブランドの射程圏内で実質的な時間を過ごしました。',
      'sec.04.body.p2': 'MMAのクレディビリティを持つブランドにとって、UAEは地球上でこれほど稀有な環境はありません。UAE連邦内閣は<strong>2015年、すべての公立学校で柔術を必修化</strong>しました。ドバイのクラウンプリンスは柔術黒帯を持ち、自らこの政策を率いています。<strong>AJP World Pro</strong>はアブダビを拠点に毎年開催され、Sheikh Mohammed bin Zayadが後援しています。<strong>UFCはFight Island 2020以来、ヤス島に恒久拠点を置いています。</strong>',
      'sec.04.body.p3': 'そしてこの都市は、すでに秋山様をご存じです。現役ファイターとしてではなく — ドバイは秋山様を<strong>レジェンド</strong>として知っています。シルバーヘアと<em>「Sexyama」</em>の人物像でMMA史上最も認知されたファイターの一人となった、Pride/UFC時代の柔道家。現在は：<strong>NetflixのPhysical 100</strong>、<strong>YouTubeチャンネル登録者198万人</strong>、ブランドファウンダー。韓国と日本の文化的な橋として、両国のディアスポラに慕われる存在。人々が自然とついていく<strong>リーダー</strong>であり、ドバイのプレミアム・フィットネス顧客が注目するまさにその種の人物です。',
      'sec.04.chart1.title': 'ドバイを発射台として — 3つの層',
      'sec.04.royal.h3': 'ロイヤルファミリーが鍛えるとき、<br/><em style="color:var(--olive-deep);">国全体が鍛える。</em>',
      'sec.04.royal.p1': '<strong>Sheikh Mohammed bin Zayed</strong>（UAE大統領・アブダビ統治者）は、2009年にAJP World Proをご自身で創設され、2015年にはUAEの全公立学校で柔術を必修化する勅令を発布されました。弟君の<strong>Sheikh Tahnoun bin Zayed Al Nahyan</strong>（アブダビ副統治者・国家安全保障顧問）はブラジリアン柔術の<strong>黒帯</strong>をお持ちで、首長国の<em>「柔術の父」</em>として広く知られ、連盟インフラをご自身で整備された方です。<strong>Sheikh Hamdan bin Mohammed</strong>（Fazza・ドバイクラウンプリンス）はアドベンチャースポーツとライフスタイル政策を率いられており、御子息の<strong>Sheikh Rashid</strong>と<strong>Sheikh Maktoum bin Hamdan</strong>は連盟レベルでBJJに取り組まれています。',
      'sec.04.royal.p2': 'アブダビとドバイ、支配一族の三世代がこのスポーツを実践し後援しています。国民の圧倒的な支持を持つロイヤルファミリーがこのスポーツを体現するこの国において、MMAはニッチではありません。最高の政治的指導者から子供たちへと受け継がれる、国家のアイデンティティそのものです。秋山様がされていることへの需要は、ただここにあるだけではありません。秋山様と同じことを実践するリーダーたちが、その需要をトップから牽引しているのです。',
      'sec.04.timeline.intro': 'ドバイがMMA市場になったのは、UFCが来てからではありません。UAEは20年をかけ、トップダウンでこの文化を意図的に築きました — SUNG1975が参入するインフラは、すでに整っています。',
      'sec.04.timeline.2009': '<strong>AJP World Pro</strong>がアブダビで発足。Sheikh Mohammed bin Zayadのフラッグシップ柔術大会として始まる。',
      'sec.04.timeline.2015': '<strong>UAEの公立学校で柔術が必修化</strong> — 連邦内閣勅令。すべてのエミラティの子供が、グラップリングとともに育つことになる。',
      'sec.04.timeline.2020': '<strong>UFC Fight Island</strong>がヤス島で開催。UFCの中東恒久拠点となる。',
      'sec.04.timeline.2025': '<strong>UAE Warriors</strong>が年9大会を運営。ドバイクラウンプリンス（BJJ黒帯）が政策をトップから推進。',
      'sec.04.timeline.2026': '<strong>SUNG1975、参入。</strong> まさにそのために自らを築いてきた都市へ、MMAクレディビリティブランドが踏み込む。',
      'sec.04.chart.src': 'Dubai DET 2024訪問者レポート · エミレーツ飛行半径資料 · AJP / UAE Warriorsプレス · UAE内閣2015年BJJ義務教育令 · Dubai Media Office · <span style="color:var(--olive-deep);">スナップショット · 2026-05-18</span>',

      // ── §04.5 market the UAE is still building ─────────────────────
      'sec.04-5.hero.h': '毎年、10万人を超えるエミラティの子供たちが畳の上にいます。5歳から、ずっと。',
      'sec.04-5.hero.sub': 'アブダビが2008年にプログラムを開始。連邦内閣が2015年に全国へ展開。UAEの公立学校に通うすべての生徒が、教育期間を通じてグラップリングに取り組みます。',
      'sec.04-5.stat1.body': '小学校から高校まで、すべてのエミラティの子供がグラップリングを続けます。このパイプラインは止まりません。',
      'sec.04-5.stat2.body': 'グラップリング文化の中で育った一世代のエミラティが、いま大人になり、親になり、購買者になっています。',
      'sec.04-5.stat3.body': '全7首長国の連盟認定成人アカデミー — 7万人を超えるアクティブな競技者。',
      'sec.04-5.stat4.body': '格闘技スポーツへの参加者数と視聴者数がともに、前年比で二桁の成長を続けています。',
      'sec.04-5.takeaway': '秋山様 — UAEでSUNG1975が必要とするすべての顧客は、国家の費用で、秋山様のされていることを大切にするよう、すでに育てられています。',
      'sec.04-5.src': '◦ 出典：UAE内閣2015年BJJ義務教育令 · UAEJJF連盟資料 · UAE教育省 · Khaleej Times / The National報道 · 業界推計。<span style="color:var(--olive-deep);">スナップショット · 2026-05-18。</span>最終数値は進行中のディープリサーチで確定。',

      // ── §04.6 who they are ──────────────────────────────────────────
      'sec.04-6.label': '04.6 — 顧客像 · エンゲージドコホートの実態',
      'sec.04-6.h2': 'オーディエンスはすでに、ここに住んでいます。<br/><em>数字で見るとこうなります。</em>',
      'sec.04-6.hero.eyebrow': 'UAE在住成人 · フィットネス＋格闘技エンゲージ層 · 2026年',
      'sec.04-6.hero.sub': '20〜50歳のUAE在住者で、積極的にトレーニングし、格闘技イベントに参加し、プレミアムフィットネスウェアラブルを所有している層。これがSUNG1975のファーストサークル市場です。',
      'sec.04-6.bd.label': '100万人の内訳 · コホート別',
      'sec.04-6.bd.c1.lbl': 'アクティブなジム会員',
      'sec.04-6.bd.c1.body': 'GymNation、Warehouse Gym、Fitness First、F45、Barry\'s、Symmetry、Crank。79%が週2回以上トレーニングしています。',
      'sec.04-6.bd.c2.lbl': 'BJJ・グラップリング成人',
      'sec.04-6.bd.c2.body': 'UAEJJF公認＋カジュアル実践者。連盟登録7万人＋未登録推計8万人。',
      'sec.04-6.bd.c3.lbl': 'UFC・MMAファン · UAE',
      'sec.04-6.bd.c3.body': 'UFC 321はエティハド・アリーナで13,220席を完売。オンラインエンゲージメントはライブ動員の5〜8倍。',
      'sec.04-6.bd.c4.lbl': 'CrossFit・ファンクショナル・HIIT',
      'sec.04-6.bd.c4.body': 'UAE全土のボックス会員。ブランドへの親和性が高く、アパレル支出も多い層（Nike→CrossFit Reebokと同じプレイブック）。',
      'sec.04-6.bd.c5.lbl': 'ボクシング・ムエタイ・K1',
      'sec.04-6.bd.c5.body': '専門アカデミー＋商業ジムで取り組む打撃系競技者。MMA視聴者との重なりが大きい。',
      'sec.04-6.behav.label': '行動データ · GymNation UAE+KSA調査 2026',
      'sec.04-6.behav.s1': '週2回以上トレーニング — OECDメジアン（35%）を大きく上回る',
      'sec.04-6.behav.s2': 'フィットネスウェアラブルを毎日使用（Apple Watch、Whoop、Garmin）',
      'sec.04-6.behav.s3': '過去12ヶ月でフィットネス支出が増加',
      'sec.04-6.behav.s4': 'その増加分のうち<strong>アパレル＋アクセサリー</strong>が占める割合 — SUNG1975が置かれる棚そのものです',
      'sec.04-6.gcc.lbl1': 'UAEの外へ · GCCという広がり',
      'sec.04-6.gcc.b1': 'フィットネス＋格闘技に関わるGCC成人。サウジビジョン2030が女性のジム参加率を2023年以来40〜45% CAGRで押し上げ。リヤドはボリュームの場、ドバイはプレミアムの場。',
      'sec.04-6.gcc.lbl2': 'SUNG1975にとって何を意味するか',
      'sec.04-6.gcc.b2': 'まずUAEで実績を積む — 検証済みのリテール、プレミアムなオーディエンス、英語＋アラビア語メディアへのリーチ。次にサウジ、ボリュームはそこにある。そしてGCC全域へ。',
      'sec.04-6.src': '◦ 出典：UAE統計局人口内訳 · UAEJJF 2025連盟レポート · GymNation UAE+KSAヘルス&フィットネスレポート2026（11万人調査） · UFC Abu Dhabi 2025動員数 · UFC MENAビューアーパネル · Statista / Deep Market Insightsアスレジャーレポート2026 · 業界推計。<span style="color:var(--olive-deep);">スナップショット · 2026-05-28。</span>最終数値は進行中のディープリサーチで確定。',

      // ── §04.7 five percent ─────────────────────────────────────────
      'sec.04-7.body.p1': '4つのコホート。4つのシナリオ。それぞれのカードが同じ問いを立てます — この層の<strong>5%</strong>は、年間売上でどれくらいになるか。保守的なARPUで。2年目をベースラインとして。',
      'sec.04-7.cardA.tag': 'コホートA · UAE BJJ卒業生＋家族',
      'sec.04-7.cardA.body': '60万人がアドレサブル — グラップリングとともに育った成人と、その保護者。',
      'sec.04-7.cardB.tag': 'コホートB · UAE MMA＋プレミアムフィットネス成人',
      'sec.04-7.cardB.body': '100万人がアドレサブル — UFCファン、BJJ成人、プレミアムジム会員。',
      'sec.04-7.cardC.tag': 'コホートC · GCC MMAエンゲージ・オーディエンス',
      'sec.04-7.cardC.body': '500万人がアドレサブル — サウジアラビア、クウェート、カタール、バーレーン、オマーン。',
      'sec.04-7.cardD.tag': 'コホートD · ドバイ・スポーツ観光客＋グローバルファン',
      'sec.04-7.cardD.body': '200万人がアドレサブル — MMAに関心を持つ訪問者＋秋山様の世界のファン。',
      'sec.04-7.scen1.label': '保守的シナリオ · ブレンドキャプチャ1%',
      'sec.04-7.scen1.sub': '≈ $9M USD · 妥当な2年目の水準',
      'sec.04-7.scen2.label': 'ターゲットシナリオ · ブレンドキャプチャ5%',
      'sec.04-7.scen3.label': 'ストレッチシナリオ · ブレンドキャプチャ10%',
      'sec.04-7.scen3.sub': '≈ $91M USD · カテゴリーリーダーとなった場合',
      'sec.04-7.hero.tag': 'ターゲットシナリオ · ブレンドキャプチャ5%',
      'sec.04-7.hero.sub': '≈ $45M USD · 年間売上 · 3〜4年目の到達レンジ',
      'sec.04-7.details.summary': '▾ この数字の内訳 — 4つのコホート別',
      'sec.04-7.details.src': '◦ 方向性シミュレーション。コホート規模：UAE内閣 · UAEJJF · Dubai DET 2024 · 業界推計。ARPUはALO / Lululemon / Vuori / TGMのUAE小売実勢でベンチマーク。<span style="color:var(--olive-deep);">スナップショット · 2026-05-18。</span>最終数値はPerplexity / Gemini / ChatGPTで進行中のディープリサーチで確定。',

      // ── §04.8 five-year trajectory ─────────────────────────────────
      'sec.04-8.label': '04.8 — 5年間の軌跡',
      'sec.04-8.h2': '1年目のAED 36Mから、<br/>5年目までに<em>累計AED 500M</em>へ。',
      'sec.04-8.body': 'ターゲットケース（5%キャプチャ）は、1年目に達成する数字ではありません。チャネルが軌道に乗り、カプセルサイクルを1回、Athlete Editionの波を1回、ファイトナイトのシーズンを3回積み上げた後、<strong>3〜4年目</strong>に到達する天井です。キャプチャシナリオ別の累計売上推移を以下に示します。',
      'sec.04-8.s1.lbl': '保守的 · 1%',
      'sec.04-8.s1.sub': '累計 · 5年 · 約$27M USD',
      'sec.04-8.s2.lbl': '現実的 · 3%',
      'sec.04-8.s2.sub': '累計 · 5年 · 約$79M USD',
      'sec.04-8.s3.lbl': 'ターゲット · 5%',
      'sec.04-8.s3.sub': '累計 · 5年 · 約$136M USD',
      'sec.04-8.s4.lbl': 'ストレッチ · 8%',
      'sec.04-8.s4.sub': '累計 · 5年 · 約$218M USD',
      'sec.04-8.src': '◦ カーブの前提：1年目＝定常状態ターゲットの約25%（チャネル立ち上がり）、2年目＝65%、3年目＝95%、4年目＝100%、5年目＝105%。ARPUはカテゴリー中央値（AED 350〜500）で固定。<span style="color:var(--olive-deep);">スナップショット · 2026-05-28。</span>',

      // ── §05 reference case ─────────────────────────────────────────
      'sec.05.body.p1': '2020年ドバイ発、<strong>Dominic Nowell-Barnes</strong>が創業。1点あたり$4を寄付するチャリタブル・メカニズムを持つプレミアム・アスレジャー。4年以内に5カ国13店舗（うちUAE 8店舗）、Knuru Capital・Turmeric Capital主導のSeries A $15Mを達成。2023年9月時点でAED 2,000万超を慈善団体へ寄付（135万点超の販売に相当）。',
      'sec.05.body.p2': 'Tシャツ小売AED 249〜299（$67〜81）。フーディAED 499〜599（$135〜163）。デザインはミニマル、モノクロ、アラビックグラフィックを用いたヒーローカプセル — SUNG1975自身の美学に隣接しています。<strong>ファウンダーは2025年5月に既存投資家に売却</strong>（2026年5月に公表）。新CEO Rania Masri El Khatibは高コストに終わった米国展開の失敗を受け、明示的にMENA優先への回帰を宣言しています。',
      'sec.05.body.p3': 'Giving Movementは、ドバイ発のブランドが外へ向けてスケールできることを証明しました。私どもは同じ構造を逆向きに使うことをご提案します — 東京・ソウル発のブランドが、ドバイを通じて世界の中心へスケールしていく。<strong>彼らの教訓が、私どもの羅針盤です。</strong>',
      'sec.05.pull': '「私たちが犯した過ちの一つは、米国へ行こうと言ったことでした。<br/>でも本当に、自分たちのフィールドをまだ掌握できていましたか？」<br/><span style="font-size:14px; color:var(--muted); font-style:normal; letter-spacing:.04em">— Rania Masri El Khatib、TGM CEO · 2026年1月31日</span>',
      'sec.05.hero1.h': 'ドバイ発がグローバルにスケールした場所。',
      'sec.05.hero1.sub': '2020年の単独DTCサイトから5年で5カ国13店舗へ。私どもが逆向きに辿る参照事例です。',

      // ── §06 online presence ────────────────────────────────────────
      'sec.06.body.p1': '秋山様はすでに、アジアのスポーツ・エンターテインメント界で最大規模かつ最もエンゲージメントの高いパーソナル・オーディエンスの一つをお持ちです — InstagramとYouTube合わせて<strong>286万人</strong>、エンゲージメント率はメガインフルエンサーの中央値の<strong>14倍</strong>。秋山様のワークアウト動画を、みんな観ます。Physical 100のクリップを、みんな観ます。SUNG1975の瞬間も、私どもが届ければ、必ず観ます。',
      'sec.06.body.p2': 'しかし今、そのオーディエンスはブランドとほとんど繋がっていません。<strong>@sung1975_krと@sung1975_japanの合計は23,172フォロワー</strong> — 秋山様の声とブランドの声の間には、<strong>38倍のギャップ</strong>があります。これは欠陥ではありません。まだ点火されていない、弾薬満載の発射台です。',
      'sec.06.body.p3': '1年目にドバイで展開するすべてのアクティベーション — Dubai Muscle Showのブース、Forgeのセミナーツアー、Sheikh Zayed Roadのビルボード、アラビア書道カプセル、ファイトナイトのフロアウォーク — そのすべてが、秋山様の既存チャンネルへコンテンツとして直接流れ込みます。<strong>286万人が、その瞬間それぞれを観ます。</strong>ドバイがステージに。秋山様のチャンネルが放送局に。SUNG1975が、そのすべてを通じて秋山様が身につけるブランドになります。',
      'sec.06.body.p4': 'これがこのベンチャーの商業的な仕組みの全体です：<strong>ドバイ ＋ 秋山様 × 既存リーチ ＝ グローバル乗数。</strong>ドバイのアスレジャー棚に並ぶ他のどのファウンダーも、これほどのオーディエンスに接続できる状況にありません。',
      'sec.06.chart1.title': 'Day 1から使えるオーディエンス',
      'sec.06.multiplier.title': '乗数が動く仕組み',
      'sec.06.media.h3': '秋山様が東京で収録し、ドバイに降り立ちます。<em style="color:var(--olive-deep);">Dubai Muscle Showのフロアを歩きます。</em>',
      'sec.06.media.sub': 'ローンチの瞬間に、有料メディアは必要ありません。ブランドは東京で秋山様ご自身のポッドキャストで事前告知し、着陸後はドバイ最大の英語アンカーと繋がります。3つのアーンドメディア、1回の渡航 — 7日以内に286万人＋ドバイ最大の週間ラジオ＋Netflixのオーディエンス全員に届きます。',
      'sec.06.card1.h': 'UAEローンチを事前に告知する',
      'sec.06.card1.body': '秋山様がご自身のYouTubeチャンネルで収録します — 2024年11月以来<strong>登録者198万人</strong>に成長したチャンネルです。日常の1エピソードが<strong>1,000万回超再生。</strong>費用ゼロ。ご自身のオーディエンスが、最初に聞きます。',
      'sec.06.card2.h': '合同ワークアウトリール ＋ One on One収録 ＋ IGテイクオーバー',
      'sec.06.card2.body': 'Kris Fade — <strong>Virgin Radio Dubai朝の番組ホスト</strong>、自身のポッドキャストホスト、<strong>Netflixの<em>Dubai Bling</em>のメインキャスト。</strong><strong>温かいコネクションがあります。</strong>決め手はフィットネス層です：Fadeは自らのトランスフォーメーションをチャンネルで公開してきました — 秋山様との間にしかないオーディエンスの重なりです。Warehouse Gym（§06.5参照）で一緒にトレーニングし、ポッドキャストに同席させ、FadeがSUNG1975を画面全体に映しながら秋山様をドバイ中でホストします。',
      'sec.06.card3.h': 'ファウンダーがブースに立つ',
      'sec.06.card3.body': '<strong>来場者45,000人</strong> · フィットネス＆ライフスタイルのオーディエンス。秋山様がSUNG1975のブースでサインします。来場者全員が撮影します。クリップは、3日前に旅程を告知した198万人チャンネルへ直接流れ込み、ループが閉じます。',

      // ── §06.5 warehouse gym ────────────────────────────────────────
      'sec.06-5.body.p1': 'Warehouse Gymは、ドバイのフィットネスメディアが特集するジムです。2拠点がその建築で<em>Dezeen</em>と<em>Wallpaper*</em>に掲載されています。会員はAED 600〜1,200/月を支払います — AED 250〜600のアスレジャーを購買するまさにその世帯層です。私どもは温かいコネクションを持っています。最初のミーティングは私どもがセットします。',
      'sec.06-5.body.p2': '<strong>すでに適切な価格帯にいるプレミアム・オーディエンス。</strong>Warehouse Gymの会員はAED 600〜1,200/月の会費を支払います — AED 250〜600のアスレジャーを購買する世帯層と完全に一致します。毎日フロアでパフォーマンスブランドを着用しています。このポップアップはSUNG1975の価格帯を<em>紹介</em>する必要がありません — 顧客はすでにその価格帯の中にいます。',
      'sec.06-5.body.p3': '<strong>ブランドの美学に合うデザインの系譜。</strong>Springs拠点が<em>Dezeen</em>（VSHD Design）に、Dubai Design District拠点が<em>Wallpaper*</em>に掲載されました。インダストリアル・ラグジュアリーなコンクリート＋テラコッタ＋ブラス — SUNG1975の侘び寂びのトーンに隣接する美学です。ここでのポップアップは、キュレートされたコラボとして読まれます。キオスクとは一線を画します。',
      'sec.06-5.body.p4': '<strong>8拠点、8つのデモグラフィック圏。</strong>まず1拠点を選び、さらに2拠点へ広げます。DIFCはホワイトカラー向け。Springs / ジュメイラパークはビラ家族向け。Yas Bayはアブダビへのリーチのため。Al Quozはデザインディストリクト・フィットネス向け。<strong>温かいイントロ一本で、すべてをカバーできます。</strong>',
      'sec.06-5.formats.h3': '会場レンタルではありません。<em style="color:var(--olive-deep);">キュレートされたアクティベーション・カレンダーです。</em>',
      'sec.06-5.honesty.h': '温かいコネクションがあります。<em style="color:var(--olive-deep);">最初のミーティングは私どもがセットします。</em>',
      'sec.06-5.honesty.p': '現状：Warehouse Gymリーダーシップとの温かい実務コネクションがあります。<strong>最初のミーティングで合意すべきこと：</strong>フラッグシップ拠点の選定 · アクティベーション・カレンダー · カプセルドロップの収益配分 · 独占期間。私どもがアイデアを持ち込みます — 先方は話を聞く姿勢があります。<strong>このデッキでのコミットメントは、この会話が最初の30日以内に行われることであり、契約がすでに署名されていることではありません。</strong>',

      // ── §06.6 launch moment ────────────────────────────────────────
      'sec.06-6.body.p1': '秋山様がドバイに降り立ったとき、ブランドにはその到着をバイラルな出来事に変えるドバイネイティブのメディアの声が必要です。適任者は一人、明確にいます — そして決め手はNetflixの重なりだけではありません。Fadeが何年もかけて静かに築いてきたフィットネス層です。',
      'sec.06-6.body.p2': '<strong>Kris Fade</strong>はVirgin Radio Dubaiの朝の番組ホスト（UAE最大の英語モーニングショー）、<em>One on One with Kris Fade</em>（対談ポッドキャスト）の制作者・ホスト、そして<strong>Netflixの<em>Dubai Bling</em>のメインキャスト</strong>です。<strong>私どもには温かいコネクションがあります。</strong>',
      'sec.06-6.body.p3': '決め手は<strong>フィットネス層</strong>です：Fadeは自身のブランド<strong>Fade Fit</strong>（@fadefit · Kite Beachでの週次ランクラブ · 複数年にわたる公開トランスフォーメーション · 全チャンネルでのジムコンテンツ・トレーニングルーティン）を運営しています。彼のオーディエンスは彼を<em>本物のフィットネス・エンゲージ・パーソナリティ</em>として認識しています。単なるエンターテイナーではないのです。',
      'sec.06-6.body.p4': 'ドバイの他のメディアは、秋山様をセレブのカーペットに乗せます。<strong>Fadeは秋山様をジムに連れていきます。</strong>オーディエンスの重なりは際立って精確です：Fadeのリスナー＋<em>Dubai Bling</em>ビューワー＋ポッドキャストサブスクライバーは、<em>Physical: 100</em>で秋山様をすでに知っていた、同じ英語圏の在外・GCCコホートです。実際の肉体的偉業を成し遂げる人々のエンターテインメントという同じ棚に並ぶ、2人のNetflixアンカー・パーソナリティ。',
      'sec.06-6.closer.h': '1回の渡航。3つのソーシャルファーストのアーンドメディア。<em style="color:var(--accent);">有料費用ゼロ。</em>',
      'sec.06-6.closer.p': 'ドバイのアスレジャー棚のどの競合もこれを模倣できません。Giving Movement、lululemon、Gymshark — ドバイのラジオホストから、Netflixのオーディエンスから、286万人のパーソナルチャンネルまで、認知のトリガーとなるファウンダーの顔を持つブランドは一つもありません。',
      'sec.06-6.hero.h': '秋山様 × Kris Fade — 合同ワークアウトリール、Warehouse Gymにて。',
      'sec.06-6.hero.sub': '1回の渡航。1本のアセットを2人のチャンネルへ。秋山様の286万フォロワー＋Virgin Radio Dubai＋Dubai Bling Netflixビューワー、ひとつの画面の中に。',
      'sec.06-6.lang-note': '◦ 言語について · 秋山様は日本語・韓国語のネイティブスピーカーです（英語は使いません）。Kris Fadeとのコンテンツはすべて、初日から日本語・韓国語の字幕を同期させて制作します。合同ワークアウトリールとポッドキャストには通訳を同席させ、秋山様が終始日本語または韓国語でお話しいただけるよう、事前にスクリプトを準備します。',

      // ── §07 same shelf different story ────────────────────────────
      'sec.07.body.p1': 'SUNG1975はすでに日本において、ドバイのアスレジャー・プレミアム帯のど真ん中の価格で販売されています。<strong>私どもは顧客に新しい価格帯を発見させようとしているのではありません。</strong>顧客がすでに購買している価格帯の中で、新しい名前を発見させようとしているのです。そしてその棚に並ぶどのブランドも、SUNG1975の物語は持っていません。',
      'sec.07.anchors.title': 'この棚の他のどのブランドも主張できない、3つのアンカー',

      // ── §08 who we are ─────────────────────────────────────────────
      'sec.08.body.p1': '秋山様には、このマーケットで出荷する方法も東京とのコミュニケーション方法も、すでに熟知しているパートナーが必要です。ご一緒いただくチームとは、まさにそのようなチームです。',

      // ── §09 why us ────────────────────────────────────────────────
      'sec.09.body.p1': '<strong>Balraj Singh Kalra</strong> · ドバイ在住5年 · ドバイのプレミアム・ライフスタイルおよびリアルエステート・ベンチャーにわたる現役オペレーター · UAEオペレーション、フルフィルメント・インフラ、自社物流・梱包。',
      'sec.09.body.p2': '<strong>山田さん</strong> · ドバイ在住5年 · <strong>Portgate</strong>（portgg.com）代表 · 元CyberAgentグループ · Portgateは2022年以来、4名のドバイチームで<strong>40社超の日系企業</strong>のUAE進出を支援してきました。また、現役MMA競技者として格闘技イベントの共同主催も行っています。',
      'sec.09.body.p3': '<strong>PortgateがすべてをエンドツーエンドでHandleします</strong> — UAE法人設立、銀行口座、商標、ビザ、マーケティング、物流、フルフィルメント。秋山様にご署名いただく書類はゼロです。一つのオペレーター、一つの責任窓口、ドバイに日本語対応チーム。',
      'sec.09.body.p4': '私どもがお願いするのは、資金ではありません。ご承諾と、アクティベーションの際に年2〜3回ドバイにお越しいただくこと、それだけです。',
      'sec.09.mansoor.who': '<strong>Mansoor</strong>は格闘技とプレミアムリテールの両方に片足を置く、長年のドバイ・オペレーターです。ローンチフェーズのアドバイザーとして参画いただくことで合意しました — 私どもが彼のネットワークを広げ、彼が私どものドアを開きます。<span style="color:var(--muted);">書面でのお名前掲載よりも、直接ご紹介する形を取っています。</span>',
      'sec.09.mansoor.combat': 'MansoorはThe Forge Gym × Roger Gracie Dubai Academyを所有・運営しています — Roger GracieはBJJの王族です。彼を通じて、MMAイベントのブース設置、BJJ連盟ネットワーク、共同主催セミナーへの温かいコネクションが得られます。',
      'sec.09.mansoor.airport': 'Mansoorは<strong>@power at DXB Duty Free</strong>（ドバイ最大の空港免税店の単独運営）を手がけています。これはフェーズ3のカプセル配置に向けた温かい会話につながります — Giving Movementの観光客向け販売を牽引してきたのと同じチャネルです。',
      'sec.09.mansoor.launch': '<strong>Dubai Muscle Show — 来場者45,000人。</strong>Mansoorは主催者と個人的に面識があり、ブース交渉のご紹介を申し出てくれています。これが私どもの推奨するフェーズ1ローンチイベントです。',
      'sec.09.pull': '「私どもはドアを開きます。<br/>成果を約束するのではなく — 勝ち取ります。」',

      // ── §10 MMA × Dubai overlap ────────────────────────────────────
      'sec.10.body.p1': 'UFC Fight Island以来、ドバイとアブダビはグローバルなファイトカレンダーの恒久的な拠点となっています。しかしこのローンチで本当に重要な関係性は、MMAプロモーションではなく<strong>BJJ連盟</strong>です。アドバイザーのMansoorのネットワークを通じ、連盟レベルの<strong>AJP（Abu Dhabi Jiu-Jitsu Pro）</strong>と<strong>UAEJJF（UAE Jiu-Jitsu Federation）</strong>、そしてUAEのすべてのBJJアカデミーへの道が開かれます。柔道家として、その後にMMAファイターとして — 秋山様にとって、これは文化的に一致したルートです。',
      'sec.10.body.p2': 'そして<strong>Dubai Muscle Show</strong> — 来場者45,000人、フィットネス＆ライフスタイルのオーディエンス。Mansoorは主催者と個人的に面識があり、ブース交渉のご紹介を申し出てくれています。<strong>これが私どもの推奨するローンチイベントです。</strong>国内のどのUFCカードよりも大きな集客で、アスレジャーに最も適したオーディエンスが揃っています。',
      'sec.10.body.p3': '1年目のプラン：Dubai Muscle Showをアンカー・ローンチとして · AJPカプセルを文化的コ・クリエイトとして · UAE全BJJアカデミーにわたる秋山様主導の投げ技セミナーツアー（費用ゼロ、グラップリングコミュニティ全体にアーンドメディアを生成） · UAEWまたはUFCのシグネチャーカードへの1ブース出展と、秋山様自身のフロアウォーク。',
      'sec.10.bb.eyebrow': 'ビルボード展開 — イメージ',
      'sec.10.bb.1.lbl': 'Sheikh Zayed Road · 夜',
      'sec.10.bb.1.body': '1年目のアンカービルボード。この都市の大動脈の上に、秋山様のお顔を。',
      'sec.10.bb.2.lbl': 'Burj Khalifa · LEDファサード',
      'sec.10.bb.2.body': 'カプセルドロップ週のアクティベーション — 世界一高いビルが、秋山様のキャンペーンをまとう。',
      'sec.10.bb.3.lbl': 'Mall of the Emirates · コンコース',
      'sec.10.bb.3.body': 'カプセルローンチのバナーをMoEの中に — アスレジャーを買う人が必ず通る道。',
      'sec.10.bb.src': '◦ コンセプトレンダー。最終的な掲出場所とクリエイティブは、秋山様とともに制作前に検討します。',

      // ── §11 phase plan ────────────────────────────────────────────
      'sec.11.ph1.title': 'チャネルを開く',
      'sec.11.ph2.title': 'ローンチを確定させる',
      'sec.11.ph3.title': 'この都市で存在感を確立する',
      'sec.11.ph4.title': '自分たちの足で立つ',

      // ── §11.5 revenue channels ────────────────────────────────────
      'sec.11-5.label': '11.5 — 売上が入ってくる6つの経路',
      'sec.11-5.h2': '6つの収益チャネル。<br/><em>定常状態での最適なミックス。</em>',
      'sec.11-5.body': '定常状態（3年目以降）の売上は6つのチャネルに分散します — それぞれ異なる利益率、マーケティングコスト、在庫回転を持ちます。最も転換率の高いチャネルに投資を集中させますが、以下のミックスを計画の基準とします。',
      'sec.11-5.chart.eyebrow': '定常状態のチャネルミックス · 売上比率',
      'sec.11-5.c1.lbl': 'DTC · .ae Eコマース',
      'sec.11-5.c1.body': '最高利益率 · 常時稼働 · ブランドが持つオウンドオーディエンス。法人設立の月1から立ち上げます。',
      'sec.11-5.c2.lbl': '空港リテール · DXBデューティーフリー',
      'sec.11-5.c2.body': '2025年に9,520万人が利用。プレミアム・インパルスバイヤー。旅行ギフト向け限定SKU構成 — 2年目以降。',
      'sec.11-5.c3.lbl': 'ジム・ポップアップ · Warehouse Gym',
      'sec.11-5.c3.body': '高意欲のフィットネス層。Warehouse Gymの8拠点をローテーション。プレミアム会員とのクロスオーバー。',
      'sec.11-5.c4.lbl': 'MMA・ファイトナイト・ブース',
      'sec.11-5.c4.body': 'AJP World Pro · Dubai Muscle Show · UAE Warriors。集中したプレミアム動員。ブランドを定義するチャネル。',
      'sec.11-5.c5.lbl': 'Athlete Edition · 招待制',
      'sec.11-5.c5.body': '意図的に低ボリューム。残り95%のためのシグナル発信源。§13.5をご参照ください。',
      'sec.11-5.c6.lbl': 'ホールセール · 厳選のみ',
      'sec.11-5.c6.body': '選定したリテールのみ — Areej、Bloomingdale\'s、THAT Concept Store。ボリュームよりもブランド保護を優先。',
      'sec.11-5.src': '◦ 定常状態ミックスはALO / Lululemon / Gymshark / Giving MovementのUAEチャネル構造＋ChatGPTディープリサーチ推奨をベンチマーク。1年目は他チャネルが立ち上がる前のため、DTCに大きく偏ります（約70%）。<span style="color:var(--olive-deep);">スナップショット · 2026-05-28。</span>',

      // ── §12 activation calendar ────────────────────────────────────
      'sec.12.body.p1': 'フェーズ計画は、全体の流れを示すものでした。これは戦術的なリズムです。1年目のすべての現地アクティベーションを、時期と効果、そして実現のために秋山様にどの程度のご関与が必要かとともに、設計しました。',
      'sec.12.q1.title': 'ソフトローンチ ＆ 最初の人波',
      'sec.12.q2.title': 'グラップリングコミュニティに根を張る',
      'sec.12.q3.title': 'フィジカルリテールの橋頭堡を築く',
      'sec.12.q4.title': 'スケール ＆ GCCへの橋',

      // ── §13 capsule ───────────────────────────────────────────────
      'sec.13.hero.h': 'ファウンダーが、カプセルを着る。最初の着用者が、常に最も重要な着用者です。',
      'sec.13.body.p1': 'このマーケットで成功したすべてのプレミアム・ブランドが、UAEコードのカプセルをドロップしています。<strong>Nike</strong>はドバイモール旗艦店のアラビック・ジオメトリック・タイポグラフィに、エジプト人アーティストのMohamed Samirを起用しました — <em>#weplaydxb</em>キャンペーンのアンカーとして。<strong>Gymshark</strong>は初の海外恒久店舗（ドバイモール、2025年1月）のオープニングに、レバノン系カナダ人インフルエンサーのLeana Deebとのアラビア書道カプセルをコ・クリエイトしました。<strong>Louis Vuitton × Nada Debs</strong>「LV Mirage」はマシュラビーヤ模様と砂丘にインスパイアされたモチーフを使いました。Giving Movementは「Born in Dubai」グラフィックラインを継続的に展開しています。',
      'sec.13.body.p2': 'このパターンは証明済みで、この市場に根付いています。毎年SUNG1975 × UAEカプセルをドロップすることをご提案します。2〜4点。SUNG1975の既存シルエットに手を加えず、単色のアラビック・タイポグラフィを乗せる。空港、旗艦店、オンラインでのみ販売 — ホールセールはなし。',
      'sec.13.body.p3': '文化的な敬意は、交渉の余地がありません。書道はUAEを拠点とするアラビア書家にクレジット付きで発注し、制作前に双方がレビューします。<strong>以下のモックアップはAI生成のコンセプトであり、最終デザインではありません。</strong>',
      'sec.13.pull': '「アラビア書道を、世界の主要ブランドの店舗に見られるコートラインや<br/>ジオメトリックパターンとして扱ってください。」<br/><span style="font-size:14px; color:var(--muted); font-style:normal; letter-spacing:.04em">— Mohamed Samir、Nike Dubaiタイポグラファー（TypeRoom）</span>',

      // ── §13.5 athlete edition ──────────────────────────────────────
      'sec.13-5.label': '13.5 — Athlete Edition · 招待制',
      'sec.13-5.h2': 'ファイターだけが買えるカプセル。<br/><em>SUNG1975のRed Bullムーブ。</em>',
      'sec.13-5.intro.eyebrow': 'ブランドの規律',
      'sec.13-5.intro.body': '最初の認定アスリート着用者は、秋山様ご自身です。そこから広がっていく — ただし、認証を通じてのみ。取引だけでは、手に入りません。',
      'sec.13-5.hero.eyebrow': 'ブランドの規律 · Red Bullから借りたアイデア',
      'sec.13-5.hero.body': 'Red Bullのロゴはアスリートに贈られます — 誰でも買えるものではありません。認定された競技者だけが着用できます。街で見かけたとき、そのパッチが意味するのは：<em style="color:var(--accent); font-style:italic;">この人は、実際に戦っている。</em>',
      'sec.13-5.hero.cta': '私どもはSUNG1975に同じ規律を提案します。年に1つのカプセルラインを、認定された格闘技・フィジーク競技者のみに販売します。それ以外は、購入できません。例外なし。',
      'sec.13-5.who.label': '購入資格者',
      'sec.13-5.who.list': '<li style="margin-bottom:10px;"><span style="color:var(--olive-deep);">▸</span> <strong>BJJ黒帯</strong>（UAEJJF登録）</li><li style="margin-bottom:10px;"><span style="color:var(--olive-deep);">▸</span> <strong>AJP World Proメダリスト</strong>（直近24ヶ月）</li><li style="margin-bottom:10px;"><span style="color:var(--olive-deep);">▸</span> <strong>UAE Warriors / UFC / PFL</strong>現役ロスター</li><li style="margin-bottom:10px;"><span style="color:var(--olive-deep);">▸</span> <strong>Dubai Muscle Show</strong>上位3位入賞者</li><li><span style="color:var(--olive-deep);">▸</span> 既存着用者からの招待（2年目以降）</li>',
      'sec.13-5.who.foot': 'すべて、販売時点で連盟IDと写真により認証。認証なくして販売なし。',
      'sec.13-5.what.label': '着用者が得るもの',
      'sec.13-5.what.list': '<li style="margin-bottom:10px;"><span style="color:var(--olive-deep);">✦</span> アスリート専用カラーウェイ（他では購入不可）</li><li style="margin-bottom:10px;"><span style="color:var(--olive-deep);">✦</span> 胸に<strong>「AE」刺繍パッチ</strong> — 連盟コード入り</li><li style="margin-bottom:10px;"><span style="color:var(--olive-deep);">✦</span> 首元の内側タグに個人名＋競技名</li><li style="margin-bottom:10px;"><span style="color:var(--olive-deep);">✦</span> 一般公開より48時間早いカプセルドロップへのアクセス</li><li><span style="color:var(--olive-deep);">✦</span> SUNG主催のプライベート・トレーニングセッションへの招待</li>',
      'sec.13-5.what.foot': '価格：通常リテール。割引なし。希少性そのものが価値であり、特典として安売りするものではありません。',
      'sec.13-5.brand.label': 'ブランドが得るもの',
      'sec.13-5.brand.list': '<li style="margin-bottom:10px;"><span style="color:var(--accent);">→</span> <strong>獲得した社会的証明</strong> — 街で目に見えるかたちで</li><li style="margin-bottom:10px;"><span style="color:var(--accent);">→</span> 手動のゲーティングなしで在庫をコントロール</li><li style="margin-bottom:10px;"><span style="color:var(--accent);">→</span> プレスストーリー：「ファイターしか買えないブランド」</li><li style="margin-bottom:10px;"><span style="color:var(--accent);">→</span> 認証フローを通じた連盟パートナーシップの確立</li><li><span style="color:var(--accent);">→</span> メインのコマーシャルラインへのアスピレーショナルな引力</li>',
      'sec.13-5.brand.foot': '「この人は戦っている」— 20メートル先からでも伝わる。',
      'sec.13-5.cohort.label': '1年目のアドレサブル・アスリートコホート · UAE在住者のみ',
      'sec.13-5.cohort.c1': 'BJJ黒帯 · UAEJJF',
      'sec.13-5.cohort.c2': 'AJPメダリスト · 直近24ヶ月',
      'sec.13-5.cohort.c3': 'UAEW / UFC / PFL現役ロスター · UAE在住',
      'sec.13-5.cohort.c4': 'Muscle Show上位3位＋UAEボディビル連盟',
      'sec.13-5.cohort.total': '1年目のアドレサブル総数：<strong style="color:var(--olive-deep);">UAE在住認定アスリート約5,750人。</strong>30%転換率 × AED 800平均バスケット ＝ <strong>このカプセル単体でAED 138万の売上。</strong>ボリュームは小さい。しかし発信するシグナルは、巨大です。',
      'sec.13-5.closer': '2年目以降、現着用者からの招待がなければ非アスリートはSUNG Athlete Editionを購入できません。ブランドは円になります。その円が、マーケティングになります。',

      // ── §14 pricing ───────────────────────────────────────────────
      'sec.14.body.p1': '新しい価格帯を作る必要はありません。日本ストアの小売りをそのままベースに、AED価格をプレミアム・アスレジャーの標準的なラウンド数値に設定することをご提案します。',

      // ── §15 structure ─────────────────────────────────────────────
      'sec.15.hero.h': 'テープカットは秋山様が。会社のオーナーも秋山様です。私どもはただ、運営を担います。',
      'sec.15.body.p1': 'シンプルな構造です。<strong>秋山様がSUNG1975 Arabiaの100%を保有します。</strong><strong>Portgateが基本報酬＋利益シェアの契約ですべてをエンドツーエンドで運営します</strong> — 秋山様側に株式の希薄化も日常業務の負担もなく、パフォーマンスリスクはオペレーター側が負います。',
      'sec.15.asym.eyebrow': '非対称な提案 — 一枚でわかる',
      'sec.15.asym.you.label': '秋山様',
      'sec.15.asym.you.headline': 'ゼロ。',
      'sec.15.asym.you.sub': '資金 · 運営負担 · ご署名',
      'sec.15.asym.you.l1': '<span style="color:var(--accent);">✓</span> UAE+GCC独占ライセンス（ブランドのご許諾）',
      'sec.15.asym.you.l2': '<span style="color:var(--accent);">✓</span> クリエイティブ＋UAE限定カプセルへの最終承認',
      'sec.15.asym.you.l3': '<span style="color:var(--accent);">✓</span> 年2〜3回のドバイご来訪',
      'sec.15.asym.us.label': 'Portgate',
      'sec.15.asym.us.headline': 'すべて。',
      'sec.15.asym.us.sub': '資金 · リスク · 運営 · 法的責任',
      'sec.15.asym.us.l1': '<span style="color:var(--accent);">▸</span> 全運転資金＋UAE法人設立',
      'sec.15.asym.us.l2': '<span style="color:var(--accent);">▸</span> 4名のドバイチーム · 日本語対応 · エンドツーエンド',
      'sec.15.asym.us.l3': '<span style="color:var(--accent);">▸</span> 全運営リスク · マーケティング · 物流 · フルフィルメント',
      'sec.15.asym.us.l4': '<span style="color:var(--accent);">▸</span> パフォーマンスリスクは、オペレーター側が全面的に負います',
      'sec.15.asym.you.takes.label': '秋山様が受け取るもの',
      'sec.15.asym.you.takes': '100%の所有権 · ロイヤリティ収入 · 残余利益のすべて',
      'sec.15.asym.us.takes.label': 'Portgateが受け取るもの',
      'sec.15.asym.us.takes': '売上が立つまで、私どもは無報酬で動きます。売上が生まれたとき、初めて売上の20%を受け取ります。',
      'sec.15.flow.label': '資金フロー · ウォーターフォール',
      'sec.15-5.label': '15.5 — 主要条件 · タームシート協議に向けて',
      'sec.15-5.h2': '法的フレームワーク。<br/><em>合意すべき8つの条項。</em>',
      'sec.15.struct.summary': '<strong>秋山様がSUNG1975 Arabiaの100%のオーナー兼CEOです。</strong> <strong>Portgateは売上が立つまで無報酬で運営し、その後売上の20%を受け取ります</strong> — 秋山様がキャップテーブルを保持し、Portgateがパフォーマンスリスクを引き受け、秋山様の後に初めて報酬を得ます。',
      'sec.15.portgate.note': '<strong>Portgateについて。</strong>Portgate（portgg.com）は山田さんのドバイ運営会社です。2022年以来、4名のドバイチームで40社超の日系企業のUAE進出を支援してきました — フルスタック対応：法人設立、銀行口座、ビザ、商標、マーケティング、物流、フルフィルメント。一人の日本語対応オペレーターがすべてのワークフローをエンドツーエンドで管理します。秋山様にご署名いただく書類はゼロです。',

      // ── §16 skincare ─────────────────────────────────────────────
      'sec.16.body.p1': '秋山様とTWENTY FIFTY — 韓国のナノファイバー・コラーゲンブランド — とのコラボレーションは、私どもがこれまで見た中でこのマーケットに最も合致した製品の一つです。GCCのメンズグルーミング市場は<strong>$8.5B</strong>規模；UAE単体で<strong>$288M（2024年）→ $426.8M（2030年）</strong>へと年率6.75%で成長しています。UAE Kビューティーは別途<strong>$31.6M（2023年）→ $51.1M（2032年）</strong>へと拡大。そしてメンズKビューティーのグローバルセグメントは<strong>10.9%</strong>で複利成長 — Kビューティーのあらゆるスライスの中で最速です。',
      'sec.16.body.p2': '韓国スキンケアはGCCにおいて、ローカルオペレーターとのパートナーシップを通じてすでに実績を積んでいます。Laneigは2024年5月にARミラーを備えたドバイモール旗艦店をオープン。Beauty of Joseon、COSRX、SulwhasooはWatsons、Sephora ME、Boots、Bloomingdale\'sで流通中。JKOSMECは2025年10月にApparel Group＋Carrefour経由で参入。このモデルは機能します。',
      'sec.16.body.p3': 'セレブリティ・スキンケアの最も近い比較対象：<strong>Le Domaine（Brad Pitt × Famille Perrin）</strong>が2022年末にローンチ — クレンジングエマルジョン$80、セラム$385、クリーム$320。仏・英・伊・独・スイス・米国で流通；中東はThe Rite Store経由。意図的な「これはセレブリティブランドではない」というフレーミング — 秋山様のスキンケアラインをバニティプロジェクトではなく本物の製品として感じさせるための、そのままのプレイブックです。',
      'sec.16.pull': '「MMAのレジェンド · 韓国スキンケア · 湾岸のメンズグルーミング。<br/>この交点を、誰も所有していません。」',

      // ── §17 next steps ────────────────────────────────────────────
      'sec.17.hero.h': 'ドバイモール旗艦店で、最初の顧客を迎えます。東京で生まれたブランドが、湾岸で迎え入れられる瞬間。',
      'sec.17.w1.title': 'タームシート',
      'sec.17.w1.body': 'ハイレベルのタームシートを起草・署名します。独占期間を確定します。',
      'sec.17.w2.title': '法人＋ブランド登録',
      'sec.17.w2.body': 'UAE法人を設立します（メインランドまたはフリーゾーン — 秋山様とご相談の上決定）。UAE＋GCCでの商標を出願します。',
      'sec.17.w3.title': '初回コンテナ計画',
      'sec.17.w3.body': 'プレローンチの需要に合わせた初期在庫ミックスを設計します。秋山様の工場で生産スロットを確保します。',
      'sec.17.w4.title': 'Eコマース＋コンテンツのキックオフ',
      'sec.17.w4.body': 'UAE .aeサイトを構築します。バイリンガル・コンテンツエンジンを稼働させます。ソフトローンチの日程を設定します。'
    }"""

with open('/Users/a44/sung1975-uae-pitch/v1/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the jp block boundaries
start_marker = '    jp: {'
end_marker = '    }\n  };'

start_idx = content.find(start_marker)
# Find the closing }  }; after the jp block
end_idx = content.find(end_marker, start_idx)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: markers not found. start={start_idx}, end={end_idx}")
    exit(1)

end_idx_full = end_idx + len(end_marker)
old_block = content[start_idx:end_idx_full]

new_block = NEW_JP + '\n    }\n  };'

new_content = content[:start_idx] + new_block + content[end_idx_full:]

with open('/Users/a44/sung1975-uae-pitch/v1/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done. Replaced {len(old_block)} chars with {len(new_block)} chars.")
print(f"JP keys written: {new_block.count(chr(39))//2} approximate")
