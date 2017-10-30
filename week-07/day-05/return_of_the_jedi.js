let images = [  {title : 'spaceship', description : 'this is a madafakin\' spaceship', url : 'e:\greenfox\Kucika14\week-07\day-05\images\thumb-1920-339209.jpg'},
                {title : 'AT-AT', description : 'this is a madafakin\' AT-AT', url : 'e:\greenfox\Kucika14\week-07\day-05\images\JTjy2Of.jpg'},
                {title : 'happy group picture', description : 'guys with lightsabers', url : 'e:\greenfox\Kucika14\week-07\day-05\images\star-wars-lightsaber-characters-wallpaper-5474.jpg'},
                {title : 'STAR WARS', description : 'S.T.A.R.W.A.R.S.!.!.!', url : 'e:\greenfox\Kucika14\week-07\day-05\images\thumb-1920-339209.jpg'},
                {title : 'Darth Vader', description : 'Vader bitches', url : 'e:\greenfox\Kucika14\week-07\day-05\images\757812.png'}]

let nav = document.querySelector('.navigation');
images.forEach(function(e) {
    let listElements = document.createElement('li');
    nav.appendChild(listElements);
    listElements.classList.add('thumbnails')
});










