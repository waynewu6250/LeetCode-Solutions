/*
   @Problem 3:（60 分）
   關於資料探勘（data mining），幾種常見的任務包含關聯性（association）、分類（classification）、分群（clustering）。
   今天讓我們來學點關聯性分析。
   一個常見的例子發生在零售領域：當某個消費者買了若干品項並結帳，一個零售商能不能根據歷史交易記錄來猜，推薦哪個商品給消費者會得到最高的購買機率？
   這也是一個推薦系統（recommender system）問題。

   讓我們具體地描述這個問題。
   假設我們有在銷售的品項（item）集合為I = {1, 2, ..., n}，而歷史上發生過的交易（transaction）集合為T = {1, 2, ..., m}。
   在交易j中，某消費者買了Tj ⊂ I，亦即他從品項集合I中挑了一些東西買，這些東西的集合Tj是I的子集合。
   理論上，Tj是有可能等於I，但這表示此消費者買了店裡所有的商品。
   由於這未免太不切實際，讓我們假設Tj不會等於I。
   為了簡單起見，讓我們假設每個品項都最多被買一個。
   現在一個新的消費者買了品項集合S ⊂ I並且結帳了，我們想要在他付錢閃人之前（或是在網站上按下「結帳」之前），從他沒有買的品項集合I ∖ S中挑一個商品推薦給他，
   而我們的任務是在I ∖ S中找出他購買機率最大的那個商品。

   讓我們來舉個例子。
   假設我的店裡賣五種A、B、C、D、E開店至今一共有10個人來買過，交易記錄如下表所示，也就是第一個人買了D和E、第二個人買了A和C和D，依此類推。
   若是用我們剛剛定義的參數來描述，我們有n = 5、m = 10、I = {A, B, C, D, E}、T1 = {D, E}、T2 = {A, C, D}，依此類推。

   ---------------
    A  B  C  D  E
   ---------------
    0  0  0  1  1
    1  0  1  1  0
    1  0  0  1  0
    1  0  0  1  0
    0  0  0  1  1
    0  1  1  1  0
    1  1  0  0  1
    1  0  0  1  0
    0  0  1  1  1
    0  0  1  1  0
   ---------------
   表1：歷史交易紀錄範例

   所謂的「購買機率最大」，需要考慮幾件事。

   • 首先，我們會考慮消費者一起購買某些商品的機率，畢竟如果某人已經買了義美牛奶，你應該不想要推薦他林鳳營牛奶，應該會想推薦他麵包（如果他沒有買麵包）。
     給定任何一個品項集合（itemset）S，我們可以計算其出現過的次數f(S)，再除以總交易數m，就是該品項一起被購買的機率，
     在關聯性分析的領域中我們將之稱為support（支持度）。
     舉例來說，我們有f(C) = 4、f(D) = 9、f({C, D}) = 4，以及f({C, D, E}) = 1，
     因此他們各自的support就是supp(C) = 0.4、supp({C, D, E}) = 0.1，依此類推。

   • 我們另外也要考慮已知消費者購買一些商品後，也購買另一些商品的條件機率。
     以我們的例子來說，買了C的人也買D的機率是100%，但買了D的人也買C的機率只有44.4%，因此對買C的人推薦D成功率較高，對買D的人推薦C成功率就比較低了。
     給定前提品項集合（antecedent itemset）X跟結果品項集合（consequent itemset）Y，我們用f(Y|X)表示買X的人也買Y的次數，再除以有購買X的交易次數f(X)，
     就得到被稱為confidence（信賴度的條件機率conf(Y|X)。
     在我們的例子中，conf(D|C) = 1、conf(C|D) = 4 / 9，以及conf(D|{C, E}) = 1。

   有了support和confidence的觀念後，要根據某消費者的購買品項集合S來做推薦，就不是那麼沒有頭緒了。
   為了簡單起見，讓我們假設我們只想推銷一個單品（而不是一個集合），那麼我們要做的就是兩件事：

   1. 對一個在集合I ∖ S中的商品i，計算其與S一起被購買的support supp({i} ∪ S)。
      根據一個給定的目標值s，如果supp({i} ∪ S) ≥ s就保留i，反之則不考慮推薦i。
   2. 對於通過第一步驟篩選的品項，一一考慮購買S後也購買該品項的機率，也就是conf(i|S)，然後挑出confidence最大的那個品項做推薦。

   請想想我們為什麼要同時考慮support和confidence。
   考慮confidence是直觀的：如果某人買了S，而且以往有一堆買了S的人也買i，那推薦他買i的成功率自然不低。
   但於此同時S和i的support也是需要注意的。
   如果support太低，那麼這個高confidence很可能就是個巧合，只有在某個組合有高support的情況下，我們才真的相信它們的confidence是有用的。

   在本題中，你將會被給定品項與歷史交易資訊。
   接著你會被給定一筆交易中購買的品項集合，以及support必須夠高的門檻值。
   你的任務是根據上述規則，找出應該推薦的品項。
   如果有複數個品項都通過support的要求並且同樣有最高的confidence，就推薦編號最小的那個。
   如果沒有任何品項可以推薦（因為都不滿足support門檻），就不要推薦任何東西。

   [特殊要求：動態陣列]

   如果要實做這一題要求的任務，一個很直觀的想法是：如果總品項數為n、總交易次數為m，那就用一個m × n的靜態二維陣列來存交易記錄，
   然後再寫一些迴圈、函數之類的東西去反覆翻攪這個靜態二維陣列，去算出我們要的答案。
   這樣的想法固然沒錯，但這只有在n和m夠小的時候才比較適合。
   實務上一個零售店通常有成千上萬個品項，如果是電子商務網站更是有可能有幾十萬、上百萬，要分析的交易筆數同樣也可能幾百萬、上千萬。
   假設各一百萬吧，如果建一個1000000 × 1000000的二維陣列，會非常浪費空間。
   認真算一下，如果這二維陣列存的是整數，那4 × 1012 byte可是4TB 之多，幾乎沒有誰的個人電腦有4 TB的記憶體。
   除此之外，使用靜態陣列意味著貴店不能增加品項，能容許的交易次數也有其上限，這些都會讓你的程式很不具彈性。

   那怎麼辦呢？
   好消息是，絕大部分的消費者在一次交易中，通常只買頂多十幾個品項，因此如果用m × n的二維陣列來存交易記錄，就會有非常非常多的陣列元素都是存0，
   這些0某方面來講其實就跳過不要存就好了。
   因此在這一題，我們要來練習用動態二維陣列儲存歷史交易資料。
   要是真的有幾千萬個品項和幾百億個交易，我們這門課介紹的任何資料結構和演算法都不足以針對推薦問題做良好的運算。
   你肯定需要更好的資料結構和更好的演算法，而這可能是你得要去修更進階的課的動機吧。

   在我們即將實作的陣列中，我們依然會有m列，一列代表一次交易，但現在我們在一列中將只儲存該次交易中被購買的品項的編號。
   因為兩次交易中購買的品項數未必相同，所以我們的每一列都會是一個一維動態陣列，長度恰好為該次交易被購買的品項數。
   換言之，我們的「表格」將會「各列長度不一」，而且「表格」的列數是可以持續增加的（不過在這一題中，我們不會要求你做這件事）。

   本題有兩個具體要求：
   1. 你必須使用二維動態陣列來儲存交易資料，而且兩個維度（列跟欄）都必須是動態的。

   2. 你必須寫一個函數：void setTransactions(int** trans, int* itemCnt, int m);
       其中trans是儲存歷史交易資料的二維動態陣列、itemCnt是儲存每筆交易中各購買了幾個品項的一維動態陣列、m是由測試資料讀入的歷史交易資料筆數。
       你的main function必須呼叫此函數一次，在此函數中讀入測試資料中的歷史交易資料，並將相關資訊記錄在trans和itemCnt中，以便後續程式做處理和運算。

   為了強迫你這麼做，在這一題我們會對你的程式在PDOGS上的記憶體用量有所限制，讓你如果用m × n的二維靜態陣列就會超出記憶體的限制，因此在部份測試資料得不到分數。
   當然如果你真的應付不了動態陣列，那寫靜態陣列也是可以取得一部分規模較小的測試資料的分數的，不過，動態記憶體配置是會在未來持續被使用的功能，請大家還是盡可能地練習吧！
*/

/*
   @Input：
   系統會提供20筆測試資料，每筆測試資料裝在一個檔案裡。
   在每個檔案中，第一列存放兩個整數n、m和一個三位小數s，分別代表總品項數、總交易數和support門檻。
   品項編號為1、2、3一直到n，而交易編號為1、2、3一直到 m。
   在第二列至第m + 1列中，第j + 1列存放kj + 1個介於1到n的不重複整數，其中第一個數字kj代表歷史上第j筆交易所購買的品項數，
   後面kj個數字則是品項集合Tj − 1中的品項編號。
   第m + 2列中也有km + 1 + 1個介於1到n的不重複整數，代表現在要被推薦的消費者購買的品項數以及品項集合S中的品項編號。
   每一列中的兩個數字都用一個空白鍵隔開。

   在前10筆測試資料中，我們已知1 ≤ n ≤ 20以及1 ≤ m ≤ 500。
   在後10筆測試資料中，我們已知1 ≤ n ≤ 20000以及1 ≤ m ≤ 50000。
*/

/*
   @Output：
   根據規則找出應該推薦的品項後，請依序輸出該品項的編號、該品項與S共同出現的交易次數（亦即support乘以m），
   以及S出現的交易次數（亦即給定S會購買該品項的confidence的分母）。
   各數字用一個逗點隔開。
   如果沒有任何品項可以推薦（因為都不滿足support門檻），就不要印出任何東西。
*/

/*
   @Sample Input：
   #sample 1: 
        5    10 0.100
        2     4     5
        3     1     3     4
        2     1     4
        2     1     4
        2     4     5
        3     2     3     4
        3     1     2     5
        2     1     4
        3     3     4     5
        2     3     4
        1     4

   @Sample Output：
   #sample 1: 1,4,9
*/

#include <iostream>
using namespace std;

// Set transactions:
void setTransactions(int** trans, int* itemCnt, int m)
{
    for (int i = 0; i < m; i++)
    {
        cin >> itemCnt[i];

        trans[i] = new int[itemCnt[i]]; // 1 history of transaction (1D)
        for (int j = 0; j < itemCnt[i]; j++)
            cin >> trans[i][j];
    }
}

int main()
{
    /* ----------- INPUT ----------- */

    int n = 0; // sales items
    int m = 0; // history of transaction
    float s = 0; // target value
    cin >> n >> m >> s;

    // History:
    int* k = new int[m]; // count items
    int** ttrans = new int*[m]; // total history of transcation (2D)
    setTransactions(ttrans, k, m);

    // Now:
    int knc = 0; // count items which the consumer wants to buy now
    int* nctrans = new int[knc]; // 1 transaction (1D)
    cin >> knc;
    for (int i = 0; i < knc; i++)
        cin >> nctrans[i];
    

    /* ----------- CHECK ----------- */

    int check = 0; // check items which the consumer wants to buy now in history
    float* f = new float[n]; // count one item frequency
    int* tem = new int[n]; // temporary
    for (int i = 0; i < n; i++)
    {
        tem[i] = 0;
        f[i] = 0;
    }

    // calculate f:
    for (int i = 0; i < m; i++)
    {   
        // record 1D transaction
        for (int j = 0; j < k[i]; j++)
            tem[ttrans[i][j] - 1] += 1;
        // check items
        for (int j = 0; j < knc; j++)
        {
            if (tem[nctrans[j] - 1] == 1)
                check += 1;
        }
        if (check == knc)
        {
            for (int j = 0; j < n; j++)
                f[j] += tem[j]; // add in f[s]
        }

        //cout << "f:   " << f[0] << " " << f[1] << " " << f[2] << " " << f[3] << " " << f[4] << "\n";
        
        // clear
        check = 0;
        for (int j = 0; j < n; j++)
            tem[j] = 0;
    }

    delete[] k;
    delete[] tem;

    // calculate supp and conf
    float conf = 0;
    float supp = 0;
    float tems = 0;
    float temc = 0;
    int it = 0;
    for (int i = 0; i < n; i++)
    {
        if (i == nctrans[0] - 1)
            continue;
        else
        {
            // support
            tems = f[i] / m;
            // confidence
            temc = f[i] / f[nctrans[0] - 1];
            if (tems > supp && tems >= s && temc > conf)
            {
                supp = tems;
                conf = temc;
                it = i + 1;
            }
        }

    }

    //cout << supp << " " << it;

    if (it != 0)
        cout <<  it << "," << f[it - 1] << "," << f[nctrans[0] - 1];

    return 0;
}