const cron = require('node-cron');

const axios = require('axios');
const cheerio = require('cheerio');
const iconv = require('iconv-lite');


// ES6 문법을 따른다.
const ax = async (url) => {
    try{
        return await axios.get(url, {responseEncoding : 'binary', responseType : 'arraybuffer'});
    } catch (error) {
        console.log(error);
    }
}

// 혹시라도 이해하기 힘들까 다른 문법도 가져와봤다.
// url 값을 인자로 받는다.
function ax(url) {
	// url, 뒤의 내용은 설정에 관련된 내용이다.
	// 저렇게 내용을 적지 않으면 인코딩 에러가 나서 글씨가 깨지게 된다.
    return axios.get(url, {responseEncoding : 'binary', responseType : 'arraybuffer'});
}

cron.schedule('*/10 * * * * *', () => {
	// 실행할 함수 내용
});

// 네이버 뉴스 IT 속보 주소이다.
const url = `https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105`;

    ax(url)
        .then(htmlDoc => {
// iconv를 이용해 EUC-KR에서 UTF-8로 인코딩해준다.
           let html = iconv.decode(htmlDoc.data, 'EUC-KR');
// result 라는 빈 함수를 만들어 이 곳에 결과값들을 넣어준다.
            let result = [];
// cheerio를 톨해 html내용을 $에 넣는다
            const $ = cheerio.load(html);
// col이란 함수에 $("ul.type06_headline").children("li") 가 들어간다.
            let col = $("ul.type06_headline").children("li");
// 그럼 이제 col에 들어간 데이터 만큼 반복문을 돌린다.
// each문을 사용했다.
            col.each(function(i, element) {
// 해당하는 DOM의 text값을 가져온다.
// 좌우에 공백이 상당히 많기에 trim을 써서 제거해줬다.
                result[i] = $(this).find('dl dt:nth-child(2)').text().trim();
// 만약 이미지가 없는 글이라 nth-child(2)의 내용이 ''라면
// nth-child의 인자를 1로 고쳐 다시 가져온다.
                if(result[i] === '') {
                    result[i] = $(this).find('dl dt:nth-child(1)').text().trim();
                }
            });
// 반복문이 끝나고 그 결과를 로그로 띄워준다.
            console.log(result);
        })

        module.export = cron