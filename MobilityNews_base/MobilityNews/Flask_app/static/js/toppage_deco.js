function gazoon(news_list) {
    /**
     * gazoonのニュースを表示するタグの作成をする
     */
    //htmlのspanタグにニュースを埋め込む
    var target_tag = document.getElementById('gazoon');
    //引数を取り出す
    var title = news_list[0]
    var url = news_list[1]
    var img_src = news_list[2]

    //タグの作成
    //<p><a href=url>あああああ</a><img src=img_url/></p>
    //の形になるように作成

    //pタグの作成
    var p_tag = document.createElement("p");
    //aタグの作成
    var make_atag = document.createElement("a");
    make_atag.setAttribute("href", url);
    make_atag.innerHTML = title;
    //pタグにaタグを埋め込む
    p_tag.appendChild(make_atag)
    //imgタグの作成
    var make_imgtag = document.createElement("img");
    make_imgtag.setAttribute("src", img_src)
    make_imgtag.setAttribute("width", "20%")
    make_imgtag.setAttribute("height", "20%")
    //pタグにimgタグを埋め込む
    p_tag.appendChild(make_imgtag)
    //spanタグにpタグを埋め込む
    target_tag.appendChild(p_tag);

}

function techcrunch(news_list) {
    /**
     * techcrunchのニュースを出力するためのタグを作成する
     */
    var target_tag = document.getElementById('techcrunch');
    var title = news_list[0]
    var url = news_list[1]
    var img_src = news_list[2]

    var p_tag = document.createElement("p");
    var make_atag = document.createElement("a");
    make_atag.setAttribute("href", url);
    make_atag.innerHTML = title;
    p_tag.appendChild(make_atag)

    var make_imgtag = document.createElement("img");
    make_imgtag.setAttribute("src", img_src)
    p_tag.appendChild(make_imgtag)

    target_tag.appendChild(p_tag);

}