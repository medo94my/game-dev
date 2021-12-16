const student = document.querySelector('#form-student');
const major = document.querySelector('#form-major');
const job = document.querySelector('#form-job');
// const non_student = document.querySelector('#non-student');

// student.addEventListener('click', change);
// function change() {
//   student.innerHTML = 'hellow';
// }
var rad = document.querySelectorAll('#student');
var prev = null;
for (var i = 0; i < rad.length; i++) {
  rad[i].addEventListener('click', function() {
    console.log(this.value);
    val = this.value;
    if (val === 'Student') {
      student.style.display = 'block';
      job.style.display = 'none';
      job.value == '';
    } else {
      student.style.display = 'none';
      major.style.display = 'none';
      job.style.display = 'block';
    }
  });
}
student_choice = document.querySelectorAll('#choice');
for (var i = 0; i < student_choice.length; i++) {
  student_choice[i].addEventListener('change', function() {
    VAL = this.value;
    if (
      VAL == 'Bachelor Degree' ||
      VAL == 'Graduated' ||
      VAL == 'Home Schooled'
    ) {
      major.style.display = 'block';
    } else {
      major.style.display = 'none';
    }
  });
}
