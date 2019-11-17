const pads_btn = document.querySelectorAll('.pads');
const txt_f = document.querySelectorAll('.inputz');
const remove_btn = document.getElementById('pad');
// const run_btn = document.querySelector('.run');
const form = document.getElementById('formHandler');

count = 0;
insert_num_list = [];
function Msg(msg) {
  document.querySelector('#msg').innerHTML = '' + msg;
  clearTimeout(error);
}
pads_btn.forEach(btn => {
  if (insert_num_list.length != 4) {
    btn.addEventListener('click', insert_num);
    function insert_num() {
      event.preventDefault();
      btn_val = btn.value;
      // console.log(btn.value);
      if (txt_f[count].value == '') {
        if (insert_num_list.indexOf(btn_val) === -1) {
          txt_val = txt_f[count].value = btn_val;
          insert_num_list.push(txt_val);
        } else {
          count -= 1;
          // console.log(count);
          error = setTimeout(Msg, 0, 'Duplication is not Allowed :(');

          // document.querySelector("#msg").innerHTML = "Duplication is not Allowed :("
        }
        error = setTimeout(Msg, 3000, '');
        // console.log(insert_num_list);
      } else {
      }
      if (count < 3) {
        count++;
      } else {
        count = 0;
      }
    }
  } else {
    btn.removeEventListener('click', insert_num);
  }
});

remove_btn.addEventListener('click', function() {
  event.preventDefault();
  txt_f.forEach(txt => {
    txt.value = '';
    count = 0;
    insert_num_list.pop();
    // console.log(insert_num_list);
  });
});
const start = document.querySelector('.start_btn');
const dsc = document.querySelector('#dsc-contain');
start.addEventListener('click', start_game);
function start_game() {
  document.querySelector('.container').style.display = 'flex';
  start.style.display = 'none';
  dsc.style.display = 'none';
}
form.addEventListener('submit', runGame);

function runGame(e) {
  e.preventDefault();

  send_to_python = insert_num_list;
  fetch('/process', {
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
    .then(function(response) {
      // At this point, Flask has printed our JSON
      return response.json();
    })
    .then(function(myjson) {
      // console.log('POST response: ');
      // console.log(myjson);

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
    </tr>`;
      if (Right == 4) {
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
    });
  txt_f.forEach(txt => {
    txt.value = '';
    insert_num_list.pop();
    // console.log(insert_num_list);
  });
  count = 0;
}
if (window.performance) {
  // console.info('window.performence works fine on this browser');
}
if (performance.navigation.type == 1) {
  fetch('/process', {
    // Specify the method
    method: 'post',

    // JSON
    headers: {
      'Content-Type': 'application/json'
    },

    // A JSON payload
    body: JSON.stringify('counter')
  })
    .then(function(response) {
      // At this point, Flask has printed our JSON
      return response.text();
    })
    .then(function(data) {
      // console.log('response');
      // console.log(data);
    });
  txt_f.forEach(txt => {
    txt.value = '';
    insert_num_list.pop();
    // console.log(insert_num_list);
  });
  count = 0;
} else {
  // console.info('this page is nit reloaded');
}
