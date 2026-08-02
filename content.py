# -*- coding: utf-8 -*-
"""Kurs içeriği: her modül bir zaman aralığı, teorik anlatım ve kısa bir quiz içerir."""

MODULES = [
    {
        "id": 1,
        "slug": "dogus",
        "years": "1943 – 1956",
        "title": "Yapay Zekânın Doğuşu",
        "intro": "Bir fikrin makineye dönüşmeye başladığı yıllar.",
        "body": [
            "Yapay zekâ fikri, bilgisayarlardan çok daha eski bir soruyla başlar: "
            "'Düşünme dediğimiz şey, aslında bir tür hesaplama mı?' 1943'te Warren "
            "McCulloch ve Walter Pitts, beyindeki nöronların basit açma-kapama "
            "mantık kapıları gibi çalışabileceğini gösteren matematiksel bir model "
            "yayımladı. Bu, yapay bir 'sinir hücresi' fikrinin ilk taslağıydı.",
            "1950 yılında Alan Turing, 'Computing Machinery and Intelligence' "
            "makalesinde ünlü soruyu sordu: 'Makineler düşünebilir mi?' Bu soruyu "
            "doğrudan cevaplamak yerine, bugün Turing Testi olarak bilinen pratik "
            "bir ölçüt önerdi: bir insan, karşısındaki bir makine mi yoksa insan mı "
            "olduğunu ayırt edemiyorsa, o makine 'düşünüyor' sayılabilir.",
            "Alanın resmî doğum günü ise 1956 yazıdır. John McCarthy, Marvin "
            "Minsky, Nathaniel Rochester ve Claude Shannon, Dartmouth College'da "
            "iki aylık bir çalıştay düzenledi ve ilk kez 'artificial intelligence' "
            "(yapay zekâ) terimini kullandılar. Çalıştayın önerisi oldukça "
            "iddialıydı: öğrenmenin ve zekânın her yönünün, prensipte, bir "
            "makinenin taklit edebileceği kadar kesin biçimde tarif edilebileceğini "
            "savunuyorlardı.",
            "Bu dönemde araştırmacılar iyimserdi; birkaç on yıl içinde makinelerin "
            "insan seviyesinde akıl yürüteceğini düşünüyorlardı. Ancak bu iyimserlik, "
            "ilerleyen bölümlerde göreceğimiz gibi, gerçeklikle sık sık çarpışacaktı.",
        ],
        "turkiye_notu": (
            "Türkiye'nin bilgisayarla tanışması da tam bu döneme denk gelir: "
            "ODTÜ, 1960'ta ülkenin ilk dijital bilgisayarı olan IBM 650'yi "
            "getirdi. Yani dünya 'makineler düşünebilir mi' sorusunu "
            "tartışırken, Türkiye'de de bilgisayar bilimi filizleniyordu."
        ),
        "quiz": [
            {
                "q": "Turing Testi'nin temel fikri nedir?",
                "options": [
                    "Bir makinenin saniyede kaç işlem yaptığını ölçmek",
                    "Bir insanın, konuştuğu tarafın insan mı makine mi olduğunu ayırt edip edemediğine bakmak",
                    "Bir makinenin satranç oynayıp oynayamadığını test etmek",
                    "Bir makinenin fiziksel görevleri yerine getirip getiremediğini ölçmek",
                ],
                "correct": 1,
            },
            {
                "q": "'Yapay zekâ' teriminin ilk kez kullanıldığı etkinlik neresidir?",
                "options": [
                    "MIT Yapay Zekâ Laboratuvarı",
                    "Bell Labs",
                    "Dartmouth College çalıştayı (1956)",
                    "Stanford Üniversitesi konferansı",
                ],
                "correct": 2,
            },
            {
                "q": "McCulloch ve Pitts'in 1943'teki modeli neyi taklit etmeye çalışıyordu?",
                "options": [
                    "Bir bilgisayarın belleğini",
                    "Beyindeki nöronların basit mantıksal çalışmasını",
                    "İnsan gözünün görme sistemini",
                    "Bir yazı makinesinin tuş dizilimini",
                ],
                "correct": 1,
            },
        ],
    },
    {
        "id": 2,
        "slug": "kislar",
        "years": "1957 – 1993",
        "title": "Yapay Zekâ Kışları ve Yeniden Doğuş",
        "intro": "Aşırı iyimserlikten hayal kırıklığına, oradan yeni bir umuda.",
        "body": [
            "1958'de Frank Rosenblatt, 'perceptron' adını verdiği ve basit "
            "örüntüleri tanıyabilen bir yapay sinir ağı geliştirdi. Basın bunu "
            "neredeyse bilinçli bir makine gibi sundu. Ama 1969'da Marvin Minsky "
            "ve Seymour Papert, 'Perceptrons' adlı kitaplarında bu tek katmanlı "
            "modelin XOR gibi çok basit bazı mantıksal problemleri bile "
            "çözemediğini matematiksel olarak gösterdi. Bu eleştiri, sinir ağı "
            "araştırmalarına verilen fonların büyük ölçüde kesilmesine yol açtı.",
            "1970'lerin ortasından itibaren, abartılı vaatlerin tutmaması "
            "yüzünden hem ABD hem İngiltere'de yapay zekâ finansmanı ciddi "
            "biçimde daraldı. Bu döneme literatürde 'AI kışı' (AI winter) denir. "
            "Araştırmacılar sinir ağlarını bırakıp, kurallara dayalı 'uzman "
            "sistemler' gibi farklı yaklaşımlara yöneldi.",
            "1980'lerde ikinci bir dalga geldi: uzman sistemler (expert systems) "
            "şirketlerde ticari başarı kazandı, çünkü belirli bir alandaki "
            "uzmanın bilgisini if-then kurallarına döküyorlardı. Ama bu sistemler "
            "kırılgandı; öğrenilmemiş bir duruma çabuk şaşırıyorlardı. 1980'lerin "
            "sonunda bu pazar da çöktü ve ikinci bir kış yaşandı.",
            "Asıl dönüm noktalarından biri 1986'da geldi: David Rumelhart, "
            "Geoffrey Hinton ve Ronald Williams, çok katmanlı sinir ağlarını "
            "eğitmek için 'geri yayılım' (backpropagation) algoritmasını "
            "popülerleştirdi. Bu, ağın kendi hatalarından geriye doğru "
            "'öğrenebilmesini' sağladı ve bugünün derin öğrenmesinin matematiksel "
            "temelini attı — gerçek meyvelerini vermesi için ise iki on yıl daha "
            "geçmesi gerekecekti.",
        ],
        "turkiye_notu": (
            "Dünya bu 'kışları' yaşarken Türkiye kendi bilim altyapısını "
            "kuruyordu: TÜBİTAK 1963'te kuruldu, üniversitelerdeki bilgisayar "
            "mühendisliği bölümleri bu dönemde yaygınlaşmaya başladı. Yani "
            "dışarıda soğuk rüzgârlar eserken, Türkiye'de temeller yavaş "
            "yavaş atılıyordu."
        ),
        "quiz": [
            {
                "q": "'Perceptrons' kitabı (1969) neyi göstererek fon kesintilerine yol açtı?",
                "options": [
                    "Bilgisayarların çok yavaş olduğunu",
                    "Tek katmanlı perceptron'un XOR gibi basit problemleri çözemediğini",
                    "İnternetin henüz var olmadığını",
                    "Uzman sistemlerin daha iyi çalıştığını",
                ],
                "correct": 1,
            },
            {
                "q": "'AI kışı' ne anlama gelir?",
                "options": [
                    "Yapay zekâ konferanslarının kışın yapılması",
                    "Yapay zekâ araştırmalarına olan ilgi ve finansmanın ciddi biçimde azalması",
                    "Bilgisayarların soğuk ortamda daha iyi çalışması",
                    "Kış aylarında yapılan özel bir yapay zekâ yarışması",
                ],
                "correct": 1,
            },
            {
                "q": "1986'da popülerleşen ve çok katmanlı ağların eğitilmesini mümkün kılan algoritma hangisidir?",
                "options": [
                    "Turing Testi",
                    "Geri yayılım (backpropagation)",
                    "Perceptron kuralı",
                    "Monte Carlo yöntemi",
                ],
                "correct": 1,
            },
        ],
    },
    {
        "id": 3,
        "slug": "ml-temelleri",
        "years": "Teori",
        "title": "Makine Öğrenmesi Temelleri",
        "intro": "Bir makine, hiç programlanmadığı bir şeyi nasıl 'öğrenir'?",
        "body": [
            "Klasik programlamada insan, kuralları yazar; bilgisayar bu kuralları "
            "uygular. Makine öğrenmesinde ise mantık tersine döner: insan örnekleri "
            "(veriyi) verir, makine bu örneklerden kuralları kendisi çıkarır. "
            "Örneğin 'bu bir kedi mi köpek mi' sorusunu kurallarla yazmak yerine, "
            "binlerce etiketlenmiş kedi-köpek fotoğrafı gösteririz ve model kendi "
            "örüntüsünü bulur.",
            "Üç temel öğrenme türü vardır. Denetimli öğrenmede (supervised "
            "learning), her örneğin doğru cevabı (etiketi) bellidir — model bu "
            "eşleşmeleri ezberlemek yerine genelleyerek öğrenir. Denetimsiz "
            "öğrenmede (unsupervised learning) etiket yoktur; model veride kendi "
            "başına örüntü veya kümeler bulmaya çalışır. Pekiştirmeli öğrenmede "
            "(reinforcement learning) ise bir ajan, bir ortamda deneme-yanılma "
            "yaparak ödül sinyaline göre en iyi stratejiyi bulur.",
            "Her makine öğrenmesi sisteminin üç bileşeni vardır: veri (öğrenmenin "
            "hammaddesi), model (verideki örüntüyü yakalayan matematiksel yapı) ve "
            "eğitim (modelin parametrelerini veriye göre ayarlama süreci). Eğitim "
            "sırasında model tahminler yapar, bu tahminlerin gerçek değerden ne "
            "kadar saptığı bir 'kayıp fonksiyonu' (loss function) ile ölçülür ve "
            "model bu hatayı azaltacak şekilde adım adım güncellenir.",
            "Burada kritik bir tuzak vardır: aşırı öğrenme (overfitting). Model "
            "eğitim verisini ezberleyip gerçek dünyada hiç görmediği yeni "
            "örneklerde başarısız olabilir — tıpkı bir öğrencinin sadece geçmiş "
            "sınav sorularını ezberleyip mantığı kavramamasına benzer. Bu yüzden "
            "modeller, hiç görmediği ayrı bir 'test verisi' üzerinde "
            "değerlendirilir.",
        ],
        "turkiye_notu": (
            "Bugün Türkiye'de de makine öğrenmesi gündelik hayatın tam "
            "içinde: Trendyol'un 'sana özel' ürün önerileri, Getir'in "
            "teslimat süresi tahminleri, bankaların anlık dolandırıcılık "
            "uyarıları — hepsi az önce öğrendiğin denetimli öğrenme "
            "mantığının günlük hayattaki karşılığı."
        ),
        "quiz": [
            {
                "q": "Klasik programlama ile makine öğrenmesi arasındaki temel fark nedir?",
                "options": [
                    "Makine öğrenmesinde internet bağlantısı şarttır",
                    "Klasik programlamada kurallar insan tarafından yazılır; makine öğrenmesinde kurallar veriden çıkarılır",
                    "Makine öğrenmesi sadece görsellerle çalışır",
                    "Aralarında fark yoktur",
                ],
                "correct": 1,
            },
            {
                "q": "Etiketlenmemiş veride model kendi başına örüntü ararsa, bu hangi öğrenme türüdür?",
                "options": [
                    "Denetimli öğrenme",
                    "Pekiştirmeli öğrenme",
                    "Denetimsiz öğrenme",
                    "Aktif öğrenme",
                ],
                "correct": 2,
            },
            {
                "q": "Bir modelin eğitim verisini ezberleyip yeni verilerde başarısız olmasına ne denir?",
                "options": [
                    "Underfitting",
                    "Overfitting (aşırı öğrenme)",
                    "Backpropagation",
                    "Gradient descent",
                ],
                "correct": 1,
            },
        ],
    },
    {
        "id": 4,
        "slug": "sinir-aglari",
        "years": "Teori",
        "title": "Sinir Ağları ve Derin Öğrenme",
        "intro": "Beyinden ilham alan, katman katman çalışan matematiksel yapılar.",
        "body": [
            "Yapay bir sinir ağı, 'nöron' adı verilen basit hesaplama "
            "birimlerinden oluşur. Her nöron, girdilerini alır, bunları belirli "
            "'ağırlıklarla' çarpıp toplar ve sonucu bir 'aktivasyon fonksiyonu' "
            "üzerinden geçirir. Bu fonksiyon, nöronun ne zaman 'ateşleneceğine' "
            "karar veren bir eşik gibi düşünülebilir; ağırlıklar ise ağın eğitim "
            "sırasında öğrendiği şeydir.",
            "Nöronlar katmanlar hâlinde düzenlenir: bir girdi katmanı, bir veya "
            "daha fazla gizli katman (hidden layer) ve bir çıktı katmanı. Bilgi "
            "girdi katmanından çıktı katmanına doğru katman katman ilerler; her "
            "katman, bir öncekinden gelen bilgiyi biraz daha soyut bir temsile "
            "dönüştürür. Örneğin görüntü tanımada ilk katmanlar kenarları, sonraki "
            "katmanlar şekilleri, daha sonraki katmanlar ise nesnenin tamamını "
            "temsil edebilir.",
            "'Derin öğrenme' (deep learning) terimi, tam olarak bu çok katmanlı "
            "yapıya işaret eder — 'derin', çok sayıda gizli katman anlamına gelir. "
            "Bir ağ ne kadar derinse, o kadar karmaşık ve soyut örüntüleri "
            "yakalayabilir; ama aynı zamanda eğitmesi o kadar zorlaşır ve daha "
            "fazla veri, hesaplama gücü gerektirir.",
            "2012 yılı bir dönüm noktasıdır: Geoffrey Hinton'ın öğrencileri "
            "tarafından geliştirilen AlexNet adlı derin sinir ağı, ImageNet "
            "görüntü tanıma yarışmasını önceki yöntemleri açık farkla geride "
            "bırakarak kazandı. Bu başarı, hem büyük veri setlerinin hem de "
            "GPU'ların (grafik işlemcilerinin) paralel hesaplama gücünün devreye "
            "girmesiyle mümkün oldu ve derin öğrenmenin bugünkü patlamasını "
            "başlattı.",
        ],
        "turkiye_notu": (
            "Türk bankacılık sektörü, kredi kartı işlemlerinde anormal "
            "davranışı anlık yakalamak için tam bu bölümde anlattığımız "
            "türden derin sinir ağları kullanıyor. Bir işlem 'şüpheli' diye "
            "işaretlendiğinde, arkasında genelde katman katman çalışan böyle "
            "bir ağ var."
        ),
        "quiz": [
            {
                "q": "Bir yapay nöronda 'ağırlıklar' ne işe yarar?",
                "options": [
                    "Modelin dosya boyutunu belirler",
                    "Eğitim sırasında öğrenilen ve girdilerin önemini belirleyen değerlerdir",
                    "Sadece görüntü verisi için kullanılır",
                    "Ağın hızını doğrudan artırır",
                ],
                "correct": 1,
            },
            {
                "q": "'Derin öğrenme' terimindeki 'derin' ne anlama gelir?",
                "options": [
                    "Modelin çok fazla veri kullanması",
                    "Ağda çok sayıda gizli katman bulunması",
                    "Modelin çok yavaş çalışması",
                    "Modelin sadece metinle çalışması",
                ],
                "correct": 1,
            },
            {
                "q": "2012'de derin öğrenmenin patlamasını tetikleyen olay nedir?",
                "options": [
                    "Turing Testi'nin geçilmesi",
                    "AlexNet'in ImageNet yarışmasını büyük farkla kazanması",
                    "İlk perceptron'un yapılması",
                    "Dartmouth çalıştayının düzenlenmesi",
                ],
                "correct": 1,
            },
        ],
    },
    {
        "id": 5,
        "slug": "modern-cag",
        "years": "2017 – Günümüz",
        "title": "Modern Çağ: Transformer'lar ve Büyük Dil Modelleri",
        "intro": "Bugün konuştuğumuz asistanların arkasındaki fikir.",
        "body": [
            "2017'de Google araştırmacıları 'Attention Is All You Need' başlıklı "
            "makalede 'Transformer' mimarisini tanıttı. Bu mimarinin kalbinde "
            "'dikkat mekanizması' (attention) vardır: model, bir cümledeki her "
            "kelimeyi işlerken, cümledeki diğer tüm kelimelere ne kadar "
            "'dikkat etmesi' gerektiğine karar verir. Bu sayede, önceki "
            "mimarilerin aksine, uzun metinlerdeki uzak ilişkileri de yakalayabilir "
            "ve hesaplamalar paralel olarak yapılabilir — bu da devasa veri "
            "setleriyle eğitimi pratik hâle getirdi.",
            "Büyük dil modelleri (Large Language Model, LLM), Transformer "
            "mimarisini kullanarak internetteki devasa miktarda metinle eğitilir. "
            "Eğitim hedefi aslında basittir: bir metindeki bir sonraki kelimeyi "
            "tahmin etmek. Ama milyarlarca parametre ve trilyonlarca kelimelik "
            "veriyle bu basit hedef, dil bilgisinden mantık yürütmeye, kod "
            "yazmaktan özetlemeye kadar uzanan şaşırtıcı yetenekler doğurdu.",
            "Bir LLM eğitildikten sonra genellikle bir ek aşamadan geçer: insan "
            "geri bildirimiyle pekiştirmeli öğrenme (RLHF) gibi yöntemlerle model, "
            "'faydalı, dürüst ve zararsız' cevaplar vermeye doğru ayarlanır. Bu "
            "aşama, ham bir dil modelini bugün sohbet ettiğimiz türde bir "
            "asistana dönüştürür.",
            "2022'de ChatGPT'nin halka açılması, bu teknolojiyi laboratuvardan "
            "gündelik hayata taşıdı. Bugün Claude gibi asistanlar da aynı temel "
            "fikirler — Transformer mimarisi, büyük ölçekli eğitim ve insan "
            "geri bildirimiyle ince ayar — üzerine inşa edilir. Bu kursun "
            "sonundaki chatbot pratiği de tam olarak bu tür bir modelle "
            "konuşarak öğrendiklerini pekiştirmen için var.",
        ],
        "turkiye_notu": (
            "Türkiye'de de yerli büyük dil modeli çalışmaları hız kazandı: "
            "Trendyol açık kaynaklı Trendyol-LLM'i yayımladı, yazılım "
            "şirketi VNGRS ise sıfırdan Türkçe için eğitilen Kumru LLM'i "
            "tanıttı; TÜBİTAK da kendi Türkçe dil modeli projesini "
            "yürütüyor. Yani bu kursun sonunda konuştuğun chatbot'un "
            "arkasındaki fikir, Türkiye'de de aktif şekilde geliştiriliyor."
        ),
        "quiz": [
            {
                "q": "Transformer mimarisinin kalbinde yer alan mekanizma hangisidir?",
                "options": [
                    "Geri yayılım",
                    "Dikkat mekanizması (attention)",
                    "Perceptron kuralı",
                    "Konvolüsyon",
                ],
                "correct": 1,
            },
            {
                "q": "Bir büyük dil modelinin temel eğitim hedefi nedir?",
                "options": [
                    "Görüntüleri sınıflandırmak",
                    "Bir metindeki bir sonraki kelimeyi tahmin etmek",
                    "Satranç oynamayı öğrenmek",
                    "Ses tanımak",
                ],
                "correct": 1,
            },
            {
                "q": "RLHF ne işe yarar?",
                "options": [
                    "Modelin daha hızlı çalışmasını sağlar",
                    "Modelin donanım maliyetini düşürür",
                    "Ham dil modelini, insan geri bildirimiyle daha faydalı/güvenli bir asistana dönüştürür",
                    "Modelin veri setini büyütür",
                ],
                "correct": 2,
            },
        ],
    },
]


def get_module(slug):
    for m in MODULES:
        if m["slug"] == slug:
            return m
    return None


def get_module_by_id(module_id):
    for m in MODULES:
        if m["id"] == module_id:
            return m
    return None
