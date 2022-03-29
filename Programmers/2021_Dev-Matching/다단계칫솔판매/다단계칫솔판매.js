function solution(enroll, referral, seller, amount) {
    // {추천 받은 사람 : 추천인 }
    let dict = {}
    let answer = {}

    for (let i=0; i<enroll.length; i++) {
        dict[enroll[i]] = referral[i];
        answer[enroll[i]] = 0;
    }
    
    // console.log('dict :', dict);
    // console.log('answer :', answer);
    
    for (i=0; i<seller.length; i++) {
        salesman = seller[i];
        recommender = dict[salesman];
        profit = amount[i] * 100;
        
        while (recommender !== '-') {
            recommender_profit = Math.floor(profit * 0.1);
            my_profit = profit - recommender_profit;
            
            if (recommender_profit == 0) {
                answer[salesman] += profit;
                break;
            } else {
                answer[salesman] += my_profit;
                profit = recommender_profit;
                salesman = recommender;
                recommender = dict[salesman];
            }
        }
        
        if (recommender === '-') {
            recommender_profit = Math.floor(profit * 0.1);
            answer[salesman] += (profit - recommender_profit);
        }
    }
    
    let result = [];
    for (let e of enroll) {
        result.push(answer[e]);
    }
    
    return result;
}
