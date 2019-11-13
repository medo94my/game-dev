const pads_btn = document.querySelectorAll('.pads');
const txt_f = document.querySelector('.inputz');
const remove_btn = document.getElementById('clear');
// const run_btn = document.querySelector('.run');
const form = document.getElementById('formHandler');


insert_num_list = [];
function Msg(msg) {
  document.querySelector('#msg').innerHTML = '' + msg;
  clearTimeout(error);
}
counter = 0
pads_btn.forEach(btn => {
  // if (insert_num_list.length != 26) {
  btn.addEventListener('click', insert_num);
  function insert_num() {
    event.preventDefault();
    btn_val = btn.value;
    console.log(btn.value);

    // if (txt_f[count].value == '') {
    if (insert_num_list.indexOf(btn_val) === -1) {

      txt_val = txt_f.value += btn_val;
      insert_num_list.push(btn_val);
      counter++
      console.log(counter);
      console.log(insert_num_list);
      // counter = txt_f.value.length
    } else {
      count -= 1;
      // console.log(count);
      error = setTimeout(Msg, 0, 'Duplication is not Allowed :(');

      // document.querySelector("#msg").innerHTML = "Duplication is not Allowed :("
    }
    //   error = setTimeout(Msg, 3000, '');
    //   console.log(insert_num_list);
    // } else {
    // }
    // if (count < 5) {
    //   count++;
    // } else {
    //   count = 0;
    // }
  }
  // } else {
  //   btn.removeEventListener('click', insert_num);
  // }
});

remove_btn.addEventListener('click', function () {
  event.preventDefault();
  // txt_f.forEach(txt => {

  var value = txt_f.value;
  txt_f.value = value.substr(0, value.length - 1);

  count = 0;
  insert_num_list.pop();
  // console.log(insert_num_list);
  // });
});
const start = document.querySelector('.start_btn');
const dsc = document.querySelector('#dsc-contain');
start.addEventListener('click', start_game);
function start_game() {
  document.querySelector('.container').style.display = 'flex';
  start.style.display = 'none';
  dsc.style.display = 'none';
  const num = document.getElementById('num').value;
  const color = document.getElementById('color').value;
  const letter = document.getElementById('letter').value;
  const enter = document.querySelector('.record-1')
  console.log(
    'num:' + num + ' ' + 'color:' + color + ' ' + 'letters:' + letter
  );
  enter.style.display = 'block'
  total = parseInt(num) + parseInt(color) + parseInt(letter)

  enter.innerHTML = "N: " + num + " " + "C: " + color + " " + "L: " + " " + letter + " "
  // console.log(counter)

  fetch('/MM_A02_002_P ', {
    // Specify the method
    method: 'POST',

    // JSON
    headers: {
      'Content-Type': 'application/json'
    },

    // A JSON payload
    body: JSON.stringify({
      number: num,
      color: color,
      letter: letter
    })
  })
    .then(function (response) {
      // At this point, Flask has printed our JSON
      return response.json();
    })
    .then(function (myjson) {
      console.log('POST response: ');
      console.log(myjson);
      len_of_answer = myjson
      console.log(len_of_answer)
    });
}
form.addEventListener('submit', runGame);

function runGame(e) {
  e.preventDefault();

  send_to_python = insert_num_list;
  fetch('/MM_A02_002_Post  ', {
    // Specify the method
    method: 'POST',

    // JSON
    headers: {
      'Content-Type': 'application/json'
    },

    // A JSON payload
    body: JSON.stringify({
      Guess: send_to_python
    })
  })
    .then(function (response) {
      // At this point, Flask has printed our JSON
      return response.json();
    })
    .then(function (myjson) {
      console.log('POST response: ');
      console.log(myjson);

      correct = myjson['correct'];
      Right = myjson['right'];
      Wrong = myjson['wrong'];
      guessed = myjson['number'];
      Score = myjson['score'];
      counter = myjson['Counter'];
      // console.log(counter);
      document.getElementById('txt-score').innerHTML = Score;
      document.getElementById('correct').innerHTML = correct;
      document.getElementById('cright').innerHTML = Right;
      document.getElementById('cwrong').innerHTML = Wrong;
      document.querySelector('.list').innerHTML += `<tr class="row">
        <th scope="col">${counter}</th>
        <th scope="col">${guessed}</th>
        <th scope="col">${correct}</th>
        <th scope="col">${Right}</th>
        <th scope="col">${Wrong}</th>
      </<th>`;
      txt_f.value = '';
      insert_num_list.splice(0, insert_num_list.length)
      // insert_num_list.pop();
      if (Right == total) {
        // document.querySelector('#msg').innerHTML =
        setTimeout(() => {
          restart_game = confirm(
            'Congratulations!! YOU WON !!\n\n Do you Like to play new game??' +
            '\n\n Your Score = ' +
            Score
          );
          if (restart_game == true) {
            start.style.display = 'block';
            document.querySelector('.container').style.display = 'none';
            document.location.reload();
          } else {
            location.href = 'games';
          }
        }, 3000);

        document.querySelector('.lbl-score1').style.visibility = 'visible';
      } else if (counter == 10) {
        // document.querySelector('#msg').innerHTML
        lost_game = confirm('YOU LOST !! \n\n Do You Want to Try again');
        // setTimeout(() => {
        if (lost_game == true) {
          start.style.display = 'block';
          document.querySelector('.container').style.display = 'none';
          document.location.reload();
        } else {
          location.href = 'games';
        }
        // }, 1000);
      }
      txt_f.value = '';
      insert_num_list.pop();
    });

  txt_f.value = '';
  insert_num_list.pop();
  // console.log(insert_num_list);

  count = 0;
}
if (window.performance) {
  // console.info('window.performence works fine on this browser');
}
if (performance.navigation.type == 1) {

  //the code send to back end after clicking submit button 
  fetch('/MM_A02_002_Post', {
    // Specify the method
    method: 'post',

    // JSON
    headers: {
      'Content-Type': 'application/json'
    },

    // A JSON payload
    body: JSON.stringify('counter')
  })
    .then(function (response) {
      // At this point, Flask has printed our JSON
      return response.text();
    })
    .then(function (data) {
      // console.log('response');
      // console.log(data);
    });

  txt_f.value = '';
  insert_num_list.pop();
  // console.log(insert_num_list);
  count = 0;
} else {
  // console.info('this page is nit reloaded');
}

// function to restrict input field to numbers only
function numOnly(evt) {
  let num = String.fromCharCode(evt.which);
  if (!(/[0-9]/.test(num))) {
    evt.preventDefault();
  }
}
