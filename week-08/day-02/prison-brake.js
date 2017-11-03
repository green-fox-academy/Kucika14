// Create a prison function, that has your name as a private fugutive variable
// The function should return an object that has two methods:
//  - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//  - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable

let prison = function(name) {
    let fugitive = name;
    return {
        visit_counter: 0,
        visit: function() {
            if (fugitive === '') {
                console.log('Scofield gone, Bellick is angry now!')
            } else {
            this.visit_counter++;
            console.log(fugitive + ' is visited ' + this.visit_counter + ' time(s)')
            }
        },
        escape: function() {
            fugitive = '';
            nameOfFuggitive = name
            console.log('BREAKING NEWS, ' + nameOfFuggitive + ' escaped the prison again');
        }
    }
}


const  foxRiver= prison('Michael Scofield');

foxRiver.visit()
foxRiver.visit()
foxRiver.escape()
foxRiver.visit()