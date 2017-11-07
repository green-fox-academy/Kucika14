'use strict';

const sum = class {
    sum (arrayOfNums) {
        try {
            let asd = arrayOfNums.reduce(function (acc, curr) {
                if (typeof curr != "number") throw new Error('ez bizony error, yapp!')
                acc += curr;
                return acc;
            }, 0);
            return asd;
        } catch (e) {
            
        }
    }
}

module.exports = sum;

